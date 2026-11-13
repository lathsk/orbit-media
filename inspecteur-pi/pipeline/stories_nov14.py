from render_e2x import *
import os
B.NUM='MINI-ÉNIGME'
D='../stories/2026-11-14/'; os.makedirs(D,exist_ok=True)
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
def board(dd,x0,y0,c,hl=None):
    for i in range(8):
        for j in range(8):
            col=rgb('#EAD9B8') if (i+j)%2==0 else rgb('#5A3A22')
            box(dd,x0+j*c,y0+i*c,c,c,fill=col)
    box(dd,x0-3,y0-3,8*c+6,3,fill=DARK); box(dd,x0-3,y0+8*c,8*c+6,3,fill=DARK); box(dd,x0-3,y0-3,3,8*c+6,fill=DARK); box(dd,x0+8*c,y0-3,3,8*c+6,fill=DARK)
    if hl:
        k,(i,j)=hl; box(dd,x0+j*c,y0+i*c,k*c,k*c,fill=None,border=CORAL,bw=3)
def q1(lay,dd):
    board(dd,60,112,24)
    lbl(dd,SW/2,318,'COMBIEN DE CARRÉS ?',CORAL,12)
def a1(lay,dd):
    board(dd,108,112,12)
    for (x,y,w,h) in ((105,109,102,3),(105,208,102,3),(105,109,3,102),(204,109,3,102)): box(dd,x,y,w,h,fill=CORAL)
    T(dd,'1+4+9+16',SW/2,224,16,'press',13,CYAN,align='c'); T(dd,'+25+36+49+64',SW/2,246,16,'press',13,CYAN,align='c')
    nb(dd,SW/2,276,'= 204',GOLD,w=210,h=44,size=24)
    lbl(dd,SW/2,326,'8x8 : 1 · 7x7 : 4 · 6x6 : 9 ...',CREAM,9)
def q2(lay,dd):
    days=['L','M','M','J','V','S','D']
    for i,d in enumerate(days): nb(dd,30+i*42,130,d,GOLD if i==0 else CYAN,w=38,h=44,size=18)
    lbl(dd,50,184,'LUNDI',GOLD,10)
    nb(dd,SW/2,222,'+ 100 JOURS',CORAL,w=250,h=48,size=18)
    nb(dd,SW/2,290,'QUEL JOUR ?',GOLD,w=220,h=40,size=16)
def a2(lay,dd):
    nb(dd,SW/2,118,'100 = 14 x 7 + 2',GOLD,w=290,h=44,size=15)
    lbl(dd,SW/2,176,'14 SEMAINES : MÊME JOUR',CYAN,10)
    lbl(dd,SW/2,208,'IL RESTE 2 JOURS',CYAN,11)
    days=['L','M','M','J','V','S','D']
    for i,d in enumerate(days): nb(dd,30+i*42,240,d,CORAL if i==2 else (GOLD if i==0 else EDGE),w=38,h=44,size=18)
    nb(dd,SW/2,300,'MERCREDI',GOLD,w=240,h=40,size=18)
mk(q1,[('Combien de ',CREAM),('carrés',GOLD),(' sur un ',CREAM),('échiquier',CORAL),(' ?',CREAM)],'LE DÉFI',D+'q1.png',foot='RÉPONSE CE SOIR')
mk(a1,[('Réponse : ',CREAM),('204',GOLD),(' carrés !',CREAM)],'LA RÉPONSE',D+'a1.png',foot='ON COMPTE TOUTES LES TAILLES')
mk(q2,[('Un ',CREAM),('lundi,',GOLD),(' + ',CREAM),('100 jours',CORAL),(' : quel jour ?',CREAM)],'LE DÉFI',D+'q2.png',foot='RÉPONSE CE SOIR')
mk(a2,[('Réponse : ',CREAM),('mercredi',GOLD),(' !',CREAM)],'LA RÉPONSE',D+'a2.png',foot='100 = 14 SEMAINES + 2 JOURS')
