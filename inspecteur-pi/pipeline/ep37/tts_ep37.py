import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Sept nuits à l'auberge, et pour tout argent, une chaîne en or ! L'inspecteur doit payer l'aubergiste chaque soir. Le premier soir, il lui doit un maillon. Le deuxième soir, deux maillons en tout. Et ainsi de suite, jusqu'à sept. Mais sa chaîne a exactement sept maillons, et l'aubergiste accepte de rendre les morceaux déjà reçus. Seul problème : l'orfèvre n'ouvrira qu'un seul maillon. Où l'inspecteur doit-il couper sa chaîne ?", '03_reponse': "La réponse : il coupe le troisième maillon ! Cela donne trois morceaux : un maillon seul, une chaîne de deux, et une chaîne de quatre. Premier soir, il donne le maillon seul. Deuxième soir, il donne la chaîne de deux, et reprend le maillon seul. Troisième soir, il redonne le maillon seul : trois en tout. Quatrième soir, il donne la chaîne de quatre, et reprend les deux petits morceaux. Et ainsi de suite ! C'est comme les poids un, deux, quatre : un seul maillon coupé suffit pour sept nuits."}
for k,t in SEG.items():
    if os.path.exists(f'{OUT}/{k}.wav'): continue
    time.sleep(4)
    body={"contents":[{"parts":[{"text":STYLE+chr(34)+t+chr(34)}]}],
      "generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"voiceConfig":{"prebuiltVoiceConfig":{"voiceName":VOICE}}}}}
    req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
      data=json.dumps(body).encode(),headers={"Content-Type":"application/json","x-goog-api-key":KEY})
    d=None
    for a in range(3):
        try:
            r=json.load(urllib.request.urlopen(req,timeout=150)); d=r['candidates'][0]['content']['parts'][0]['inlineData']['data']; break
        except Exception as e:
            print(k,'retry',a,str(e)[:100]); time.sleep(8)
    if d is None: continue
    pcm=base64.b64decode(d)
    with wave.open(f"{OUT}/{k}.wav","wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000); w.writeframes(pcm)
    print(k, round(len(pcm)/48000,2),'s')
