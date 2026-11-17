from render_e4x import *
import inspect
B.NUM='#046'
def aline(dd,p,q,col,w=4):
    dd.line([(p[0]*S,p[1]*S),(q[0]*S,q[1]*S)],fill=col,width=w*S)
    a=math.atan2(q[1]-p[1],q[0]-p[0]); L=11
    pts=[(q[0]+L*0.6*math.cos(a),q[1]+L*0.6*math.sin(a)),(q[0]-L*math.cos(a)+L*0.7*math.sin(a),q[1]-L*math.sin(a)-L*0.7*math.cos(a)),(q[0]-L*math.cos(a)-L*0.7*math.sin(a),q[1]-L*math.sin(a)+L*0.7*math.cos(a))]
    dd.polygon([(x*S,y*S) for x,y in pts],fill=col)
WATER=rgb('#1B3A6E'); WATERL=rgb('#2B5A9A'); LAND=rgb('#3E8A5E'); LANDD=rgb('#245C42'); WOODB=rgb('#C98F4A')
LANDS={'B':(24,96,264,34),'D':(244,166,54,98),'C':(24,298,264,34),'A':(96,196,108,44)}
BR_={1:(124,130,124,196),2:(176,130,176,196),3:(124,240,124,298),4:(176,240,176,298),5:(204,218,244,218),6:(272,130,272,166),7:(272,264,272,298)}
ZC={'B':(156,113),'C':(156,315),'A':(150,218),'D':(271,215)}
def bridge(dd,i,col=None):
    x1,y1,x2,y2=BR_[i]; c=col or WOODB
    if x1==x2: box(dd,x1-6,y1,12,y2-y1,fill=c,border=DARK,bw=2); [box(dd,x1-6,y,12,2,fill=DARK) for y in range(y1+6,y2,8)]
    else: box(dd,x1,y1-6,x2-x1,12,fill=c,border=DARK,bw=2); [box(dd,x,y1-6,2,12,fill=DARK) for x in range(x1+6,x2,8)]
def mapw(dd,t=0.0,letters=False,bcols=None,nums=False,show=7):
    box(dd,14,88,284,252,fill=WATER)
    for (x,y) in ((60,150),(200,170),(70,265),(230,285),(40,200),(180,275)): box(dd,x,y,14,3,fill=WATERL)
    for k,(x,y,w,h) in LANDS.items(): box(dd,x,y,w,h,fill=LAND,border=LANDD,bw=3)
    for i in range(1,show+1): bridge(dd,i,(bcols or {}).get(i))
    if letters:
        for k,(x,y) in ZC.items(): T(dd,k,x,y-10,22,'press',16,CREAM,align='c',shadow=(2,2,BLACK))
    if nums:
        for i in range(1,show+1):
            x1,y1,x2,y2=BR_[i]; T(dd,str(i),(x1+x2)/2+(14 if x1==x2 else 0),(y1+y2)/2-(6 if x1==x2 else 20),14,'press',11,GOLD,align='c',shadow=(2,2,BLACK))
def deg(dd,k,v,col=GOLD,size=22):
    x,y=ZC[k]; disc(dd,x,y,18,DARK); disc(dd,x,y,16,CARD,col,3); T(dd,str(v),x,y-9,20,'press',size-4,col,align='c')
HEADS={'s1':[('Sept ponts, ',CREAM),('une règle',GOLD)],
 's2':[('Visite d’',CREAM),('une ville',GOLD)],
 's3':[('Une ',CREAM),('rivière, ',CYAN),('une île',GOLD)],
 's4':[('Quatre ',CREAM),('zones',GOLD)],
 's5':[('Sept ',CREAM),('ponts',GOLD)],
 's6':[('Chaque pont : ',CREAM),('une fois',CORAL)],
 's7':[('Départ : ',CREAM),('où il veut',CYAN)],
 'q':[('Peut-il ',CREAM),('y arriver',CORAL),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('impossible',RED)],
 'r1':[('Le génie ',CREAM),('Euler',GOLD)],
 'r2':[('La théorie des ',CREAM),('graphes',CYAN)],
 'r3':[('Les quatre ',CREAM),('zones',GOLD)],
 'r4':[('Ponts par ',CREAM),('zone',CYAN)],
 'r5':[('On entre, ',CREAM),('on sort',CORAL)],
 'r6':[('Les ponts vont ',CREAM),('par deux',GOLD)],
 'r7':[('Seuls ',CREAM),('départ',CYAN),(' et ',CREAM),('arrivée',CORAL)],
 'r8':[('Ici : ',CREAM),('4 impaires',RED)],
 'r9':[('Donc ',CREAM),('impossible',RED)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','q')
PATH=[1,3,4,2,6,5]
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            mapw(dd,t); T(dd,'?',60,196,80,'press',64,GOLD,align='c',shadow=(5,5,BLACK))
            tagc(dd,cx,364,'TRAVERSE CHAQUE PONT UNE FOIS',GOLD)
        elif key=='s2':
            mapw(dd,t); sprite(dd,DET,DPAL,34,129-24*1.8+math.sin(t*4)*1,1.8,20)
            tagc(dd,cx,364,'UNE VILLE ET SA RIVIÈRE',CYAN)
        elif key=='s3':
            mapw(dd,t); lbl(dd,60,106,'RIVE',CREAM,9); lbl(dd,60,308,'RIVE',CREAM,9); lbl(dd,150,206,'ÎLE',GOLD,10)
            tagc(dd,cx,364,'UNE ÎLE ET DEUX RIVES',CYAN)
        elif key=='s4':
            mapw(dd,t,letters=True); tagc(dd,cx,364,'QUATRE ZONES',GOLD)
        elif key=='s5':
            n=1+int(lt/0.22); mapw(dd,t,nums=True,bcols={i:CYAN for i in range(1,min(7,n)+1)}); tagc(dd,cx,364,'RELIÉES PAR SEPT PONTS',GOLD)
        elif key=='s6':
            k=sum(1 for th in (0.3,1.2,2.1,3.0,3.9,4.6) if lt>th)
            mapw(dd,t,bcols={PATH[j]:CYAN for j in range(k)}); tagc(dd,cx,364,'CHAQUE PONT, UNE SEULE FOIS',CORAL)
        elif key=='s7':
            mapw(dd,t,letters=True)
            for k_,(x,y) in ZC.items():
                if int(t*2)%2==0: T(dd,'?',x+22,y-26,18,'press',14,GOLD,align='c',shadow=(2,2,BLACK))
            tagc(dd,cx,364,'IL PART D’OÙ IL VEUT',CYAN)
        elif key=='q':
            sprite(dd,DET,DPAL,14,352-24*3.4+math.sin(t*4)*1.5,3.4,20)
            T(dd,'?',216,120,120,'press',100,GOLD,align='c',shadow=(5,5,BLACK)); stamp(dd,216,262,'POSSIBLE ?',CORAL,13)
            tagc(dd,cx,364,'PEUT-IL Y ARRIVER ?',CORAL)
        elif key=='r0':
            T(dd,'!',cx,130,150,'press',120,RED,align='c',shadow=(7,7,BLACK)); star(dd,48,210,t,6); star(dd,264,210,t+1,6)
            stamp(dd,cx,320,'IMPOSSIBLE',RED,14); tagc(dd,cx,364,'LA RÉPONSE',GOLD)
        elif key=='r1':
            T(dd,'EULER',cx,130,60,'press',44,GOLD,align='c',shadow=(5,5,BLACK)); T(dd,'1736',cx,200,50,'press',40,CREAM,align='c',shadow=(4,4,BLACK))
            star(dd,40,104,t,6); star(dd,272,104,t+1,6); stamp(dd,cx,290,'LA PREUVE',CORAL,12); tagc(dd,cx,364,'EULER L’A PROUVÉ EN 1736',GOLD)
        elif key=='r2':
            P={'B':(156,124),'C':(156,300),'A':(86,212),'D':(226,212)}
            def ed(a,b,off=0):
                (x1,y1),(x2,y2)=P[a],P[b]; dx,dy=y2-y1,-(x2-x1); L=math.hypot(dx,dy) or 1; ox,oy=dx/L*off,dy/L*off
                dd.line([((x1+ox)*S,(y1+oy)*S),((x2+ox)*S,(y2+oy)*S)],fill=CYAN,width=3*S)
            for a,b,o in (('A','B',-5),('A','B',5),('A','C',-5),('A','C',5),('A','D',0),('B','D',0),('C','D',0)): ed(a,b,o)
            for k_,(x,y) in P.items(): disc(dd,x,y,16,CARD,GOLD,3); T(dd,k_,x,y-9,20,'press',16,GOLD,align='c')
            tagc(dd,cx,364,'ZONES = POINTS, PONTS = TRAITS',CYAN)
        elif key=='r3':
            mapw(dd,t,letters=True); tagc(dd,cx,364,'LES QUATRE ZONES DE LA VILLE',GOLD)
        elif key=='r4':
            mapw(dd,t,letters=False)
            for (k_,v,th) in (('A',5,0.4),('B',3,1.15),('C',3,1.8),('D',3,2.4)):
                if lt>th: deg(dd,k_,v,GOLD)
            tagc(dd,cx,364,'5, 3, 3 ET 3 PONTS',GOLD)
        elif key=='r5':
            box(dd,86,170,140,80,fill=CARD,border=GOLD,bw=3,shadow=(4,4,BLACK)); T(dd,'UNE ZONE',cx,200,22,'press',14,GOLD,align='c')
            aline(dd,(cx-30,100),(cx-30,166),CYAN,5); aline(dd,(cx+30,254),(cx+30,320),CORAL,5)
            lbl(dd,cx-70,120,'ENTRE',CYAN,10); lbl(dd,cx+76,290,'SORT',CORAL,10); stamp(dd,cx+60,128,'2 PONTS',CREAM,11)
            tagc(dd,cx,364,'ENTRER PUIS SORTIR',CORAL)
        elif key=='r6':
            for i in range(5):
                x=cx+(i-2)*52; last=(i==4)
                box(dd,x-18,150,36,56,fill=CARD,border=(RED if last else (CYAN if i<2 else CORAL)),bw=3,shadow=(3,3,BLACK))
                if last and lt<1.0: box(dd,x-18,150,36,56,fill=CARD,border=EDGE,bw=3)
                box(dd,x-6,160,12,36,fill=WOODB,border=DARK,bw=2)
            T(dd,'2',cx-78,222,30,'press',24,CYAN,align='c'); T(dd,'+',cx-26,222,30,'press',24,CREAM,align='c'); T(dd,'2',cx+26,222,30,'press',24,CORAL,align='c')
            if lt>1.0: T(dd,'+',cx+65,222,30,'press',24,CREAM,align='c'); T(dd,'1',cx+104,222,30,'press',24,RED,align='c'); stamp(dd,cx,290,'1 PONT SEUL = IMPAIR',RED,11)
            tagc(dd,cx,364,'LES PONTS VONT PAR DEUX',GOLD)
        elif key=='r7':
            box(dd,26,130,120,90,fill=CARD,border=CYAN,bw=3,shadow=(3,3,BLACK)); T(dd,'DÉPART',86,150,18,'press',12,CYAN,align='c'); T(dd,'IMPAIR OK',86,182,16,'silk7',11,GOLD,align='c',sp=1)
            box(dd,166,130,120,90,fill=CARD,border=CORAL,bw=3,shadow=(3,3,BLACK)); T(dd,'ARRIVÉE',226,150,18,'press',12,CORAL,align='c'); T(dd,'IMPAIR OK',226,182,16,'silk7',11,GOLD,align='c',sp=1)
            stamp(dd,cx,270,'LES AUTRES : PAIR',GREY if False else CREAM,11)
            tagc(dd,cx,364,'DEUX IMPAIRES AU MAXIMUM',GOLD)
        elif key=='r8':
            mapw(dd,t)
            for (k_,v) in (('A',5),('B',3),('C',3),('D',3)): deg(dd,k_,v,RED)
            tagc(dd,cx,364,'ICI : QUATRE ZONES IMPAIRES',RED)
        elif key=='r9':
            xmark_(dd,cx,190,70,12,RED); stamp(dd,cx,320,'IMPOSSIBLE',RED,14); tagc(dd,cx,364,'AUCUN PARCOURS POSSIBLE',RED)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#046'
    def fn(lay,dd):
        mapw(dd,t,bcols={i:CYAN for i in (1,3,4,2,6,5)}); T(dd,'?',58,196,80,'press',64,GOLD,align='c',shadow=(5,5,BLACK))
        T(dd,'TRAVERSE CHAQUE PONT',SW/2,16,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'UNE SEULE FOIS',SW/2,50,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="LES SEPT PONTS D'EULER"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#047','ENVOIE-LA À QUELQU’UN')
