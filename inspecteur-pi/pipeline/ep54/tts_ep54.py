import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Une mouche, deux trains : combien de kilomètres ? Deux trains sont à cent kilomètres l'un de l'autre. Ils roulent l'un vers l'autre, à cinquante kilomètres à l'heure chacun. Une mouche part du premier train, à soixante-quinze kilomètres à l'heure. Elle file vers l'autre train, fait demi-tour, et repart, encore et encore, jusqu'à ce que les trains se rencontrent. Quelle distance totale parcourt la mouche ?", '03_reponse': "La réponse : soixante-quinze kilomètres ! Oublie tous les demi-tours de la mouche. Les deux trains se rapprochent de cent kilomètres à l'heure, car chacun fait cinquante. Ils sont à cent kilomètres : ils se rencontrent donc en une heure. Pendant ce temps, la mouche vole sans s'arrêter, à soixante-quinze kilomètres à l'heure. En une heure, elle parcourt soixante-quinze kilomètres. Le piège : inutile d'additionner une infinité de trajets, il suffit de compter le temps !"}
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
