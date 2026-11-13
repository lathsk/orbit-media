from render_e2x import *
B.NUM='#037'
PANEL=rgb('#0D1124')
KEEP=dict(MPAL); KEEP.update({'T':'#F3E6CF','P':'#6B4A2E','K':'#2A1F18'})
PC={1:CORAL,2:CYAN,4:GOLD}
def tri(dd,pts,fill): dd.polygon([(x*S,y*S) for x,y in pts],fill=fill)
def panel(dd,x,y,w,h,col=EDGE): box(dd,x,y,w,h,fill=PANEL,border=col,bw=3)
def lk(dd,cx,cy,col=GOLD,flat=True,w=36,h=28,bw=5,cut=False):
    if not flat: h=int(h*0.66)
    box(dd,cx-w/2-1,cy-h/2-1,w+2,h+2,fill=DARK); box(dd,cx-w/2,cy-h/2,w,h,fill=col)
    box(dd,cx-w/2+bw,cy-h/2+bw,w-2*bw,h-2*bw,fill=PANEL)
    if cut:
        box(dd,cx+w/2-bw-2,cy-5,bw+4,10,fill=PANEL); box(dd,cx+w/2-bw-3,cy-6,2,12,fill=RED); box(dd,cx+w/2+1,cy-6,2,12,fill=RED)
def chain(dd,cx,cy,n=7,pitch=32,cols=None,w=36,h=28,nums=False,ncol=GREY,cut=None,flat_first=True):
    x0=cx-(n-1)*pitch/2; cols=cols or [GOLD]*n
    for i in range(n):
        if (i%2==0)==flat_first: lk(dd,x0+i*pitch,cy,cols[i],flat=True,w=w,h=h,cut=(cut==i))
    for i in range(n):
        if (i%2==0)!=flat_first: lk(dd,x0+i*pitch,cy,cols[i],flat=False,w=w,h=h,cut=(cut==i))
    if nums:
        for i in range(n): T(dd,str(i+1),x0+i*pitch,cy+h/2+8,16,'press',11,(cols[i] if cols[i]!=DIM else GREY),align='c')
def piece(dd,cx,cy,n,col,pitch=25,w=28,h=22):
    chain(dd,cx,cy,n=n,pitch=pitch,cols=[col]*n,w=w,h=h)
def scissors(dd,cx,cy,k=1.0,op=0.5,col=CREAM):
    a=0.12+0.42*op; L=34*k
    for s in (-1,1):
        x2=cx+s*L*math.sin(a); y2=cy+L*math.cos(a)
        dd.line([(cx*S,cy*S),(x2*S,y2*S)],fill=col,width=int(4*k*S))
        hx=cx-s*18*k*math.sin(a+0.25); hy=cy-18*k*math.cos(a+0.25)
        dd.line([(cx*S,cy*S),(hx*S,hy*S)],fill=CORAL,width=int(3*k*S))
        disc(dd,hx-s*5*k,hy-9*k,7*k,None,CORAL,int(3*k))
    disc(dd,cx,cy,3*k,GOLD)
def arrow(dd,x1,x2,y,col,w=4):
    d=1 if x2>x1 else -1
    box(dd,min(x1,x2),y-w/2,abs(x2-x1)-8,w,fill=col); tri(dd,[(x2,y),(x2-d*12,y-8),(x2-d*12,y+8)],col)
def inn(dd,cx,t):
    box(dd,cx-62,190,124,112,fill=rgb('#5A3A22'),border=DARK,bw=3)
    tri(dd,[(cx-76,194),(cx,134),(cx+76,194)],rgb('#8A3A2E')); box(dd,cx-76,192,152,6,fill=DARK)
    box(dd,cx-14,240,28,62,fill=rgb('#2A1F18'),border=DARK,bw=2)
    for wx in (cx-52,cx+26):
        box(dd,wx,214,26,22,fill=GOLD if (int(t*2)%7)!=3 else rgb('#C9A22F'),border=DARK,bw=2)
    box(dd,cx-34,176,68,16,fill=CARD,border=GOLD,bw=2); T(dd,'AUBERGE',cx,179,12,'silk7',9,GOLD,align='c',sp=1)
def night_sky(dd,t):
    disc(dd,258,140,16,LGOLD,GOLD,2); disc(dd,264,134,12,rgb('#10142A'))
    for x,y in ((40,128),(92,150),(196,124),(60,214),(250,220)): star(dd,x,y,t,3)
def lbl2(dd,cx,y,txt,col=GOLD,size=22,sh=(3,3,BLACK)): T(dd,txt,cx,y,size+6,'press',size,col,align='c',shadow=sh)
LEDGER=[{1:'I',2:'I',4:'I'},{1:'A',2:'I',4:'I'},{1:'I',2:'A',4:'I'},{1:'A',2:'A',4:'I'},{1:'I',2:'I',4:'A'},{1:'A',2:'I',4:'A'},{1:'I',2:'A',4:'A'},{1:'A',2:'A',4:'A'}]
SLOT={1:42,2:112,4:222}
def ledger(dd,n0,n1,p,t,lt=0.0,label=True):
    panel(dd,10,108,292,92,GOLD); panel(dd,10,262,292,92,CYAN)
    T(dd,'AUBERGISTE',156,112,12,'silk7',9,GOLD,align='c',sp=1); T(dd,'INSPECTEUR',156,340,12,'silk7',9,CYAN,align='c',sp=1)
    ya,yi=152,308
    for k in (1,2,4):
        o0=LEDGER[n0][k]; o1=LEDGER[n1][k]
        y0=ya if o0=='A' else yi; y1=ya if o1=='A' else yi
        y=y0+(y1-y0)*ease(p)
        piece(dd,SLOT[k],y,k,PC[k])
        T(dd,str(k),SLOT[k]+(0 if k==1 else (k-1)*13-0),y+19,14,'press',11,PC[k],align='c') if False else None
    tot=sum(k for k in (1,2,4) if LEDGER[n1][k]=='A')
    return tot
def ledger_mid(dd,n,tot):
    box(dd,10,204,292,54,fill=CARD,border=EDGE,bw=2)
    T(dd,'SOIR %d'%n,24,212,22,'press',16,GOLD,align='l',shadow=(2,2,BLACK))
    T(dd,'%d MAILLON%s'%(tot,'S' if tot>1 else ''),288,236,16,'silk7',11,CREAM,align='r',sp=1)
    for i in range(7):
        c=GOLD if i<n else DIM
        box(dd,24+i*14,238,10,10,fill=c)
HEADS={'s1':[('Sept nuits',GOLD),(' à l’auberge',CREAM)],
 's2':[('Une ',CREAM),('chaîne en or',GOLD)],
 's3':[('Payer ',CREAM),('chaque soir',CORAL)],
 's4':[('Soir ',CREAM),('un',GOLD),(' : 1 maillon',CREAM)],
 's5':[('Soir ',CREAM),('deux',GOLD),(' : 2 maillons',CREAM)],
 's6':[('Jusqu’à ',CREAM),('sept',GOLD),(' maillons',CREAM)],
 's7':[('Exactement ',CREAM),('7 maillons',GOLD)],
 's8':[('Il rend les ',CREAM),('morceaux',CORAL)],
 's9':[('Un seul ',CREAM),('maillon',GOLD),(' coupé',CREAM)],
 'q':[('Où ',CREAM),('couper',CORAL),(' la chaîne ?',CREAM)],
 'r0':[('Couper le ',CREAM),('3e maillon',GOLD)],
 'r1':[('Trois ',CREAM),('morceaux',GOLD)],
 'r2':[('Soir ',CREAM),('un',GOLD),(' : le seul',CREAM)],
 'r3':[('Soir ',CREAM),('deux',GOLD),(' : échange',CREAM)],
 'r4':[('Soir ',CREAM),('trois',GOLD),(' : 1 + 2',CREAM)],
 'r5':[('Soir ',CREAM),('quatre',GOLD),(' : le gros',CREAM)],
 'r6':[('Comme les ',CREAM),('poids',GOLD),(' 1, 2, 4',CREAM)],
 'r7':[('Une coupure, ',CREAM),('sept nuits',GRN)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            night_sky(dd,t); inn(dd,156,t); tagc(dd,SW/2,364,'SEPT NUITS À L’AUBERGE',GOLD)
        elif key=='s2':
            panel(dd,12,150,288,110,GOLD); chain(dd,156,205,7,cols=[GOLD]*7)
            star(dd,40,128,t,4); star(dd,272,282,t+1,4); tagc(dd,SW/2,364,'UNE CHAÎNE EN OR',GOLD)
        elif key=='s3':
            insp(dd,64,GY,t,k=2.8); sprite(dd,MAN,KEEP,248-5*3.0,GY-14*3.0+math.sin(t*3)*1.2,3.0,10)
            lk(dd,156,226,GOLD); arrow(dd,112,200,174,CORAL,3); lbl(dd,156,128,'CHAQUE SOIR',CYAN,11)
            tagc(dd,SW/2,364,'IL DOIT PAYER CHAQUE SOIR',CORAL)
        elif key=='s4':
            lbl2(dd,SW/2,112,'SOIR 1',GOLD,24); panel(dd,12,170,288,76,EDGE); chain(dd,156,208,7,cols=[GOLD]+[DIM]*6)
            stamp(dd,SW/2,290,'1 MAILLON',GOLD,16); tagc(dd,SW/2,364,'LE PREMIER SOIR : 1 MAILLON',GOLD)
        elif key=='s5':
            lbl2(dd,SW/2,112,'SOIR 2',GOLD,24); panel(dd,12,170,288,76,EDGE); chain(dd,156,208,7,cols=[GOLD]*2+[DIM]*5)
            stamp(dd,SW/2,290,'2 MAILLONS EN TOUT',GOLD,13); tagc(dd,SW/2,364,'LE DEUXIÈME SOIR : 2 EN TOUT',GOLD)
        elif key=='s6':
            n=min(7,int(lt/dur*8)+1)
            for i in range(1,8):
                if i>n: continue
                x=28+(i-1)*38; h=i*28; box(dd,x,320-h,30,h,fill=GOLD if i==n else rgb('#B8921F'),border=DARK,bw=2)
                T(dd,str(i),x+15,320-h-22,16,'press',13,GOLD if i==n else CREAM,align='c')
            lbl(dd,SW/2,112,'SOIR 1 À SOIR 7',CYAN,11); tagc(dd,SW/2,364,'UN MAILLON DE PLUS CHAQUE SOIR',GOLD)
        elif key=='s7':
            panel(dd,12,150,288,120,GOLD); chain(dd,156,200,7,cols=[GOLD]*7,nums=True,ncol=CREAM)
            stamp(dd,SW/2,310,'7 MAILLONS',GOLD,18); tagc(dd,SW/2,364,'LA CHAÎNE : 7 MAILLONS',GOLD)
        elif key=='s8':
            insp(dd,64,GY,t,k=2.8); sprite(dd,MAN,KEEP,248-5*3.0,GY-14*3.0+math.sin(t*3)*1.2,3.0,10)
            ph=(t*0.9)%1.0
            piece(dd,112+88*ph,184,2,CYAN) if False else None
            arrow(dd,108,204,168,CORAL,3); arrow(dd,204,108,224,CYAN,3); piece(dd,156,148,1,CORAL); piece(dd,156,196,2,CYAN)
            lk(dd,92+130*ph,168-20,CORAL,w=26,h=18,bw=4) if False else None
            lbl(dd,156,110,'ON PEUT RENDRE',GRN,11); tagc(dd,SW/2,364,'IL RENDRA LES MORCEAUX',CYAN)
        elif key=='s9':
            panel(dd,12,170,288,90,EDGE); chain(dd,156,220,7); sx=156+110*math.sin(t*1.6)
            scissors(dd,sx,136,1.3,0.5+0.5*math.sin(t*9)); stamp(dd,SW/2,300,'1 SEULE COUPURE',RED,14); tagc(dd,SW/2,364,'UN SEUL MAILLON OUVERT',RED)
        elif key=='q':
            panel(dd,12,236,288,96,EDGE); chain(dd,156,282,7,nums=True,ncol=CREAM)
            lbl2(dd,SW/2,108,'?',CORAL,56); scissors(dd,60+((t*60)%190),210,1.1,0.5+0.5*math.sin(t*9))
            tagc(dd,SW/2,364,'OÙ FAUT-IL COUPER ?',CORAL)
        elif key=='r0':
            cols=[GOLD]*7; cols[2]=CORAL
            panel(dd,12,150,288,120,CORAL); chain(dd,156,200,7,cols=cols,nums=True,cut=2)
            sx=156-34; sy=118+6*math.sin(t*5)
            scissors(dd,sx,sy,1.1,0.5+0.5*math.sin(t*8)); stamp(dd,SW/2,310,'LE 3E MAILLON',CORAL,16); tagc(dd,SW/2,364,'ON COUPE LE TROISIÈME',CORAL)
        elif key=='r1':
            sp=ease(lt/0.9)*1.0
            xa=60-26*sp; xb=156; xc=244+26*sp
            piece(dd,56-14*sp+0,196,2,CYAN) if False else None
            pa=(18+29, 56*0+0)
            piece(dd,62-18*sp+0,196,2,CYAN)
            piece(dd,156,196,1,CORAL)
            piece(dd,252+12*sp,196,4,GOLD,pitch=22,w=28,h=22) if False else piece(dd,238,196,4,GOLD)
            if lt>1.4: T(dd,'1',156,226,24,'press',18,CORAL,align='c',shadow=(2,2,BLACK))
            if lt>3.0: T(dd,'2',62-18*sp,226,24,'press',18,CYAN,align='c',shadow=(2,2,BLACK))
            if lt>4.0: T(dd,'4',238,226,24,'press',18,GOLD,align='c',shadow=(2,2,BLACK))
            lbl(dd,SW/2,128,'3 MORCEAUX',CREAM,12); tagc(dd,SW/2,364,'1 SEUL · 2 · 4',GOLD)
        elif key in ('r2','r3','r4','r5'):
            n=int(key[1])-1  # nuit
            p=ease(lt/1.0); tot=ledger(dd,n-1,n,p,t); ledger_mid(dd,n,tot)
            tg={'r2':'SOIR 1 : LE MAILLON SEUL','r3':'SOIR 2 : ON ÉCHANGE','r4':'SOIR 3 : LE SEUL REVIENT','r5':'SOIR 4 : LA CHAÎNE DE QUATRE'}[key]
            tagc(dd,SW/2,364,tg,GOLD)
        elif key=='r6':
            seg=min(2,int(lt/1.05)); n0=4+seg; n1=n0+1
            p=ease((lt-seg*1.05)/0.7); tot=ledger(dd,n0,n1,p,t); ledger_mid(dd,n1,tot)
            tagc(dd,SW/2,364,'COMME LES POIDS 1 · 2 · 4',GOLD)
        elif key=='r7':
            for i in range(7):
                x=22+i*40; box(dd,x,150,34,34,fill=CARD,border=GRN,bw=3); T(dd,str(i+1),x+17,155,24,'press',14,GRN,align='c')
                if lt>0.2+i*0.18: box(dd,x+9,166,16,8,fill=GRN)
            lbl(dd,SW/2,120,'7 NUITS PAYÉES',GRN,11)
            panel(dd,40,206,232,60,GOLD); chain(dd,156,236,7,pitch=29,w=32,h=24,cols=[GOLD]*7)
            stamp(dd,SW/2,308,'1 SEULE COUPURE',GRN,15); tagc(dd,SW/2,364,'UN MAILLON COUPÉ SUFFIT',GRN)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#037'
    def fn(lay,dd):
        panel(dd,12,160,288,110,GOLD); chain(dd,156,222,7); scissors(dd,156+90*math.sin(t*1.2),146,1.3,0.5+0.5*math.sin(t*7))
        insp(dd,70,GY,t,k=2.2); sprite(dd,MAN,KEEP,238-5*2.4,GY-14*2.4+math.sin(t*3)*1.2,2.4,10)
        T(dd,'UNE CHAÎNE EN OR',SW/2,16,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'UNE SEULE COUPURE ?',SW/2,52,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DE LA CHAÎNE D'OR"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#038')
