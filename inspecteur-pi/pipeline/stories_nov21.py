from render_e4x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-21/'; os.makedirs(D,exist_ok=True)
def mk(fn,head,label,out,foot=None,t=0.0):
    def f(lay,dd):
        fn(lay,dd)
        if foot:
            B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); f_=F('silk4',11); T(d2,foot,SW/2-tw(foot,f_,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    lay=B.make_scene(f,t,head=head)
    B.frame_with(lay,label).save(out)
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-18: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')

def q1(lay,dd):
    vals=['2','3','5','7','11','?']
    for i,v in enumerate(vals):
        y=112+i*36; col=GOLD if v=='?' else (CYAN if i%2 else CORAL)
        nb(dd,SW/2,y,v,col,w=max(70,len(v)*20+40),h=30,size=14)
def a1(lay,dd):
    for i,v in enumerate(['2','3','5','7','11']):
        nb(dd,SW/2-108+i*54,126,v,CYAN if i%2 else CORAL,w=48,h=40,size=14)
    arrow_d(dd,SW/2,176,26,CREAM)
    nb(dd,SW/2,212,'13',GRN,w=120,h=56,size=26)
    lbl(dd,SW/2,286,'DIVISIBLES SEULEMENT PAR 1 ET EUX-MÊMES',GREY,7)
def roof(dd,dx=0):
    dd.polygon([(60*S,330*S),(SW/2*S,226*S),(260*S,330*S)],fill=rgb('#8A4A3A'),outline=rgb('#4A2A22'))
    dd.polygon([(60*S,330*S),(260*S,330*S),(260*S,336*S),(60*S,336*S)],fill=rgb('#4A2A22'))
def egg(dd,x,y):
    dd.ellipse([(x-14)*S,(y-18)*S,(x+14)*S,(y+18)*S],fill=CREAM,outline=rgb('#C9B78F'),width=3*S)
def q2(lay,dd):
    roof(dd); egg(dd,SW/2,206)
    T(dd,'?',60,150,60,'press',44,CORAL,align='c',shadow=(4,4,BLACK)); T(dd,'?',260,150,60,'press',44,CYAN,align='c',shadow=(4,4,BLACK))
    arrow_r(dd,100,214,34,CORAL) if False else None
    lbl(dd,SW/2,118,'UN ŒUF SUR UN TOIT POINTU',GOLD,8)
def a2(lay,dd):
    roof(dd)
    stamp(dd,SW/2,150,'UN COQ NE POND PAS !',GRN,14)
    lbl(dd,SW/2,196,'IL N’Y A PAS D’ŒUF',CORAL,9)
mk(q1,[('Quel est le ',CREAM),('nombre',GOLD),(' suivant ?',CREAM)],'LE DÉFI',D+'q1.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a1,[('Réponse : ',CREAM),('13',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='LES NOMBRES PREMIERS')
mk(q2,[('Un coq pond un œuf,',CORAL),(' de quel ',CREAM),('côté',GOLD),(' tombe-t-il ?',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a2,[('Réponse : ',CREAM),('aucun',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='UN COQ NE PEUT PAS PONDRE')
from PIL import Image
for k in ('q1','a1','q2','a2'):
    Image.open(D+k+'.png').convert('RGB').save(D+k+'.jpg',quality=93)
