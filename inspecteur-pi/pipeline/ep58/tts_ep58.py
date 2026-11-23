import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Tes amis ont plus d'amis que toi ! Vrai ou faux ? Imagine un village. Chaque habitant compte ses amis. Puis il regarde chacun de ses amis, et compte combien d'amis il a. Il fait la moyenne de tout ça. Alors : en moyenne, nos amis ont-ils plus d'amis que nous ?", '03_reponse': "La réponse : vrai ! Prenons un village de cinq personnes : une star qui connaît tout le monde, et quatre villageois qui ne connaissent que la star. Chaque villageois n'a qu'un seul ami : la star, qui en a quatre ! En moyenne, on a un virgule six ami, mais nos amis en ont trois virgule quatre. La raison : une star compte parmi les amis de beaucoup de monde, donc on tombe sur elle bien plus souvent. Et ça marche dans presque tous les groupes de gens : une école, un village, un réseau social. Le piège : croire que tes amis te ressemblent. Envoie-la à quelqu'un qui va se tromper."}
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
