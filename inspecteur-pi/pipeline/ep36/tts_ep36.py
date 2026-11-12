import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Un café à payer, une pièce truquée, et un tirage qui doit être parfaitement équitable ! L'inspecteur et son ami veulent tirer au sort celui qui paiera. Mais la seule pièce disponible est truquée : elle tombe plus souvent d'un côté que de l'autre, et personne ne sait lequel. Si l'inspecteur choisit pile, il risque d'être désavantagé. Comment obtenir quand même un tirage au sort juste, cinquante-cinquante, avec cette pièce truquée ?", '03_reponse': "La réponse : on lance la pièce deux fois de suite ! Pile puis face, l'inspecteur gagne. Face puis pile, c'est son ami qui gagne. Et si les deux lancers sont identiques, on recommence. Pourquoi ça marche ? Imaginons que pile sorte sept fois sur dix. Pile puis face, c'est sept dixièmes fois trois dixièmes. Face puis pile, c'est trois dixièmes fois sept dixièmes. C'est exactement pareil ! Les deux camps ont la même chance."}
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
