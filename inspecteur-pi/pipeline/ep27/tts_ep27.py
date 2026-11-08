import os, sys, json, base64, wave, urllib.request, time
KEY=os.environ['GKEY']
MODEL='gemini-2.5-flash-preview-tts'; VOICE='Puck'; OUT='voix'
os.makedirs(OUT,exist_ok=True)
STYLE="Say in an energetic, friendly, playful way: "
SEG={'01_histoire': "Attention, l'inspecteur n'a que deux œufs, et devant lui, un immeuble de cent étages ! Il doit trouver l'étage le plus haut d'où un œuf peut tomber sans se casser. Si l'œuf survit, il peut le ramasser et le relancer. Mais s'il casse, il est perdu pour toujours. Avec seulement deux œufs, combien de lancers faut-il, au minimum, pour être certain de trouver l'étage, même dans le pire des cas ?", '03_reponse': "La réponse : quatorze lancers ! L'astuce : le premier œuf monte par paliers. D'abord le quatorzième étage, puis le vingt-septième, puis le trente-neuvième, en réduisant le saut d'un étage à chaque fois. Dès qu'il casse, le second œuf vérifie les étages restants, un par un. Ainsi, on ne dépasse jamais quatorze lancers ! Et quatorze plus treize plus douze, jusqu'à un, ça fait cent cinq : de quoi couvrir les cent étages."}
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
