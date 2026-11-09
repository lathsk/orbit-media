from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-10/'; os.makedirs(D,exist_ok=True)
def mk(fn,head,label,out,foot=None,t=0.0):
    def f(lay,dd):
        fn(lay,dd)
        if foot:
            B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); f_=F('silk4',11); T(d2,foot,SW/2-tw(foot,f_,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    lay=B.make_scene(f,t,head=head)
    B.frame_with(lay,label).save(out)
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
WATER=rgb('#4DA3FF')
def glass(dd,cx,y,full,col=WATER,hl=None):
    w=30; h=56
    if hl: box(dd,cx-w/2-6,y-6,w+12,h+12,fill=None,border=hl,bw=3)
    box(dd,cx-w/2,y,w,h,fill=CARD,border=CREAM,bw=3)
    if full: box(dd,cx-w/2+3,y+14,w-6,h-17,fill=col)
MOIS=['JAN','FÉV','MARS','AVR','MAI','JUIN','JUIL','AOÛT','SEPT','OCT','NOV','DÉC']
def months(dd,col=None,y0=128):
    for i,m in enumerate(MOIS):
        r,c=divmod(i,4); x=62+c*62
        nb(dd,x,y0+r*52,m,(col or CYAN),w=58,h=42,size=10)
def q1(lay,dd):
    nb(dd,SW/2,120,'2 PÈRES + 2 FILS',CYAN,w=270,h=40,size=14)
    nb(dd,SW/2,176,'3 POISSONS',GOLD,w=230,h=50,size=18)
    lbl(dd,SW/2,246,'UN POISSON CHACUN',CREAM,11)
    nb(dd,SW/2,274,'COMBIEN DE PERSONNES ?',CORAL,w=290,h=40,size=11)
    insp(dd,SW/2,GY,0.3,k=1.5)
def a1(lay,dd):
    nb(dd,SW/2,116,'3',GOLD,w=110,h=70,size=40)
    nb(dd,SW/2,202,'GRAND-PÈRE',CYAN,w=230,h=34,size=13)
    nb(dd,SW/2,242,'PÈRE',GOLD,w=230,h=34,size=13)
    nb(dd,SW/2,282,'FILS',CORAL,w=230,h=34,size=13)
    lbl(dd,SW/2,326,'LE PÈRE EST AUSSI UN FILS',CREAM,10)
def q2(lay,dd):
    months(dd)
    nb(dd,SW/2,290,'28 JOURS : COMBIEN ?',CORAL,w=290,h=40,size=13)
def a2(lay,dd):
    months(dd,col=GOLD)
    nb(dd,SW/2,290,'12 : TOUS !',GOLD,w=230,h=40,size=15)
mk(q1,[('2 pères ',CREAM),('+ 2 fils',GOLD),(' pêchent ',CREAM),('3 poissons',CORAL),(' : un chacun',CREAM)],'LE DÉFI',D+'q1.png',foot='RÉPONSE CE SOIR')
mk(a1,[('Réponse : ',CREAM),('3',GOLD),(' personnes !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='GRAND-PÈRE, PÈRE ET FILS')
mk(q2,[('Combien de ',CREAM),('mois',GOLD),(' ont ',CREAM),('28 jours',CORAL),(' ?',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONSE CE SOIR')
mk(a2,[('Réponse : les ',CREAM),('12',GOLD),(' mois !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='TOUS ONT AU MOINS 28 JOURS')
