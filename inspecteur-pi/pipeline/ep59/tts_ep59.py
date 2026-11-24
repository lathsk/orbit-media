import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': 'Ta première réponse sera fausse ! Une batte et une balle coûtent un euro dix en tout. La batte coûte un euro de plus que la balle. Combien coûte la balle ?', '03_reponse': "La réponse : cinq centimes ! Si tu as dit dix, tu es en bonne compagnie : même des étudiants de grandes universités se trompent ici. Ton cerveau a crié dix centimes. Mais alors la batte coûterait un euro dix, et le total monterait à un euro vingt. Dessine-le : la batte, c'est la balle plus un euro. Donc deux balles plus un euro font un euro dix. Enlève l'euro : il reste dix centimes pour deux balles. Une balle coûte cinq centimes ! La batte coûte un euro cinq. Vérifie : le total fait un euro dix, et l'écart est bien d'un euro. Le piège : couper un euro dix en un euro plus dix centimes. Enregistre cette énigme pour la refaire plus tard."}
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
