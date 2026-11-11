from render_e2x import *
B.NUM='#033'
DOCP=dict(MPAL); DOCP.update({'T':'#F3EBDD','P':'#8FE3FF','K':'#5A3A22'})
HEADS={'s1':[('Ton ',CREAM),('test',GOLD),(' est tombé',CREAM)],
 's2':[('Positif : ',CORAL),('maladie rare',CREAM)],
 's3':[('Le ',CREAM),('médecin',CYAN),(' s’inquiète',CREAM)],
 's4':[('Attends, ',CREAM),('pas de panique',GOLD)],
 's5':[('1 personne',GOLD),(' sur ',CREAM),('1000',GOLD)],
 's6':[('Le test est ',CREAM),('fiable',GRN)],
 's7':[('99 malades',GOLD),(' sur 100 repérés',CREAM)],
 's8':[('Mais il ',CREAM),('se trompe',RED),(' aussi',CREAM)],
 's9':[('1 personne ',RED),('saine',CREAM),(' sur 100',RED)],
 's10':[('Déclarée ',CREAM),('malade',RED),(' à tort',CREAM)],
 's11':[('Toi, ',CREAM),('positif !',CORAL)],
 'q':[('Vraiment ',CREAM),('malade ?',RED)],
 'r0':[('Environ ',CREAM),('9 %',GOLD),(' seulement',CREAM)],
 'r1':[('1000',GOLD),(' personnes testées',CREAM)],
 'r2':[('1 seul ',GOLD),('vrai malade',CREAM)],
 'r3':[('999 ',CREAM),('en bonne santé',CYAN)],
 'r4':[('Environ ',CREAM),('10 faux',RED),(' positifs',CREAM)],
 'r5':[('11 ',CREAM),('positifs,',CORAL),(' 1 malade',GOLD)],
 'r6':[('1 chance',GOLD),(' sur ',CREAM),('11',GOLD)],
 'r7':[('Maladie ',CREAM),('très rare',CYAN)],
 'r8':[('Erreurs',RED),(' > ',CREAM),('vrais malades',GOLD)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','q')
SICK=GOLD; OKC=rgb('#9FB0E0'); FALSE=RED
def grid(dd,x0,y0,cols,rows,pitch,sz,fn):
    """fn(i)-> couleur | None"""
    for i in range(cols*rows):
        c=fn(i)
        if c is None: continue
        r,k=divmod(i,cols); box(dd,x0+k*pitch,y0+r*pitch,sz,sz,fill=c)
def sickcell(dd,x0,y0,pitch,i,cols=50,col=GOLD):
    r,k=divmod(i,cols); cx=x0+k*pitch+2; cy=y0+r*pitch+2
    box(dd,cx-5,cy-5,10,10,fill=col,border=DARK,bw=1); ring_(dd,cx-9,cy-9,18,18,col,2)
def ring_(dd,x,y,w,h,col,bw=2):
    box(dd,x,y,w,bw,fill=col); box(dd,x,y+h-bw,w,bw,fill=col); box(dd,x,y,bw,h,fill=col); box(dd,x+w-bw,y,bw,h,fill=col)
def testcard(dd,cx,cy,res=True,t=0.0,w=150,h=88):
    box(dd,cx-w/2,cy-h/2,w,h,fill=rgb('#F3EBDD'),border=DARK,bw=3,shadow=(4,4,BLACK))
    box(dd,cx-w/2+12,cy-h/2+14,w-24,24,fill=rgb('#C9D3F0'),border=DARK,bw=2)
    for xx in (cx-30,cx+14):
        box(dd,xx,cy-h/2+16,5,20,fill=(RED if (res or xx<cx) else rgb('#C9D3F0')))
    T(dd,'C',cx-37,cy-h/2+44,12,'press',9,DARK); T(dd,'T',cx+7,cy-h/2+44,12,'press',9,DARK)
    if res: stamp(dd,cx,cy+h/2-12,'POSITIF',RED,14)
def virus(dd,cx,cy,t,r=26):
    b=math.sin(t*4)*2
    for i in range(12):
        a=i*math.pi/6+t*0.4; x1=cx+(r)*math.cos(a); y1=cy+b+(r)*math.sin(a); x2=cx+(r+11)*math.cos(a); y2=cy+b+(r+11)*math.sin(a)
        dd.line([(x1*S,y1*S),(x2*S,y2*S)],fill=DARK,width=4*S); disc(dd,x2,y2,4,RED)
    disc(dd,cx,cy+b,r+2,DARK); disc(dd,cx,cy+b,r,rgb('#C93A55'))
    box(dd,cx-12,cy+b-9,7,10,fill=CREAM); box(dd,cx+5,cy+b-9,7,10,fill=CREAM); box(dd,cx-10,cy+b-5,4,5,fill=DARK); box(dd,cx+7,cy+b-5,4,5,fill=DARK)
    box(dd,cx-9,cy+b+9,18,3,fill=DARK)
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            testcard(dd,SW/2,200,res=(lt>0.9),t=t); tagc(dd,SW/2,364,'TON TEST EST TOMBÉ',GOLD)
        elif key=='s2':
            virus(dd,SW/2,196,t,r=34); stamp(dd,SW/2,300,'POSITIF',RED,16); tagc(dd,SW/2,364,'UNE MALADIE RARE',CORAL)
        elif key=='s3':
            sprite(dd,MAN,DOCP,SW/2-5*6,GY-14*6+math.sin(t*3)*1.2,6,10)
            bubble(dd,172,112,120,46,['OH OH...'],RED,12)
            tagc(dd,SW/2,364,'LE MÉDECIN EST INQUIET',CYAN)
        elif key=='s4':
            insp(dd,SW/2,GY,t,k=3.6); bubble(dd,160,112,132,46,['ATTENDS !'],GOLD,12)
            tagc(dd,SW/2,364,'PAS DE PANIQUE',GOLD)
        elif key=='s5':
            grid(dd,12,150,50,20,5.8,4,lambda i:(None if i==617 else rgb('#4A5588'))); sickcell(dd,12,150,5.8,617)
            lbl(dd,SW/2,300,'1 MALADE SUR 1000',GOLD,11); tagc(dd,SW/2,364,'UNE PERSONNE SUR MILLE',GOLD)
        elif key=='s6':
            testcard(dd,SW/2,190,res=False,t=t); stamp(dd,SW/2,290,'FIABLE',GRN,16); tagc(dd,SW/2,364,'LE TEST EST FIABLE',GRN)
        elif key=='s7':
            n=min(99,int(lt/1.3*99)+1) if lt<1.3 else 99
            grid(dd,86,122,10,10,14,11,lambda i:(SICK if i<n else None) if i<99 else (DIM if lt>1.3 else None))
            if lt>1.0: T(dd,'99 / 100',SW/2,278,36,'press',24,GOLD,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'99 MALADES REPÉRÉS',GOLD)
        elif key=='s8':
            grid(dd,86,122,10,10,14,11,lambda i:OKC)
            lbl(dd,SW/2,290,'DES GENS EN BONNE SANTÉ',CYAN,10); tagc(dd,SW/2,364,'IL SE TROMPE AUSSI',RED)
        elif key=='s9':
            grid(dd,86,122,10,10,14,11,lambda i:(RED if i==37 else OKC))
            if int(t*3)%2==0: ring_(dd,86+7*14-4,122+3*14-4,19,19,GOLD,2)
            T(dd,'1 / 100',SW/2,278,36,'press',24,RED,align='c',shadow=(3,3,BLACK)); tagc(dd,SW/2,364,'UNE PERSONNE SAINE SUR 100',RED)
        elif key=='s10':
            grid(dd,86,122,10,10,14,11,lambda i:(RED if i==37 else OKC))
            xx=86+7*14+5; yy=122+3*14+5
            ring_(dd,xx-14,yy-14,28,28,GOLD,2)
            stamp(dd,SW/2,276,'FAUX POSITIF',RED,13); tagc(dd,SW/2,364,'DÉCLARÉE MALADE À TORT',RED)
        elif key=='s11':
            insp(dd,76,GY,t,k=3.0); testcard(dd,206,200,res=True,t=t,w=130,h=80); tagc(dd,SW/2,364,'TON TEST EST POSITIF',CORAL)
        elif key=='q':
            insp(dd,SW/2,GY,t,k=2.6); T(dd,'? %',SW/2,130,60,'press',48,GOLD,align='c',shadow=(4,4,BLACK))
            tagc(dd,SW/2,364,'CHANCE D’ÊTRE MALADE ?',CORAL)
        elif key=='r0':
            T(dd,'9%',SW/2,150,80,'press',64,GOLD,align='c',shadow=(5,5,BLACK)); star(dd,40,150,t,5); star(dd,272,150,t,5)
            lbl(dd,SW/2,290,'ENVIRON, PAS PLUS',CYAN,11); tagc(dd,SW/2,364,'MOINS D’UNE CHANCE SUR DIX',GOLD)
        elif key=='r1':
            grid(dd,12,150,50,20,5.8,4,lambda i:rgb('#4A5588')); lbl(dd,SW/2,300,'1000 PERSONNES TESTÉES',CREAM,11)
            tagc(dd,SW/2,364,'IMAGINE MILLE PERSONNES',CREAM)
        elif key=='r2':
            grid(dd,12,150,50,20,5.8,4,lambda i:(None if i==617 else rgb('#4A5588'))); sickcell(dd,12,150,5.8,617); stamp(dd,SW/2,300,'POSITIF',RED,13)
            tagc(dd,SW/2,364,'1 SEUL VRAI MALADE',GOLD)
        elif key=='r3':
            grid(dd,12,150,50,20,5.8,4,lambda i:(None if i==617 else OKC)); sickcell(dd,12,150,5.8,617,col=DIM)
            lbl(dd,SW/2,300,'999 EN BONNE SANTÉ',CYAN,11); tagc(dd,SW/2,364,'1 SUR 100 SE TROMPE',RED)
        elif key=='r4':
            fp=[i for i in random.Random(7).sample(range(1000),40) if 2<=i%50<=47 and abs(i%50-17)+abs(i//50-12)>5][:10]
            m=min(10,int(lt/0.18)+1)
            grid(dd,12,150,50,20,5.8,4,lambda i:(None if (i==617 or i in fp[:m]) else OKC)); sickcell(dd,12,150,5.8,617)
            for j in fp[:m]: sickcell(dd,12,150,5.8,j,col=RED)
            lbl(dd,SW/2,300,'ENVIRON 10 FAUX POSITIFS',RED,11); tagc(dd,SW/2,364,'DIX FAUX POSITIFS',RED)
        elif key=='r5':
            for i in range(11):
                r,c=divmod(i,6); x=SW/2+(c-2.5)*40; y=140+r*70
                col=GOLD if i==0 else RED
                box(dd,x-14,y,28,34,fill=col,border=DARK,bw=2,shadow=(2,2,BLACK)); T(dd,'+',x,y+7,24,'press',20,DARK,align='c')
            lbl(dd,SW/2,290,'11 POSITIFS, 1 MALADE',CORAL,11); tagc(dd,SW/2,364,'UN SEUL VRAI MALADE',GOLD)
        elif key=='r6':
            for i in range(11):
                x=SW/2+(i-5)*24; box(dd,x-9,140,18,26,fill=(GOLD if i==0 else DIM),border=DARK,bw=2)
            T(dd,'1 / 11',SW/2,200,50,'press',40,GOLD,align='c',shadow=(4,4,BLACK)); T(dd,'< 10 %',SW/2,262,34,'press',24,CREAM,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'UNE CHANCE SUR ONZE',GOLD)
        elif key=='r7':
            virus(dd,SW/2,180,t,r=30)
            lbl(dd,SW/2,280,'1 PERSONNE SUR 1000',CYAN,11); tagc(dd,SW/2,364,'UNE MALADIE TRÈS RARE',CYAN)
        elif key=='r8':
            f=min(1,lt/1.2)
            T(dd,'FAUX POSITIFS',24,122,16,'silk7',11,RED,sp=1); box(dd,24,142,264,26,fill=CARD,border=EDGE,bw=2); box(dd,26,144,int(260*f),22,fill=RED); T(dd,'10',280,146,18,'press',14,CREAM,align='r') if f>0.9 else None
            T(dd,'VRAIS MALADES',24,190,16,'silk7',11,GOLD,sp=1); box(dd,24,210,264,26,fill=CARD,border=EDGE,bw=2); box(dd,26,212,max(2,int(26*f)),22,fill=GOLD); T(dd,'1',280,214,18,'press',14,CREAM,align='r') if f>0.9 else None
            T(dd,'10',280,148,18,'press',14,CREAM,align='r') if False else None
            stamp(dd,SW/2,290,'ERREURS > MALADES',CORAL,11); insp(dd,SW-48,GY,t,k=1.6); tagc(dd,SW/2,364,'PLUS D’ERREURS QUE DE MALADES',CORAL)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#033'
    def fn(lay,dd):
        testcard(dd,SW/2,196,res=True,t=t,w=170,h=100)
        insp(dd,58,334,t,k=2.8); virus(dd,252,292,t,r=22)
        T(dd,'TON TEST EST POSITIF !',SW/2,10,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'ES-TU MALADE ?',SW/2,44,36,'anton',26,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DU TEST POSITIF"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#034')
