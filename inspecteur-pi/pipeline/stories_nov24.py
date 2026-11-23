from render_e4x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-24/'; os.makedirs(D,exist_ok=True)
def mk(fn,head,label,out,foot=None,t=0.0):
    def f(lay,dd):
        fn(lay,dd)
        if foot:
            B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); fs=11
            while fs>6 and tw(foot,F('silk4',fs),1)>SW-16: fs-=1
            f_=F('silk4',fs); T(d2,foot,SW/2-tw(foot,f_,1)/2,SH-30,14,'silk4',fs,CREAM,sp=1)
    lay=B.make_scene(f,t,head=head)
    B.frame_with(lay,label).save(out)
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-18: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')


def q1(lay,dd):
    cx=SW/2
    for i,x in enumerate((cx-84,cx,cx+84)): nb(dd,x,150,'9',[GOLD,CYAN,CORAL][i],w=64,h=70,size=40)
    T(dd,'?',cx,252,60,'press',50,GOLD,align='c',shadow=(4,4,BLACK))
    lbl(dd,cx,320,'TU PEUX UTILISER DES PUISSANCES',CREAM,8)
def a1(lay,dd):
    cx=SW/2
    T(dd,'9',cx-62,170,100,'press',80,GOLD,align='c',shadow=(5,5,BLACK))
    T(dd,'9',cx+8,150,70,'press',50,CYAN,align='c',shadow=(4,4,BLACK))
    T(dd,'9',cx+52,126,50,'press',34,CORAL,align='c',shadow=(3,3,BLACK))
    lbl(dd,cx,262,'9 PUISSANCE (9 PUISSANCE 9)',CREAM,8)
    stamp(dd,cx,300,'PLUS DE 369 MILLIONS DE CHIFFRES',GRN,7)
def q2(lay,dd):
    cx=SW/2
    rows=[('1','5',CORAL),('2','25',CYAN),('3','125',CORAL),('4','625',CYAN),('5','?',GOLD)]
    for i,(a,b,c) in enumerate(rows):
        y=112+i*50
        nb(dd,cx-80,y,a,c,w=56,h=42,size=22); T(dd,'=',cx-34,y+8,26,'press',20,CREAM,align='c'); nb(dd,cx+46,y,b,c,w=100,h=42,size=22)
def a2(lay,dd):
    cx=SW/2
    nb(dd,cx-80,128,'1',CORAL,w=56,h=48,size=26); T(dd,'=',cx-34,138,26,'press',20,CREAM,align='c'); nb(dd,cx+46,128,'5',CORAL,w=100,h=48,size=26)
    arrow_d(dd,cx,184,26,CREAM)
    nb(dd,cx-80,226,'5',GRN,w=56,h=48,size=26); T(dd,'=',cx-34,236,26,'press',20,CREAM,align='c'); nb(dd,cx+46,226,'1',GRN,w=100,h=48,size=26)
    lbl(dd,cx,300,'LA 1RE LIGNE DIT : 1 = 5',CORAL,9)
FOOT='RÉPONDS-MOI EN MESSAGE, JE TE DIS SI C’EST BON'
mk(q1,[('Avec ',CREAM),('trois 9',GOLD),(', quel est le plus ',CREAM),('grand nombre',CORAL),(' ?',CREAM)],'LE DÉFI',D+'q1.png',foot=FOOT)
mk(a1,[('Réponse : ',CREAM),('9',GOLD),(' puissance ',CREAM),('9',CYAN),(' puissance ',CREAM),('9',CORAL)],'LA RÉPONSE',D+'a1.png',foot='PAS 999 : UN NOMBRE GIGANTESQUE')
mk(q2,[('Si 1 = 5, 2 = 25, 3 = 125, 4 = 625… ',CREAM),('5 = ?',GOLD)],'LE DÉFI',D+'q2.png',foot=FOOT)
mk(a2,[('Réponse : ',CREAM),('1',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='SI 1 = 5, ALORS 5 = 1')
from PIL import Image
for k in ('q1','a1','q2','a2'):
    Image.open(D+k+'.png').convert('RGB').save(D+k+'.jpg',quality=93)
