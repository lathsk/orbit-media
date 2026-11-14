import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Il a gagné une fortune avec un dé, puis il a commencé à perdre avec deux dés ! Au dix-septième siècle, un noble joueur propose ce pari : lancer un dé quatre fois, et sortir au moins un six. Il gagne souvent et il s'enrichit. Alors il invente un pari pareil : lancer deux dés vingt-quatre fois, et sortir au moins un double six. Son calcul semble parfait : le double six est six fois plus rare, mais il a six fois plus de lancers. Pourtant, il commence à perdre ! Quel est le piège ?", '03_reponse': "La réponse : le premier pari gagne, le second perd ! Pour le premier, calculons la chance de ne jamais sortir de six : cinq sixièmes, quatre fois de suite. Cela fait environ quarante-huit pour cent. Donc au moins un six : environ cinquante-deux pour cent. Pour le second, ne pas sortir de double six, c'est trente-cinq chances sur trente-six. Vingt-quatre fois de suite, cela fait environ cinquante et un pour cent. Donc au moins un double six : environ quarante-neuf pour cent. Le piège, c'était la règle de trois : les chances ne s'ajoutent pas, elles se multiplient !"}
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
