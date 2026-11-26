from render_e4x import *
import inspect, math
B.NUM='#064'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
BC=[CYAN,CORAL,GOLD,GRN,rgb('#B05CFF'),RED,CYAN]
def ball(dd,cx,cy,n,col=None,r=18,k=1.0,dim=False):
    r=r*k; c=rgb('#5a5f73') if dim else (col or CREAM)
    dd.ellipse([(cx-r)*S,(cy-r)*S,(cx+r)*S,(cy+r)*S],fill=c,outline=DARK,width=2*S)
    dd.ellipse([(cx-r*0.55)*S,(cy-r*0.65)*S,(cx-r*0.2)*S,(cy-r*0.3)*S],fill=rgb('#FFFFFF'))
    sz=int(max(8,r*0.9)); txt=str(n)
    T(dd,txt,cx+1,cy-sz/2-2+2,sz+4,'press',sz,DARK,align='c')
def row(dd,cx,cy,nums,r=18,gap=None,cols=None,t=0.0,thr=None,lt=9,pulse=False,dim=False):
    gap=gap or (r*2+10); x0=cx-gap*(len(nums)-1)/2
    for i,n in enumerate(nums):
        if thr is not None and lt<thr[i]: continue
        k=1.0
        if pulse and thr is not None:
            nxt=thr[i+1] if i+1<len(thr) else 99
            if thr[i]<=lt<min(nxt,thr[i]+0.5): k=1.18
        ball(dd,x0+i*gap,cy+math.sin(t*3+i)*(0 if thr else 1.5),n,(cols[i] if cols else BC[i%6]),r,k,dim)
SEQ=[1,2,3,4,5,6]; MIX=[7,13,22,31,38,44]
def bookmark(dd,cx,cy,col=GOLD):
    box(dd,cx-22,cy-34,44,56,fill=col,border=DARK,bw=3)
def man(dd,cx,cy,col,k=1.0):
    dd.ellipse([(cx-5*k)*S,(cy-18*k)*S,(cx+5*k)*S,(cy-8*k)*S],fill=rgb('#F3C9A0'),outline=DARK,width=1*S)
    box(dd,cx-7*k,cy-8*k,14*k,16*k,fill=col,border=DARK,bw=1)
    box(dd,cx-6*k,cy+8*k,5*k,8*k,fill=DARK); box(dd,cx+1*k,cy+8*k,5*k,8*k,fill=DARK)
def envelope(dd,cx,by,t):
    bx=cx-46; box(dd,bx,by,92,64,fill=CREAM,border=DARK,bw=3,shadow=(4,4,BLACK))
    dd.line([(bx*S,by*S),((bx+46)*S,(by+34)*S),((bx+92)*S,by*S)],fill=DARK,width=3*S)
T1=[0.0,0.38,0.92,1.5,1.95,2.52]
T3=[0.92,1.37,1.8,2.14,2.45,2.78]
T4=[0.84,1.46,1.93,2.55,3.17,3.8]
HEADS={'s1':[('Un, deux, trois, quatre, cinq, six',CREAM),(' : ',CREAM),('gagnant ?',GOLD)],
 's2':[('Au loto : ',CREAM),('6 numéros',GOLD),(' parmi ',CREAM),('49',CYAN)],
 's3':[('Ton ami',CYAN),(' joue ',CREAM),('1 2 3 4 5 6',GOLD)],
 's4':[('Toi',CORAL),(' : des numéros ',CREAM),('mélangés',GOLD)],
 'q':[('Qui a le plus de ',CREAM),('chances',GOLD),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('les mêmes',GRN)],
 'r1':[('Presque ',CREAM),('14 millions',GOLD),(' de combinaisons',CREAM)],
 'r2':[('Une seule ',CREAM),('gagne',GOLD)],
 'r3':[('La ',CREAM),('boule',CYAN),(' ne se souvient de rien',CREAM)],
 'r4':[('1 2 3 4 5 6',GOLD),(' : pas plus rare',CREAM)],
 'r5':[('Le piège : ',CREAM),('trop parfaite',RED)],
 'r6':[('Mais ',CREAM),('beaucoup',GOLD),(' la jouent',CREAM)],
 'r7':[('Le ',CREAM),('gain',GOLD),(' serait ',CREAM),('partagé',CORAL)],
 'r8':[('Envoie-la !',CREAM)]}
STORY=('s1','s2','s3','s4','q')
def two(dd,t,eq=None,y1=176,y2=258,r=13):
    lbl(dd,cx_,y1-40,'TON AMI',CYAN,9); row(dd,cx_,y1,SEQ,r,t=t)
    lbl(dd,cx_,y2-40,'TOI',CORAL,9); row(dd,cx_,y2,MIX,r,cols=[CORAL]*6,t=t)
cx_=156
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            row(dd,cx,190,SEQ,19,t=t,thr=[0]*6,lt=9,pulse=False)
            # pulse the ball currently spoken
            for i,th in enumerate(T1):
                if th<=lt<th+0.45: dd.rectangle([(cx-115+i*46-22)*S,(190+26)*S,(cx-115+i*46+22)*S,(190+31)*S],fill=GOLD)
            numcard(dd,cx,262,'GAGNANT ?',GOLD,18)
            tagc(dd,cx,364,'UN, DEUX, TROIS, QUATRE, CINQ, SIX',GOLD)
        elif key=='s2':
            u=27; x0=cx-3.5*u; y0=116
            picks=[4,11,19,27,33,45]; ths=[1.0,1.3,1.6,1.9,2.2,2.5]
            for i in range(49):
                n=i+1; cxx=x0+(i%7)*u+u/2; cyy=y0+(i//7)*u+u/2
                on=n in picks and lt>=ths[picks.index(n)]
                box(dd,cxx-12,cyy-12,24,24,fill=(GOLD if on else CARD),border=(DARK if on else EDGE),bw=2)
                T(dd,str(n),cxx,cyy-6,10,'press',8 if n<10 else 7,(DARK if on else GREY),align='c')
            tagc(dd,cx,364,'SIX NUMÉROS PARMI QUARANTE-NEUF',GOLD)
        elif key=='s3':
            numcard(dd,cx,128,'TON AMI',CYAN,18)
            row(dd,cx,214,SEQ,19,t=t,thr=T3,lt=lt,pulse=True)
            if lt>3.0: lbl(dd,cx,270,'1 2 3 4 5 6',GOLD,12)
            tagc(dd,cx,364,'TON AMI JOUE 1, 2, 3, 4, 5, 6',CYAN)
        elif key=='s4':
            numcard(dd,cx,128,'TOI',CORAL,18)
            row(dd,cx,214,MIX,19,cols=[CORAL]*6,t=t,thr=T4,lt=lt,pulse=True)
            tagc(dd,cx,364,'TOI : 7, 13, 22, 31, 38, 44',CORAL)
        elif key=='q':
            two(dd,t)
            numcard(dd,cx,306,'QUI GAGNE ?',GOLD,16)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            two(dd,t)
            if lt<1.55: numcard(dd,cx,306,'?',GOLD,16)
            else:
                numcard(dd,cx,300,'=  MÊMES CHANCES',GRN,12)
                star(dd,24,214,t,6); star(dd,288,214,t+1,6)
            tagc(dd,cx,364,'EXACTEMENT LES MÊMES CHANCES',GRN)
        elif key=='r1':
            numcard(dd,cx,150,'14 MILLIONS',GOLD,20)
            lbl(dd,cx,222,'COMBINAISONS POSSIBLES',CREAM,10)
            row(dd,cx,290,[3,17,25,36,41,49],14,t=t,cols=[CYAN,GOLD,CORAL,GRN,CYAN,GOLD])
            tagc(dd,cx,364,'14 MILLIONS DE COMBINAISONS',GOLD)
        elif key=='r2':
            u=19; x0=cx-5*u; y0=116
            for i in range(10):
                for j in range(10):
                    g=(i==6 and j==4)
                    box(dd,x0+j*u,y0+i*u,u-3,u-3,fill=(GOLD if (g and (blink(t) or lt>1)) else rgb('#1f5f7a')))
            lbl(dd,cx,y0+10*u+14,'UNE SEULE GAGNE',GOLD,10)
            tagc(dd,cx,364,'CHACUNE A LA MÊME CHANCE',GOLD)
        elif key=='r3':
            ball(dd,cx,208,'?',CYAN,38)
            if blink(t) or lt<0.6: stamp(dd,cx,300,'AUCUN SOUVENIR',RED,10)
            tagc(dd,cx,364,'LA BOULE NE SE SOUVIENT DE RIEN',CYAN)
        elif key=='r4':
            row(dd,cx,170,SEQ,13,t=t); box(dd,cx-16,202,32,6,fill=CREAM); box(dd,cx-16,214,32,6,fill=CREAM)
            row(dd,cx,262,MIX,13,cols=[CORAL]*6,t=t)
            if lt>1.6: stamp(dd,cx,320,'PAS PLUS RARE',GRN,12)
            tagc(dd,cx,364,'PAS PLUS RARE QUE LES AUTRES',GRN)
        elif key=='r5':
            row(dd,cx,200,SEQ,19,t=t)
            star(dd,30,150,t,6); star(dd,284,150,t+1,6)
            numcard(dd,cx,276,'TROP PARFAITE ?',RED,14)
            tagc(dd,cx,364,'ELLE SEMBLE TROP PARFAITE',RED)
        elif key=='r6':
            cols=[CYAN,CORAL,GOLD,GRN,rgb('#B05CFF'),RED]
            for i in range(18):
                man(dd,48+(i%6)*44,160+(i//6)*52+math.sin(t*3+i)*1.2,cols[(i*5)%6],1.15)
            lbl(dd,cx,330,'1 2 3 4 5 6',GOLD,10)
            tagc(dd,cx,364,'BEAUCOUP DE GENS LA JOUENT',GOLD)
        elif key=='r7':
            trophy(dd,cx,130,2.0)
            for i,xx in enumerate((60,108,204,252)): man(dd,xx,318,[CYAN,CORAL,GRN,RED][i],1.2)
            numcard(dd,cx,246,'GAIN PARTAGÉ',GOLD,14)
            tagc(dd,cx,364,'LE GAIN SERAIT PARTAGÉ',CORAL)
        elif key=='r8':
            envelope(dd,cx,150,t)
            if blink(t): arrow_r(dd,cx-20,260,48,GOLD)
            tagc(dd,cx,364,'À QUELQU’UN QUI VA SE TROMPER',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#064'
    def fn(lay,dd):
        cx=SW/2
        row(dd,cx,190,SEQ,19,t=0.0,thr=[0]*6)
        numcard(dd,cx,262,'GAGNANT ?',GOLD,18)
        T(dd,'1 2 3 4 5 6 AU LOTO',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'GAGNANT ?',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="QUI A LE PLUS DE CHANCES ?"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')

def make_decide2():
    ns=dict(vars(R14))
    src=inspect.getsource(R14.decide).replace('COMMENTE TON PLAN','RÉPONDS EN COMMENTAIRE').replace("[('Écris ton idée en ',CREAM),('commentaire',CORAL),(' !',CREAM)]","[('Écris ta ',CREAM),('réponse',CORAL),(' en commentaire !',CREAM)]").replace('def decide','def decide_')
    exec(src,ns)
    return lambda n,t,ft=None: ns['decide_'](n,t,ft)
def make_end2(num_next,pill):
    ns=dict(vars(R14))
    src=inspect.getsource(R14.end).replace("bulb(d,262,150,True,k=1.3,t=t,gk=1.0)","star(d,262,176,t,8)").replace("'#010 >>'","'%s >>'"%num_next).replace("'PARTAGE LA VIDÉO À UN AMI'",repr(pill)).replace('def end','def end_')
    ns['star']=star
    exec(src,ns)
    return lambda level,t: ns['end_'](level,t)
decide=make_decide2()
end=make_end2('#065','ENVOIE-LA À QUELQU’UN')
