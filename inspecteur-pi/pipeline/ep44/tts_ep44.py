import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "L'inspecteur lit dans tes pensées, ou presque ! Choisis un nombre à quatre chiffres. Mélange ses chiffres pour en faire un autre nombre. Soustrais le plus petit au plus grand. Barre un chiffre du résultat, mais pas un zéro, puis annonce à l'inspecteur les chiffres qui restent. Il devine aussitôt le chiffre que tu as barré ! Comment fait-il ?", '03_reponse': "La réponse : le résultat est toujours un multiple de neuf ! Quand tu mélanges les chiffres d'un nombre, la différence est divisible par neuf. Et dans un multiple de neuf, la somme des chiffres est aussi un multiple de neuf. Exemple : six mille quatre cent quatre-vingt-trois, moins trois mille huit cent soixante-quatre, ça fait deux mille six cent dix-neuf. Si tu barres le six, il reste deux, un et neuf, qui font douze. Pour arriver à dix-huit, il manque six ! L'inspecteur complète simplement jusqu'au multiple de neuf suivant."}
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
