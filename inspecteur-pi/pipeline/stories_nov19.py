from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-19/'; os.makedirs(D,exist_ok=True)
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
    for i,(x,l,c) in enumerate(((56,'BOUGIE',GOLD),(156,'LAMPE',CYAN),(256,'CHEMINÉE',CORAL))):
        nb(dd,x,124,'?',c,w=84,h=56,size=26) if False else box(dd,x-42,124,84,52,fill=CARD,border=c,bw=3,shadow=(3,3,BLACK)); T(dd,l,x,144,14,'press',8 if len(l)>6 else 10,c,align='c')
    stick(dd,SW/2,214,h=62,head=CORAL); lbl(dd,SW/2,286,'1 SEULE ALLUMETTE',CREAM,10)
    lbl(dd,SW/2,322,'JE TE DIS SI C’EST BON',CYAN,9)
def a1(lay,dd):
    stick(dd,SW/2,140,h=70,head=CORAL,hl=True)
    nb(dd,SW/2,236,'L’ALLUMETTE',GRN,w=250,h=50,size=20)
    lbl(dd,SW/2,322,'SANS ELLE, RIEN NE S’ALLUME',GOLD,9)
def q2(lay,dd):
    toks='7 + 7 / 7 + 7 x 7 - 7'.split()
    for i,c in enumerate(toks[:5]): nb(dd,SW/2+(i-2)*52,130,c,GOLD if c.isdigit() else CORAL,w=44,h=50,size=22)
    for i,c in enumerate(toks[5:]): nb(dd,SW/2+(i-2.5)*46,196,c,GOLD if c.isdigit() else CORAL,w=40,h=50,size=22)
    nb(dd,SW/2,262,'= ?',CYAN,w=120,h=48,size=26)
    lbl(dd,SW/2,322,'JE TE DIS SI C’EST BON',CYAN,9)
def a2(lay,dd):
    nb(dd,SW/2,118,'7 / 7 = 1',GOLD,w=250,h=44,size=18)
    nb(dd,SW/2,172,'7 x 7 = 49',CYAN,w=250,h=44,size=18)
    nb(dd,SW/2,226,'7+1+49-7 = 50',GRN,w=290,h=50,size=18)
    lbl(dd,SW/2,322,'× ET ÷ AVANT + ET -',CORAL,9) if False else lbl(dd,SW/2,322,'x ET / AVANT + ET -',CORAL,9)
mk(q1,[('Une ',CREAM),('allumette',GOLD),(' : bougie, ',CREAM),('lampe',GOLD),(' ou ',CREAM),('cheminée',CORAL),(' ?',CREAM),(' ',CREAM),('Qu’allumes-tu',CORAL),(' d’abord ?',CREAM)],'LE DÉFI',D+'q1.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a1,[('Réponse : ',CREAM),('l’allumette',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='LE PIÈGE : LE FEU D’ABORD')
mk(q2,[('Combien font ',CREAM),('7+7/7+7x7-7',GOLD),(' ?',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a2,[('Réponse : ',CREAM),('50',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='LA MULTIPLICATION D’ABORD')
