from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-17/'; os.makedirs(D,exist_ok=True)
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

DAYS='LMMJVSD'
def strip(dd,y,marks=None,hlset=()):
    w=36; g=5; x0=(SW-(7*w+6*g))/2
    for i,c in enumerate(DAYS):
        col=[CREAM]*7
        cc=CREAM
        if i in hlset: cc=hlset[i] if isinstance(hlset,dict) else GOLD
        nb(dd,x0+i*(w+g)+w/2,y,c,cc,w=w,h=48,size=18)
    return x0,w,g
def q1(lay,dd):
    x0,w,g=strip(dd,170,hlset={6:GOLD})
    lbl(dd,SW-76,122,'APRÈS-DEMAIN',GOLD,8)
    T(dd,'DIMANCHE',SW/2,236,22,'press',14,GOLD,align='c')
    T(dd,'?',SW/2,262,60,'press',44,CORAL,align='c',shadow=(4,4,BLACK))
    lbl(dd,SW/2,320,'QUEL JOUR ÉTAIT HIER ?',CORAL,10)
def a1(lay,dd):
    x0,w,g=strip(dd,170,hlset={3:GRN,4:CYAN,5:CREAM,6:GOLD})
    for i,t_,c in ((3,'HIER',GRN),(4,'AUJ.',CYAN),(5,'DEM.',CREAM),(6,'DIM.',GOLD)):
        T(dd,t_,x0+i*(w+g)+w/2,226,12,'silk7',8,c,align='c')
    nb(dd,SW/2,118,'HIER = JEUDI',GRN,w=250,h=44,size=16)
    lbl(dd,SW/2,300,'DIMANCHE - 2 = VENDREDI',CREAM,9)
def q2(lay,dd):
    for i,x in enumerate((46,116,186,256)): nb(dd,x,150,'9',[GOLD,CYAN,CORAL,CREAM][i],w=44,h=60,size=28)
    for x in (81,151,221): T(dd,'?',x,164,26,'press',20,CREAM,align='c')
    nb(dd,SW/2,238,'= 100',GRN,w=190,h=46,size=22)
    lbl(dd,SW/2,310,'+ - x / ET PARENTHÈSES',GOLD,9)
def a2(lay,dd):
    nb(dd,SW/2,128,'99 + 9 / 9',GOLD,w=290,h=56,size=20)
    lbl(dd,SW/2,200,'9 / 9 = 1',CYAN,11)
    nb(dd,SW/2,236,'99 + 1 = 100',GRN,w=290,h=50,size=17)
    lbl(dd,SW/2,306,'DEUX 9 COLLÉS FONT 99',GOLD,10)
mk(q1,[('Après-demain ',CREAM),('c’est dimanche.',GOLD),(' Quel jour était ',CREAM),('hier ?',CORAL)],'LE DÉFI',D+'q1.png',foot='RÉPONSE CE SOIR')
mk(a1,[('Réponse : ',CREAM),('jeudi',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='AUJOURD’HUI, C’EST VENDREDI')
mk(q2,[('Avec ',CREAM),('quatre 9',GOLD),(' et des opérations, ',CREAM),('fais 100',CORAL)],'LE DÉFI',D+'q2.png',foot='RÉPONSE CE SOIR')
mk(a2,[('Réponse : ',CREAM),('99 + 9 / 9',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='99 + 1 = 100')
