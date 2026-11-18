import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Six piles d'affilée : rare ou normal ? L'inspecteur lance une pièce cent fois, et note chaque résultat. Pas de triche : à chaque lancer, c'est pile ou face, une chance sur deux. Il se demande : sur ces cent lancers, quelle est la chance de voir au moins six fois la même face d'affilée ? Six piles de suite, ou six faces de suite. Une chance sur dix ? Une sur deux ? Plus ?", '03_reponse': "La réponse : environ quatre-vingts pour cent ! À chaque lancer, une série de six peut commencer, avec une chance sur trente-deux. Et avec près de cent départs possibles, elle arrive presque toujours, environ quatre fois sur cinq. Ce qui semble rare est en réalité tout à fait normal : le hasard fabrique des séries ! Un humain qui invente des lancers évite presque toujours ces séries : c'est comme ça qu'on repère les faux !", '04_fin': "Tu avais trouvé ? Bravo ! Envoie cette énigme à quelqu'un qui va se tromper. Abonne-toi ! Demain, une nouvelle énigme !"}
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
