import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Le feu d'artifice doit partir dans exactement quarante-cinq minutes, mais l'inspecteur n'a ni montre, ni horloge ! Il a seulement deux mèches et un briquet. Chaque mèche brûle en exactement une heure, mais pas à vitesse régulière : une moitié peut brûler vite, l'autre très lentement. Il ne peut donc pas couper une mèche en deux pour mesurer la moitié du temps. Comment l'inspecteur peut-il mesurer quarante-cinq minutes ?", '03_reponse': "La réponse : il allume la première mèche des deux bouts, et la seconde d'un seul bout, en même temps ! Avec deux flammes, la première brûle deux fois plus vite : elle s'éteint après exactement trente minutes. À cet instant, il reste trente minutes de seconde mèche. L'inspecteur allume alors son autre bout : les deux flammes se rejoignent en quinze minutes. Trente plus quinze, ça fait quarante-cinq minutes !"}
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
