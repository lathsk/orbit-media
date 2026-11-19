import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Combien de carrés sur un échiquier ? L'inspecteur observe un échiquier : huit cases sur huit. Presque tout le monde répond soixante-quatre. Mais regarde bien : il y a aussi de plus grands carrés, formés de plusieurs cases ! Deux cases sur deux, trois sur trois, jusqu'au grand carré de huit sur huit. Au total, combien de carrés peux-tu compter sur cet échiquier ?", '03_reponse': "La réponse : deux cent quatre ! D'abord, soixante-quatre petits carrés d'une case. Puis des carrés de deux cases sur deux : il y en a quarante-neuf, car on peut les placer à sept endroits en largeur, et sept en hauteur. Ensuite, trente-six carrés de trois sur trois, vingt-cinq de quatre sur quatre, seize, neuf, quatre, et un seul grand carré de huit sur huit. Soixante-quatre, plus quarante-neuf, plus trente-six, plus vingt-cinq, plus seize, plus neuf, plus quatre, plus un : deux cent quatre ! Le piège : on ne compte que les petites cases, mais les grands carrés comptent aussi !"}
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
