from render_e4x import *
import inspect, random
B.NUM='#048'
_r=random.Random(47); SEQ=[_r.randint(0,1) for _ in range(100)]   # 0 = pile (P), 1 = face (F) ; série de 6 faces aux lancers 2..7
RUN=(2,7)
PC=GOLD; FC_=CYAN
def cell(dd,x,y,v,w=22,hl=False,dim=False,q=False):
    col=PC if v==0 else FC_
    if dim: col=DIM
    box(dd,x,y,w,w,fill=CARD,border=(CORAL if hl else col),bw=3 if not hl else 4)
    ch='?' if q else ('P' if v==0 else 'F'); sz=max(8,int(w*0.5))
    T(dd,ch,x+w/2,y+(w-sz)/2+1,sz+4,'press',sz,(GOLD if q else col),align='c')
GX0=(SW-10*24)/2; GY0=94
def grid(dd,n=100,hl=(),dim=False,w=22,gap=24,y0=GY0,seq=SEQ,upto=None):
    x0=(SW-10*gap)/2+(gap-w)/2
    for i in range(min(n,len(seq))):
        r,c=divmod(i,10); cell(dd,x0+c*gap,y0+r*gap,seq[i],w,hl=(i in hl),dim=dim)
def row(dd,vals,y,w=26,gap=28,hl=(),cx=None,q=()):
    n=len(vals); x0=(cx or SW/2)-(n*gap-(gap-w))/2
    for i,v in enumerate(vals): cell(dd,x0+i*gap,y,v,w,hl=(i in hl),q=(i in q))
def coinf(dd,cx,cy,r,face,squash=1.0):
    col=PC if face==0 else FC_
    h=max(3,int(r*squash))
    disc(dd,cx,cy+r-h if False else cy,r+3,DARK) if squash>0.95 else None
    if squash>0.95: disc(dd,cx,cy,r,col,DARK,3); T(dd,'P' if face==0 else 'F',cx,cy-r*0.35,r,'press',int(r*0.9),DARK,align='c')
    else:
        hh=max(3,r*squash); dd.ellipse([(cx-r)*S,(cy-hh)*S,(cx+r)*S,(cy+hh)*S],fill=col,outline=DARK,width=3*S)
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-18: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
HEADS={'s1':[('6 piles ',CREAM),('d’affilée',GOLD),(' : rare ?',CREAM)],
 's2':[('Une pièce, ',CREAM),('100 lancers',GOLD)],
 's3':[('L’inspecteur ',CREAM),('note',CORAL),(' tout',CREAM)],
 's4':[('Pile ou face : ',CREAM),('1 chance sur 2',GOLD)],
 's5':[('Sur ces ',CREAM),('100 lancers',GOLD),(' ?',CREAM)],
 's6':[('6 fois la ',CREAM),('même face',CORAL),(' de suite',CREAM)],
 's7':[('6 piles',GOLD),(' ou ',CREAM),('6 faces',CYAN)],
 'q':[('1 sur 10, ',CREAM),('1 sur 2,',GOLD),(' plus ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('environ 80 %',GOLD)],
 'r1':[('Une série peut ',CREAM),('commencer',CORAL),(' ici',CREAM)],
 'r2':[('1 chance sur ',CREAM),('32',GOLD)],
 'r3':[('Près de ',CREAM),('100 départs',CYAN)],
 'r4':[('Elle arrive ',CREAM),('presque toujours',CORAL)],
 'r5':[('4 fois ',CREAM),('sur 5',GOLD)],
 'r6':[('Rare ? ',CREAM),('Non, normal',GRN)],
 'r7':[('Le hasard fait des ',CREAM),('séries',CORAL)],
 'r8':[('Un humain ',CREAM),('les évite',RED)],
 'r9':[('On repère les ',CREAM),('faux',RED)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','q')
HUM=[0,1,0,0,1,1,0,1,0,1,1,0]
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            nn=min(6,int(t*5)+2); row(dd,[0]*nn,150,w=38,gap=46,hl=range(nn)) if nn==6 else [cell(dd,SW/2-(6*46-8)/2+i*46,150,0,38,hl=True) for i in range(nn)]; T(dd,'?',cx,214,70,'press',52,GOLD,align='c',shadow=(5,5,BLACK))
            tagc(dd,cx,364,'RARE OU NORMAL ?',GOLD)
        elif key=='s2':
            f=int(t*6)%2; sq=abs(math.cos(t*6)); coinf(dd,cx,190,44,f,squash=1.0 if sq>0.5 else 0.35)
            nb(dd,cx,260,'100',CORAL,w=130,h=50,size=32)
            tagc(dd,cx,364,'UNE PIÈCE, CENT LANCERS',CORAL)
        elif key=='s3':
            n=min(100,int(lt*38)); grid(dd,n,y0=GY0+4)
            tagc(dd,cx,364,'IL NOTE CHAQUE RÉSULTAT',CORAL)
        elif key=='s4':
            coinf(dd,100,210,34,0); coinf(dd,212,210,34,1)
            box(dd,cx-60,276,120,18,fill=CARD,border=CREAM,bw=2); T(dd,'50 % / 50 %',cx,280,12,'silk7',10,CREAM,align='c',sp=1)
            T(dd,'ET',cx,198,14,'press',12,CREAM,align='c') ; stamp(dd,cx,320,'PAS DE TRICHE',GRN,11)
            tagc(dd,cx,364,'UNE CHANCE SUR DEUX',GOLD)
        elif key=='s5':
            grid(dd,100,y0=GY0+4,hl=());
            if int(t*2)%2==0: T(dd,'?',cx,200,60,'press',44,WHITE if False else CREAM,align='c',shadow=(5,5,BLACK))
            tagc(dd,cx,364,'SUR CES 100 LANCERS ?',CYAN)
        elif key=='s6':
            hl=range(RUN[0],RUN[1]+1) if lt>0.8 else ()
            grid(dd,100,y0=GY0+4,hl=hl)
            tagc(dd,cx,364,'6 FOIS LA MÊME FACE D’AFFILÉE',CORAL)
        elif key=='s7':
            row(dd,[0]*6,150,w=38,gap=44); row(dd,[1]*6,230,w=38,gap=44)
            lbl(dd,cx,118,'6 PILES DE SUITE',GOLD,10); lbl(dd,cx,198,'6 FACES DE SUITE',CYAN,10)
            tagc(dd,cx,364,'PILES OU FACES, PEU IMPORTE',CORAL)
        elif key=='q':
            for i,(v,c,l) in enumerate((('1/10',GOLD,'1 SUR 10'),('1/2',CYAN,'1 SUR 2'),('+',CORAL,'PLUS ?'))):
                x=52+i*104; nb(dd,x,150,v,c,w=88,h=80,size=26); lbl(dd,x,244,l,CREAM,9)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'80%',cx,130,100,'press',78,GOLD,align='c',shadow=(6,6,BLACK)); star(dd,40,200,t,6); star(dd,272,200,t+1,6)
            stamp(dd,cx,310,'4 CHANCES SUR 5',GRN,12); tagc(dd,cx,364,'LA RÉPONSE : ENVIRON 80 %',GOLD)
        elif key=='r1':
            vals=SEQ[:12]; pos=min(6,int(lt*2.2))
            row(dd,vals,196,w=22,gap=24,hl=()); x0=SW/2-(12*24-2)/2
            box(dd,x0+pos*24-3,190,6*24+4-2,34,fill=None,border=CORAL,bw=3) if False else None
            dd.rectangle([(x0+pos*24-4)*S,186*S,(x0+pos*24+6*24-4)*S,(196+22+4)*S],outline=CORAL,width=3*S)
            lbl(dd,cx,150,'6 LANCERS D’AFFILÉE',CORAL,9)
            tagc(dd,cx,364,'UNE SÉRIE PEUT COMMENCER ICI',CORAL)
        elif key=='r2':
            cell(dd,28,170,1,w=38);
            for i in range(5):
                if lt>0.3+i*0.35: cell(dd,28+(i+1)*46,170,1,w=38,q=True); T(dd,'1/2',28+(i+1)*46+19,216,12,'silk7',10,CYAN,align='c')
            if lt>2.1: nb(dd,cx,250,'1/32',GOLD,w=130,h=50,size=26)
            tagc(dd,cx,364,'5 FOIS « UNE CHANCE SUR DEUX »',GOLD)
        elif key=='r3':
            n=min(95,int(lt*38)); grid(dd,100,y0=GY0+4,dim=True)
            x0=(SW-10*24)/2+1
            for i in range(n):
                r,c=divmod(i,10); cell(dd,x0+c*24,GY0+4+r*24,SEQ[i],22)
            lbl(dd,cx,348,'95 DÉPARTS POSSIBLES',CYAN,9) if False else None
            tagc(dd,cx,364,'PRESQUE 100 DÉPARTS POSSIBLES',CYAN)
        elif key=='r4':
            for i in range(10):
                x=46+(i%5)*56; y=150+(i//5)*86
                box(dd,x-22,y,44,60,fill=CARD,border=EDGE,bw=3)
                if lt>0.15+i*0.17:
                    bad=i in (3,7); (xmark_(dd,x,y+30,12,5,RED) if bad else check(dd,x,y+30,12,5,GRN))
            tagc(dd,cx,364,'ELLE ARRIVE PRESQUE TOUJOURS',CORAL)
        elif key=='r5':
            for i in range(5):
                x=44+i*56; y=170
                box(dd,x-22,y,44,60,fill=CARD,border=(RED if i==4 else GRN),bw=3)
                if lt>0.2+i*0.3:
                    (xmark_(dd,x,y+30,12,5,RED) if i==4 else check(dd,x,y+30,12,5,GRN))
            if lt>1.6: nb(dd,cx,260,'4 SUR 5',GOLD,w=140,h=46,size=24)
            tagc(dd,cx,364,'QUATRE FOIS SUR CINQ',GOLD)
        elif key=='r6':
            stamp(dd,cx,170,'RARE',CORAL,18);
            if lt>0.5: xmark_(dd,cx,170,30,6,RED)
            if lt>1.5: stamp(dd,cx,260,'NORMAL',GRN,18); check(dd,cx+96,258,14,6,GRN) if False else None
            tagc(dd,cx,364,'EN RÉALITÉ : TOUT À FAIT NORMAL',GRN)
        elif key=='r7':
            vals=SEQ[:20]
            n=min(20,int(lt*7)+1)
            for i in range(n):
                rr,cc=divmod(i,10); cell(dd,SW/2-(10*26-4)/2+cc*26,170+rr*30,SEQ[i],22,hl=(RUN[0]<=i<=RUN[1] and n>8))
            lbl(dd,cx,128,'LE HASARD FABRIQUE DES SÉRIES',CORAL,8) if False else None
            tagc(dd,cx,364,'LE HASARD FABRIQUE DES SÉRIES',CORAL)
        elif key=='r8':
            lbl(dd,cx,112,'HUMAIN QUI INVENTE',CYAN,9); row(dd,[0,1,0,1,1,0,1,0,0,1],136,w=22,gap=26)
            lbl(dd,cx,208,'VRAI HASARD',GOLD,9); row(dd,SEQ[0:10],232,w=22,gap=26,hl=range(2,8))
            stamp(dd,cx,314,'PRESQUE JAMAIS DE SÉRIE',RED,9)
            tagc(dd,cx,364,'L’HUMAIN ÉVITE LES SÉRIES',RED)
        elif key=='r9':
            sprite(dd,DET,DPAL,28,150,5.0,20)
            stamp(dd,226,170,'FAUX !',RED,16); stamp(dd,226,236,'VRAI',GRN,16)
            tagc(dd,cx,364,'L’INSPECTEUR REPÈRE LES FAUX',RED)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#048'
    def fn(lay,dd):
        grid(dd,100,hl=range(RUN[0],RUN[1]+1),y0=GY0+8)
        T(dd,'6 PILES D’AFFILÉE,',SW/2,14,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'RARE OU NORMAL ?',SW/2,48,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="100 LANCERS DE PIÈCE"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#049','ENVOIE-LA À QUELQU’UN')
