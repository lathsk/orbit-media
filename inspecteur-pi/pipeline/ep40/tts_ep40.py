import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Un gâteau, un couteau, et un casse-tête redoutable ! Un pâtissier doit couper un gros gâteau en forme de cube en vingt-sept petits cubes identiques. Sa méthode : deux coups de couteau dans chaque direction, soit six coups en tout. Mais il est malin : après chaque coup, il peut déplacer et empiler les morceaux pour en couper plusieurs d'un seul coup ! Peut-il faire mieux que six coups ? Combien de coups de couteau, au minimum ?", '03_reponse': "La réponse : six coups, pas un de moins ! Regarde le petit cube du centre : il est caché au cœur du gâteau, aucune de ses faces n'est visible. Il a six faces, et seul le couteau peut les créer. Or un coup de couteau ne crée qu'une seule face de ce cube. Il faut donc au moins six coups. Déplacer les morceaux ne change rien ! Le piège, c'était de croire qu'empiler économise des coups. Mais le cube du centre en demande toujours six !"}
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
