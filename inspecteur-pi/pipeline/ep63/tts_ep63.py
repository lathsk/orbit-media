import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Un seul pour cent change tout ! Un marchand a cent kilos de pommes de terre. Elles contiennent quatre-vingt-dix-neuf pour cent d'eau. Il les laisse sécher au soleil. Maintenant, elles contiennent quatre-vingt-dix-huit pour cent d'eau. Seulement un point de moins ! Combien pèsent-elles maintenant ?", '03_reponse': "La réponse : cinquante kilos ! Pas quatre-vingt-dix-neuf. Regarde la matière sèche : dans cent kilos, un pour cent, c'est un seul kilo. Ce kilo ne disparaît pas quand l'eau s'évapore. À la fin, il représente deux pour cent du total, puisqu'il reste quatre-vingt-dix-huit pour cent d'eau. Un kilo, c'est deux pour cent de cinquante kilos. Le poids a été divisé par deux ! Le piège : regarder l'eau, pas la matière sèche. Enregistre cette énigme pour la refaire plus tard."}
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
