from render_e4x import *
import inspect, math
from shapely.geometry import Polygon, box as sbox
from shapely.ops import unary_union
B.NUM='#062'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def ease(p): return p*p*(3-2*p)
def blink(t): return int(t*2.5)%2==0
SQ={'A':[(0,0),(5,0),(5,3),(0,5)],'B':[(0,5),(5,3),(5,8),(0,8)],'T1':[(5,0),(8,0),(8,8)],'T2':[(5,0),(5,8),(8,8)]}
RC={'A':[(0,0),(5,0),(5,3),(0,5)],'B':[(8,2),(13,0),(13,5),(8,5)],'T1':[(8,2),(8,5),(0,5)],'T2':[(13,0),(5,0),(5,3)]}
COL={'A':CYAN,'B':CORAL,'T1':GOLD,'T2':GRN}
ORDER=['A','B','T1','T2']
GAP=Polygon([(0,0),(13,0),(13,5),(0,5)]).difference(unary_union([Polygon(RC[k]) for k in ORDER]))
def sc(p,H,u,x0,y0): return (x0+p[0]*u, y0+(H-p[1])*u)
def poly(dd,pts,fill,border=DARK,bw=2):
    dd.polygon([(x*S,y*S) for x,y in pts],fill=fill)
    if border is not None: dd.line([(x*S,y*S) for x,y in pts+[pts[0]]],fill=border,width=bw*S)
U=22
SQX,SQY=(312-8*U)/2,126      # square origin (top-left) 
RCX,RCY=(312-13*U)/2,SQY+3*U   # rectangle top-left (bottom aligned with square)
def square(dd,u=U,x0=SQX,y0=SQY,sep=0.0,grid=False,keys=ORDER,dim=()):
    for k in keys:
        pts=[sc(p,8,u,x0,y0) for p in SQ[k]]
        if sep:
            cx=sum(p[0] for p in SQ[k])/len(SQ[k]); cy=sum(p[1] for p in SQ[k])/len(SQ[k])
            dx=(cx-4)*sep; dy=-(cy-4)*sep*0.3
            pts=[(x+dx,y+dy) for x,y in pts]
        poly(dd,pts,COL[k] if not dim else rgb('#5a5f73'),border=None if grid else DARK)
    if grid:
        for i in range(9):
            dd.line([((x0+i*u)*S,y0*S),((x0+i*u)*S,(y0+8*u)*S)],fill=DARK,width=1*S)
            dd.line([(x0*S,(y0+i*u)*S),((x0+8*u)*S,(y0+i*u)*S)],fill=DARK,width=1*S)
        dd.rectangle([x0*S,y0*S,(x0+8*u)*S,(y0+8*u)*S],outline=CREAM,width=2*S)
def rect(dd,u=U,x0=RCX,y0=RCY,gap=None,jit=0.0):
    for k in ORDER:
        pts=[sc(p,5,u,x0,y0) for p in RC[k]]
        poly(dd,pts,COL[k])
    if gap is not None:
        geoms=GAP.geoms if hasattr(GAP,'geoms') else [GAP]
        for g in geoms:
            poly(dd,[sc(p,5,u,x0,y0) for p in list(g.exterior.coords)[:-1]],gap,border=gap,bw=1)
def fit(P,Q):
    a0=math.atan2(P[1][1]-P[0][1],P[1][0]-P[0][0]); a1=math.atan2(Q[1][1]-Q[0][1],Q[1][0]-Q[0][0]); return a1-a0
def moving(dd,p):
    p=ease(p)
    for k in ORDER:
        P=[sc(q,8,U,SQX,SQY) for q in SQ[k]]; Q=[sc(q,5,U,RCX,RCY) for q in RC[k]]
        th=fit(P,Q)*p; c,s=math.cos(th),math.sin(th)
        pc=(sum(x for x,_ in P)/len(P),sum(y for _,y in P)/len(P)); qc=(sum(x for x,_ in Q)/len(Q),sum(y for _,y in Q)/len(Q))
        cxm=pc[0]+(qc[0]-pc[0])*p; cym=pc[1]+(qc[1]-pc[1])*p
        pts=[]
        for (x,y) in P:
            dx,dy=x-pc[0],y-pc[1]; pts.append((cxm+dx*c-dy*s,cym+dx*s+dy*c))
        poly(dd,pts,COL[k])
def clipped(dd,u,cxm,cym,scx,scy,gap=None,lim=(10,112,302,340)):
    win=sbox(*lim)
    def mp(p): return (scx+(p[0]-cxm)*u, scy+(cym-p[1])*u)   # math y-up around (cxm,cym)
    for k in ORDER:
        g=Polygon([mp(p) for p in RC[k]]).intersection(win)
        if g.is_empty: continue
        for gg in (g.geoms if hasattr(g,'geoms') else [g]):
            if gg.geom_type=='Polygon': poly(dd,list(gg.exterior.coords)[:-1],COL[k])
    if gap is not None:
        geoms=GAP.geoms if hasattr(GAP,'geoms') else [GAP]
        for g0 in geoms:
            g=Polygon([mp(p) for p in list(g0.exterior.coords)[:-1]]).intersection(win)
            if g.is_empty: continue
            for gg in (g.geoms if hasattr(g,'geoms') else [g]):
                if gg.geom_type=='Polygon': poly(dd,list(gg.exterior.coords)[:-1],gap,border=gap,bw=1)
def envelope(dd,cx,by,t):
    bx=cx-46; box(dd,bx,by,92,64,fill=CREAM,border=DARK,bw=3,shadow=(4,4,BLACK))
    dd.line([(bx*S,by*S),((bx+46)*S,(by+34)*S),((bx+92)*S,by*S)],fill=DARK,width=3*S)
HEADS={'s1':[('Une ',CREAM),('case',GOLD),(' est apparue de ',CREAM),('nulle part',RED)],
 's2':[('Un ',CREAM),('carré',CYAN),(' : ',CREAM),('64',GOLD),(' cases',CREAM)],
 's3':[('On coupe en ',CREAM),('4 morceaux',CORAL)],
 's4':[('En ',CREAM),('rectangle',CYAN),(' 13 sur 5',CREAM)],
 's5':[('5 × 13',GOLD),(' = ',CREAM),('65',RED),(' cases',CREAM)],
 'q':[('La ',CREAM),('case',GOLD),(' en plus ?',CREAM)],
 'r0':[('Ça ',CREAM),('ne colle pas',RED)],
 'r1':[('Une ',CREAM),('fente',RED),(' le long de la diagonale',CREAM)],
 'r2':[('La fente fait ',CREAM),('1 case',GOLD)],
 'r3':[('Pentes ',CYAN),('presque égales',CREAM)],
 'r4':[('2/5',CYAN),(' et ',CREAM),('3/8',GOLD)],
 'r5':[('Presque, ',GOLD),('mais pas ',CREAM),('exact',RED)],
 'r6':[('La suite de ',CREAM),('Fibonacci',GOLD)],
 'r7':[('64',CYAN),(' + ',CREAM),('1',RED),(' = ',CREAM),('65',GRN)],
 'r8':[('Diagonale ',CREAM),('pas droite',CORAL)],
 'r9':[('Envoie-la !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            u=11
            square(dd,u,18,150)
            arrow_r(dd,114,196,28,CREAM)
            rect(dd,u,150,183)
            numcard(dd,62,262,'64',CYAN,18); numcard(dd,230,262,'65 ?',RED,18)
            tagc(dd,cx,364,'UNE CASE EN PLUS ?',RED)
        elif key=='s2':
            square(dd,20,(312-160)/2,126,grid=True,keys=['A','B','T1','T2'],dim=True)
            numcard(dd,cx,306,'8 × 8 = 64',GOLD,14)
            tagc(dd,cx,364,'UN CARRÉ DE 64 CASES',CYAN)
        elif key=='s3':
            p=ease(sp(lt,0.1,0.9))
            square(dd,U,SQX,SQY-6,sep=7*p)
            tagc(dd,cx,364,'ON LE COUPE EN QUATRE MORCEAUX',CORAL)
        elif key=='s4':
            p=sp(lt,0.2,1.6)
            if p<=0: square(dd,U,SQX,SQY,sep=0)
            else: moving(dd,p)
            tagc(dd,cx,364,'ON LES RÉARRANGE : 13 SUR 5',CYAN)
        elif key=='s5':
            rect(dd,U,RCX,RCY-10)
            numcard(dd,cx,300,'5 × 13 = 65',RED,14)
            tagc(dd,cx,364,'65 CASES : UNE DE PLUS ?',RED)
        elif key=='q':
            square(dd,13,22,150); T(dd,'?',cx,198,40,'press',30,GOLD,align='c',shadow=(3,3,BLACK))
            rect(dd,13,150,164) if False else None
            numcard(dd,66,262,'64',CYAN,16); numcard(dd,246,262,'65',RED,16)
            rect(dd,10,180,186)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            rect(dd,U,RCX,RCY-10,gap=(RED if blink(t) else CREAM))
            if lt>0.5 and blink(t): stamp(dd,cx,300,'ILS NE COLLENT PAS',RED,10)
            tagc(dd,cx,364,'LES MORCEAUX NE COLLENT PAS',RED)
        elif key=='r1':
            rect(dd,U,RCX,RCY-10,gap=RED)
            dd.line([(RCX*S,(RCY-10)*S),((RCX+13*U)*S,(RCY-10+5*U)*S)],fill=CREAM,width=0) if False else None
            arrow_d(dd,cx-4,RCY-10+5*U+8,26,RED); lbl(dd,cx+60,RCY-10+5*U+16,'LA FENTE',RED,10)
            tagc(dd,cx,364,'UNE FENTE LE LONG DE LA DIAGONALE',RED)
        elif key=='r2':
            clipped(dd,52,6.5,2.5,SW/2,215,gap=RED)
            numcard(dd,cx,312,'FENTE = 1 CASE',GOLD,13)
            tagc(dd,cx,364,'ELLE FAIT EXACTEMENT 1 CASE',GOLD)
        elif key=='r3':
            u=20; by=262
            for (w,h,x0,col,txt) in [(5,2,22,CYAN,'2/5'),(8,3,138,GOLD,'3/8')]:
                poly(dd,[(x0,by),(x0+w*u,by),(x0+w*u,by-h*u)],CARD,border=col,bw=3)
                T(dd,txt,x0+w*u/2,by+14,16,'press',14,col,align='c')
                T(dd,str(h),x0+w*u-16,by-h*u/2-6,12,'press',10,col)
                T(dd,str(w),x0+w*u/2,by-26 if False else by-18,12,'press',9,CREAM,align='c') if False else None
            lbl(dd,cx,150,'PENTE = HAUTEUR ÷ LARGEUR',CREAM,9)
            tagc(dd,cx,364,'PRESQUE LA MÊME PENTE',CYAN)
        elif key=='r4':
            numcard(dd,cx,128,'2/5 = 0,4',CYAN,18)
            numcard(dd,cx,214,'3/8 = 0,375',GOLD,18)
            tagc(dd,cx,364,'DEUX CINQUIÈMES, TROIS HUITIÈMES',GOLD)
        elif key=='r5':
            numcard(dd,cx,150,'PRESQUE',GOLD,22)
            if lt>0.5: numcard(dd,cx,240,'PAS TOUT À FAIT',RED,12)
            tagc(dd,cx,364,'PRESQUE, MAIS PAS TOUT À FAIT',RED)
        elif key=='r6':
            numcard(dd,cx,120,'FIBONACCI',GOLD,16)
            xs=[48,112,176,254]
            for i,(v,thr) in enumerate([('3',2.25),('5',2.9),('8',3.65),('13',4.25)]):
                if lt>thr: numcard(dd,xs[i],230,v,[CYAN,CORAL,GOLD,GRN][i],18)
            tagc(dd,cx,364,'3 · 5 · 8 · 13',GOLD)
        elif key=='r7':
            numcard(dd,86,140,'64',CYAN,22); lbl(dd,86,210,'MORCEAUX',CYAN,9)
            if lt>1.9: numcard(dd,236,140,'+ 1',RED,22); lbl(dd,236,210,'FENTE',RED,9)
            if lt>2.9: numcard(dd,cx,252,'= 65',GRN,24)
            tagc(dd,cx,364,'64 + 1 = 65',GRN)
        elif key=='r8':
            rect(dd,U,RCX,RCY-10,gap=RED)
            xmark_(dd,cx,RCY-10+5*U+34,14,6,RED)
            tagc(dd,cx,364,'LA DIAGONALE N’EST PAS UNE DROITE',CORAL)
        elif key=='r9':
            envelope(dd,cx,150,t)
            if blink(t): arrow_r(dd,cx-20,260,48,GOLD)
            tagc(dd,cx,364,'À QUELQU’UN QUI VA SE TROMPER',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#062'
    def fn(lay,dd):
        cx=SW/2
        square(dd,14,24,150); arrow_r(dd,140,200,28,CREAM); rect(dd,10,172,180)
        numcard(dd,66,262,'64',CYAN,16); numcard(dd,236,262,'65 ?',RED,16)
        T(dd,'UNE CASE EN PLUS',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'DE NULLE PART ?',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="D’OÙ VIENT LA CASE EN PLUS ?"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#063','ENVOIE-LA À QUELQU’UN')
