import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Sept ponts, une règle : peux-tu y arriver ? L'inspecteur visite la ville de Königsberg. Une rivière entoure une île et sépare deux rives : cela fait quatre zones, reliées par sept ponts. Il veut se promener en traversant chaque pont exactement une fois, ni plus, ni moins, en partant d'où il veut. Peut-il y arriver ?", '03_reponse': "La réponse : c'est impossible ! Le génie Euler l'a prouvé en dix-sept cent trente-six, et il a inventé la théorie des graphes. Regarde les quatre zones de la ville. Elles touchent cinq, trois, trois et trois ponts. Quand on traverse une zone, on entre par un pont et on sort par un autre : les ponts se consomment par deux. Seules la zone de départ et celle d'arrivée peuvent avoir un nombre impair de ponts. Ici, les quatre sont impaires : c'est impossible !", '04_fin': "Tu avais trouvé ? Bravo ! Envoie cette énigme à quelqu'un qui va se tromper. Abonne-toi ! Demain, une nouvelle énigme !"}
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
