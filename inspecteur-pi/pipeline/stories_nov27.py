from render_e4x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-27/'; os.makedirs(D,exist_ok=True)
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
    numcard(dd,cx,128,'1 2 3 ... 100',CYAN,16)
    numcard(dd,cx,200,'100 PAGES',GOLD,18)
    T(dd,'? CHIFFRES',cx,284,40,'press',22,CORAL,align='c',shadow=(4,4,BLACK))
def a1(lay,dd):
    cx=SW/2
    numcard(dd,cx,118,'1 A 9 : 9 CHIFFRES',CYAN,11)
    numcard(dd,cx,172,'10 A 99 : 90 X 2 = 180',GOLD,10)
    numcard(dd,cx,226,'100 : 3 CHIFFRES',CORAL,11)
    arrow_d(dd,cx,276,20,CREAM)
    numcard(dd,cx,298,'9+180+3 = 192',GRN,14)
def q2(lay,dd):
    cx=SW/2
    for i,(v,c) in enumerate([('1. DOUBLE-LE',CYAN),('2. AJOUTE 10',GOLD),('3. DIVISE PAR 2',CORAL),('4. RETIRE TON NOMBRE',GRN)]):
        numcard(dd,cx,112+i*46,v,c,12)
    T(dd,'= ?',cx,296,34,'press',26,CORAL,align='c',shadow=(4,4,BLACK))
def a2(lay,dd):
    cx=SW/2
    vals=['7','14','24','12','5']
    for i,v in enumerate(vals):
        x=36+i*60; nb(dd,x,130,v,GRN if i==4 else GOLD,w=46,h=46,size=18)
        if i<4: arrow_r(dd,x+25,152,10,CREAM)
    lbl(dd,cx,196,'EXEMPLE AVEC 7',GREY,9)
    numcard(dd,cx,240,'TOUJOURS 5',GRN,22)
    lbl(dd,cx,300,'QUEL QUE SOIT TON NOMBRE',CREAM,9)
FOOT='RÉPONDS-MOI EN MESSAGE, JE TE DIS SI C’EST BON'
mk(q1,[('Un livre de ',CREAM),('100 pages',GOLD),(' : combien de ',CREAM),('chiffres',CORAL),(' pour les numéroter ?',CREAM)],'LE DÉFI',D+'q1.png',foot=FOOT)
mk(a1,[('Réponse : ',CREAM),('192',GOLD)],'LA RÉPONSE',D+'a1.png',foot='ON COMPTE LES CHIFFRES, PAS LES PAGES')
mk(q2,[('Pense à un ',CREAM),('nombre',CORAL),(' : quel résultat ?',CREAM)],'LE DÉFI',D+'q2.png',foot=FOOT)
mk(a2,[('Réponse : ',CREAM),('toujours 5',GOLD)],'LA RÉPONSE',D+'a2.png',foot='TON NOMBRE DISPARAÎT DANS LE CALCUL')
from PIL import Image
for k in ('q1','a1','q2','a2'):
    Image.open(D+k+'.png').convert('RGB').save(D+k+'.jpg',quality=93)
