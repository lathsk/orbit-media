import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Deux enfants, dont une fille : et l'autre ? L'inspecteur rencontre une famille avec deux enfants. Il sait seulement une chose : ce ne sont pas deux garçons. Autrement dit, il y a au moins une fille. Presque tout le monde répond : une chance sur deux que l'autre soit aussi une fille. Mais est-ce vraiment juste ? Quelle est la chance que les deux enfants soient des filles ?", '03_reponse': "La réponse : une chance sur trois ! Note les deux enfants dans l'ordre, du plus grand au plus petit. Il y a quatre familles possibles : fille-fille, fille-garçon, garçon-fille, et garçon-garçon. Mais l'inspecteur sait que ce n'est pas garçon-garçon. Il reste trois familles, toutes aussi probables. Une seule des trois a deux filles. Donc une chance sur trois, pas une sur deux ! Le piège : fille-garçon et garçon-fille sont deux cas bien différents."}
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
