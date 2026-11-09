from render_e2x import *
B.NUM='#029'
HEADS={'s1':[('Cent ',CREAM),('casiers',GOLD),(' fermés',CREAM)],
 's2':[('Lesquels resteront ',CREAM),('ouverts',GRN),(' ?',CREAM)],
 's3':[('Cent ',CREAM),('élèves',CORAL),(' passent',CREAM)],
 's4':[('Le ',CREAM),('premier',GOLD),(' ouvre ',CREAM),('tout',GRN)],
 's5':[('Le ',CREAM),('deuxième',GOLD),(' : un sur ',CREAM),('deux',CORAL)],
 's6':[('On ',CREAM),('inverse',GOLD),(' l’état du casier',CREAM)],
 's7':[('Le ',CREAM),('troisième',GOLD),(' : un sur ',CREAM),('trois',CORAL)],
 's8':[('Ainsi de suite ',CREAM),('jusqu’au 100e',GOLD)],
 's9':[('Tout le monde ',CREAM),('est passé',GOLD)],
 'q':[('Combien ',CREAM),('ouverts',GRN),(' ?',CREAM)],
 'r0':[('Réponse : ',CREAM),('10',GOLD),(' casiers !',CREAM)],
 'r1':[('Passages = ',CREAM),('diviseurs',GOLD)],
 'r2':[('Casier ',CREAM),('12',GOLD),(' : ',CREAM),('6',CORAL),(' diviseurs',CREAM)],
 'r3':[('6 passages : ',CREAM),('fermé',RED)],
 'r4':[('Diviseurs ',CREAM),('par paires',GOLD)],
 'r5':[('Sauf les ',CREAM),('carrés',GOLD),(' parfaits',CREAM)],
 'r6':[('9 : le ',CREAM),('3',GOLD),(' est ',CREAM),('seul',CORAL)],
 'r7':[('3 passages : ',CREAM),('ouvert',GRN)],
 'r8':[('Ouverts : les ',CREAM),('carrés',GOLD),(' parfaits',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','q')
def bignum(dd,cx,y,txt,col=GOLD,w=120,h=64,size=32):
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=4,shadow=(4,4,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
def state(n,upto):
    o=[False]*(n+1)
    for k in range(1,upto+1):
        for m in range(k,n+1,k): o[m]=not o[m]
    return o
def lockers(dd,st,x0=46,y0=124,p=22,c=20,hl=(),unk=False,lit=None):
    for i in range(100):
        r,cc=divmod(i,10); n=i+1; x=x0+cc*p; y=y0+r*p
        op=st[n] if st else False
        if unk: fill,br=CARD,EDGE
        else: fill,br=(GOLD if op else DIM),DARK
        if n in hl: br=CORAL
        box(dd,x,y,c,c,fill=fill,border=br,bw=(2 if n in hl else 1))
        if unk and i%7==3: pass
def bigl(dd,cx,y,op,w=60,h=90):
    box(dd,cx-w/2,y,w,h,fill=(GOLD if op else DIM),border=DARK,bw=3,shadow=(3,3,BLACK))
    box(dd,cx-w/2+8,y+10,w-16,10,fill=DARK); box(dd,cx-w/2+8,y+26,w-16,10,fill=DARK)
    box(dd,cx+w/2-16,y+h/2+8,6,16,fill=DARK)
def arrow(dd,cx,cy,col=GOLD):
    dd.rectangle([(cx-16)*S,(cy-4)*S,(cx+4)*S,(cy+4)*S],fill=col)
    dd.polygon([((cx+2)*S,(cy-12)*S),((cx+18)*S,cy*S),((cx+2)*S,(cy+12)*S)],fill=col)
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            lockers(dd,[False]*101); tagc(dd,SW/2,364,'CENT CASIERS FERMÉS',GOLD)
        elif key=='s2':
            lockers(dd,[False]*101,x0=76,y0=122,p=16,c=14)
            insp(dd,SW/2,GY,t,k=2.3)
            T(dd,'?',SW/2+70,260,60,'press',50,GRN,align='c',shadow=(4,4,BLACK))
            tagc(dd,SW/2,364,'LESQUELS RESTENT OUVERTS',GRN)
        elif key=='s3':
            n=min(10,1+int(lt*5))
            for i in range(n): stick(dd,36+i*27,150,42,[CORAL,CYAN,GOLD][i%3])
            bignum(dd,SW/2,236,'100 ÉLÈVES',CORAL,w=230,h=48,size=16)
            lbl(dd,SW/2,300,'UN PAR UN',CREAM,11)
            tagc(dd,SW/2,364,'CENT ÉLÈVES',CORAL)
        elif key=='s4':
            k=min(100,int(lt*160))
            st=[False]+[(i<=k) for i in range(1,101)]
            lockers(dd,st); tagc(dd,SW/2,364,'IL OUVRE TOUS LES CASIERS',GRN)
        elif key=='s5':
            ph=lt>0.9
            st=state(100,2) if ph else state(100,1)
            lockers(dd,st,hl=(range(2,101,2) if True else ()))
            tagc(dd,SW/2,364,'IL CHANGE 2, 4, 6, 8…',CORAL)
        elif key=='s6':
            bigl(dd,70,120,True); arrow(dd,SW/2,165); bigl(dd,242,120,False)
            lbl(dd,70,218,'OUVERT',GRN,10); lbl(dd,242,218,'FERMÉ',RED,10)
            bigl(dd,70,246,False,h=76); arrow(dd,SW/2,284); bigl(dd,242,246,True,h=76)
            tagc(dd,SW/2,364,'ON INVERSE L’ÉTAT',GOLD)
        elif key=='s7':
            ph=lt>0.9
            st=state(100,3) if ph else state(100,2)
            lockers(dd,st,hl=range(3,101,3)); tagc(dd,SW/2,364,'IL CHANGE 3, 6, 9, 12…',CORAL)
        elif key=='s8':
            for i in range(3): bignum(dd,60+i*96,130,['4E','5E','6E'][i],[CYAN,GOLD,CORAL][i],w=80,h=56,size=18)
            T(dd,'…',SW/2,206,40,'press',34,CREAM,align='c')
            bignum(dd,SW/2,250,'100E ÉLÈVE',GOLD,w=250,h=52,size=18)
            tagc(dd,SW/2,364,'JUSQU’AU CENTIÈME',GOLD)
        elif key=='s9':
            group(dd,SW/2,130,10,gap=26,dim=True)
            insp(dd,SW/2,GY,t,k=2.3)
            tagc(dd,SW/2,364,'TOUT LE MONDE EST PASSÉ',CREAM)
        elif key=='q':
            lockers(dd,[False]*101,x0=76,y0=122,p=16,c=14,unk=True)
            T(dd,'?',SW/2,176,100,'press',90,GRN,align='c',shadow=(5,5,BLACK))
            insp(dd,SW/2,GY,t,k=2.3)
            tagc(dd,SW/2,364,'COMBIEN OUVERTS ?',GRN)
        elif key=='r0':
            insp(dd,64,GY,t,k=3.8); bignum(dd,212,150,'10',GOLD,w=150,h=100,size=60)
            star(dd,282,128,t,5); star(dd,150,120,t,4)
            tagc(dd,SW/2,364,'DIX CASIERS',GOLD)
        elif key=='r1':
            bigl(dd,SW/2,118,True,w=50,h=76)
            bignum(dd,SW/2,206,'PASSAGES',CYAN,w=220,h=40,size=14)
            T(dd,'=',SW/2,252,30,'press',26,GOLD,align='c',shadow=(3,3,BLACK))
            bignum(dd,SW/2,286,'DIVISEURS',CORAL,w=220,h=40,size=14)
            tagc(dd,SW/2,364,'AUTANT QUE DE DIVISEURS',GOLD)
        elif key=='r2':
            bignum(dd,SW/2,120,'12',GOLD,w=110,h=60,size=30)
            ds=[(1,2.1),(2,2.55),(3,3.3),(4,3.9),(6,4.4),(12,4.9)]
            for i,(v,th) in enumerate(ds):
                if lt>=th: bignum(dd,40+i*46.4,214,str(v),[CYAN,GOLD,CORAL][i%3],w=42,h=44,size=14)
            if lt>=5.05: lbl(dd,SW/2,278,'6 DIVISEURS',CORAL,12)
            tagc(dd,SW/2,364,'1 2 3 4 6 12',GOLD)
        elif key=='r3':
            bigl(dd,SW/2-60,126,False); bignum(dd,SW/2+50,140,'6',CORAL,w=90,h=70,size=40)
            stamp(dd,SW/2,260,'FERMÉ',RED,18)
            lbl(dd,SW/2,316,'NOMBRE PAIR DE FOIS',CREAM,10)
            tagc(dd,SW/2,364,'6 FOIS : FERMÉ',RED)
        elif key=='r4':
            prs=[(1,12),(2,6),(3,4)]
            for i,(a,b) in enumerate(prs):
                y=124+i*66; bignum(dd,80,y,str(a),CYAN,w=70,h=52,size=22); T(dd,'×',SW/2,y+10,30,'press',24,GOLD,align='c'); bignum(dd,232,y,str(b),CORAL,w=70,h=52,size=22)
            lbl(dd,SW/2,326,'= 12 À CHAQUE FOIS',CREAM,10)
            tagc(dd,SW/2,364,'PAR PAIRES',GOLD)
        elif key=='r5':
            bignum(dd,SW/2,120,'9',GOLD,w=100,h=64,size=34)
            T(dd,'=',SW/2,196,30,'press',26,CREAM,align='c')
            bignum(dd,SW/2,230,'3 × 3',CORAL,w=180,h=56,size=24)
            tagc(dd,SW/2,364,'CARRÉ PARFAIT',GOLD)
        elif key=='r6':
            bignum(dd,80,124,'1',CYAN,w=70,h=52,size=22); T(dd,'×',SW/2,134,30,'press',24,GOLD,align='c'); bignum(dd,232,124,'9',CORAL,w=70,h=52,size=22)
            bignum(dd,80,200,'3',GOLD,w=70,h=52,size=22); T(dd,'×',SW/2,210,30,'press',24,GOLD,align='c'); bignum(dd,232,200,'3',GOLD,w=70,h=52,size=22)
            lbl(dd,SW/2,274,'LE MÊME 3 : UN SEUL',CREAM,10)
            tagc(dd,SW/2,364,'3 DIVISEURS EN TOUT',GOLD)
        elif key=='r7':
            bigl(dd,SW/2-60,126,True); bignum(dd,SW/2+50,140,'3',GRN,w=90,h=70,size=40)
            stamp(dd,SW/2,260,'OUVERT',GRN,18)
            lbl(dd,SW/2,316,'PAS UN NOMBRE PAIR',CREAM,10)
            tagc(dd,SW/2,364,'3 FOIS : OUVERT',GRN)
        elif key=='r8':
            sq=[(1,1.3),(4,1.95),(9,2.5),(16,3.05),(25,3.6),(36,4.3),(49,5.0),(64,5.65),(81,6.5),(100,7.2)]
            sqs={n for n,th in sq if lt>=th}
            st=[False]+[(i in sqs) for i in range(1,101)]
            lockers(dd,st,p=22)
            tagc(dd,SW/2,364,'1 4 9 16 25 36 49 64 81 100',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#029'
    def fn(lay,dd):
        lockers(dd,[False]*101,x0=76,y0=160,p=16,c=14)
        T(dd,'?',SW/2,320,36,'press',32,GRN,align='c',shadow=(3,3,BLACK))
        T(dd,'100 CASIERS, 100 ÉLÈVES,',SW/2,10,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'COMBIEN RESTENT OUVERTS ?',SW/2,44,36,'anton',22,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DES CASIERS"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#030')
