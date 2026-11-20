import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Plus cinquante pour cent, puis moins cinquante ? L'inspecteur repère un manteau à cent euros. Le marchand augmente le prix de cinquante pour cent. Puis il fait des soldes : moins cinquante pour cent ! Presque tout le monde pense retrouver cent euros. Mais est-ce vraiment le cas ? Quel est le prix final du manteau ?", '03_reponse': "La réponse : soixante-quinze euros ! D'abord, cent euros plus cinquante pour cent, ça fait cent cinquante euros. Ensuite, moins cinquante pour cent... mais de cent cinquante euros, pas de cent ! La moitié de cent cinquante, c'est soixante-quinze. Le manteau coûte donc vingt-cinq euros de moins qu'au départ. Le piège : les deux pourcentages ne portent pas sur le même prix ! Pour revenir à cent euros, il faudrait remonter d'un tiers."}
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
