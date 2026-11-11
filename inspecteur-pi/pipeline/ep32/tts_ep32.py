import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Un voleur a mélangé toutes les étiquettes de l'entrepôt, et l'inspecteur n'a droit qu'à un seul fruit pour tout réparer ! Il y a trois caisses : une ne contient que des pommes, une ne contient que des oranges, et la dernière, un mélange des deux. Mais le voleur a remis les étiquettes, pommes, oranges et mélange, et pas une seule n'est à la bonne place. L'inspecteur peut piocher un seul fruit, dans une seule caisse, sans rien voir d'autre. Dans quelle caisse doit-il piocher ?", '03_reponse': "La réponse : la caisse marquée mélange ! Son étiquette est fausse, donc elle contient forcément un seul type de fruit. Si l'inspecteur en sort une pomme, c'est la caisse des pommes. Alors la caisse marquée oranges ne peut pas contenir d'oranges, ni de pommes, déjà trouvées : c'est le mélange ! Et la dernière, marquée pommes, contient donc les oranges. Un seul fruit, et tout est remis en ordre !"}
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
