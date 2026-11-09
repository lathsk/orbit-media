import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Cent casiers fermés dans un couloir, et l'inspecteur doit prédire lesquels resteront ouverts ! Cent élèves passent un par un. Le premier ouvre tous les casiers. Le deuxième change un casier sur deux : s'il est ouvert, il le ferme, s'il est fermé, il l'ouvre. Le troisième change un casier sur trois, et ainsi de suite, jusqu'au centième élève. Quand tout le monde est passé, combien de casiers restent ouverts ?", '03_reponse': "La réponse : dix casiers ! Chaque casier est touché autant de fois que son nombre de diviseurs. Le casier douze, par exemple, est touché par un, deux, trois, quatre, six et douze : six fois, donc il finit fermé. Les diviseurs vont presque toujours par paires. Sauf pour un carré parfait, comme neuf, trois fois trois : un diviseur n'a pas de partenaire. Le nombre de passages n'est pas pair, donc le casier reste ouvert ! Ce sont les casiers un, quatre, neuf, seize, vingt-cinq, trente-six, quarante-neuf, soixante-quatre, quatre-vingt-un et cent."}
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
