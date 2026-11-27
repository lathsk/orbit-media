from render_e4x import *
import inspect, math
import numpy as np
from PIL import Image
B.NUM='#066'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
PURP=(176,92,255)
PAL=[CYAN,CORAL,GOLD,GRN,PURP,RED,CREAM]
PR=84.0
CX_,CY_=156,206
def mkline(theta_deg,d):
    a=math.radians(theta_deg); return (math.cos(a),math.sin(a),d)
TRI=[mkline(90,26),mkline(210,26),mkline(330,26)]
FOUR=TRI+[mkline(80,25)]
DIAM=[mkline(0,0),mkline(60,0),mkline(120,0)]
_G={}
def grid(R):
    k=round(R*10)
    if k not in _G:
        N=int(2*(R+3)*S); c=N/2.0
        ys,xs=np.mgrid[0:N,0:N]; X=(xs+0.5-c)/S; Y=(ys+0.5-c)/S
        _G[k]=(N,X,Y,np.hypot(X,Y))
    return _G[k]
def region_ids(lines,R):
    N,X,Y,r=grid(R); rid=np.zeros((N,N),np.int32)
    for i,(nx,ny,d) in enumerate(lines): rid|=((nx*X+ny*Y)>d).astype(np.int32)<<i
    return rid
def regions(lines,R):
    """renvoie (rid compacté, nb, centroïdes) pour la configuration"""
    N,X,Y,r=grid(R); rid=region_ids(lines,R); inside=r<=R
    ids=sorted(set(np.unique(rid[inside]).tolist())); mp={v:i for i,v in enumerate(ids)}
    comp=np.full(rid.shape,-1,np.int32)
    for v,i in mp.items(): comp[(rid==v)&inside]=i
    cents=[]
    dm=(R-r).copy()
    for (nx,ny,d) in lines: dm=np.minimum(dm,np.abs(nx*X+ny*Y-d))
    for i in range(len(ids)):
        m=(comp==i)
        dd_=np.where(m,dm,-1.0); k=np.argmax(dd_); yy,xx=divmod(int(k),dd_.shape[1])
        cents.append((float(X[yy,xx]),float(Y[yy,xx])))
    return comp,len(ids),cents
_RC={}
def regs(lines,R):
    k=(tuple(lines),R)
    if k not in _RC: _RC[k]=regions(list(lines),R)
    return _RC[k]
_TOP=[(-30,-34,9),(26,-40,9),(46,6,9),(8,-6,9),(-48,8,9),(-20,38,9),(30,44,9),(-4,60,8),(-58,-26,8)]
def pizza(lay,dd,cx,cy,R=PR,lines=(),prog=None,color=None,hl=None,dim=(),labels=False,toppings=False,linecol=None,lw=1.7,hlcol=GOLD):
    """lines : coupes (toutes dessinées) ; color : liste de couleurs par région ; prog : avancement de la DERNIÈRE ligne (0-1)"""
    N,X,Y,r=grid(R)
    lines=list(lines)
    full=lines if (prog is None or prog>=1) else lines[:-1]
    img=np.zeros((N,N,4),np.uint8)
    inside=r<=R
    crust=(r>R-7)&inside
    base=np.zeros((N,N,3),np.float32); base[:]=(242,179,61)
    comp=None; nreg=1; cents=[]
    if full:
        comp,nreg,cents=regs(full,R)
    if color is not None and comp is not None:
        for i in range(nreg):
            col=color[i%len(color)] if not isinstance(color,dict) else color.get(i,(90,95,115))
            base[comp==i]=col
        cr=base*0.72
    else:
        cr=np.zeros_like(base); cr[:]=(201,138,60)
    out=np.where(crust[...,None],cr,base)
    if toppings:
        for (tx,ty,tr) in _TOP:
            m=np.hypot(X-tx,Y-ty)<=tr
            out[m]=(214,60,70); m2=np.hypot(X-tx,Y-ty)<=tr-3.5; out[m2]=(235,92,92)
    # lignes de coupe
    for i,(nx,ny,d) in enumerate(lines):
        pr=1.0
        if i==len(lines)-1 and prog is not None: pr=prog
        if pr<=0: continue
        dist=np.abs(nx*X+ny*Y-d)
        tx_,ty_=-ny,nx; half=math.sqrt(max(R*R-d*d,1));
        u=((X-d*nx)*tx_+(Y-d*ny)*ty_)  # -half..half
        m=(dist<lw/2)&(u<=-half+2*half*pr+0.01)&(r<=R+0.5)
        col=linecol if linecol is not None else DARK
        if hl is not None and i==hl: col=hlcol
        out[m]=col
        if hl is not None and i==hl:
            m2=(dist<lw/2+1.3)&(u<=-half+2*half*pr+0.01)&(r<=R+0.5)&(~m); out[m2]=DARK
    img[...,:3]=np.clip(out,0,255).astype(np.uint8)
    ring=(r<=R+2.0)
    img[...,3]=np.where(ring,255,0)
    edge=(r>R)&(r<=R+2.0); img[edge,:3]=DARK
    im=Image.fromarray(img,'RGBA')
    lay.paste(im,(int(round((cx)*S-N/2)),int(round((cy)*S-N/2))),im)
    if labels and comp is not None:
        for i,(x,y) in enumerate(cents):
            if isinstance(labels,(list,tuple)) and i>=len(labels): continue
            T(dd,str(i+1),cx+x,cy+y-6,12,'press',11 if nreg<8 else 9,DARK,align='c')
    return comp,nreg,cents
def arrow_dir(dd,x1,y1,x2,y2,col=CREAM,w=4):
    dd.line([(x1*S,y1*S),(x2*S,y2*S)],fill=col,width=w*S)
    a=math.atan2(y2-y1,x2-x1); L=9
    p=[(x2,y2),(x2-L*math.cos(a-0.5),y2-L*math.sin(a-0.5)),(x2-L*math.cos(a+0.5),y2-L*math.sin(a+0.5))]
    dd.polygon([(px*S,py*S) for px,py in p],fill=col)
def knife(dd,cx,top,col=CREAM,hcol=rgb('#8A5E2E')):
    dd.polygon([((cx-9)*S,(top+4)*S),((cx+9)*S,(top)*S),((cx+9)*S,(top+54)*S),((cx-9)*S,(top+54)*S)],fill=col,outline=DARK)
    dd.line([((cx-9)*S,(top+4)*S),((cx+9)*S,(top)*S)],fill=DARK,width=2*S)
    box(dd,cx-9,top+54,18,22,fill=hcol,border=DARK,bw=2)
def envelope(dd,cx,by,t):
    bx=cx-46; box(dd,bx,by,92,64,fill=CREAM,border=DARK,bw=3,shadow=(4,4,BLACK))
    dd.line([(bx*S,by*S),((bx+46)*S,(by+34)*S),((bx+92)*S,by*S)],fill=DARK,width=3*S)
HEADS={'s1':[('Trois coups de ',CREAM),('couteau',GOLD)],
 's2':[('Une pizza ',CREAM),('bien ronde',GOLD)],
 's3':[('Trois coups ',CREAM),('droits',CORAL)],
 's4':[('Tu coupes ',CREAM),('où tu veux',GOLD)],
 's5':[('On ne ',CREAM),('déplace',RED),(' rien',CREAM)],
 'q':[('Combien de ',CREAM),('parts',GOLD),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('7 parts',GRN)],
 'r1':[('Beaucoup disent ',CREAM),('6',RED)],
 'r2':[('Premier coup : ',CREAM),('2 parts',CYAN)],
 'r3':[('2e coup : ',CREAM),('4 parts',CYAN)],
 'r4':[('3e coup : ',CREAM),('croise tout',GOLD)],
 'r5':[('Il coupe ',CREAM),('3 morceaux',GOLD)],
 'r6':[('4 + 3 = ',CREAM),('7',GRN)],
 'r7':[('4e coup : ',CREAM),('11 parts',GOLD)],
 'r8':[('Coup ',CREAM),('n',GOLD),(' : ajoute ',CREAM),('n',GOLD),(' parts',CREAM)],
 'r9':[('Envoie-la !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            pizza(lay,dd,cx,CY_,toppings=True)
            numcard(dd,cx,306,'COMBIEN DE PARTS ?',GOLD,12)
            tagc(dd,cx,364,'3 COUPS DE COUTEAU',GOLD)
        elif key=='s2':
            pizza(lay,dd,cx,CY_,toppings=True)
            if blink(t): star(dd,34,138,t,4); star(dd,280,280,t+1,4)
            numcard(dd,cx,306,'1 PIZZA RONDE',CORAL,14)
            tagc(dd,cx,364,'UNE PIZZA BIEN RONDE',CORAL)
        elif key=='s3':
            pizza(lay,dd,cx,176,R=62,toppings=True)
            th=[0.55,1.35,2.15]
            for i,x in enumerate((62,156,250)):
                on=lt>=th[i]
                knife(dd,x,262+(0 if not on else -6),CREAM if on else rgb('#5a5f73'))
                numchip=T(dd,str(i+1),x,242,16,'press',14,GOLD if on else GREY,align='c')
            tagc(dd,cx,364,'TROIS COUPS DE COUTEAU DROITS',CORAL)
        elif key=='s4':
            pizza(lay,dd,cx,CY_,toppings=True)
            p_=sp(lt,0.2,1.2); a_=math.radians(25)
            if True:
                ox,oy=cx-70*math.cos(a_)*(1-p_)-0,0
            numcard(dd,cx,306,'CHOISIS OÙ COUPER',CYAN,12)
            for k_,(qx,qy) in enumerate(((100,150),(214,150),(100,262),(214,262))):
                if lt>=0.2+0.35*k_: star(dd,qx,qy,t+k_,3)
            tagc(dd,cx,364,'TU PEUX COUPER OÙ TU VEUX',CYAN)
        elif key=='s5':
            pizza(lay,dd,cx,CY_,R=66,toppings=True)
            for (a,b,c_,d_) in ((156,110,156,84),(156,302,156,328),(76,206,48,206),(236,206,264,206)):
                pass
            for (x1,y1,x2,y2) in ((84,206,56,206),(228,206,256,206),(156,138,156,112)):
                arrow_dir(dd,x1,y1,x2,y2,rgb('#5a5f73'),4)
            xmark_(dd,cx,CY_,92,7,RED)
            stamp(dd,cx,318,'ON NE BOUGE RIEN',RED,11)
            tagc(dd,cx,364,'ON NE DÉPLACE JAMAIS LES MORCEAUX',RED)
        elif key=='q':
            pizza(lay,dd,cx,CY_,toppings=True)
            numcard(dd,cx,306,'? PARTS MAX',GOLD,14)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            pizza(lay,dd,cx,CY_,lines=TRI,color=PAL,labels=True)
            numcard(dd,cx,306,'7 PARTS',GRN,16)
            tagc(dd,cx,364,'AU MAXIMUM : 7 PARTS',GRN)
        elif key=='r1':
            pizza(lay,dd,cx,CY_,lines=DIAM,color=[CYAN,CORAL,GOLD,GRN,PURP,CREAM],labels=True)
            if lt>2.6: xmark_(dd,cx,CY_,88,7,RED)
            numcard(dd,cx,306,'3 PAR LE CENTRE = 6',RED,10)
            tagc(dd,cx,364,'PAR LE CENTRE : SEULEMENT 6',RED)
        elif key=='r2':
            pizza(lay,dd,cx,CY_,lines=TRI[:1],color=[CYAN,CORAL],labels=True,prog=sp(lt,0.1,0.8))
            numcard(dd,cx,306,'2 PARTS',CYAN,16)
            tagc(dd,cx,364,'LE PREMIER COUP : 2 PARTS',CYAN)
        elif key=='r3':
            pizza(lay,dd,cx,CY_,lines=TRI[:2],color=[CYAN,CORAL,GOLD,GRN],labels=True,prog=sp(lt,0.1,0.8))
            numcard(dd,cx,306,'4 PARTS',CYAN,16)
            tagc(dd,cx,364,'IL CROISE LE PREMIER : 4 PARTS',CYAN)
        elif key=='r4':
            pizza(lay,dd,cx,CY_,lines=TRI,color=[CYAN,CORAL,PURP,GRN],prog=sp(lt,0.3,2.0),hl=2,linecol=DARK)
            numcard(dd,cx,306,'CROISE LES DEUX',GOLD,12)
            tagc(dd,cx,364,'LOIN DU CENTRE, IL CROISE TOUT',GOLD)
        elif key=='r5':
            comp,nreg,cents=regs(TRI[:2],PR)
            # régions de 2 coups traversées par le 3e
            N,X,Y,r=grid(PR); nx,ny,d=TRI[2]; band=(np.abs(nx*X+ny*Y-d)<1.0)&(r<=PR)
            crossed=set(np.unique(comp[band]).tolist())-{-1}
            pc=[CYAN,CORAL,GRN,PURP]; col={i:(pc[i%4] if i in crossed else (60,66,90)) for i in range(nreg)}
            pizza(lay,dd,cx,CY_,lines=TRI,color=None,hl=2,linecol=DARK) if False else None
            # on colore les régions des 2 premiers coups et on trace le 3e
            lines=TRI
            # image : couleurs par région à 2 coups + tracé du 3e coup
            _pizza2(lay,dd,cx,CY_,col,crossed,t)
            numcard(dd,cx,306,'3 MORCEAUX COUPÉS',GOLD,10)
            tagc(dd,cx,364,'CHACUN COUPÉ EN DEUX',GOLD)
        elif key=='r6':
            pizza(lay,dd,cx,170,R=62,lines=TRI,color=PAL,labels=False)
            numcard(dd,64,262,'4',CYAN,16); numcard(dd,156,262,'+ 3',GOLD,16); numcard(dd,252,262,'= 7',GRN,16)
            tagc(dd,cx,364,'4 + 3 = 7 PARTS',GRN)
        elif key=='r7':
            pizza(lay,dd,cx,CY_,R=80,lines=FOUR,color=PAL+[rgb('#FF9ECF'),rgb('#7CFFB2'),rgb('#FFA94D'),rgb('#9DB4FF')],labels=False,prog=sp(lt,0.1,0.9))
            numcard(dd,cx,306,'+ 4 = 11 PARTS',GOLD,12)
            tagc(dd,cx,364,'AVEC 4 COUPS : 11 PARTS',GOLD)
        elif key=='r8':
            th=[0.1,0.5,0.9,1.3]; tot=[2,4,7,11]
            for i in range(4):
                if lt<th[i]: continue
                y=122+i*54
                lbl(dd,72,y+10,'COUP %d'%(i+1),CYAN,10); T(dd,'+ %d'%(i+1),156,y+8,20,'press',14,GOLD,align='c')
                numcard(dd,246,y,str(tot[i]),GRN if i==3 else CORAL,16)
            tagc(dd,cx,364,'CHAQUE COUP AJOUTE SON NUMÉRO',GOLD)
        elif key=='r9':
            envelope(dd,cx,150,t)
            if blink(t): arrow_r(dd,cx-20,260,48,GOLD)
            tagc(dd,cx,364,'À QUELQU’UN QUI VA SE TROMPER',GOLD)
    return fn
def _pizza2(lay,dd,cx,cy,col,crossed,t):
    """pizza à 2 coups colorée par région (régions traversées par le 3e coup en or), plus le 3e trait"""
    comp,nreg,cents=regs(TRI[:2],PR)
    N,X,Y,r=grid(PR)
    base=np.zeros((N,N,3),np.float32)
    for i in range(nreg): base[comp==i]=col[i]
    crustm=(r>PR-7)
    base=np.where(crustm[...,None],base*0.72,base)
    for (nx,ny,d) in TRI[:2]:
        base[(np.abs(nx*X+ny*Y-d)<0.85)&(r<=PR)]=DARK
    nx,ny,d=TRI[2]; m=(np.abs(nx*X+ny*Y-d)<1.1)&(r<=PR)
    base[m]=CREAM if blink(t) else GOLD
    img=np.zeros((N,N,4),np.uint8); img[...,:3]=np.clip(base,0,255).astype(np.uint8)
    img[...,3]=np.where(r<=PR+2,255,0); edge=(r>PR)&(r<=PR+2); img[edge,:3]=DARK
    im=Image.fromarray(img,'RGBA'); lay.paste(im,(int(round(cx*S-N/2)),int(round(cy*S-N/2))),im)
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#066'
    def fn(lay,dd):
        cx=SW/2
        pizza(lay,dd,cx,CY_+6,toppings=True)
        numcard(dd,cx,306,'MAX : ? PARTS',GOLD,14)
        T(dd,'TROIS COUPS',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'DE COUTEAU',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="COMBIEN DE PARTS AU MAXIMUM ?"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#067','ENVOIE-LA À QUELQU’UN')
