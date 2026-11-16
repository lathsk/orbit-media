import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Trois fourmis, un triangle, et une collision presque certaine ! Une fourmi est posée sur chaque coin d'un triangle. En même temps, chacune choisit au hasard l'un des deux autres coins, et part tout droit le long du côté. Si deux fourmis se croisent sur un même côté, elles se rencontrent : c'est la collision. Chaque fourmi choisit sa direction à pile ou face. Quelle est la probabilité qu'aucune fourmi ne rencontre une autre ?", '03_reponse': "La réponse : une chance sur quatre ! Chaque fourmi a deux choix, donc il y a huit façons de partir. Pour éviter toute collision, il faut que les trois fourmis tournent dans le même sens. Soit toutes dans le sens des aiguilles d'une montre, soit toutes dans l'autre sens. Ça ne fait que deux cas sur huit, donc vingt-cinq pour cent ! Autrement dit, il y a trois chances sur quatre que deux fourmis se rencontrent !"}
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
