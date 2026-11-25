import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Une case est apparue de nulle part ! Voici un carré de huit sur huit : soixante-quatre cases. On le coupe en quatre morceaux. On les réarrange en rectangle : treize sur cinq. Cinq fois treize : soixante-cinq cases ! D'où vient la case en plus ?", '03_reponse': "La réponse : les morceaux ne collent pas ! Le long de la diagonale, il reste une fente très fine, presque invisible. Cette fente fait exactement une case. Les pentes sont presque égales : deux cinquièmes, et trois huitièmes. Presque, mais pas tout à fait ! Ces nombres viennent de la suite de Fibonacci : trois, cinq, huit, treize. Les morceaux couvrent soixante-quatre cases, la fente vide fait la soixante-cinquième. Le piège : croire que la diagonale est une vraie droite. Envoie-la à quelqu'un qui va se tromper."}
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
