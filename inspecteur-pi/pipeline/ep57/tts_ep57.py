import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Cent pièces, cinq pirates : combien garde le chef ? Cinq pirates doivent se partager cent pièces d'or. Le chef propose un partage. Tout le monde vote. Si au moins la moitié dit oui, le partage est adopté. Sinon, le chef est jeté à l'eau, et le pirate suivant propose à son tour. Chaque pirate veut le plus d'or possible. À gain égal, il préfère voir le chef à l'eau. Combien de pièces le chef peut-il garder ?", '03_reponse': "La réponse : quatre-vingt-dix-huit pièces ! Pour le comprendre, on commence par la fin. S'il ne reste que les pirates quatre et cinq, le quatrième prend tout : son propre vote suffit. À trois, le troisième donne une pièce au cinquième, qui sinon n'aurait rien. À quatre, le deuxième donne une pièce au quatrième. Et à cinq, le chef offre une pièce au troisième et une au cinquième. Ils n'auraient rien eu sinon : ils votent oui ! Le chef garde quatre-vingt-dix-huit pièces. Le piège : croire à un partage égal. Enregistre cette énigme pour la refaire plus tard."}
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
