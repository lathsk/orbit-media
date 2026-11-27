from render_e4x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-28/'; os.makedirs(D,exist_ok=True)
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


def door(dd,cx,y,w=84,h=120):
    box(dd,cx-w/2,y,w,h,fill=rgb('#6B4A2E'),border=DARK,bw=3,shadow=(3,3,BLACK))
    box(dd,cx-w/2+8,y+8,w-16,h/2-12,fill=rgb('#8A5E2E'),border=DARK,bw=2)
    box(dd,cx-w/2+8,y+h/2+4,w-16,h/2-14,fill=rgb('#8A5E2E'),border=DARK,bw=2)
    dd.ellipse([(cx+w/2-18)*S,(y+h/2)*S,(cx+w/2-8)*S,(y+h/2+10)*S],fill=GOLD,outline=DARK,width=2*S)
def keys(dd,cx,y,n=7,kw=32,kh=96,hl=False):
    x0=cx-kw*n/2
    for i in range(n):
        box(dd,x0+i*kw,y,kw-2,kh,fill=CREAM,border=DARK,bw=2)
    for i in (0,1,3,4,5):
        if i<n-1: box(dd,x0+(i+1)*kw-9,y,16,kh*0.6,fill=DARK,border=BLACK,bw=1)
def q1(lay,dd):
    cx=SW/2
    door(dd,cx,118,84,128); xmark_(dd,cx,182,58,7,RED)
    numcard(dd,cx,262,'DES TOUCHES',CYAN,14)
    T(dd,'? ',cx,318,40,'press',22,CORAL,align='c',shadow=(4,4,BLACK))
def a1(lay,dd):
    cx=SW/2
    keys(dd,cx,128,7,34,104)
    numcard(dd,cx,252,'UN CLAVIER',GRN,18)
    lbl(dd,cx,318,'OU UN PIANO',GOLD,10)
def q2(lay,dd):
    cx=SW/2
    L=['U','D','T','Q','C','S','S','H','?']
    for i,l in enumerate(L):
        r,c=divmod(i,5); x=cx+(c-(4 if r==0 else 3)/2)*58; y=134+r*74
        nb(dd,x,y,l,CORAL if l=='?' else GOLD,w=50,h=50,size=22)
    lbl(dd,cx,300,'QUELLE EST LA LETTRE SUIVANTE ?',CREAM,8)
def a2(lay,dd):
    cx=SW/2
    W=['UN','DEUX','TROIS','QUATRE','CINQ','SIX','SEPT','HUIT','NEUF']
    for i,w_ in enumerate(W):
        r,c=divmod(i,3); x=62+c*94; y=116+r*76
        nb(dd,x,y,w_[0],GRN if i==8 else GOLD,w=44,h=44,size=18)
        T(dd,w_,x,y+50,12,'silk7',9,GRN if i==8 else CREAM,align='c')
FOOT='RÉPONDS-MOI EN MESSAGE, JE TE DIS SI C’EST BON'
mk(q1,[('Des ',CREAM),('touches',CYAN),(' mais aucune ',CREAM),('porte',CORAL),(' à ouvrir : quoi ?',CREAM)],'LE DÉFI',D+'q1.png',foot=FOOT)
mk(a1,[('Réponse : ',CREAM),('un clavier',GOLD)],'LA RÉPONSE',D+'a1.png',foot='LES TOUCHES D’UN CLAVIER OU D’UN PIANO')
mk(q2,[('U, D, T, Q, C, S, S, H : ',CREAM),('la suite',GOLD),(' ?',CREAM)],'LE DÉFI',D+'q2.png',foot=FOOT)
mk(a2,[('Réponse : ',CREAM),('N',GOLD),(' comme neuf',CREAM)],'LA RÉPONSE',D+'a2.png',foot='LES INITIALES DE UN, DEUX, TROIS...')
from PIL import Image
for k in ('q1','a1','q2','a2'):
    Image.open(D+k+'.png').convert('RGB').save(D+k+'.jpg',quality=93)
