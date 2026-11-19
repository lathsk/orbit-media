from render_e4x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-20/'; os.makedirs(D,exist_ok=True)
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
    vals=['1','11','21','1211','111221','?']
    for i,v in enumerate(vals):
        y=112+i*36; col=GOLD if v=='?' else (CYAN if i%2 else CORAL)
        nb(dd,SW/2,y,v,col,w=max(70,len(v)*20+40),h=30,size=14)
    lbl(dd,SW/2,332,'RÉPONDS-MOI EN MESSAGE',CREAM,8) if False else None
def a1(lay,dd):
    for i,(v,l) in enumerate((('111','3 x 1'),('22','2 x 2'),('1','1 x 1'))):
        x=SW/2+(i-1)*92; nb(dd,x,118,v,CYAN,w=84,h=40,size=16); lbl(dd,x,164,l,GREY,9)
        arrow_d(dd,x,184,26,CREAM)
        nb(dd,x,214,['31','22','11'][i],CORAL,w=84,h=40,size=16)
    nb(dd,SW/2,272,'312211',GRN,w=250,h=46,size=20)
def q2(lay,dd):
    box(dd,20,236,272,84,fill=rgb('#6B4A2E'),border=rgb('#4A3220'),bw=3)
    dd.ellipse([(SW/2-34)*S,244*S,(SW/2+34)*S,276*S],fill=rgb('#1A1008'),outline=rgb('#4A3220'),width=3*S)
    dd.polygon([(214*S,236*S),(262*S,236*S),(238*S,206*S)],fill=rgb('#8A6238'))
    T(dd,'?',SW/2,150,60,'press',44,GOLD,align='c',shadow=(5,5,BLACK))
    lbl(dd,SW/2,118,'PLUS ON ENLÈVE, PLUS JE GRANDIS',CORAL,8)
def a2(lay,dd):
    box(dd,20,236,272,84,fill=rgb('#6B4A2E'),border=rgb('#4A3220'),bw=3)
    dd.ellipse([(SW/2-70)*S,240*S,(SW/2+70)*S,296*S],fill=rgb('#1A1008'),outline=rgb('#4A3220'),width=3*S)
    dd.polygon([(222*S,236*S),(282*S,236*S),(252*S,196*S)],fill=rgb('#8A6238'))
    stamp(dd,SW/2,140,'UN TROU !',GRN,22)
    lbl(dd,SW/2,322,'',CORAL,9) if False else None
mk(q1,[('Quelle est la ',CREAM),('suite',GOLD),(' ?',CREAM)],'LE DÉFI',D+'q1.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a1,[('Réponse : ',CREAM),('312211',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='ON DÉCRIT LE NOMBRE D’AVANT')
mk(q2,[('Plus on ',CREAM),('m’enlève,',CORAL),(' plus je ',CREAM),('grandis',GOLD),(' !',CREAM),(' ',CREAM),('Qui suis-je',CYAN),(' ?',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a2,[('Réponse : ',CREAM),('un trou',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='PLUS ON CREUSE, PLUS IL GRANDIT')
