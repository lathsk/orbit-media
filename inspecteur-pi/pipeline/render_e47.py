from render_e4x import *
import inspect
B.NUM='#047'
COIN=rgb('#FFD23F'); COIN2=rgb('#E8A917'); COINR=rgb('#B8800F')
FC=(156,214); R0=34
def coin(dd,cx,cy,r,ang=None,dim=False,mark=RED):
    disc(dd,cx,cy,r+3,DARK); disc(dd,cx,cy,r,COIN,COINR,3); disc(dd,cx,cy,r-8,COIN2)
    if ang is not None:
        ex,ey=cx+(r-3)*math.cos(ang),cy+(r-3)*math.sin(ang)
        dd.line([(cx*S,cy*S),(ex*S,ey*S)],fill=DARK,width=4*S); disc(dd,ex,ey,5,mark,DARK,2)
    disc(dd,cx,cy,3,DARK)
def mpos(th,R=2*R0): return (FC[0]+R*math.cos(th),FC[1]+R*math.sin(th))
def mang(th): return math.pi+2*th
def dots(dd,cx,cy,R,col=CYAN,n=48,frac=1.0,w=3):
    for i in range(int(n*frac)):
        a=2*math.pi*i/n; disc(dd,cx+R*math.cos(a),cy+R*math.sin(a),w,col)
def arc(dd,cx,cy,r,a0,a1,col,w=5):
    dd.arc([(cx-r)*S,(cy-r)*S,(cx+r)*S,(cy+r)*S],math.degrees(a0),math.degrees(a1),fill=col,width=w*S)
def pair(dd,th,mk=True,fixed_mark=True,t=0.0):
    coin(dd,FC[0],FC[1],R0,(0.0 if False else None) if not fixed_mark else math.pi/2+0.0,mark=CYAN)
    x,y=mpos(th); coin(dd,x,y,R0,mang(th) if mk else None)
def aline(dd,p,q,col,w=4):
    dd.line([(p[0]*S,p[1]*S),(q[0]*S,q[1]*S)],fill=col,width=w*S)
    a=math.atan2(q[1]-p[1],q[0]-p[0]); L=11
    pts=[(q[0]+L*0.6*math.cos(a),q[1]+L*0.6*math.sin(a)),(q[0]-L*math.cos(a)+L*0.7*math.sin(a),q[1]-L*math.sin(a)-L*0.7*math.cos(a)),(q[0]-L*math.cos(a)-L*0.7*math.sin(a),q[1]-L*math.sin(a)+L*0.7*math.cos(a))]
    dd.polygon([(x*S,y*S) for x,y in pts],fill=col)
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-18: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
HEADS={'s1':[('Combien de ',CREAM),('tours',GOLD),(' ?',CREAM)],
 's2':[('Deux pièces ',CREAM),('identiques',GOLD)],
 's3':[('L’une reste ',CREAM),('immobile',CYAN)],
 's4':[('L’autre fait le ',CREAM),('tour',CORAL),(' de la première',CREAM)],
 's5':[('Elle roule ',CREAM),('sans glisser',GOLD)],
 's6':[('Comme une vraie ',CREAM),('roue',CORAL)],
 's7':[('Retour au ',CREAM),('départ',GOLD)],
 's8':[('Combien de ',CREAM),('tours',CORAL),(' sur elle-même ?',CREAM)],
 'q':[('Un tour, ',CREAM),('deux tours,',GOLD),(' ou plus ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('2 tours',GOLD)],
 'r1':[('Regarde le ',CREAM),('centre',CORAL)],
 'r2':[('Un cercle ',CREAM),('2 fois',GOLD),(' plus grand',CREAM)],
 'r3':[('Donc ',CREAM),('2 fois',GOLD),(' plus long',CREAM)],
 'r4':[('Elle roule ',CREAM),('2 contours',CYAN)],
 'r5':[('Deux tours ',CREAM),('complets',GOLD)],
 'r6':[('Un tour : ',CREAM),('le contour',CYAN)],
 'r7':[('Un tour de ',CREAM),('plus',CORAL),(' : le trajet',CREAM)],
 'r8':[('Teste avec ',CREAM),('2 pièces',GOLD)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            th=min(t*1.7,2*math.pi*0.97); dots(dd,FC[0],FC[1],2*R0,CYAN,n=36,w=2); pair(dd,th)
            T(dd,'?',cx,100,80,'press',64,GOLD,align='c',shadow=(5,5,BLACK)) if False else None
            if int(t*2)%2==0: T(dd,'?',60,150,50,'press',40,CORAL,align='c',shadow=(4,4,BLACK))
            tagc(dd,cx,364,'COMBIEN DE TOURS ?',GOLD)
        elif key=='s2':
            pair(dd,0.0); sprite(dd,DET,DPAL,14,286-24*1.5+math.sin(t*4)*1,1.5,20)
            lbl(dd,FC[0],262,'PIÈCE 1',CYAN,9); lbl(dd,FC[0]+2*R0,262,'PIÈCE 2',CORAL,9)
            tagc(dd,cx,364,'DEUX PIÈCES IDENTIQUES',CYAN)
        elif key=='s3':
            x,y=mpos(0.0); coin(dd,x,y,R0,math.pi,mark=RED); coin(dd,FC[0],FC[1],R0,math.pi/2,mark=CYAN)
            box(dd,FC[0]-20,FC[1]+R0+8,40,18,fill=CARD,border=CYAN,bw=2); T(dd,'FIXE',FC[0],FC[1]+R0+12,12,'silk7',10,CYAN,align='c',sp=1)
            tagc(dd,cx,364,'CELLE-CI NE BOUGE PAS',CYAN)
        elif key=='s4':
            th=min(lt*1.15,2*math.pi*0.95); dots(dd,FC[0],FC[1],2*R0,CYAN,n=36,frac=1.0,w=2)
            pair(dd,th); tagc(dd,cx,364,'ELLE FAIT LE TOUR DE L’AUTRE',CORAL)
        elif key=='s5':
            th=min(0.35+lt*0.45,1.4)
            pair(dd,th); arc(dd,FC[0],FC[1],R0+5,0,th,CYAN,5)
            x,y=mpos(th); arc(dd,x,y,R0+5,math.pi+th,math.pi+2*th,CORAL,5)
            lbl(dd,cx,106,'MÊME LONGUEUR',GOLD,9)
            tagc(dd,cx,364,'ELLE ROULE, ELLE NE GLISSE PAS',GOLD)
        elif key=='s6':
            r=26; p=min(1.0,lt/max(dur,1.5)); xx=40+p*232
            box(dd,14,230+r+3,284,8,fill=TABLEC,border=TABLED,bw=2)
            for i in range(12): box(dd,22+i*24,230+r+13,10,3,fill=TABLED)
            coin(dd,xx,230,r,(xx-40)/r+math.pi/2)
            tagc(dd,cx,364,'COMME UNE ROUE SUR UNE ROUTE',CORAL)
        elif key=='s7':
            p=min(1.0,lt/1.7); th=2*math.pi*p; dots(dd,FC[0],FC[1],2*R0,CYAN,n=36,w=2)
            pair(dd,th); sx,sy=mpos(0.0);
            lbl(dd,FC[0]+2*R0+4,FC[1]-R0-26,'DÉPART',GOLD,9) if False else lbl(dd,262,98,'DÉPART',GOLD,9)
            tagc(dd,cx,364,'JUSQU’AU POINT DE DÉPART',GOLD)
        elif key=='s8':
            th=lt*1.3; pair(dd,th); x,y=mpos(th)
            if int(t*2)%2==0: T(dd,'?',x,y-R0-34,40,'press',32,GOLD,align='c',shadow=(3,3,BLACK))
            tagc(dd,cx,364,'TOURS SUR ELLE-MÊME ?',CORAL)
        elif key=='q':
            for i,(v,c,l) in enumerate((('1',GOLD,'TOUR'),('2',CYAN,'TOURS'),('+',CORAL,'PLUS'))):
                x=52+i*104; nb(dd,x,150,v,c,w=80,h=80,size=44); lbl(dd,x,244,l,CREAM,10)
            T(dd,'?',cx,274,60,'press',44,CORAL,align='c',shadow=(4,4,BLACK)) if False else None
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'2',cx,118,150,'press',120,GOLD,align='c',shadow=(7,7,BLACK)); star(dd,48,200,t,6); star(dd,264,200,t+1,6)
            stamp(dd,cx,320,'PAS UN SEUL',RED,13); tagc(dd,cx,364,'LA RÉPONSE : DEUX TOURS',GOLD)
        elif key=='r1':
            th=lt*1.0; x,y=mpos(th); pair(dd,th,mk=False,fixed_mark=False)
            for k in range(int(th*8)): a=k/8; px,py=mpos(a); disc(dd,px,py,2,CORAL)
            disc(dd,x,y,6+2*abs(math.sin(t*5)),CORAL,DARK,2)
            tagc(dd,cx,364,'LE CENTRE DE LA PIÈCE QUI ROULE',CORAL)
        elif key=='r2':
            coin(dd,FC[0],FC[1],R0,None); dots(dd,FC[0],FC[1],2*R0,CORAL,n=40,w=2)
            aline(dd,FC,(FC[0]-R0+2,FC[1]),CYAN,3) if False else None
            dd.line([(FC[0]*S,FC[1]*S),((FC[0]-R0)*S,FC[1]*S)],fill=CYAN,width=4*S); dd.line([((FC[0]-R0)*S,FC[1]*S),((FC[0]-2*R0)*S,FC[1]*S)],fill=CORAL,width=4*S)
            lbl(dd,FC[0]-R0/2,FC[1]-30,'r',CYAN,10); lbl(dd,FC[0]-R0*1.5,FC[1]-30,'r',CORAL,10); lbl(dd,FC[0]-R0*1.5,FC[1]+40,'2r',CORAL,10) if False else None
            lbl(dd,FC[0]+2*R0-6,FC[1]-30,'2r',CORAL,10) if False else None
            tagc(dd,cx,364,'RAYON DOUBLE DE LA PIÈCE',CORAL)
        elif key=='r3':
            box(dd,56,150,100,22,fill=CYAN,border=DARK,bw=2); lbl(dd,106,118,'CONTOUR DE LA PIÈCE',CYAN,8)
            q=min(1.0,max(0,(lt-0.5)/0.9)); (box(dd,56,232,max(6,200*q),22,fill=CORAL,border=DARK,bw=2) if q>0.02 else None); lbl(dd,156,200,'TRAJET DU CENTRE',CORAL,8)
            if q>=1.0: stamp(dd,cx,300,'2 FOIS PLUS LONG',GOLD,11)
            tagc(dd,cx,364,'DEUX FOIS PLUS LONG',GOLD)
        elif key=='r4':
            r=20; L=2*math.pi*r; p=min(1.0,lt/max(dur-0.3,1.6)); xx=28+p*2*L
            box(dd,20,190+r+3,272,8,fill=TABLEC,border=TABLED,bw=2)
            for i,v in enumerate((0,1,2)):
                px=28+v*L; box(dd,px-1,190+r+12,3,14,fill=CREAM)
            lbl(dd,28+L,190+r+30,'1 CONTOUR',CYAN,8); lbl(dd,232,190+r+54,'2 CONTOURS',CORAL,8)
            coin(dd,xx,190,r,(xx-28)/r+math.pi/2)
            tagc(dd,cx,364,'ELLE ROULE DEUX CONTOURS',CYAN)
        elif key=='r5':
            p=min(1.0,lt/1.9); th=2*math.pi*p; dots(dd,FC[0],FC[1],2*R0,CYAN,n=36,w=2); pair(dd,th)
            turns=min(2,int(2*th/(2*math.pi)+0.001)); nb(dd,262,100,str(turns),GOLD,w=50,h=40,size=24); lbl(dd,262,144,'TOURS',GOLD,8)
            tagc(dd,cx,364,'DEUX TOURS COMPLETS',GOLD)
        elif key=='r6':
            r=26; ang=min(1.0,lt/1.6)*2*math.pi
            coin(dd,cx,200,r+10,ang+math.pi/2)
            aline(dd,(30,150),(30,150),CYAN) if False else None
            stamp(dd,cx,300,'+1 : LE CONTOUR ROULÉ',CYAN,10); T(dd,'1',cx,92,50,'press',40,CYAN,align='c',shadow=(4,4,BLACK)) if False else None
            tagc(dd,cx,364,'UN TOUR POUR LE CONTOUR',CYAN)
        elif key=='r7':
            th=min(1.0,lt/1.8)*2*math.pi; coin(dd,FC[0],FC[1]-2,22,None); dots(dd,FC[0],FC[1]-2,60,CORAL,n=30,w=2)
            x=FC[0]+60*math.cos(th); y=FC[1]-2+60*math.sin(th); coin(dd,x,y,22,None)
            stamp(dd,cx,300,'+1 : LE TOUR DE L’AUTRE',CORAL,10)
            if lt>1.9: T(dd,'1+1=2',cx,94,40,'press',32,GOLD,align='c',shadow=(4,4,BLACK))
            tagc(dd,cx,364,'UN TOUR DE PLUS : LE TRAJET',CORAL)
        elif key=='r8':
            box(dd,24,262,264,14,fill=TABLEC,border=TABLED,bw=2)
            coin(dd,120,230,26,math.pi/2+t*0.0,mark=CYAN); coin(dd,172,230,26,math.pi,mark=RED) if False else coin(dd,172,230,26,math.pi+0.0,mark=RED)
            sprite(dd,DET,DPAL,226,280-24*1.5+math.sin(t*4)*1,1.5,20) if False else None
            stamp(dd,cx,320,'TESTE-LE !',GOLD,13); T(dd,'2',cx,98,60,'press',44,GOLD,align='c',shadow=(4,4,BLACK))
            tagc(dd,cx,364,'DEUX PIÈCES DE MONNAIE',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#047'
    def fn(lay,dd):
        x,y=mpos(2.2); pair(dd,2.2); dots(dd,FC[0],FC[1],2*R0,CYAN,n=36,w=2)
        T(dd,'COMBIEN DE TOURS',SW/2,16,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'FAIT LA PIÈCE ?',SW/2,50,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="LE PARADOXE DES DEUX PIÈCES"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#048','ENREGISTRE-LA POUR PLUS TARD')
