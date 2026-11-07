import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Je te parie que dans cette salle, deux personnes fêtent leur anniversaire le même jour ! Dans la salle, il y a des invités, et chacun est né un jour au hasard de l'année. L'année compte trois cent soixante-cinq jours. Tu penses sûrement qu'il faut des centaines d'invités pour que ça arrive. Alors, combien d'invités faut-il, au minimum, pour avoir plus d'une chance sur deux que deux d'entre eux soient nés le même jour ?", '03_reponse': "La réponse : vingt-trois seulement ! Étonnant, non ? Avec vingt-trois invités, il y a deux cent cinquante-trois paires possibles. Chaque paire a une petite chance d'avoir le même anniversaire, et toutes ces chances s'additionnent ! Résultat : cinquante virgule sept pour cent. Avec cinquante-sept invités, on monte à quatre-vingt-dix-neuf pour cent. Et avec soixante-dix, c'est presque certain ! Notre cerveau compte les personnes, mais il oublie de compter les paires."}
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
