import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Un marchand de l'ancien temps ne possède qu'une balance à deux plateaux, et il doit pouvoir peser n'importe quelle masse entière, de un à quarante kilos ! Mais il n'a que quatre poids. Il peut les poser sur les deux plateaux, même du côté de la marchandise. Tu penses sûrement qu'il faut au moins six ou sept poids. Alors, quels quatre poids doit-il choisir pour tout peser jusqu'à quarante kilos ?", '03_reponse': "La réponse : un, trois, neuf et vingt-sept kilos ! Chaque poids vaut trois fois le précédent. Pour peser deux kilos, le marchand met la marchandise avec le poids de un kilo, et le poids de trois kilos de l'autre côté : trois moins un, égale deux. Pour cinq kilos : neuf d'un côté, trois et un avec la marchandise, car neuf moins quatre, égale cinq. Et un plus trois plus neuf plus vingt-sept, ça fait exactement quarante !"}
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
