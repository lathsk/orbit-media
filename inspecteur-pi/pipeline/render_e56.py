from render_e4x import *
import inspect, math
B.NUM='#056'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
DICE={'r':(RED,[2,2,4,4,9,9],'ROUGE'),'c':(CYAN,[1,1,6,6,8,8],'CYAN'),'o':(GOLD,[3,3,5,5,7,7],'OR')}
def die_row(dd,y,k,dim=False,hl=False):
    col,fa,nm=DICE[k]; c=DIM if dim else col
    box(dd,14,y,284,54,fill=CARD,border=c,bw=4 if hl else 3,shadow=(3,3,BLACK))
    for j,v in enumerate(fa):
        box(dd,24+j*44,y+8,38,38,fill=rgb('#1B2342'),border=c,bw=2); T(dd,str(v),24+j*44+19,y+14,26,'press',18,c,align='c')
def dice_all(dd,hl=None,show=('r','c','o'),dim=()):
    for i,k in enumerate(('r','c','o')):
        if k in show: die_row(dd,122+i*70,k,dim=(k in dim),hl=(k==hl))
def arr(dd,p,q,col=CREAM,w=5,h=11):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L; nx,ny=-uy,ux
    bx,by=q[0]-ux*h,q[1]-uy*h
    dd.line([(p[0]*S,p[1]*S),(bx*S,by*S)],fill=col,width=w*S)
    dd.polygon([(q[0]*S,q[1]*S),((bx+nx*h*0.7)*S,(by+ny*h*0.7)*S),((bx-nx*h*0.7)*S,(by-ny*h*0.7)*S)],fill=col)
NODE={'r':(156,150),'c':(240,290),'o':(72,290)}
def node(dd,k,dim=False,hl=False):
    col,fa,nm=DICE[k]; c=DIM if dim else col; x,y=NODE[k]
    box(dd,x-38,y-22,76,44,fill=CARD,border=c,bw=4 if hl else 3,shadow=(3,3,BLACK)); T(dd,nm,x,y-8,16,'press',11,c,align='c')
def cyc(dd,n,t,lt=9.0,dimn=False):
    for k in 'rco': node(dd,k,dim=dimn)
    A=[((190,178),(222,262),RED,'r'),((196,304),(118,304),CYAN,'c'),((54,262),(124,178),GOLD,'o')]
    cc=[CYAN,GOLD,RED]
    for i in range(n):
        p,q,col,_=A[i]; arr(dd,p,q,col)
    lab=[(262,205),(156,312),(44,200)]
    for i in range(n):
        x,y=lab[i]; numcard(dd,x,y,'5/9',[RED,CYAN,GOLD][i],9)
HEADS={'s1':[('Choisis ton ',CREAM),('dé',GOLD),(' !',CREAM)],
 's2':[('Trois ',CREAM),('dés',GOLD),(' spéciaux',CREAM)],
 's3':[('Le dé ',CREAM),('rouge',RED)],
 's4':[('Le dé ',CREAM),('cyan',CYAN)],
 's5':[('Le dé ',CREAM),('or',GOLD)],
 's6':[('Toi, puis ',CREAM),('ton ami',CORAL)],
 's7':[('Le plus ',CREAM),('grand',GOLD),(' gagne',CREAM)],
 'q':[('Qui a l’avantage',CREAM),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('ton ami',GOLD)],
 'r1':[('Rouge',RED),(' bat ',CREAM),('cyan',CYAN)],
 'r2':[('Cyan',CYAN),(' bat ',CREAM),('or',GOLD)],
 'r3':[('Or',GOLD),(' bat ',CREAM),('rouge',RED)],
 'r4':[('Toujours un ',CREAM),('meilleur',GOLD)],
 'r5':[('Ton ami ',CREAM),('choisit après',CORAL)],
 'r6':[('Le piège : ',CREAM),('le meilleur dé',CORAL)],
 'r7':[('Envoie-la à un ',CREAM),('ami',GOLD)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','q')
def bigdie(dd,cx,y,v,col,s=70,hl=False):
    box(dd,cx-s/2,y,s,s,fill=CARD,border=col,bw=5 if hl else 3,shadow=(4,4,BLACK)); T(dd,str(v),cx,y+s/2-22,50,'press',40,col,align='c')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            dice_all(dd); 
            tagc(dd,cx,364,'TU CHOISIS UN DÉ : TU VAS PERDRE',GOLD)
        elif key=='s2':
            dice_all(dd,show=[k for i,k in enumerate('rco') if lt>0.05+i*0.45]); tagc(dd,cx,364,'TROIS DÉS SPÉCIAUX',GOLD)
        elif key=='s3':
            dice_all(dd,hl='r',dim=('c','o')); tagc(dd,cx,364,'DÉ ROUGE : 2, 4 ET 9',RED)
        elif key=='s4':
            dice_all(dd,hl='c',dim=('r','o')); tagc(dd,cx,364,'DÉ CYAN : 1, 6 ET 8',CYAN)
        elif key=='s5':
            dice_all(dd,hl='o',dim=('r','c')); tagc(dd,cx,364,'DÉ OR : 3, 5 ET 7',GOLD)
        elif key=='s6':
            numcard(dd,82,126,'TOI',CYAN,14); numcard(dd,230,126,'AMI',CORAL,14)
            bigdie(dd,82,196,'?',CYAN,76,True)
            if lt>2.4 or blink(t): bigdie(dd,230,196,'?',CORAL,76,lt>2.4)
            tagc(dd,cx,364,'TU CHOISIS, TON AMI PREND UN AUTRE',CORAL)
        elif key=='s7':
            seq=[(9,8),(4,6),(2,1),(9,6),(5,3),(9,8)]
            i=min(int(lt*2.2),len(seq)-1); a,b=seq[i]
            bigdie(dd,86,170,a,GOLD if a>b else DIM,84,a>b); bigdie(dd,226,170,b,GOLD if b>a else DIM,84,b>a)
            T(dd,'VS',cx,200,36,'press',22,CREAM,align='c')
            tagc(dd,cx,364,'LE PLUS GRAND NOMBRE GAGNE',GOLD)
        elif key=='q':
            bigdie(dd,86,150,'?',CYAN,84,True); bigdie(dd,226,150,'?',CORAL,84,True)
            T(dd,'VS',cx,180,36,'press',22,CREAM,align='c')
            if blink(t): stamp(dd,cx,290,'QUI GAGNE ?',GOLD,16)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'AMI',cx,140,100,'press',64,GOLD,align='c',shadow=(6,6,BLACK)); star(dd,30,120,t,6); star(dd,290,120,t+1,6)
            stamp(dd,cx,290,'IL CHOISIT APRÈS TOI',CORAL,11); tagc(dd,cx,364,'LA RÉPONSE : TON AMI',GOLD)
        elif key=='r1':
            cyc(dd,1,t); 
            tagc(dd,cx,364,'ROUGE BAT CYAN : 5 FOIS SUR 9',RED)
        elif key=='r2':
            cyc(dd,2,t); tagc(dd,cx,364,'CYAN BAT OR : 5 FOIS SUR 9',CYAN)
        elif key=='r3':
            cyc(dd,3,t); tagc(dd,cx,364,'OR BAT ROUGE : 5 FOIS SUR 9',GOLD)
        elif key=='r4':
            cyc(dd,3,t); 
            hl='rco'[int(lt*1.2)%3]; node(dd,hl,False,True)
            tagc(dd,cx,364,'POUR CHAQUE DÉ, UN MEILLEUR EXISTE',GOLD)
        elif key=='r5':
            numcard(dd,82,126,'TOI',CYAN,14); numcard(dd,230,126,'AMI',CORAL,14)
            bigdie(dd,82,196,'2,4,9',RED,92) if False else None
            box(dd,36,196,92,50,fill=CARD,border=RED,bw=3,shadow=(3,3,BLACK)); T(dd,'ROUGE',82,212,16,'press',11,RED,align='c')
            if lt>1.2: box(dd,184,196,92,50,fill=CARD,border=CYAN,bw=3,shadow=(3,3,BLACK)); T(dd,'CYAN',230,212,16,'press',11,CYAN,align='c'); arr(dd,(176,222),(130,222),CORAL,5,10)
            if lt>2.4: stamp(dd,cx,300,'55,6 % POUR LUI',CORAL,13)
            tagc(dd,cx,364,'TON AMI CHOISIT APRÈS TOI',CORAL)
        elif key=='r6':
            cyc(dd,3,t,dimn=True)
            if lt>0.4: xmark_(dd,156,230,40,9,RED)
            tagc(dd,cx,364,'IL N’Y A PAS DE MEILLEUR DÉ',CORAL)
        elif key=='r7':
            bx,by=cx-46,150; box(dd,bx,by,92,64,fill=CREAM,border=DARK,bw=3,shadow=(4,4,BLACK))
            dd.line([(bx*S,by*S),((bx+46)*S,(by+34)*S),((bx+92)*S,by*S)],fill=DARK,width=3*S)
            if blink(t): arrow_r(dd,cx-20,260,48,GOLD)
            tagc(dd,cx,364,'À QUELQU’UN QUI VA SE TROMPER',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#056'
    def fn(lay,dd):
        dice_all(dd)
        T(dd,'CHOISIS TON DÉ,',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'TU VAS PERDRE !',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="TROIS DÉS, UN SEUL GAGNANT"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#057','ENVOIE-LA À QUELQU’UN')
