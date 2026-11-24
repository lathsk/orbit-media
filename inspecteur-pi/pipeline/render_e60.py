from render_e4x import *
import inspect, math
B.NUM='#060'
RIB=rgb('#FF4D5E')
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
def gift(dd,cx,cy,k=1.0,col=None,t=0.0):
    col=col or CORAL; w=70*k; h=54*k; x=cx-w/2; y=cy-h/2
    box(dd,x,y+10*k,w,h-10*k,fill=col,border=DARK,bw=2)
    box(dd,x-4*k,y,w+8*k,14*k,fill=lerpc(col,(255,255,255),0.2),border=DARK,bw=2)
    box(dd,cx-5*k,y,10*k,h,fill=GOLD)
    box(dd,cx-14*k,y-10*k,12*k,11*k,fill=GOLD,border=DARK,bw=1); box(dd,cx+2*k,y-10*k,12*k,11*k,fill=GOLD,border=DARK,bw=1)
def hat(dd,cx,cy,w=120):
    """chapeau (haut-de-forme)"""
    box(dd,cx-w/2,cy+20,w,10,fill=DARK,border=CREAM,bw=2)
    box(dd,cx-w*0.32,cy-26,w*0.64,48,fill=DARK,border=CREAM,bw=2)
    box(dd,cx-w*0.32,cy+2,w*0.64,8,fill=CORAL)
def slip(dd,cx,cy,txt,col=CREAM,w=52,h=24,rot=0):
    box(dd,cx-w/2,cy-h/2,w,h,fill=CREAM,border=DARK,bw=2,shadow=(2,2,BLACK))
    T(dd,txt,cx,cy-6,12,'press',8,DARK,align='c')
NAMES=['LÉA','TOM','AMY','ZOÉ','LUC','EVA']
def dots(dd,hl=None,all_=False,cols=10,y0=130,gap=22,col=CYAN,t=0.0):
    x0=SW/2-(cols-1)*gap/2
    for i in range(100):
        x=x0+(i%cols)*gap; y=y0+(i//cols)*gap
        c=GREY
        if all_: c=col
        if hl is not None and i==hl: c=GOLD
        r=4 if c in (GREY,col) else 7
        dd.rectangle([(x-r)*S,(y-r)*S,(x+r)*S,(y+r)*S],fill=c)
HEADS={'s1':[('Père Noël ',CREAM),('secret',RED),(' : le tirage ',CREAM),('rate',GOLD)],
 's2':[('100 amis, ',GOLD),('un ',CREAM),('chapeau',CORAL)],
 's3':[('Chacun ',CREAM),('pioche',CYAN),(' un papier',CREAM)],
 's4':[('Il pioche ',CREAM),('son propre nom',RED)],
 's5':[('Tu crois que ',CREAM),('c’est rare',GOLD),(' ?',CREAM)],
 'q':[('Quelle ',CREAM),('chance',CORAL),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('63 %',GRN)],
 'r1':[('Presque ',CREAM),('2 fois sur 3',GOLD)],
 'r2':[('Chacun : ',CREAM),('1 sur 100',CYAN)],
 'r3':[('Mais ils sont ',CREAM),('100',GOLD)],
 'r4':[('Les petites chances ',CREAM),('s’accumulent',CORAL)],
 'r5':[('10, 100 ou 1000 : ',CREAM),('pareil',GRN)],
 'r6':[('En moyenne : ',CREAM),('1 personne',GOLD)],
 'r7':[('Dès ',CREAM),('7 amis',CYAN),(' : 63 %',GRN)],
 'r8':[('On ',CREAM),('recommence',CORAL),(' le tirage',CREAM)],
 'r9':[('Le piège : ',CREAM),('le cumul',CORAL)],
 'r10':[('Envoie-la !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            gift(dd,cx-70,200,1.5,CORAL); gift(dd,cx+60,230,1.1,CYAN); gift(dd,cx+100,160,0.8,GRN)
            if blink(t): stamp(dd,cx,112,'TIRAGE AU SORT',GOLD,11)
            tagc(dd,cx,364,'PÈRE NOËL SECRET : LE TIRAGE RATE',RED)
        elif key=='s2':
            hat(dd,cx,206,130)
            for i,(x,y) in enumerate([(70,128),(130,116),(190,120),(250,130)]): slip(dd,x,y+int(math.sin(t*2+i)*3),NAMES[i])
            numcard(dd,cx,270,'100 NOMS',GOLD,14)
            tagc(dd,cx,364,'100 NOMS DANS UN CHAPEAU',GOLD)
        elif key=='s3':
            hat(dd,90,220,110)
            sorted_man(dd,230,290,t,CANDP[1],k=3.4)
            arrow_r(dd,130,200,70,CREAM)
            slip(dd,176,176-int(sp(lt,0,1.0)*0),'? ? ?')
            tagc(dd,cx,364,'CHACUN PIOCHE UN PAPIER AU HASARD',CYAN)
        elif key=='s4':
            sorted_man(dd,90,240,t,CANDP[3],k=4.0); T(dd,'TOM',90,160,16,'press',12,GOLD,align='c')
            slip(dd,236,196,'TOM',w=64,h=30)
            if blink(t): stamp(dd,cx,300,'SON PROPRE NOM !',RED,10)
            arrow_r(dd,150,196,52,RED)
            tagc(dd,cx,364,'ET SI TOM PIOCHE « TOM » ?',RED)
        elif key=='s5':
            for i,x in enumerate((64,160,256)):
                sorted_man(dd,x,290,t,CANDP[i],k=3.0); numcard(dd,x,170,'?',[CORAL,CYAN,GOLD][i],14)
            tagc(dd,cx,364,'TU CROIS QUE C’EST RARE ?',GOLD)
        elif key=='q':
            numcard(dd,cx,150,'? %',GOLD,34)
            T(dd,'CHANCE QUE QUELQU’UN',cx,236,16,'press',11,CREAM,align='c'); T(dd,'PIOCHE SON NOM',cx,260,16,'press',11,CREAM,align='c')
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'63 %',cx,150,80,'press',60,GRN,align='c',shadow=(6,6,BLACK)); star(dd,30,120,t,6); star(dd,290,120,t+1,6)
            check(dd,cx,270,26,9,GRN)
            tagc(dd,cx,364,'LA RÉPONSE : 63 %',GRN)
        elif key=='r1':
            p=sp(lt,0.2,1.4)
            box(dd,36,150,248,50,fill=CARD,border=CREAM,bw=3)
            w=int(244*0.632*p)
            if w>2: box(dd,38,152,w,46,fill=RED)
            T(dd,'QUELQU’UN SE PIOCHE',cx,112,16,'press',10,CREAM,align='c')
            if lt>1.0: numcard(dd,cx,228,'63 %',GRN,20)
            tagc(dd,cx,364,'PRESQUE 2 FOIS SUR 3',GOLD)
        elif key=='r2':
            dots(dd,hl=44,t=t);
            numcard(dd,cx,150,'1 / 100',GOLD,14) if False else None
            tagc(dd,cx,364,'CHACUN : 1 CHANCE SUR 100',CYAN)
        elif key=='r3':
            dots(dd,all_=lt>0.4,col=CYAN,t=t)
            tagc(dd,cx,364,'MAIS 100 PERSONNES PIOCHENT',GOLD)
        elif key=='r4':
            vals=['1 %','2 %','5 %','20 %','63 %']
            for j,v in enumerate(vals):
                if lt>0.1+j*0.3:
                    y=116+j*44; w=int(240*[0.01,0.02,0.05,0.2,0.632][j]+6)
                    box(dd,36,y,252,34,fill=CARD,border=EDGE,bw=2); box(dd,38,y+2,w,30,fill=[CYAN,CYAN,CYAN,CORAL,GRN][j])
                    T(dd,v,284,y+9,14,'press',11,CREAM,align='r')
            tagc(dd,cx,364,'LES PETITES CHANCES S’ACCUMULENT',CORAL)
        elif key=='r5':
            for j,(n,thr) in enumerate([('10',0.2),('100',0.9),('1000',1.6)]):
                y=118+j*70
                numcard(dd,86,y,n,CYAN,16) if lt>thr-0.2 else None
                if lt>thr: arrow_r(dd,156,y+22,40,CREAM); numcard(dd,246,y,'63 %',GRN,14)
            tagc(dd,cx,364,'10, 100 OU 1000 : PRESQUE PAREIL',GRN)
        elif key=='r6':
            dots(dd,hl=37,t=t,y0=160,gap=19)
            numcard(dd,cx,110,'1 PERSONNE',GOLD,9) if lt>0.5 else None
            tagc(dd,cx,364,'EN MOYENNE : 1 PERSONNE SE PIOCHE',GOLD)
        elif key=='r7':
            for i in range(7):
                x=24+i*42; sorted_man(dd,x+10,230,t,CANDP[i%6],k=2.2)
            numcard(dd,cx,262,'7 AMIS',CYAN,14)
            if lt>0.8: numcard(dd,cx,120,'63 %',GRN,22)
            tagc(dd,cx,364,'DÈS 7 AMIS : DÉJÀ 63 %',GRN)
        elif key=='r8':
            ang=t*2.0
            for k in range(3):
                a=ang+k*2.094
                x=cx+math.cos(a)*56; y=190+math.sin(a)*56
                slip(dd,x,y,NAMES[k],w=44,h=22)
            T(dd,'↻',cx,176,40,'press',30,CORAL,align='c') if False else None
            numcard(dd,cx,276,'ON RECOMMENCE',CORAL,10)
            tagc(dd,cx,364,'ON RECOMMENCE LE TIRAGE',CORAL)
        elif key=='r9':
            for j in range(5): numcard(dd,52+j*54,130,'1 %',CYAN,8)
            T(dd,'=',cx,196,40,'press',32,CREAM,align='c')
            if lt>0.6: numcard(dd,cx,236,'« RIEN » ?',RED,12)
            if lt>1.4: xmark_(dd,cx+118,252,16,7,RED)
            tagc(dd,cx,364,'LE PIÈGE : 100 PETITES CHANCES',CORAL)
        elif key=='r10':
            bx,by=cx-46,150; box(dd,bx,by,92,64,fill=CREAM,border=DARK,bw=3,shadow=(4,4,BLACK))
            dd.line([(bx*S,by*S),((bx+46)*S,(by+34)*S),((bx+92)*S,by*S)],fill=DARK,width=3*S)
            if blink(t): arrow_r(dd,cx-20,260,48,GOLD)
            tagc(dd,cx,364,'À QUELQU’UN QUI VA SE TROMPER',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#060'
    def fn(lay,dd):
        cx=SW/2
        hat(dd,cx-70,230,110); gift(dd,cx+70,230,1.4,CORAL)
        slip(dd,cx-70,150,'TOM',w=60,h=28)
        T(dd,'PÈRE NOËL SECRET',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'TIRAGE RATÉ ?',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="QUELLE CHANCE QU’ON SE PIOCHE ?"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#061','ENVOIE-LA À QUELQU’UN')
