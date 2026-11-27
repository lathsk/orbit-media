from render_e4x import *
import inspect, math
B.NUM='#065'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
PURP=rgb('#B05CFF')
CX_,CY_=156,214
def ang(n): return n*math.pi/6   # angle (depuis le haut, sens horaire) du nombre n
def pol(cx,cy,r,a): return (cx+r*math.sin(a), cy-r*math.cos(a))
def clockface(dd,cx,cy,R,cols=None,size=13,dim=False,hide=()):
    """horloge pixel-art avec les nombres 1..12 ; cols = {n: couleur}"""
    disc(dd,cx,cy,R+4,DARK); disc(dd,cx,cy,R,rgb('#1B2145'),outline=CREAM,w=3)
    for n in range(1,13):
        if n in hide: continue
        x,y=pol(cx,cy,R*0.76,ang(n)); c=(cols or {}).get(n,CREAM)
        if dim: c=rgb('#5a5f73')
        rr=R*0.17
        disc(dd,x,y,rr,rgb('#0B0F22'),outline=c,w=2)
        T(dd,str(n),x+(1 if n<10 else 1),y-size/2+(1 if n<10 else 1),size+4,'press',size if n<10 else size-3,c,align='c')
def cutline(dd,cx,cy,R,a_deg,col=GOLD,w=4,p=1.0,off=0.0):
    """trait droit passant par le centre ; a_deg = angle (depuis le haut, horaire) d'une extrémité"""
    a=math.radians(a_deg)
    x1,y1=pol(cx,cy,R+10,a); x2,y2=pol(cx,cy,R+10,a+math.pi)
    xe=x1+(x2-x1)*p; ye=y1+(y2-y1)*p
    dd.line([(x1*S,y1*S),(xe*S,ye*S)],fill=DARK,width=(w+4)*S); dd.line([(x1*S,y1*S),(xe*S,ye*S)],fill=col,width=w*S)
def knife_dot(dd,cx,cy,R,a_deg,p):
    a=math.radians(a_deg); x,y=pol(cx,cy,R+10,a+(math.pi)*p)
    disc(dd,x,y,6,CREAM,outline=DARK,w=2)
CUT_A=105.0   # entre le 3 et le 4 (l'extrémité opposée est entre le 9 et le 10)
CUT_V=15.0    # entre le 12 et le 1 / entre le 6 et le 7 (coupe « en deux côtés »)
SETA={4,5,6,7,8,9}; SETB={10,11,12,1,2,3}
SETV1={1,2,3,4,5,6}; SETV2={7,8,9,10,11,12}
def colsets(a,b,ca=CYAN,cb=CORAL):
    d={n:ca for n in a}; d.update({n:cb for n in b}); return d
def numchip(dd,cx,cy,n,col=GOLD,s=34,fs=14):
    box(dd,cx-s/2,cy-s/2,s,s,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK))
    T(dd,str(n),cx+1,cy-fs/2+1,fs+4,'press',fs,col,align='c')
def bookmark(dd,cx,cy,col=GOLD):
    box(dd,cx-22,cy-34,44,56,fill=col,border=DARK,bw=3)
    dd.polygon([((cx-22)*S,(cy+22)*S),((cx+22)*S,(cy+22)*S),(cx*S,(cy+2)*S)],fill=rgb('#07090F'))
    dd.polygon([((cx-19)*S,(cy+22)*S),((cx+19)*S,(cy+22)*S),(cx*S,(cy+4)*S)],fill=CARD)
def envelope(dd,cx,by,t):
    bx=cx-46; box(dd,bx,by,92,64,fill=CREAM,border=DARK,bw=3,shadow=(4,4,BLACK))
    dd.line([(bx*S,by*S),((bx+46)*S,(by+34)*S),((bx+92)*S,by*S)],fill=DARK,width=3*S)
HEADS={'s1':[('Coupe cette ',CREAM),('horloge',GOLD)],
 's2':[('Un seul ',CREAM),('trait droit',GOLD)],
 's3':[('Deux ',CREAM),('morceaux',CYAN)],
 's4':[('Le ',CREAM),('même total',GOLD)],
 'q':[('Par où passe ',CREAM),('le trait',GOLD),(' ?',CREAM)],
 'r0':[('Entre le ',CREAM),('3',CYAN),(' et le ',CREAM),('4',CYAN)],
 'r1':[('Tous les nombres : ',CREAM),('78',GOLD)],
 'r2':[('Chaque morceau : ',CREAM),('39',GRN)],
 'r3':[('Le piège : ',CREAM),('21',CYAN),(' contre ',CREAM),('57',CORAL)],
 'r4':[('Décale d’un cran : ',CREAM),('+ 6',GOLD)],
 'r5':[('21, 27, 33, ',CREAM),('39',GRN)],
 'r6':[('4 + 5 + 6 + 7 + 8 + 9',CREAM)],
 'r7':[('Enregistre',GOLD),(' l’énigme',CREAM)]}
STORY=('s1','s2','s3','s4','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            clockface(dd,cx,CY_,86)
            numcard(dd,cx,306,'MÊME SOMME ?',GOLD,16)
            tagc(dd,cx,364,'MÊME SOMME DES DEUX CÔTÉS',GOLD)
        elif key=='s2':
            clockface(dd,cx,CY_,86)
            a=CUT_V+ (lt*40)%360
            cutline(dd,cx,CY_,86,a,GOLD,4,1.0)
            numcard(dd,cx,306,'UN SEUL TRAIT',CORAL,16)
            tagc(dd,cx,364,'UN SEUL TRAIT DROIT',CORAL)
        elif key=='s3':
            clockface(dd,cx,CY_,86,cols=colsets(SETV1,SETV2))
            cutline(dd,cx,CY_,86,CUT_V,GOLD,4,1.0)
            numcard(dd,cx,306,'2 MORCEAUX',CYAN,16)
            tagc(dd,cx,364,'L’HORLOGE EN DEUX MORCEAUX',CYAN)
        elif key=='s4':
            clockface(dd,cx,176,64,cols=colsets(SETV1,SETV2),size=11)
            cutline(dd,cx,176,64,CUT_V,GOLD,3,1.0)
            numcard(dd,64,268,'?',CYAN,18); T(dd,'=',cx,274,30,'press',26,CREAM,align='c'); numcard(dd,248,268,'?',CORAL,18)
            if blink(t): lbl(dd,cx,326,'ADDITIONNÉS',GOLD,10)
            tagc(dd,cx,364,'MÊME TOTAL DES DEUX CÔTÉS',GOLD)
        elif key=='q':
            clockface(dd,cx,CY_,86)
            a=CUT_V+(lt*55)%360
            cutline(dd,cx,CY_,86,a,GOLD,4,1.0)
            numcard(dd,cx,306,'PAR OÙ ?',GOLD,16)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            p=sp(lt,0.1,1.3)
            clockface(dd,cx,CY_,86,cols=colsets(SETA,SETB) if p>=1 else None)
            cutline(dd,cx,CY_,86,CUT_A,GRN,4,p)
            if p>=1:
                for a in (CUT_A,CUT_A+180):
                    x,y=pol(cx,CY_,98,math.radians(a));
                    if blink(t): star(dd,x,y,t,3)
            numcard(dd,cx,306,'3 | 4   ET   9 | 10',GRN,12)
            tagc(dd,cx,364,'ENTRE 3 ET 4, ENTRE 9 ET 10',GRN)
        elif key=='r1':
            for i in range(12):
                numchip(dd,38+(i%6)*47.2,140+(i//6)*46,i+1,[CYAN,CORAL][i%2] if False else CREAM,34,13)
            if lt>1.2: lbl(dd,cx,244,'1 + 2 + 3 + ... + 12',CREAM,10)
            if lt>2.4: numcard(dd,cx,274,'= 78',GOLD,24)
            tagc(dd,cx,364,'TOUS LES NOMBRES FONT 78',GOLD)
        elif key=='r2':
            numcard(dd,cx,128,'78',GOLD,22); arrow_d(dd,cx-60,184,30,CREAM); arrow_d(dd,cx+60,184,30,CREAM)
            numcard(dd,72,226,'39',CYAN,22); numcard(dd,240,226,'39',CORAL,22)
            if lt>0.9: lbl(dd,cx,300,'78 ÷ 2 = 39',GRN,12)
            tagc(dd,cx,364,'CHAQUE MORCEAU DOIT VALOIR 39',GRN)
        elif key=='r3':
            clockface(dd,cx,CY_,86,cols=colsets(SETV1,SETV2))
            cutline(dd,cx,CY_,86,CUT_V,RED,4,1.0)
            numcard(dd,70,306,'21',CYAN,16); numcard(dd,242,306,'57',CORAL,16)
            if blink(t) or lt<0.5: stamp(dd,cx,102,'PAS 39 !',RED,12)
            tagc(dd,cx,364,'COUPÉ EN DEUX : 21 CONTRE 57',RED)
        elif key=='r4':
            p=sp(lt,0.4,1.6)
            a=CUT_V+30*p
            clockface(dd,cx,CY_,86,cols=colsets(set(range(1,13)) if False else set(),set()))
            cutline(dd,cx,CY_,86,CUT_V,rgb('#7a7f99'),3,1.0)
            cutline(dd,cx,CY_,86,a,GOLD,4,1.0)
            if lt>1.5: stamp(dd,252,142,'+ 6',GOLD,14)
            numcard(dd,cx,306,'1 CRAN = + 6',GOLD,14)
            tagc(dd,cx,364,'CHAQUE CRAN AJOUTE 6',GOLD)
        elif key=='r5':
            vals=[21,27,33,39]; th=[0.0,0.78,1.54,2.22]
            for i,v in enumerate(vals):
                if lt<th[i]: continue
                y=122+i*58; last=(i==3)
                numcard(dd,cx-30,y,str(v),GRN if last else CYAN,18)
                if i>0: lbl(dd,cx+80,y+12,'+ 6',GOLD,10)
            tagc(dd,cx,364,'21, 27, 33, 39',GRN)
        elif key=='r6':
            th=[0.05,0.53,1.04,1.53,1.98,2.47]
            clockface(dd,cx,296,56,cols=colsets(SETA,SETB,GRN,rgb('#5a5f73')),size=10)
            cutline(dd,cx,296,56,CUT_A,GRN,3,1.0)
            for i,n in enumerate(range(4,10)):
                if lt>=th[i]: numchip(dd,38+i*47.2,138,n,CYAN,30,13)
                if 0<i and lt>=th[i]: T(dd,'+',38+i*47.2-23.6,138-6,14,'press',11,CREAM,align='c')
            if lt>=3.4: numcard(dd,cx,176,'= 39',GRN,24)
            tagc(dd,cx,364,'4+5+6+7+8+9 = 39',GRN)
        elif key=='r7':
            bookmark(dd,cx,206)
            if blink(t): arrow_d(dd,cx,262,30,GOLD)
            tagc(dd,cx,364,'POUR LA REFAIRE PLUS TARD',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#065'
    def fn(lay,dd):
        cx=SW/2
        clockface(dd,cx,214,86)
        cutline(dd,cx,214,86,75.0,GOLD,4,1.0)
        numcard(dd,cx,306,'MÊME SOMME ?',GOLD,16)
        T(dd,'COUPE L’HORLOGE',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'EN DEUX',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="MÊME SOMME DES DEUX CÔTÉS ?"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#066','ENREGISTRE-LA POUR PLUS TARD')
