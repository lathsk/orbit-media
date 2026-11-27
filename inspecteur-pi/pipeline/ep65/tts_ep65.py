import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Coupe cette horloge, même somme des deux côtés ! Un seul trait droit sépare l'horloge en deux morceaux. Les nombres de chaque morceau, additionnés, doivent donner exactement le même total. Par où passe le trait ?", '03_reponse': "La réponse : entre le trois et le quatre, et entre le neuf et le dix ! Tous les nombres de l'horloge font soixante-dix-huit, donc chaque morceau doit valoir trente-neuf. Le piège : couper en deux côtés donne vingt et un contre cinquante-sept. Mais décale le trait d'un cran, et le total gagne six. Vingt et un, vingt-sept, trente-trois, trente-neuf ! Quatre plus cinq plus six plus sept plus huit plus neuf, ça fait trente-neuf. Enregistre cette énigme pour la refaire plus tard."}
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
