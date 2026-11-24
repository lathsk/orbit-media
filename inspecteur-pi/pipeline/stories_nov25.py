from render_e4x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-25/'; os.makedirs(D,exist_ok=True)
def mk(fn,head,label,out,foot=None,t=0.0):
    def f(lay,dd):
        fn(lay,dd)
        if foot:
            B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); fs=11
            while fs>6 and tw(foot,F('silk4',fs),1)>SW-16: fs-=1
            f_=F('silk4',fs); T(d2,foot,SW/2-tw(foot,f_,1)/2,SH-30,14,'silk4',fs,CREAM,sp=1)
    lay=B.make_scene(f,t,head=head)
    B.frame_with(lay,label).save(out)
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-18: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')


def q1(lay,dd):
    cx=SW/2
    clock(dd,cx,215,78,hh=3,mm=15)
    lbl(dd,cx,320,'3 H 15',GOLD,9)
def a1(lay,dd):
    cx=SW/2
    clock(dd,cx,190,70,hh=3,mm=15)
    numcard(dd,cx,276,'7,5 DEGRÉS',GRN,16)
def q2(lay,dd):
    cx=SW/2
    pal=CANDP
    for i in range(6):
        x=62+(i%3)*98; y=190+(i//3)*92
        sorted_man(dd,x,y,0.0,pal[i],k=3.4)
    T(dd,'?',cx,296,50,'press',40,GOLD,align='c',shadow=(4,4,BLACK))
def a2(lay,dd):
    cx=SW/2
    numcard(dd,cx,128,'6 x 5 ÷ 2',GOLD,18)
    arrow_d(dd,cx,190,26,CREAM)
    numcard(dd,cx,232,'15',GRN,34)
FOOT='RÉPONDS-MOI EN MESSAGE, JE TE DIS SI C’EST BON'
mk(q1,[('Il est ',CREAM),('3 h 15',GOLD),(' : quel angle entre les ',CREAM),('aiguilles',CORAL),(' ?',CREAM)],'LE DÉFI',D+'q1.png',foot=FOOT)
mk(a1,[('Réponse : ',CREAM),('7,5',GOLD),(' degrés',CREAM)],'LA RÉPONSE',D+'a1.png',foot='PAS 0 : L’AIGUILLE DES HEURES A BOUGÉ')
mk(q2,[('6 amis',GOLD),(' se serrent tous la main : combien de ',CREAM),('poignées',CORAL),(' ?',CREAM)],'LE DÉFI',D+'q2.png',foot=FOOT)
mk(a2,[('Réponse : ',CREAM),('15',GOLD),(' poignées',CREAM)],'LA RÉPONSE',D+'a2.png',foot='CHAQUE POIGNÉE EST COMPTÉE UNE FOIS')
from PIL import Image
for k in ('q1','a1','q2','a2'):
    Image.open(D+k+'.png').convert('RGB').save(D+k+'.jpg',quality=93)
