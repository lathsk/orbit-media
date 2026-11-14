from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-15/'; os.makedirs(D,exist_ok=True)
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
def apple(dd,cx,cy,r=20,hl=False,dim=False):
    col=rgb('#E5484D') if not dim else rgb('#7A3A44')
    if hl: dd.ellipse([(cx-r-6)*S,(cy-r-6)*S,(cx+r+6)*S,(cy+r+6)*S],outline=GOLD,width=3*S)
    disc(dd,cx,cy,r,col,DARK,2); box(dd,cx-1.5,cy-r-6,3,7,fill=rgb('#6B4A2E')); box(dd,cx+2,cy-r-5,9,5,fill=GRN)
def q1(lay,dd):
    nb(dd,78,132,'N + N',CYAN,w=124,h=56,size=20); T(dd,'=',SW/2,142,36,'press',28,CREAM,align='c'); nb(dd,234,132,'N x N',CORAL,w=124,h=56,size=20)
    lbl(dd,SW/2,206,'MÊME RÉSULTAT',GOLD,12); lbl(dd,SW/2,236,'N DIFFÉRENT DE 0',CREAM,10)
    nb(dd,SW/2,274,'N = ?',GOLD,w=170,h=56,size=26)
def a1(lay,dd):
    nb(dd,78,124,'2 + 2',CYAN,w=124,h=50,size=20); T(dd,'=',SW/2,132,36,'press',28,CREAM,align='c'); nb(dd,234,124,'4',CYAN,w=124,h=50,size=22)
    nb(dd,78,196,'2 x 2',CORAL,w=124,h=50,size=20); T(dd,'=',SW/2,204,36,'press',28,CREAM,align='c'); nb(dd,234,196,'4',CORAL,w=124,h=50,size=22)
    lbl(dd,SW/2,268,'ADDITION = PRODUIT',CREAM,10); nb(dd,SW/2,296,'DONC : 2',GOLD,w=210,h=48,size=22)
def q2(lay,dd):
    table(dd,284)
    for i in range(3): apple(dd,64+i*92,262)
    nb(dd,SW/2,120,'3 POMMES',GOLD,w=210,h=44,size=18); nb(dd,SW/2,172,'TU EN PRENDS 2',CORAL,w=270,h=40,size=14)
    T(dd,'?',SW/2,300,40,'press',30,CYAN,align='c') if False else None
def a2(lay,dd):
    apple(dd,SW/2,238,dim=True)
    for i in range(2): apple(dd,92+i*128,150,hl=True)
    lbl(dd,SW/2,112,'CELLES QUE TU AS PRISES',GOLD,10)
    lbl(dd,SW/2,274,'IL EN RESTE 1',GREY,9)
    nb(dd,SW/2,300,'TU EN AS 2',GRN,w=220,h=44,size=20)
mk(q1,[('N + N = N x N',GOLD),(' : quel ',CREAM),('nombre',CORAL),(' ?',CREAM)],'LE DÉFI',D+'q1.png',foot='RÉPONSE CE SOIR')
mk(a1,[('Réponse : ',CREAM),('2',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='2 + 2 = 4 ET 2 x 2 = 4')
mk(q2,[('3 pommes,',GOLD),(' tu en prends ',CREAM),('2.',CORAL),(' Combien en as-tu ?',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONSE CE SOIR')
mk(a2,[('Réponse : ',CREAM),('2',GOLD),(' pommes !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='TU AS PRIS 2 POMMES')
