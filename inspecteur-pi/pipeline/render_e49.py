from render_e4x import *
import inspect
B.NUM='#049'
NUMS='0,999...'
def hline_line(dd,x1,x2,y,col=CREAM):
    box(dd,x1,y,x2-x1,4,fill=col)
    for x in (x1,x2): box(dd,x-2,y-8,4,20,fill=col)
def dot(dd,cx,cy,r=7,col=GOLD): disc(dd,cx,cy,r,col,DARK,2)
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-18: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
HEADS={'s1':[('0,999… égale ',CREAM),('1',GOLD),(' ?',CREAM)],
 's2':[('Des ',CREAM),('neuf,',GOLD),(' encore des ',CREAM),('neuf',GOLD)],
 's3':[('Très, très ',CREAM),('proche',CORAL),(' de 1',CREAM)],
 's4':[('Vraiment ',CREAM),('égal',GOLD),(' à 1 ?',CREAM)],
 's5':[('Toujours un peu ',CREAM),('en dessous',CORAL),(' ?',CREAM)],
 'q':[('Égal',GOLD),(' ou juste ',CREAM),('proche',CYAN),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('exactement égal',GOLD)],
 'r1':[('Pas ',CREAM),('presque',CORAL),(' : égal',CREAM)],
 'r2':[('Un ',CREAM),('tiers,',GOLD),(' c’est ',CREAM),('0,333…',CYAN)],
 'r3':[('Fois ',CREAM),('3',CORAL),(' : ',CREAM),('un tiers',GOLD),(' donne ',CREAM),('1',GRN)],
 'r4':[('0,333…',CYAN),(' fois ',CREAM),('3',CORAL),(' : ',CREAM),('0,999…',GOLD)],
 'r5':[('Donc ',CREAM),('0,999…',GOLD),(' = ',CREAM),('1',GRN)],
 'r6':[('Aucun nombre',CORAL),(' entre les deux',CREAM)],
 'r7':[('Rien entre eux : ',CREAM),('même nombre',GRN)],
 'r8':[('On croit qu’il ',CREAM),('n’arrive jamais',CORAL)],
 'r9':[('Mais il est ',CREAM),('déjà arrivé',GRN),(' !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','q')
def line_scene(dd,cx,y=230,pos=None,gap=True):
    hline_line(dd,40,272,y)
    lbl(dd,40,y+18,'0,9',GREY,9); lbl(dd,272,y+18,'1',CREAM,11)
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            T(dd,NUMS,cx,140,60,'press',34,GOLD,align='c',shadow=(5,5,BLACK))
            T(dd,'= 1 ?',cx,214,80,'press',52,CORAL,align='c',shadow=(5,5,BLACK))
            tagc(dd,cx,364,'ÉGAL À UN ?',GOLD)
        elif key=='s2':
            items=['0',',','9','9','9','9','...']; n=min(7,int(lt*2.4)+1)
            for i,c in enumerate(items[:n]):
                col=GOLD if c=='9' else (CREAM if c in '0,' else CORAL)
                nb(dd,22+i*40+18,170,c,col,w=36,h=50,size=22 if c!='...' else 14)
            lbl(dd,cx,262,'ET ENCORE DES NEUF',CYAN,10)
            tagc(dd,cx,364,'DES NEUF SANS FIN',CORAL)
        elif key=='s3':
            line_scene(dd,cx,y=220); dot(dd,262,214,7,GOLD)
            lbl(dd,262,170,NUMS,GOLD,10)
            lbl(dd,cx,128,'À PEINE EN DESSOUS DE 1',CREAM,10)
            tagc(dd,cx,364,'TRÈS, TRÈS PROCHE DE UN',CYAN)
        elif key=='s4':
            numcard(dd,cx,124,NUMS,GOLD,22); T(dd,'= ?',cx,194,40,'press',30,CORAL,align='c',shadow=(4,4,BLACK))
            numcard(dd,cx,252,'1',CYAN,26)
            tagc(dd,cx,364,'VRAIMENT ÉGAL ?',GOLD)
        elif key=='s5':
            line_scene(dd,cx,y=250); dot(dd,262,244,6,GOLD)
            r=int(30+4*math.sin(t*4)); disc(dd,262,200,40,CARD,CORAL,3); T(dd,'?',262,176,50,'press',40,GOLD,align='c')
            lbl(dd,cx,128,'UN TOUT PETIT PEU ?',CORAL,10)
            tagc(dd,cx,364,'TOUJOURS UN PEU EN DESSOUS ?',CORAL)
        elif key=='q':
            box(dd,22,150,128,80,fill=CARD,border=GOLD,bw=3,shadow=(3,3,BLACK)); T(dd,'ÉGAL',86,178,24,'press',16,GOLD,align='c')
            lbl(dd,86,208,'EXACTEMENT 1',GOLD,8)
            box(dd,162,150,128,80,fill=CARD,border=CYAN,bw=3,shadow=(3,3,BLACK)); T(dd,'JUSTE',226,170,24,'press',13,CYAN,align='c'); T(dd,'PROCHE',226,190,24,'press',13,CYAN,align='c')
            T(dd,'OU',cx,244,20,'press',12,CREAM,align='c')
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,NUMS,cx,124,50,'press',30,GOLD,align='c',shadow=(5,5,BLACK))
            T(dd,'= 1',cx,176,90,'press',70,GRN,align='c',shadow=(6,6,BLACK)); star(dd,40,262,t,6); star(dd,272,262,t+1,6)
            stamp(dd,cx,300,'EXACTEMENT ÉGAL',GRN,12); tagc(dd,cx,364,'LA RÉPONSE : EXACTEMENT ÉGAL',GOLD)
        elif key=='r1':
            stamp(dd,cx,150,'PRESQUE',CORAL,18)
            if lt>0.5: xmark_(dd,cx,150,32,6,RED)
            if lt>1.3: stamp(dd,cx,250,'ÉGAL',GRN,22)
            tagc(dd,cx,364,'PAS PRESQUE : ÉGAL !',GRN)
        elif key=='r2':
            numcard(dd,cx,128,'1/3',GOLD,28)
            T(dd,'=',cx,190,40,'press',30,CREAM,align='c')
            if lt>1.4: numcard(dd,cx,236,'0,333...',CYAN,22)
            tagc(dd,cx,364,'UN TIERS = 0,333...',CYAN)
        elif key=='r3':
            numcard(dd,cx,126,'1/3',GOLD,24)
            if lt>0.8: arrow_d(dd,cx,184,26,CORAL); T(dd,'x 3',cx+44,190,20,'press',16,CORAL)
            if lt>1.9: numcard(dd,cx,226,'1',GRN,34)
            tagc(dd,cx,364,'UN TIERS FOIS 3 = 1',GOLD)
        elif key=='r4':
            numcard(dd,cx,126,'0,333...',CYAN,20)
            if lt>0.6: arrow_d(dd,cx,184,26,CORAL); T(dd,'x 3',cx+70,190,20,'press',16,CORAL)
            if lt>1.6: numcard(dd,cx,226,NUMS,GOLD,20)
            tagc(dd,cx,364,'0,333... FOIS 3 = 0,999...',GOLD)
        elif key=='r5':
            numcard(dd,cx,124,NUMS,GOLD,24); T(dd,'=',cx,186,40,'press',34,CORAL,align='c',shadow=(4,4,BLACK)); numcard(dd,cx,226,'1',GRN,34)
            if lt>1.0: stamp(dd,cx,320,'PROUVÉ !',GRN,14)
            tagc(dd,cx,364,'0,999... = 1',GRN)
        elif key=='r6':
            numcard(dd,84,150,NUMS,GOLD,12); numcard(dd,262,150,'1',CYAN,16)
            T(dd,'?',cx,150,40,'press',30,GOLD,align='c')
            if lt>1.0: xmark_(dd,cx,166,22,6,RED)
            lbl(dd,cx,236,'ESPACE VIDE ENTRE LES DEUX',CORAL,9)
            tagc(dd,cx,364,'AUCUN NOMBRE ENTRE LES DEUX',CORAL)
        elif key=='r7':
            numcard(dd,cx,128,NUMS,GOLD,22); T(dd,'=',cx,192,40,'press',30,GRN,align='c',shadow=(4,4,BLACK)); numcard(dd,cx,232,'1',GRN,26)
            stamp(dd,cx,320,'MÊME NOMBRE',GRN,12)
            tagc(dd,cx,364,'RIEN ENTRE EUX = MÊME NOMBRE',GRN)
        elif key=='r8':
            line_scene(dd,cx,y=230)
            x=40+(262-40)*min(1,lt/3.0)**0.7*0.93; dot(dd,x,224,7,GOLD)
            lbl(dd,cx,150,'IL S’APPROCHE...',CORAL,10)
            tagc(dd,cx,364,'ON CROIT QU’IL N’ARRIVE JAMAIS',CORAL)
        elif key=='r9':
            line_scene(dd,cx,y=230); dot(dd,272,224,8,GRN)
            star(dd,272,176,t,8); stamp(dd,cx,150,'DÉJÀ ARRIVÉ !',GRN,14)
            tagc(dd,cx,364,'IL EST DÉJÀ ARRIVÉ !',GRN)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#049'
    def fn(lay,dd):
        T(dd,NUMS,SW/2,120,60,'press',34,GOLD,align='c',shadow=(5,5,BLACK))
        T(dd,'= 1 ?',SW/2,196,80,'press',52,CORAL,align='c',shadow=(5,5,BLACK))
        T(dd,'ÉGAL OU JUSTE PROCHE ?',SW/2,286,16,'press',11,CREAM,align='c')
        T(dd,'0,999... EGAL A 1 ?',SW/2,14,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)) if False else None
        T(dd,'ZÉRO VIRGULE NEUF',SW/2,14,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'À L’INFINI',SW/2,48,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="DES NEUF SANS JAMAIS S’ARRÊTER"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#050','ENREGISTRE-LA POUR PLUS TARD')
