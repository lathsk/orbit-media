from render_e4x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-23/'; os.makedirs(D,exist_ok=True)
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
    vals=['1','1','2','3','5','8','?']
    for i,v in enumerate(vals):
        col=GOLD if v=='?' else (CYAN if i%2 else CORAL)
        x=SW/2-3*40+i*40
        nb(dd,x,170,v,col,w=36,h=44,size=14)
    lbl(dd,SW/2,250,'QUEL EST LE NOMBRE SUIVANT ?',CREAM,8)
def a1(lay,dd):
    vals=['1','1','2','3','5','8']
    for i,v in enumerate(vals):
        nb(dd,SW/2-100+i*40,140,v,CYAN if i%2 else CORAL,w=36,h=40,size=13)
    arrow_d(dd,SW/2,190,26,CREAM)
    nb(dd,SW/2,226,'13',GRN,w=110,h=56,size=26)
    lbl(dd,SW/2,296,'5 + 8 = 13',CREAM,9)
def q2(lay,dd):
    cx=SW/2
    box(dd,cx-90,150,180,70,fill=CARD,border=GOLD,bw=4,shadow=(4,4,BLACK))
    T(dd,'TOI',cx,168,40,'press',26,CREAM,align='c')
    for i,x in enumerate((cx-110,cx+110)):
        T(dd,'?',x,170,60,'press',40,CORAL,align='c',shadow=(4,4,BLACK))
    lbl(dd,cx,262,'À TOI, MAIS LES AUTRES S’EN SERVENT PLUS',GOLD,6)
def a2(lay,dd):
    cx=SW/2
    stamp(dd,cx,170,'TON PRÉNOM !',GRN,16)
    box(dd,cx-80,206,160,56,fill=CARD,border=CORAL,bw=3,shadow=(3,3,BLACK)); T(dd,'PRÉNOM',cx,222,24,'press',16,CORAL,align='c')
    lbl(dd,cx,290,'LES AUTRES L’UTILISENT PLUS QUE TOI',CORAL,7)
mk(q1,[('Quel est le ',CREAM),('nombre',GOLD),(' suivant ?',CREAM)],'LE DÉFI',D+'q1.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a1,[('Réponse : ',CREAM),('13',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='SUITE DE FIBONACCI')
mk(q2,[('Il est à toi, mais les autres l’utilisent ',CREAM),('?',GOLD)],'LE DÉFI',D+'q2.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a2,[('Réponse : ',CREAM),('ton prénom',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='LES AUTRES T’APPELLENT DESSUS')
from PIL import Image
for k in ('q1','a1','q2','a2'):
    Image.open(D+k+'.png').convert('RGB').save(D+k+'.jpg',quality=93)
