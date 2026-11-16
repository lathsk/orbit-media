from render_e4x import *
B.NUM='#043'
PA=(156,134); PB=(62,296); PC=(250,296)
EDG=rgb('#5A6BA8'); ANTC=rgb('#2A1F18'); ANTR=rgb('#C0392B')
def ant(dd,x,y,ang,k=1.0,col=None,t=0.0,walk=True):
    col=col or rgb('#E8D9B8'); k=k*1.7
    ux,uy=math.cos(ang),math.sin(ang); px,py=-uy,ux
    sw=math.sin(t*14)*1.6*k if walk else 0
    for i,off in enumerate((-3.5,0,3.5)):
        for sgn in (-1,1):
            ex=x+ux*off*k+px*sgn*(9*k+(sw if (i+(sgn>0))%2 else -sw))
            ey=y+uy*off*k+py*sgn*(9*k+(sw if (i+(sgn>0))%2 else -sw))
            dd.line([((x+ux*off*k)*S,(y+uy*off*k)*S),(ex*S,ey*S)],fill=DARK,width=max(1,int(1.6*k*S)))
    disc(dd,x-ux*9*k,y-uy*9*k,5.5*k,col,DARK,1)
    disc(dd,x,y,4*k,col,DARK,1)
    hx,hy=x+ux*7.5*k,y+uy*7.5*k
    disc(dd,hx,hy,3.6*k,col,DARK,1)
    for sgn in (-1,1):
        dd.line([(hx*S,hy*S),((hx+ux*6*k+px*sgn*4*k)*S,(hy+uy*6*k+py*sgn*4*k)*S)],fill=DARK,width=max(1,int(1.2*k*S)))
    disc(dd,hx+ux*1*k+px*1.6*k,hy+uy*1*k+py*1.6*k,0.9*k,DARK); disc(dd,hx+ux*1*k-px*1.6*k,hy+uy*1*k-py*1.6*k,0.9*k,DARK)
def tri(dd,col=EDG,w=5,P=(PA,PB,PC)):
    for i in range(3):
        a,b=P[i],P[(i+1)%3]; dd.line([(a[0]*S,a[1]*S),(b[0]*S,b[1]*S)],fill=col,width=w*S)
    for p in P: disc(dd,p[0],p[1],7,CARD,col,3)
CW=[(PA,PC),(PC,PB),(PB,PA)]    # sens horaire : A->C, C->B, B->A
CCW=[(PA,PB),(PB,PC),(PC,PA)]
def lerp(a,b,f): return (a[0]+(b[0]-a[0])*f,a[1]+(b[1]-a[1])*f)
def ang(a,b): return math.atan2(b[1]-a[1],b[0]-a[0])
def ant_on(dd,e,f,t,k=1.15,col=None,walk=True):
    p=lerp(e[0],e[1],f); ant(dd,p[0],p[1]-6,ang(*e),k,col,t,walk)
def mini(dd,cx,y,dirs,hl=None,w=66,h=80):
    c=GRN if hl=='g' else (RED if hl=='r' else EDGE)
    box(dd,cx-w/2,y,w,h,fill=CARD,border=c,bw=3,shadow=(3,3,BLACK))
    P=[(cx,y+16),(cx-22,y+58),(cx+22,y+58)]
    for i in range(3):
        a,b=P[i],P[(i+1)%3]; dd.line([(a[0]*S,a[1]*S),(b[0]*S,b[1]*S)],fill=EDGE,width=2*S)
    for i,p in enumerate(P):
        q=P[(i+1)%3] if dirs[i]=='b' else P[(i+2)%3]   # 'b' : A->B ; 'c' : A->C
        f=lerp(p,q,0.38); col=CYAN if dirs[i]=='b' else CORAL
        disc(dd,f[0],f[1],5,col,DARK,1)
ALL8=[(a,b,c) for a in 'bc' for b in 'bc' for c in 'bc']
def cases(dd,hl=None,y0=124):
    for i,d in enumerate(ALL8):
        r,c=divmod(i,4); cx=12+33+c*74
        good=(d in (('b','b','b'),('c','c','c')))   # tous dans le même sens (voir note)
        h=None
        if hl=='good': h='g' if good else None
        if hl=='all': h=None
        if hl=='bad': h='r' if not good else 'g'
        mini(dd,cx,y0+r*92,d,h)
HEADS={'s1':[('3 ',GOLD),('fourmis',CREAM)],
 's2':[('Une fourmi par ',CREAM),('coin',GOLD)],
 's3':[('Chacune ',CREAM),('choisit',CORAL),(' au hasard',CREAM)],
 's4':[('Elle part ',CREAM),('tout droit',CYAN)],
 's5':[('Deux fourmis sur le ',CREAM),('même côté',RED)],
 's6':[('Elles se ',CREAM),('rencontrent',RED)],
 's7':[('Direction : ',CREAM),('pile ou face',GOLD)],
 'q':[('Aucune ',CREAM),('collision',CORAL),(' ?',CREAM)],
 'r0':[('La ',CREAM),('réponse',GOLD)],
 'r1':[('1 chance sur ',CREAM),('4',GOLD)],
 'r2':[('Chaque fourmi : ',CREAM),('2 choix',CYAN)],
 'r3':[('Au total : ',CREAM),('8 façons',GOLD)],
 'r4':[('Éviter ',CREAM),('toute collision',RED)],
 'r5':[('Les 3 dans le ',CREAM),('même sens',GRN)],
 'r6':[('Sens des ',CREAM),('aiguilles',CYAN)],
 'r7':[('Ou le sens ',CREAM),('contraire',CORAL)],
 'r8':[('2 cas sur ',CREAM),('8',GRN)],
 'r9':[('Donc ',CREAM),('25 %',GRN)],
 'r10':[('Autrement ',CREAM),('dit',GOLD)],
 'r11':[('3 chances sur ',CREAM),('4',RED)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','q')
def coll(dd,cx,cy,t):
    r=random.Random(5)
    for i in range(12):
        a=i*math.pi/6; L=14+8*math.sin(t*12+i)
        dd.line([((cx+8*math.cos(a))*S,(cy+8*math.sin(a))*S),((cx+(8+L)*math.cos(a))*S,(cy+(8+L)*math.sin(a))*S)],fill=(GOLD if i%2 else RED),width=3*S)
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            tri(dd)
            for i,p in enumerate((PA,PB,PC)): ant(dd,p[0],p[1]-16,-math.pi/2+i*2.1,1.2,t=t,walk=False)
            tagc(dd,cx,364,'TROIS FOURMIS',GOLD)
        elif key=='s2':
            tri(dd)
            for i,p in enumerate((PA,PB,PC)):
                ant(dd,p[0],p[1]-16,-math.pi/2,1.4,t=t,walk=False)
            tagc(dd,cx,364,'UNE FOURMI SUR CHAQUE COIN',GOLD)
        elif key=='s3':
            tri(dd)
            for i,p in enumerate((PA,PB,PC)):
                ant(dd,p[0],p[1]-14,-math.pi/2,1.2,t=t,walk=False)
            T(dd,'?',cx,196,80,'press',64,GOLD,align='c',shadow=(4,4,BLACK))
            for i,(p,q1,q2) in enumerate(((PA,PB,PC),(PB,PC,PA),(PC,PA,PB))):
                for qq,col in ((q1,CYAN),(q2,CORAL)):
                    m=lerp(p,qq,0.30); disc(dd,m[0],m[1],4,col,DARK,1)
            tagc(dd,cx,364,'ELLES CHOISISSENT AU HASARD',CORAL)
        elif key=='s4':
            tri(dd)
            f=0.12+0.42*min(1,lt/max(0.6,dur-0.2))
            dirs=[CW[0],CW[1],CCW[2]]   # A->C, C->B, B->C
            dirs=[(PA,PC),(PC,PB),(PB,PA)]
            for e in dirs: ant_on(dd,e,f,t)
            tagc(dd,cx,364,'ELLES PARTENT TOUT DROIT',CYAN)
        elif key=='s5':
            tri(dd)
            f=0.12+0.2*min(1,lt/max(0.6,dur-0.2))
            ant_on(dd,(PB,PC),f,t,1.2,col=rgb('#E8D9B8')); ant_on(dd,(PC,PB),f,t,1.2,col=rgb('#F2A65A'))
            lbl(dd,cx,320,'MÊME CÔTÉ',RED,10); tagc(dd,cx,364,'SUR UN MÊME CÔTÉ',RED)
        elif key=='s6':
            tri(dd)
            m=lerp(PB,PC,0.5); ant(dd,m[0]-24,m[1]-10,0,1.2,t=t,walk=False); ant(dd,m[0]+24,m[1]-10,math.pi,1.2,col=rgb('#F2A65A'),t=t,walk=False)
            coll(dd,m[0],m[1]-34,t); stamp(dd,cx,190,'COLLISION !',RED,14)
            tagc(dd,cx,364,'ELLES SE RENCONTRENT',RED)
        elif key=='s7':
            for i,(x,c) in enumerate(((84,'P'),(228,'F'))):
                coin(dd,x,200,44,c if c=='P' else 'F',squash=abs(math.cos(t*5+i*2)))
            T(dd,'OU',cx,194,24,'press',20,CREAM,align='c')
            lbl(dd,84,262,'SENS 1',CYAN,10); lbl(dd,228,262,'SENS 2',CORAL,10)
            tagc(dd,cx,364,'PILE OU FACE POUR CHACUNE',GOLD)
        elif key=='q':
            tri(dd)
            for i,p in enumerate((PA,PB,PC)): ant(dd,p[0],p[1]-14,-math.pi/2,1.2,t=t,walk=False)
            T(dd,'?',cx,196,100,'press',80,GOLD,align='c',shadow=(5,5,BLACK))
            tagc(dd,cx,364,'AUCUNE COLLISION ?',CORAL)
        elif key=='r0':
            T(dd,'!',cx,150,150,'press',120,GOLD,align='c',shadow=(7,7,BLACK)); star(dd,50,200,t,6); star(dd,262,200,t+1,6); stamp(dd,cx,320,'LA PROBABILITÉ',GOLD,12); tagc(dd,cx,364,'LA RÉPONSE',GOLD)
        elif key=='r1':
            T(dd,'1/4',cx,160,110,'press',90,GOLD,align='c',shadow=(6,6,BLACK)); stamp(dd,cx,300,'1 CHANCE SUR 4',GOLD,12); tagc(dd,cx,364,'UNE CHANCE SUR QUATRE',GOLD)
        elif key=='r2':
            tri(dd)
            for p in (PA,PB,PC): ant(dd,p[0],p[1]-14,-math.pi/2,1.1,t=t,walk=False)
            for p,q1,q2 in ((PA,PB,PC),(PB,PC,PA),(PC,PA,PB)):
                for qq,col in ((q1,CYAN),(q2,CORAL)):
                    m=lerp(p,qq,0.32); disc(dd,m[0],m[1],5,col,DARK,1)
            T(dd,'2',cx,200,60,'press',46,GOLD,align='c',shadow=(4,4,BLACK)); T(dd,'CHOIX',cx,244,20,'press',14,CREAM,align='c')
            tagc(dd,cx,364,'DEUX CHOIX PAR FOURMI',CYAN)
        elif key=='r3':
            T(dd,'2×2×2 = 8',cx,106,30,'press',22,GOLD,align='c',shadow=(3,3,BLACK))
            cases(dd,y0=130); tagc(dd,cx,364,'HUIT FAÇONS DE PARTIR',GOLD)
        elif key=='r4':
            tri(dd)
            m=lerp(PB,PC,0.5); ant(dd,m[0]-24,m[1]-10,0,1.2,t=t,walk=False); ant(dd,m[0]+24,m[1]-10,math.pi,1.2,col=rgb('#F2A65A'),t=t,walk=False)
            xmark_(dd,cx,206,36,10,RED); tagc(dd,cx,364,'ÉVITER TOUTE COLLISION',RED)
        elif key=='r5':
            tri(dd)
            f=0.10+0.45*((lt/1.6)%1.0)
            for e in CW: ant_on(dd,e,f,t)
            check(dd,cx,206,30,9,GRN); tagc(dd,cx,364,'LES TROIS DANS LE MÊME SENS',GRN)
        elif key=='r6':
            tri(dd,col=rgb('#4A6A9A'))
            f=0.10+0.45*((lt/1.6)%1.0)
            for e in CW: ant_on(dd,e,f,t,1.0)
            clock(dd,cx,226,30,hh=10.0,mm=int(lt*10)%60,col=CREAM)
            tagc(dd,cx,364,'SENS DES AIGUILLES D’UNE MONTRE',CYAN)
        elif key=='r7':
            tri(dd,col=rgb('#9A5A4A'))
            f=0.10+0.45*((lt/1.6)%1.0)
            for e in CCW: ant_on(dd,e,f,t,1.0)
            clock(dd,cx,226,30,hh=10.0,mm=(60-int(lt*10))%60,col=CREAM)
            lbl(dd,cx,122,'SENS CONTRAIRE',CORAL,10); tagc(dd,cx,364,'TOUTES DANS L’AUTRE SENS',CORAL)
        elif key=='r8':
            T(dd,'2 / 8',cx,106,30,'press',22,GRN,align='c',shadow=(3,3,BLACK))
            cases(dd,hl='good',y0=130); tagc(dd,cx,364,'DEUX CAS SUR HUIT',GRN)
        elif key=='r9':
            T(dd,'2 / 8',cx,130,40,'press',32,CREAM,align='c',shadow=(3,3,BLACK)); vline(dd,70,SW-70,190,GOLD); T(dd,'= 1/4',cx,214,40,'press',32,CYAN,align='c')
            T(dd,'25 %',cx,270,60,'press',46,GRN,align='c',shadow=(5,5,BLACK)); tagc(dd,cx,364,'VINGT-CINQ POUR CENT',GRN)
        elif key=='r10':
            T(dd,'1 - 1/4 = 3/4',cx,150,26,'press',17,CREAM,align='c',shadow=(3,3,BLACK)); barrow(dd,2,'COLLISION : TROIS CAS SUR QUATRE','',0.75,RED); stamp(dd,cx,290,'LE CONTRAIRE',GOLD,12); tagc(dd,cx,364,'AUTREMENT DIT',GOLD)
        elif key=='r11':
            barrow(dd,0,'ELLES SE RENCONTRENT','75 %',0.75,RED,hl=True); barrow(dd,1,'AUCUNE COLLISION','25 %',0.25,GRN)
            T(dd,'3 / 4',cx,240,70,'press',54,RED,align='c',shadow=(5,5,BLACK)); tagc(dd,cx,364,'TROIS CHANCES SUR QUATRE',RED)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#043'
    def fn(lay,dd):
        tri(dd,P=((156,150),(66,310),(246,310)))
        for i,p in enumerate(((156,150),(66,310),(246,310))): ant(dd,p[0],p[1]-16,-math.pi/2+i*2.1,1.2,t=t,walk=False)
        T(dd,'?',156,222,100,'press',80,GOLD,align='c',shadow=(5,5,BLACK))
        T(dd,'3 FOURMIS,',SW/2,16,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'UNE COLLISION ?',SW/2,52,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DES TROIS FOURMIS"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#044')
