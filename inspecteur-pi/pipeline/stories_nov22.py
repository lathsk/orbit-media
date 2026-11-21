from render_e4x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-22/'; os.makedirs(D,exist_ok=True)
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
    vals=['1','4','9','16','?']
    for i,v in enumerate(vals):
        y=116+i*44; col=GOLD if v=='?' else (CYAN if i%2 else CORAL)
        nb(dd,SW/2,y,v,col,w=max(70,len(v)*20+40),h=34,size=16)
def a1(lay,dd):
    for i,v in enumerate(['1','4','9','16']):
        nb(dd,SW/2-99+i*66,126,v,CYAN if i%2 else CORAL,w=58,h=40,size=14)
    arrow_d(dd,SW/2,176,26,CREAM)
    nb(dd,SW/2,212,'25',GRN,w=120,h=56,size=26)
    lbl(dd,SW/2,286,'LES CARRÉS : 1x1, 2x2, 3x3, 4x4, 5x5',GREY,7)
def uparrow(dd,cx,top,h=120,col=CORAL):
    box(dd,cx-9,top+34,18,h-34,fill=col,border=DARK,bw=2)
    dd.polygon([((cx-34)*S,(top+38)*S),((cx+34)*S,(top+38)*S),(cx*S,top*S)],fill=col,outline=DARK)
def q2(lay,dd):
    uparrow(dd,SW/2,128,130)
    T(dd,'?',SW/2-80,200,60,'press',44,GOLD,align='c',shadow=(4,4,BLACK)); T(dd,'?',SW/2+80,200,60,'press',44,GOLD,align='c',shadow=(4,4,BLACK))
    lbl(dd,SW/2,276,'IL MONTE, MAIS NE REDESCEND JAMAIS',GOLD,7)
def a2(lay,dd):
    cx=SW/2
    box(dd,cx-70,230,140,54,fill=rgb('#C98A5A'),border=DARK,bw=3); box(dd,cx-70,226,140,12,fill=CREAM,border=DARK,bw=2)
    for i,x in enumerate((cx-40,cx,cx+40)):
        box(dd,x-3,196,7,30,fill=[CORAL,CYAN,GOLD][i],border=DARK,bw=1); box(dd,x-3,184,7,12,fill=GOLD if int(i)%2==0 else LGOLD)
    stamp(dd,cx,150,'TON ÂGE !',GRN,16)
    lbl(dd,cx,300,'IL MONTE CHAQUE ANNÉE',CORAL,9)
mk(q1,[('Quel est le ',CREAM),('nombre',GOLD),(' suivant ?',CREAM)],'LE DÉFI',D+'q1.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a1,[('Réponse : ',CREAM),('25',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='LES CARRÉS PARFAITS')
mk(q2,[('Qu’est-ce qui ',CREAM),('monte',CORAL),(' sans jamais ',CREAM),('redescendre',GOLD),(' ?',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a2,[('Réponse : ',CREAM),('ton âge',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='IL NE FAIT QUE MONTER')
from PIL import Image
for k in ('q1','a1','q2','a2'):
    Image.open(D+k+'.png').convert('RGB').save(D+k+'.jpg',quality=93)
