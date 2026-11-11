import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Demain à l'aube, dix prisonniers seront alignés en file, chacun avec un chapeau noir ou blanc posé au hasard sur la tête ! Chacun voit tous les chapeaux devant lui, mais jamais le sien, ni ceux de derrière. En partant du dernier de la file, chacun doit crier une seule fois, noir, ou blanc. Si le cri correspond à son chapeau, il est sauvé. Sinon, c'est fini. Ils peuvent se mettre d'accord cette nuit, mais ensuite, aucun autre mot, ils entendent juste les cris. Combien peuvent-ils sauver à coup sûr ?", '03_reponse': "La réponse : neuf sur dix ! Le dernier de la file compte les chapeaux blancs qu'il voit. S'il y en a un nombre pair, il crie blanc, sinon, il crie noir. Lui, il joue sa vie à pile ou face, mais il vient de donner le code. Son voisin compte à son tour les chapeaux blancs devant lui : si la parité est différente de celle annoncée, son chapeau est blanc, sinon, il est noir. Et chaque suivant fait pareil, en tenant compte des cris déjà entendus. Un seul est sacrifié, les neuf autres sont sauvés à coup sûr !"}
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
