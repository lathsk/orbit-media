from render_e4x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-26/'; os.makedirs(D,exist_ok=True)
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
    numcard(dd,cx,150,'30 ÷ 1/2',GOLD,22)
    numcard(dd,cx,226,'+ 10',CYAN,22)
    T(dd,'?',cx,296,50,'press',40,CORAL,align='c',shadow=(4,4,BLACK))
def a1(lay,dd):
    cx=SW/2
    numcard(dd,cx,128,'30 ÷ 1/2 = 60',GOLD,14)
    arrow_d(dd,cx,184,26,CREAM)
    numcard(dd,cx,226,'60 + 10 = 70',CYAN,14)
    numcard(dd,cx,290,'70',GRN,30)
def q2(lay,dd):
    cx=SW/2
    for i,v in enumerate(['2','6','12','20','30','?']):
        x=62+(i%3)*94; y=150+(i//3)*84
        nb(dd,x,y,v,GOLD if v!='?' else CORAL,w=70,h=64,size=26)
def a2(lay,dd):
    cx=SW/2
    for i,v in enumerate(['+ 4','+ 6','+ 8','+ 10','+ 12']):
        x=62+(i%3)*94 if i<3 else 108+(i-3)*94; y=130+(i//3)*66
        nb(dd,x,y,v,CYAN,w=76,h=52,size=18)
    arrow_d(dd,cx,262,22,CREAM)
    numcard(dd,cx,290,'30 + 12 = 42',GRN,12)
FOOT='RÉPONDS-MOI EN MESSAGE, JE TE DIS SI C’EST BON'
mk(q1,[('30',GOLD),(' divisé par ',CREAM),('un demi, ',CORAL),('plus 10',CREAM)],'LE DÉFI',D+'q1.png',foot=FOOT)
mk(a1,[('Réponse : ',CREAM),('70',GOLD)],'LA RÉPONSE',D+'a1.png',foot='DIVISER PAR UN DEMI, C’EST DOUBLER')
mk(q2,[('2, 6, 12, 20, 30',GOLD),(' : quel ',CREAM),('nombre',CORAL),(' ensuite',CREAM)],'LE DÉFI',D+'q2.png',foot=FOOT)
mk(a2,[('Réponse : ',CREAM),('42',GOLD)],'LA RÉPONSE',D+'a2.png',foot='ON AJOUTE 4, 6, 8, 10, PUIS 12')
from PIL import Image
for k in ('q1','a1','q2','a2'):
    Image.open(D+k+'.png').convert('RGB').save(D+k+'.jpg',quality=93)
