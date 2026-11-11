import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Ton test vient de tomber : positif à une maladie rare, et le médecin a l'air inquiet ! Mais attends avant de paniquer. Cette maladie touche une personne sur mille. Le test est fiable : il repère quatre-vingt-dix-neuf malades sur cent. Mais il se trompe aussi chez une personne en bonne santé sur cent, et la déclare malade à tort. Toi, tu as passé le test, et il est positif. Quelle est la chance que tu sois vraiment malade ?", '03_reponse': "La réponse : environ neuf pour cent seulement ! Imagine mille personnes testées. Une seule est vraiment malade, et son test est positif. Parmi les neuf cent quatre-vingt-dix-neuf en bonne santé, une sur cent se trompe : ça fait environ dix faux positifs. Donc onze tests positifs, mais un seul vrai malade. Une chance sur onze, c'est moins de dix pour cent ! Comme la maladie est très rare, les erreurs du test sont plus nombreuses que les vrais malades."}
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
