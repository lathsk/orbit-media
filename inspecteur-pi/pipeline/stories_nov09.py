from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-09/'; os.makedirs(D,exist_ok=True)
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
def q1(lay,dd):
    for i,(x,c) in enumerate(((52,'9'),(120,'19'),(188,'29'),(252,'…'))): nb(dd,x,128,c,[GOLD,CYAN,CORAL,CREAM][i],w=56,h=56,size=22)
    lbl(dd,SW/2,206,'DE 1 À 100',CREAM,11)
    nb(dd,SW/2,238,'COMBIEN DE 9 ?',CORAL,w=280,h=44,size=16)
    insp(dd,SW/2,GY,0.3,k=1.9)
def a1(lay,dd):
    nb(dd,SW/2,116,'20',GOLD,w=130,h=70,size=40)
    lbl(dd,SW/2,200,'LES 9 DES UNITÉS : 10',CYAN,10)
    lbl(dd,SW/2,228,'LES 9 DES DIZAINES : 10',CORAL,10)
    nb(dd,SW/2,262,'10 + 10 = 20',GOLD,w=250,h=40,size=15)
    lbl(dd,SW/2,312,'99 COMPTE POUR DEUX',CREAM,10)
def q2(lay,dd):
    for i in range(6): glass(dd,40+i*46.4,150,i<3)
    lbl(dd,SW/2,222,'3 PLEINS, 3 VIDES',CREAM,11)
    nb(dd,SW/2,254,'PLEIN / VIDE ?',CORAL,w=260,h=40,size=15)
    lbl(dd,SW/2,306,'SANS TOUCHER AUX AUTRES',GOLD,10)
def a2(lay,dd):
    fl=[1,0,1,0,1,0]
    for i in range(6): glass(dd,40+i*46.4,170,fl[i],hl=(GOLD if i in (1,4) else None))
    x1,x2=40+1*46.4,40+4*46.4
    pts=[]
    for k in range(25):
        f=k/24; pts.append(((x1+(x2-x1)*f)*S,(150-4*30*f*(1-f))*S))
    dd.line(pts,fill=GOLD,width=3*S)
    dd.polygon([((x2)*S,160*S),((x2-7)*S,148*S),((x2+7)*S,148*S)],fill=GOLD)
    nb(dd,SW/2,254,'VERSE LE 2E DANS LE 5E',GOLD,w=290,h=40,size=12)
    lbl(dd,SW/2,306,'PLEIN, VIDE, PLEIN, VIDE...',CYAN,10)
mk(q1,[('De ',CREAM),('1 à 100',GOLD),(' : combien de fois écrit-on le chiffre ',CREAM),('9',CORAL),(' ?',CREAM)],'LE DÉFI',D+'q1.png',foot='RÉPONSE CE SOIR')
mk(a1,[('Réponse : ',CREAM),('20',GOLD),(' fois !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='PAS 10 : IL Y A LES DIZAINES')
mk(q2,[('3 verres ',CREAM),('pleins, ',GOLD),('3 ',CREAM),('vides',CORAL),(' : alterne en bougeant ',CREAM),('un seul',GOLD),(' verre',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONSE CE SOIR')
mk(a2,[('Réponse : ',CREAM),('verse',GOLD),(' le 2e dans le 5e !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='UN SEUL VERRE BOUGE')
