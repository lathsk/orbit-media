from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-11/'; os.makedirs(D,exist_ok=True)
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
CHOC=rgb('#6B3A1E'); CHOCL=rgb('#8A4E2A')
def bar(dd,x0=28,y0=118,tile=24,gap=0,cols=6,rows=8,line=None):
    for r in range(rows):
        for c in range(cols):
            x=x0+c*(tile+gap); y=y0+r*(tile+gap)
            box(dd,x,y,tile,tile,fill=CHOC,border=DARK,bw=1)
            box(dd,x+4,y+4,tile-8,tile-8,fill=CHOCL,border=CHOC,bw=1)
def q1(lay,dd):
    bar(dd)
    nb(dd,244,124,'6 x 8',GOLD,w=108,h=48,size=20); lbl(dd,244,184,'48 CARRÉS',CREAM,11)
    lbl(dd,244,214,'1 CASSURE',CYAN,11); lbl(dd,244,238,'= 1 COUP',CYAN,11)
    nb(dd,244,268,'?',CORAL,w=80,h=60,size=36)
    lbl(dd,SW/2,334,'UN MORCEAU À LA FOIS',CREAM,10)
def a1(lay,dd):
    bar(dd,gap=3)
    nb(dd,244,124,'47',GOLD,w=108,h=56,size=30); lbl(dd,244,192,'1 COUP = +1',CYAN,11)
    lbl(dd,244,220,'MORCEAU',CYAN,11); lbl(dd,244,248,'DE 1 À 48',CORAL,11)
    lbl(dd,244,276,'47 COUPS',GOLD,12)
    lbl(dd,SW/2,334,'QUELLE QUE SOIT LA MÉTHODE',CREAM,10)
def q2(lay,dd):
    nb(dd,SW/2,122,'100 !',GOLD,w=170,h=64,size=34)
    lbl(dd,SW/2,200,'1 x 2 x 3 x ... x 100',CREAM,12)
    nb(dd,SW/2,236,'COMBIEN DE ZÉROS',CORAL,w=290,h=40,size=13); nb(dd,SW/2,282,'À LA FIN ?',CORAL,w=200,h=40,size=15)
    insp(dd,SW/2,GY,0.3,k=1.4) if False else None
def a2(lay,dd):
    nb(dd,SW/2,116,'24',GOLD,w=120,h=64,size=36)
    lbl(dd,SW/2,194,'UN ZÉRO = UN FACTEUR 5',CREAM,10)
    nb(dd,SW/2,222,'MULTIPLES DE 5 : 20',CYAN,w=290,h=36,size=11)
    nb(dd,SW/2,266,'25, 50, 75, 100 : +4',CORAL,w=290,h=36,size=11)
    nb(dd,SW/2,310,'20 + 4 = 24',GOLD,w=200,h=34,size=14)
mk(q1,[('Tablette de ',CREAM),('6 x 8',GOLD),(' carrés : combien de ',CREAM),('coups',CORAL),(' pour tout casser ?',CREAM)],'LE DÉFI',D+'q1.png',foot='RÉPONSE CE SOIR')
mk(a1,[('Réponse : ',CREAM),('47 coups',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='CHAQUE COUP FAIT UN MORCEAU DE PLUS')
mk(q2,[('Combien de ',CREAM),('zéros',GOLD),(' à la fin de ',CREAM),('1 x 2 x ... x 100 ?',CORAL)],'LE DÉFI',D+'q2.png',foot='RÉPONSE CE SOIR')
mk(a2,[('Réponse : ',CREAM),('24',GOLD),(' zéros !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='ON COMPTE LES FACTEURS 5')
