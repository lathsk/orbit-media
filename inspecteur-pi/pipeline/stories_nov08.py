from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-08/'; os.makedirs(D,exist_ok=True)
def mk(fn,head,label,out,foot=None,t=0.0):
    def f(lay,dd):
        fn(lay,dd)
        if foot:
            B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); f_=F('silk4',11); T(d2,foot,SW/2-tw(foot,f_,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    lay=B.make_scene(f,t,head=head)
    B.frame_with(lay,label).save(out)
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
def q1(lay,dd):
    # batte + balle
    box(dd,40,206,150,16,fill=rgb('#B58A4A'),border=DARK,bw=2); box(dd,28,202,20,24,fill=rgb('#8A5A3A'),border=DARK,bw=2)
    disc(dd,232,214,20,CREAM,DARK,2)
    nb(dd,SW/2,120,'1,10 EUR',GOLD,w=200,h=52,size=22)
    lbl(dd,115,240,'BATTE = BALLE + 1 EUR',CYAN,10)
    lbl(dd,232,266,'BALLE ?',CORAL,11)
    insp(dd,SW/2,GY,0.3,k=2.6)
    T(dd,'?',SW-40,290,60,'press',44,CORAL,align='c',shadow=(4,4,BLACK))
def a1(lay,dd):
    nb(dd,SW/2,120,'5 CENTIMES',GOLD,w=250,h=56,size=22)
    lbl(dd,SW/2,190,'BALLE 0,05 + BATTE 1,05',CREAM,11)
    lbl(dd,SW/2,222,'TOTAL = 1,10 EUR',CYAN,11)
    nb(dd,SW/2,256,'PAS 10 CENTIMES',RED,w=250,h=40,size=14)
    lbl(dd,SW/2,306,'10 + 1,10 = 1,20 : FAUX',RED,10)
def q2(lay,dd):
    clock(dd,SW/2,166,46,6,0)
    lbl(dd,SW/2,228,'6 COUPS = 5 SECONDES',GOLD,11)
    nb(dd,SW/2,262,'12 COUPS = ?',CORAL,w=230,h=44,size=18)
    insp(dd,40,214,0.3,k=2.0)
def a2(lay,dd):
    nb(dd,SW/2,118,'6 COUPS = 5 PAUSES',GOLD,w=290,h=40,size=14)
    lbl(dd,SW/2,168,'1 PAUSE = 1 SECONDE',CREAM,11)
    nb(dd,SW/2,200,'12 COUPS = 11 PAUSES',CYAN,w=290,h=40,size=14)
    nb(dd,SW/2,254,'11 SECONDES',GOLD,w=240,h=52,size=20)
    lbl(dd,SW/2,322,'PAS 10 SECONDES',RED,10)
mk(q1,[('Une ',CREAM),('batte',GOLD),(' et une ',CREAM),('balle',CORAL),(' coûtent 1,10 €. ',CREAM),('Prix de la balle ?',GOLD)],'LE DÉFI',D+'q1.png',foot='RÉPONSE CE SOIR')
mk(a1,[('Réponse : ',CREAM),('5 centimes',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='LA BATTE COÛTE 1,05 €')
mk(q2,[('6 coups',GOLD),(' en ',CREAM),('5 secondes',CORAL),(' : et ',CREAM),('12 coups',GOLD),(' ?',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONSE CE SOIR')
mk(a2,[('Réponse : ',CREAM),('11 secondes',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='ON COMPTE LES PAUSES')
