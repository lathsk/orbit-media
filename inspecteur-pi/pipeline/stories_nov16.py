from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-16/'; os.makedirs(D,exist_ok=True)
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
import render5 as R5
def arrow_l(dd,x,y,w=34,col=CREAM):
    box(dd,x+7,y-2,w-7,5,fill=col); dd.polygon([((x+7)*S,(y-7)*S),((x+7)*S,(y+8)*S),(x*S,(y+0.5)*S)],fill=col)
def arrow_rr(dd,x,y,w=34,col=CREAM):
    box(dd,x,y-2,w-7,5,fill=col); dd.polygon([((x+w-7)*S,(y-7)*S),((x+w-7)*S,(y+8)*S),((x+w)*S,(y+0.5)*S)],fill=col)
def rail(dd,y=300):
    box(dd,0,y,SW,5,fill=STEEL)
    for i in range(0,SW,22): box(dd,i,y+5,10,6,fill=rgb('#5A6BA8'))
def q1(lay,dd):
    R5.train(dd,40,0.3,yoff=-20,u=3.2,wag=0,smoke=False); rail(dd,336)
    lbl(dd,SW/2,118,'TRAIN : VERS LE NORD',CYAN,10); arrow_rr(dd,106,152,100,CYAN)
    lbl(dd,SW/2,172,'VENT : VERS LE SUD',CORAL,10); arrow_l(dd,106,204,100,CORAL)
    T(dd,'?',236,236,50,'press',40,GOLD,align='c',shadow=(4,4,BLACK))
def a1(lay,dd):
    R5.train(dd,40,0.3,yoff=-20,u=3.2,wag=0,smoke=False); rail(dd,336)
    xmark_(dd,76,212,22,7,RED); lbl(dd,76,166,'FUMÉE ?',RED,10)
    T(dd,'?',236,196,50,'press',40,GREY,align='c') if False else None
    nb(dd,SW/2,112,'PAS DE FUMÉE !',GOLD,w=270,h=44,size=14)
def feathers(dd,cx,cy):
    for dx,dy,r in ((-16,4,13),(0,-6,16),(16,4,13),(-6,10,12),(8,10,12),(0,-14,11)):
        disc(dd,cx+dx,cy+dy,r,CREAM,SOFT,2)
def lead(dd,cx,cy):
    box(dd,cx-24,cy-20,48,40,fill=rgb('#6B7392'),border=DARK,bw=3); box(dd,cx-20,cy-16,40,6,fill=rgb('#8A93C0'))
def q2(lay,dd):
    feathers(dd,78,200); lead(dd,232,204)
    nb(dd,78,244,'1 KG',GOLD,w=96,h=44,size=18); nb(dd,232,244,'1 KG',CYAN,w=96,h=44,size=18)
    lbl(dd,78,132,'PLUMES',CREAM,11); lbl(dd,232,132,'PLOMB',CYAN,11)
    T(dd,'?',SW/2,176,70,'press',54,CORAL,align='c',shadow=(4,4,BLACK)) if False else None
    T(dd,'?',SW/2,170,60,'press',44,CORAL,align='c',shadow=(4,4,BLACK))
def a2(lay,dd):
    box(dd,SW/2-4,176,8,110,fill=STEEL); dd.polygon([((SW/2-30)*S,300*S),((SW/2+30)*S,300*S),((SW/2)*S,270*S)],fill=STEEL)
    box(dd,40,172,232,7,fill=GOLD,border=DARK,bw=2)
    for cx in (66,246):
        box(dd,cx-1,179,3,50,fill=CREAM); box(dd,cx-30,229,60,7,fill=CREAM,border=DARK,bw=2)
    feathers(dd,66,205) ; lead(dd,246,210)
    lbl(dd,66,248,'1 KG',GOLD,10); lbl(dd,246,248,'1 KG',CYAN,10)
    nb(dd,SW/2,126,'PAREIL !',GRN,w=190,h=44,size=20)
mk(q1,[('Train électrique',CYAN),(' vers le nord,',CREAM),(' vent vers le sud : ',CREAM),('où va la fumée ?',CORAL)],'LE DÉFI',D+'q1.png',foot='RÉPONSE CE SOIR')
mk(a1,[('Réponse : ',CREAM),('pas de fumée',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='UN TRAIN ÉLECTRIQUE : PAS DE FUMÉE')
mk(q2,[('Plus lourd : ',CREAM),('1 kg de plumes',GOLD),(' ou de ',CREAM),('plomb ?',CYAN)],'LE DÉFI',D+'q2.png',foot='RÉPONSE CE SOIR')
mk(a2,[('Réponse : ',CREAM),('pareil',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='1 KILO, C’EST 1 KILO')
