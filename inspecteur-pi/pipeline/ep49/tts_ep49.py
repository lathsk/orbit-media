import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Zéro virgule neuf, neuf, neuf, égale un ? L'inspecteur écrit un zéro, une virgule, puis des neuf, encore des neuf, sans jamais s'arrêter. Ce nombre est très, très proche de un. Mais est-il vraiment égal à un ? Ou reste-t-il toujours un tout petit peu en dessous ? Réponds : égal, ou juste très proche ?", '03_reponse': "La réponse : c'est exactement égal ! Pas presque, pas à peu près : égal. Voici la preuve. Un tiers, c'est zéro virgule trois, trois, trois, à l'infini. Multiplie par trois : un tiers fois trois, ça fait un. Et zéro virgule trois, trois, trois, fois trois, ça fait zéro virgule neuf, neuf, neuf. Donc zéro virgule neuf, neuf, neuf, c'est un ! Autre preuve : entre ces deux nombres, tu ne peux placer aucun nombre. Et deux nombres sans rien entre eux, c'est le même nombre. Le piège : on croit que le nombre avance sans jamais arriver. Mais il est déjà arrivé !"}
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
