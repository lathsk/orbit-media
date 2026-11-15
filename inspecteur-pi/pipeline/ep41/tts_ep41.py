import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Un nombre magique attire tous les autres, et aucun ne lui échappe ! L'inspecteur te propose un tour de calcul étrange. Prends un nombre à quatre chiffres, pas tous identiques. Écris ses chiffres du plus grand au plus petit, puis du plus petit au plus grand. Soustrais le petit nombre au grand. Par exemple, avec trois mille cinq cent vingt-quatre, cinq mille quatre cent trente-deux moins deux mille trois cent quarante-cinq, ça fait trois mille quatre-vingt-sept. Maintenant, recommence avec le résultat, encore et encore. Quel que soit ton nombre de départ, tu finis toujours sur le même nombre ! Mais lequel ?", '03_reponse': "La réponse : six mille cent soixante-quatorze ! Avec trois mille cinq cent vingt-quatre, on obtient trois mille quatre-vingt-sept, puis huit mille trois cent cinquante-deux, puis six mille cent soixante-quatorze. Et là, plus rien ne bouge : sept mille six cent quarante et un moins mille quatre cent soixante-sept, ça redonne six mille cent soixante-quatorze ! Il se mord la queue. Et ce n'est pas de la chance : en sept étapes au plus, tous les nombres y arrivent. C'est le nombre de Kaprekar, un mathématicien indien !"}
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
