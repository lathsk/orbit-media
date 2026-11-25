import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Neuf personnes sur dix se trompent ici ! Quatre cartes sont posées sur la table. Chacune a une lettre d'un côté, et un nombre de l'autre. Tu vois : E, K, quatre, et sept. La règle : derrière une voyelle, il y a toujours un nombre pair. Quelles cartes faut-il retourner pour vérifier la règle ?", '03_reponse': 'La réponse : le E et le sept ! Beaucoup disent E et quatre. Mais le quatre est inutile : même une consonne derrière ne casse pas la règle. Le K aussi : la règle ne dit rien sur les consonnes. Le E, lui, doit cacher un nombre pair : on le retourne. Et le sept ! Si une voyelle se cache derrière, la règle est fausse. Retourne donc le E et le sept. Le piège : chercher à confirmer la règle, au lieu de chercher à la casser. Enregistre cette énigme pour la refaire plus tard.'}
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
