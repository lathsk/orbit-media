import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': 'Trois coups de couteau : combien de parts ? Voici une pizza bien ronde. Tu la coupes avec trois coups de couteau droits, pas un de plus. Tu peux couper où tu veux. Mais tu ne déplaces jamais les morceaux. Au maximum, combien de parts peux-tu obtenir ?', '03_reponse': "La réponse : sept parts ! Beaucoup disent six, en coupant trois fois par le centre. Mais regarde : le premier coup donne deux parts. Le deuxième croise le premier, et ça fait quatre. Le troisième doit croiser les deux autres, loin du centre : il traverse trois morceaux, et coupe chacun en deux. Quatre plus trois, ça fait sept ! Et ça continue : le quatrième coup ajoute quatre parts, donc onze. Chaque coup ajoute son numéro de parts. Envoie-la à quelqu'un qui va se tromper."}
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
