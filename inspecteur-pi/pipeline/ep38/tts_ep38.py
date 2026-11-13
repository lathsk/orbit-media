import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Une fortune à gagner, et il faut arriver le dernier ! Le vieux sultan a deux fils et un seul héritage. Il leur lance un défi : une course de chevaux jusqu'à l'oasis, et celui dont le cheval arrive le dernier hérite de tout. Alors chacun retient son cheval pour finir derrière l'autre. Ils avancent au pas, puis ils s'arrêtent, et le soleil se couche. Un sage s'approche, leur chuchote une seule phrase, et les deux frères partent au galop ! Que leur a dit le sage ?", '03_reponse': "La réponse : échangez vos chevaux ! Chacun monte le cheval de son frère. Maintenant, pour que son propre cheval arrive dernier, chacun doit arriver premier avec le cheval de l'autre. Alors plus personne ne ralentit : les deux frères galopent à toute vitesse ! Le piège, c'était de croire qu'il fallait ralentir. L'astuce, c'est de changer de monture, et la course reprend !"}
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
