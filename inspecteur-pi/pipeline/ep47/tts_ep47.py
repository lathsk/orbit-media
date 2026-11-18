import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Combien de tours ? Tu vas te tromper ! L'inspecteur pose deux pièces identiques sur la table. L'une reste immobile. L'autre fait le tour de la première, en roulant sans glisser, comme une vraie roue sur une route, jusqu'à revenir à son point de départ. Pendant ce trajet, combien de fois la pièce qui roule tourne-t-elle sur elle-même ? Un tour, deux tours, ou plus ?", '03_reponse': 'La réponse : deux tours, et pas un seul ! Regarde le centre de la pièce qui roule. Il décrit un cercle deux fois plus grand que la pièce, donc deux fois plus long que son contour. Elle roule donc sur deux longueurs de son contour, et fait deux tours complets sur elle-même. Un tour vient du contour qu\'elle roule, et un tour de plus vient du trajet autour de l\'autre pièce. Teste avec deux pièces de monnaie : tu verras !', '04_fin': 'Tu avais trouvé ? Bravo ! Enregistre cette énigme pour la refaire plus tard. Abonne-toi ! Demain, une nouvelle énigme !'}
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
