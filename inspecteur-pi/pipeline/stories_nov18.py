from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-18/'; os.makedirs(D,exist_ok=True)
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
    for i,(x,v,l) in enumerate(((56,'2','POULES'),(156,'2','ŒUFS'),(256,'2','JOURS'))):
        nb(dd,x,124,v,[GOLD,CYAN,CORAL][i],w=64,h=56,size=30); lbl(dd,x,188,l,CREAM,9)
    for i,(x,v,l) in enumerate(((56,'6','POULES'),(156,'?','ŒUFS'),(256,'6','JOURS'))):
        nb(dd,x,228,v,[GOLD,GRN,CORAL][i] if v!='?' else GRN,w=64,h=56,size=30); lbl(dd,x,292,l,CREAM,9)
    lbl(dd,SW/2,322,'JE TE DIS SI C’EST BON',CYAN,9)
def a1(lay,dd):
    nb(dd,SW/2,124,'1 POULE = 1 ŒUF / 2 JOURS',GOLD,w=290,h=48,size=13)
    nb(dd,SW/2,184,'6 POULES x 6 JOURS = 36',CYAN,w=290,h=48,size=13)
    nb(dd,SW/2,244,'36 / 2 = 18 ŒUFS',GRN,w=290,h=56,size=18)
    lbl(dd,SW/2,322,'PAS 6 !',RED,11)
def q2(lay,dd):
    x0=(SW-(7*38+6*5))/2
    for i,c in enumerate('JFMAMJ?'):
        nb(dd,x0+i*43+19,160,c,CORAL if c=='?' else [GOLD,CYAN][i%2],w=38,h=54,size=20)
    lbl(dd,SW/2,236,'QUELLE EST LA SUITE ?',GOLD,10)
    T(dd,'?',SW/2,262,60,'press',44,CORAL,align='c',shadow=(4,4,BLACK))
    lbl(dd,SW/2,322,'JE TE DIS SI C’EST BON',CYAN,9)
def a2(lay,dd):
    x0=(SW-(7*38+6*5))/2
    for i,c in enumerate('JFMAMJJ'):
        nb(dd,x0+i*43+19,140,c,GRN if i==6 else [GOLD,CYAN][i%2],w=38,h=54,size=20)
    lbl(dd,SW/2,214,'LES INITIALES DES MOIS',CREAM,10)
    nb(dd,SW/2,246,'JUILLET = J',GRN,w=250,h=50,size=20)
    lbl(dd,SW/2,322,'JANVIER, FÉVRIER... JUIN',GOLD,9)
mk(q1,[('2 poules',GOLD),(' pondent ',CREAM),('2 œufs',CORAL),(' en ',CREAM),('2 jours.',GOLD),(' Et ',CREAM),('6 poules',GOLD),(' en ',CREAM),('6 jours ?',CORAL)],'LE DÉFI',D+'q1.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a1,[('Réponse : ',CREAM),('18 œufs',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='LE PIÈGE : CE N’EST PAS 6')
mk(q2,[('J, F, M, A, M, J, ',GOLD),('?',CORAL),(' Quelle est la ',CREAM),('lettre suivante',CORAL),(' ?',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONDS-MOI EN MESSAGE')
mk(a2,[('Réponse : ',CREAM),('J',GOLD),(' comme ',CREAM),('juillet',GOLD)],'LA RÉPONSE',D+'a2.png',foot='LES MOIS DE L’ANNÉE')
