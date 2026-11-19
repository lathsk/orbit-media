from render_e4x import *
import inspect
B.NUM='#050'
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-18: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')

LIGHT=rgb('#D8C7A3'); DARKC=rgb('#46547E')
CS=27; BX0=(SW-8*CS)/2; BY0=112
def board(dd,hl=(),dim=False,cs=CS,x0=None,y0=BY0,n=8,outline=None):
    x0=BX0 if x0 is None else x0
    for r in range(n):
        for c in range(n):
            col=LIGHT if (r+c)%2==0 else DARKC
            if dim: col=rgb('#2A3050') if (r+c)%2==0 else rgb('#1B2038')
            dd.rectangle([(x0+c*cs)*S,(y0+r*cs)*S,(x0+(c+1)*cs)*S-1,(y0+(r+1)*cs)*S-1],fill=col)
    dd.rectangle([(x0-2)*S,(y0-2)*S,(x0+n*cs+2)*S,(y0+n*cs+2)*S],outline=DARK,width=3*S)
def sq(dd,r,c,k,col=CORAL,w=4,cs=CS,x0=None,y0=BY0,fill=None):
    x0=BX0 if x0 is None else x0
    xa=(x0+c*cs)*S; ya=(y0+r*cs)*S; xb=(x0+(c+k)*cs)*S; yb=(y0+(r+k)*cs)*S
    dd.rectangle([xa,ya,xb,yb],outline=col,width=w*S)
    if fill:
        pass
def allcells(dd,col=GOLD,k=1):
    for r in range(8):
        for c in range(8): sq(dd,r,c,k,col,2)
HEADS={'s1':[('Combien de ',CREAM),('carrés',GOLD),(' ?',CREAM)],
 's2':[('L’inspecteur ',CREAM),('observe',CORAL),(' un échiquier',CREAM)],
 's3':[('8 cases',GOLD),(' sur ',CREAM),('8 cases',CYAN)],
 's4':[('Presque tous disent ',CREAM),('64',GOLD)],
 's5':[('Mais ',CREAM),('regarde bien',CORAL),(' !',CREAM)],
 's6':[('De plus ',CREAM),('grands carrés',GOLD),(' aussi',CREAM)],
 's7':[('2 sur 2, ',GOLD),('3 sur 3,',CYAN),(' jusqu’à ',CREAM),('8 sur 8',CORAL)],
 'q':[('Au total, ',CREAM),('combien',GOLD),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('204',GOLD),(' carrés',CREAM)],
 'r1':[('D’abord ',CREAM),('64',GOLD),(' petits carrés',CREAM)],
 'r2':[('Puis des carrés de ',CREAM),('2 sur 2',CYAN)],
 'r3':[('7 en largeur,',CREAM),(' 7 en hauteur',CORAL)],
 'r4':[('Ensuite ',CREAM),('36',GOLD),(' de ',CREAM),('3 sur 3',CYAN)],
 'r5':[('25, ',GOLD),('16, ',CYAN),('9, ',CORAL),('4',GRN)],
 'r6':[('Et un seul ',CREAM),('grand carré',GOLD)],
 'r7':[('64 + 49 + 36 + ',CREAM),('…',GOLD)],
 'r8':[('On compte les ',CREAM),('petites cases',CORAL)],
 'r9':[('Les ',CREAM),('grands carrés',GOLD),(' comptent',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','q')
POS2=[(0,0),(1,3),(4,1),(5,5),(2,4),(6,2),(3,6),(0,5)]
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            board(dd); 
            if int(t*2.5)%2==0: 
                box(dd,cx-30,196,60,64,fill=CARD,border=GOLD,bw=4,shadow=(4,4,BLACK)); T(dd,'?',cx,206,60,'press',44,GOLD,align='c')
            tagc(dd,cx,364,'COMBIEN DE CARRÉS ?',GOLD)
        elif key=='s2':
            n=min(8,int(lt*4.5)+1); 
            board(dd,dim=False)
            for r in range(n,8):
                for c in range(8): dd.rectangle([(BX0+c*CS)*S,(BY0+r*CS)*S,(BX0+(c+1)*CS)*S-1,(BY0+(r+1)*CS)*S-1],fill=rgb('#10142A'))
            tagc(dd,cx,364,'UN ÉCHIQUIER',CORAL)
        elif key=='s3':
            board(dd); 
            box(dd,BX0,BY0-14,8*CS,4,fill=GOLD); box(dd,BX0-14,BY0,4,8*CS,fill=CYAN)
            T(dd,'8',cx,BY0-34,24,'press',16,GOLD,align='c'); T(dd,'8',BX0-30,BY0+8*CS/2-8,24,'press',16,CYAN,align='c')
            tagc(dd,cx,364,'HUIT CASES SUR HUIT',CYAN)
        elif key=='s4':
            board(dd,dim=True)
            box(dd,cx-70,170,140,70,fill=CARD,border=GOLD,bw=4,shadow=(4,4,BLACK)); T(dd,'64',cx,186,60,'press',42,GOLD,align='c')
            tagc(dd,cx,364,'PRESQUE TOUS DISENT 64',GOLD)
        elif key=='s5':
            board(dd)
            if int(t*3)%2==0: sq(dd,2,3,2,CORAL,5)
            tagc(dd,cx,364,'MAIS REGARDE BIEN',CORAL)
        elif key=='s6':
            board(dd); r,c=POS2[min(7,int(lt*2.4))]; k=2+(int(lt*2.4)%3); sq(dd,min(r,8-k),min(c,8-k),k,CORAL,5)
            tagc(dd,cx,364,'DE PLUS GRANDS CARRÉS AUSSI',GOLD)
        elif key=='s7':
            sz=2 if lt<1.0 else 3 if lt<1.9 else min(8,4+int((lt-1.9)*3.2))
            board(dd); sq(dd,0,0,sz,[CORAL,GOLD,CYAN][sz%3],5)
            lbl(dd,cx,BY0+8*CS+6,'%d x %d'%(sz,sz),CREAM,11)
            tagc(dd,cx,364,'2 SUR 2 JUSQU’À 8 SUR 8',CYAN)
        elif key=='q':
            board(dd,dim=True)
            box(dd,cx-120,170,240,78,fill=CARD,border=GOLD,bw=4,shadow=(4,4,BLACK)); T(dd,'? CARRÉS',cx,190,40,'press',28,GOLD,align='c'); lbl(dd,cx,228,'AU TOTAL',CREAM,10)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'204',cx,134,100,'press',80,GOLD,align='c',shadow=(6,6,BLACK)); star(dd,40,214,t,6); star(dd,272,214,t+1,6)
            stamp(dd,cx,300,'ET PAS 64 !',CORAL,14); tagc(dd,cx,364,'LA RÉPONSE : 204 CARRÉS',GOLD)
        elif key=='r1':
            board(dd); allcells(dd,GOLD,1)
            box(dd,cx-40,BY0+8*CS+8,80,0,fill=None) if False else None
            tagc(dd,cx,364,'64 PETITS CARRÉS D’UNE CASE',GOLD)
        elif key=='r2':
            board(dd); sq(dd,0,0,2,CYAN,5); sq(dd,3,4,2,CYAN,5) if lt>0.8 else None
            lbl(dd,cx,BY0+8*CS+6,'CARRÉS DE 2 x 2',CYAN,10)
            tagc(dd,cx,364,'DES CARRÉS DE 2 SUR 2',CYAN)
        elif key=='r3':
            board(dd); p=min(6,int(lt*1.6)); sq(dd,0,p,2,CYAN,5)
            for i in range(p+1): sq(dd,0,i,2,CYAN,2)
            if lt>2.6: sq(dd,min(6,int((lt-2.6)*2.0),6),0,2,CORAL,5)
            if lt>3.3: nb(dd,cx,BY0+8*CS/2-20,'7 x 7 = 49',GOLD,w=200,h=44,size=14)
            tagc(dd,cx,364,'7 EN LARGEUR, 7 EN HAUTEUR',CORAL)
        elif key=='r4':
            board(dd); sq(dd,0,0,3,CYAN,5); sq(dd,4,3,3,CYAN,5) if lt>0.6 else None
            if lt>1.3: nb(dd,cx,BY0+8*CS/2-20,'6 x 6 = 36',GOLD,w=200,h=44,size=14)
            tagc(dd,cx,364,'36 CARRÉS DE 3 SUR 3',CYAN)
        elif key=='r5':
            rows=[('CARRÉS 4x4','25',CYAN,0.05),('CARRÉS 5x5','16',CORAL,1.55),('CARRÉS 6x6','9',GOLD,2.1),('CARRÉS 7x7','4',GRN,2.55)]
            for i,(a,b,col,th) in enumerate(rows):
                y=122+i*54
                if lt>=th-0.05:
                    box(dd,36,y,240,44,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,a,112,y+16,16,'press',13,CREAM,align='c'); T(dd,b,236,y+10,24,'press',22,col,align='c')
            tagc(dd,cx,364,'25, 16, 9 ET 4 CARRÉS',GOLD)
        elif key=='r6':
            board(dd); sq(dd,0,0,8,GOLD,6)
            if lt>0.8: nb(dd,cx,BY0+8*CS/2-20,'1 SEUL : 8 x 8',GOLD,w=230,h=44,size=14)
            tagc(dd,cx,364,'UN SEUL GRAND CARRÉ',GOLD)
        elif key=='r7':
            vals=['64','49','36','25','16','9','4','1']; ths=[0.05,0.95,1.65,2.3,2.9,3.4,3.9,4.35]
            for i,(v,th) in enumerate(zip(vals,ths)):
                col=(i%2) and CYAN or CORAL
                cxx=84 if i<4 else 228; y=114+(i%4)*42
                if lt>=th-0.05:
                    numcard(dd,cxx,y,v,col,16)
                    if i not in (3,7): T(dd,'+',cxx,y+40-6,10,'press',9,CREAM,align='c') if False else None
            if lt>=2.9: T(dd,'+',156,170,20,'press',16,CREAM,align='c')
            if lt>=4.85: numcard(dd,cx,296,'= 204',GOLD,26)
            tagc(dd,cx,364,'64+49+36+25+16+9+4+1',GOLD)
        elif key=='r8':
            board(dd,dim=True); allcells(dd,GOLD,1)
            if lt>0.9: nb(dd,cx,BY0+8*CS/2-22,'SEULEMENT 64',CORAL,w=240,h=48,size=14)
            tagc(dd,cx,364,'ON COMPTE LES PETITES CASES',CORAL)
        elif key=='r9':
            board(dd)
            for k,col in ((8,GOLD),(6,CYAN),(4,CORAL),(2,GRN)): sq(dd,(8-k)//2,(8-k)//2,k,col,5)
            tagc(dd,cx,364,'LES GRANDS CARRÉS COMPTENT',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#050'
    def fn(lay,dd):
        board(dd,y0=BY0+4)
        sq(dd,1,1,5,CORAL,5,y0=BY0+4); sq(dd,2,3,3,GOLD,5,y0=BY0+4)
        T(dd,'COMBIEN DE CARRÉS',SW/2,14,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'SUR UN ÉCHIQUIER ?',SW/2,48,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="PRESQUE TOUS RÉPONDENT 64"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#051','ENVOIE-LA À QUELQU’UN')
