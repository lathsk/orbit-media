import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Presque tout le monde se trompe ici ! L'inspecteur doit monter une colline d'un kilomètre. Il la grimpe à trente kilomètres par heure, pas plus vite. Mais il veut faire soixante de moyenne sur tout l'aller-retour : la montée et la descente ! À quelle vitesse doit-il redescendre ? Réfléchis bien : ce n'est pas si simple.", '02_defi': 'Mets la vidéo en pause : tu as cinq secondes. Écris ta réponse en commentaire !', '03_reponse': "La réponse : c'est impossible ! Beaucoup répondent quatre-vingt-dix, mais c'est faux. L'aller-retour fait deux kilomètres. À soixante de moyenne, il faut deux minutes en tout, pas une de plus. Or, monter un kilomètre à trente à l'heure prend déjà deux minutes ! Il ne reste plus une seconde pour redescendre. Même en descendant à quatre-vingt-dix, il ne ferait que quarante-cinq de moyenne. Et même en tombant comme une pierre, il n'atteindrait jamais soixante. Le piège : la moyenne se calcule avec le temps, pas avec les vitesses !", '04_fin': 'Tu avais trouvé ? Bravo ! Enregistre cette énigme pour la refaire plus tard. Abonne-toi ! Demain, une nouvelle énigme !'}
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
