import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Cent candidats, une seule chance de trouver le meilleur ! L'inspecteur cherche un assistant. Les cent candidats passent un par un devant lui, dans un ordre aléatoire. Après chaque entretien, il doit répondre tout de suite : oui, ou non. Un refus est définitif, et dès qu'il dit oui, c'est terminé. Il peut comparer avec les candidats déjà vus, mais il ne connaît pas ceux qui arrivent après. Choisir au hasard, ça donne une chance sur cent. Quelle stratégie lui donne le plus de chances de choisir le meilleur des cent ?", '03_reponse': "La réponse : refuser les trente-sept premiers, quoi qu'il arrive ! Mais garde en tête le meilleur d'entre eux. Ensuite, choisis le premier candidat qui bat tous ceux que tu as déjà vus. Cette méthode trouve le meilleur dans trente-sept pour cent des cas, contre un pour cent au hasard ! Pourquoi trente-sept ? C'est environ cent divisé par deux virgule sept un huit, un nombre célèbre en maths. Si tu refuses trop peu, tu choisis trop vite. Si tu refuses trop, le meilleur est déjà passé !"}
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
