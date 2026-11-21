import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Où est passé l'euro manquant ? Trois amis paient dix euros chacun pour une chambre d'hôtel. Trente euros en tout. Mais la chambre ne coûte que vingt-cinq euros ! Le groom leur rapporte cinq euros. Il en garde deux, et rend un euro à chacun. Chaque ami a donc payé neuf euros, soit vingt-sept en tout. Avec les deux euros du groom, ça fait vingt-neuf. Mais ils avaient donné trente ! Où est passé l'euro manquant ?", '03_reponse': "La réponse : il n'y a aucun euro manquant ! Le calcul est faux dès le départ. Les amis ont payé vingt-sept euros. Et ces vingt-sept euros contiennent déjà les deux euros du groom : vingt-cinq pour la chambre, plus deux pour lui. On ne doit pas additionner les deux euros, on doit les retirer ! Pour retrouver trente, il faut compter : vingt-cinq pour la chambre, deux pour le groom, et trois rendus aux amis. Le piège : on additionne des sommes qui ne vont pas ensemble !"}
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
