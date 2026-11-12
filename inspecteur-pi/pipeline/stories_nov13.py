from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-13/'; os.makedirs(D,exist_ok=True)
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
    nb(dd,SW/2,118,'1+2+3+...+100',GOLD,w=270,h=56,size=17)
    lbl(dd,SW/2,196,'SANS CALCULATRICE',CYAN,11)
    lbl(dd,SW/2,232,'ET EN MOINS DE 10 SECONDES',CREAM,10)
    nb(dd,SW/2,276,'QUEL TOTAL ?',CORAL,w=240,h=40,size=15)
def a1(lay,dd):
    nb(dd,SW/2,112,'5050',GOLD,w=250,h=64,size=36)
    lbl(dd,SW/2,196,'1 + 100 = 101',CYAN,11)
    lbl(dd,SW/2,224,'2 + 99 = 101',CYAN,11)
    lbl(dd,SW/2,252,'3 + 98 = 101 ...',CYAN,11)
    lbl(dd,SW/2,286,'50 PAIRES x 101 = 5050',CORAL,11)
def q2(lay,dd):
    names=['LALA','LELE','LILI','LOLO']
    for i,v in enumerate(names):
        r,c=divmod(i,2); nb(dd,100+c*112,118+r*66,v,GOLD,w=100,h=52,size=17)
    nb(dd,SW/2,254,'?',CORAL,w=120,h=52,size=30)
    lbl(dd,SW/2,196,'LA 5E FILLE S\'APPELLE ?',CYAN,11) if False else None
    lbl(dd,SW/2,314,'COMMENT S\'APPELLE LA 5E ?',CYAN,11)
def a2(lay,dd):
    nb(dd,SW/2,112,'LULU',GOLD,w=250,h=64,size=36)
    for i,v in enumerate('AEIOU'):
        nb(dd,52+i*52,200,v,(CORAL if v=='U' else CYAN),w=44,h=48,size=22)
    lbl(dd,SW/2,266,'LES VOYELLES, DANS L\'ORDRE',CREAM,10)
    lbl(dd,SW/2,296,'LA-LE-LI-LO-LU : A E I O U',CYAN,10)
mk(q1,[('Total de ',CREAM),('1 à 100',GOLD),(' ?',CORAL)],'LE DÉFI',D+'q1.png',foot='RÉPONSE CE SOIR')
mk(a1,[('Réponse : ',CREAM),('5050',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='ON ASSOCIE LES NOMBRES PAR PAIRES')
mk(q2,[('La ',CREAM),('5e fille',GOLD),(' s’appelle ?',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONSE CE SOIR')
mk(a2,[('Réponse : ',CREAM),('Lulu',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='A, E, I, O, U : LES 5 VOYELLES')
