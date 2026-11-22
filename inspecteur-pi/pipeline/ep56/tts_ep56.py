import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Choisis ton dé : tu vas perdre ! Trois dés spéciaux. Le dé rouge a des deux, des quatre et des neuf. Le dé cyan a des un, des six et des huit. Le dé or a des trois, des cinq et des sept. Tu choisis un dé, ton ami prend un des deux autres. Vous lancez, le plus grand nombre gagne. Qui a l'avantage ?", '03_reponse': "La réponse : ton ami ! Le rouge bat le cyan, cinq fois sur neuf. Le cyan bat l'or, cinq fois sur neuf. Et l'or bat le rouge, cinq fois sur neuf ! Quel que soit ton dé, il y en a un meilleur. Ton ami choisit après toi, et il gagne plus souvent. Le piège : croire qu'il existe un meilleur dé ! Envoie-la à quelqu'un qui va se tromper."}
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
