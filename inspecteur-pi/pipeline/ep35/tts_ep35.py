import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Un seul geste, et le niveau du lac va changer… ou pas ! L'inspecteur est seul sur une barque, au milieu d'un lac bien calme, avec une énorme pierre posée à bord. Sur la rive, une règle graduée indique le niveau de l'eau. Il pousse la pierre par-dessus bord : plouf ! Elle coule tout au fond. Alors, une fois la pierre dans l'eau, le niveau du lac monte, descend, ou ne bouge pas ?", '03_reponse': "Le niveau du lac descend ! Voici pourquoi. Dans la barque, la pierre pèse sur elle : la barque s'enfonce et pousse une quantité d'eau qui pèse autant que la pierre. Or la pierre est bien plus lourde que l'eau, à volume égal. Cette eau poussée est donc bien plus grande que la pierre elle-même ! Par exemple, une pierre de mille kilos fait pousser mille litres d'eau dans la barque, mais seulement environ trois cent soixante-dix litres au fond. Moins d'eau poussée, donc le niveau baisse !"}
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
