from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-12/'; os.makedirs(D,exist_ok=True)
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
    nb(dd,116,124,'?',CORAL,w=70,h=80,size=44); nb(dd,196,124,'?',CORAL,w=70,h=80,size=44)
    T(dd,'2 CHIFFRES',250,138,16,'silk7',9,CREAM,align='c',sp=1) if False else None
    lbl(dd,SW/2,226,'SOMME DES CHIFFRES = 9',CYAN,11)
    lbl(dd,SW/2,262,'ON LES INVERSE : + 27',GOLD,11)
    nb(dd,SW/2,296,'QUEL NOMBRE ?',CORAL,w=240,h=36,size=14)
def a1(lay,dd):
    nb(dd,116,118,'3',GOLD,w=70,h=80,size=44); nb(dd,196,118,'6',GOLD,w=70,h=80,size=44)
    lbl(dd,SW/2,216,'3 + 6 = 9',CYAN,12)
    lbl(dd,SW/2,248,'63 - 36 = 27',GOLD,12)
    lbl(dd,SW/2,280,'ÉCART DES CHIFFRES x 9 = 27',CREAM,10)
    lbl(dd,SW/2,306,'DONC ÉCART 3, SOMME 9 : 3 ET 6',CORAL,10)
def q2(lay,dd):
    vals=['1','11','21','1211','111221','?']
    for i,v in enumerate(vals):
        r,c=divmod(i,3); x=52+c*104; y=126+r*72
        col=CORAL if v=='?' else GOLD
        nb(dd,x,y,v,col,w=92,h=56,size=(24 if len(v)<4 else 15))
    lbl(dd,SW/2,276,'QUEL EST LE SUIVANT ?',CYAN,11)
    lbl(dd,SW/2,306,'INDICE : LIS À VOIX HAUTE',CREAM,10)
def a2(lay,dd):
    nb(dd,SW/2,116,'312211',GOLD,w=250,h=60,size=30)
    lbl(dd,SW/2,196,'ON DÉCRIT LE NOMBRE D’AVANT',CREAM,10)
    lbl(dd,SW/2,226,'111221 SE LIT :',CYAN,10)
    lbl(dd,SW/2,254,'TROIS 1, DEUX 2, UN 1',CYAN,10)
    nb(dd,SW/2,286,'31  22  11',CORAL,w=250,h=40,size=14)
mk(q1,[('Nombre à ',CREAM),('2 chiffres',GOLD),(' : somme ',CREAM),('9,',CORAL),(' inversé ',CREAM),('+ 27',CORAL)],'LE DÉFI',D+'q1.png',foot='RÉPONSE CE SOIR')
mk(a1,[('Réponse : ',CREAM),('36',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='36 DEVIENT 63 : +27')
mk(q2,[('Suite : ',CREAM),('1, 11, 21, 1211, 111221,',GOLD),(' ?',CORAL)],'LE DÉFI',D+'q2.png',foot='RÉPONSE CE SOIR')
mk(a2,[('Réponse : ',CREAM),('312211',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='CHAQUE TERME DÉCRIT LE PRÉCÉDENT')
