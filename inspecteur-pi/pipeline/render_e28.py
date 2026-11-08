from render_e2x import *
B.NUM='#028'
HEADS={'s1':[('Un ',CREAM),('nombre secret',GOLD)],
 's2':[('L’inspecteur ',CREAM),('parie',CORAL),(' de le deviner',CREAM)],
 's3':[('Il pose des ',CREAM),('questions',GOLD)],
 's4':[('Réponses : ',CREAM),('oui',GRN),(' ou ',CREAM),('non',RED)],
 's5':[('Par ',CREAM),('exemple',GOLD),(' :',CREAM)],
 's6':[('Des ',CREAM),('milliers',CORAL),(' ?',CREAM)],
 'q':[('Combien de ',CREAM),('questions',CORAL),(' ?',CREAM)],
 's7':[('Pour être ',CREAM),('certain',GOLD),(' de trouver',CREAM)],
 'r0':[('Réponse : ',CREAM),('20',GOLD),(' questions !',CREAM)],
 'r1':[('Chaque question : ',CREAM),('÷ 2',GOLD)],
 'r2':[('1 million ',CREAM),('devient',CORAL),(' 500 000',GOLD)],
 'r3':[('Puis ',CREAM),('250 000',GOLD)],
 'r4':[('Puis ',CREAM),('125 000',GOLD)],
 'r5':[('Et ainsi ',CREAM),('de suite',CORAL)],
 'r6':[('Après ',CREAM),('20',GOLD),(' questions',CREAM)],
 'r7':[('2 × 2 × 2 … ',CREAM),('20 fois',GOLD)],
 'r8':[('Un peu plus d’',CREAM),('un million',GOLD)],
 'r9':[('Avec ',CREAM),('19',GOLD),(' questions : ',CREAM),('impossible',RED)]}
STORY=('s1','s2','s3','s4','s5','s6','q','s7')
def bignum(dd,cx,y,txt,col=GOLD,w=120,h=64,size=32):
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=4,shadow=(4,4,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
def bar(dd,y,frac,txt,col=GOLD,hl=True):
    box(dd,22,y,268,30,fill=CARD,border=(col if hl else EDGE),bw=3)
    w=max(2,(268-8)*frac)
    box(dd,26,y+4,w,22,fill=(col if hl else DIM))
    f=F('press',11); tx=txt
    if w>130: T(dd,tx,26+w-6,y+9,14,'press',11,DARK,align='r')
    else: T(dd,tx,26+w+8,y+9,14,'press',11,(col if hl else CREAM),align='l')
CH=[(1.0,'1 000 000'),(0.5,'500 000'),(0.25,'250 000'),(0.125,'125 000')]
def chain(dd,k,y0=120,dy=46):
    for i in range(k): bar(dd,y0+i*dy,CH[i][0],CH[i][1],GOLD if i==k-1 else CYAN,hl=(i==k-1))
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            box(dd,86,120,140,140,fill=CARD,border=GOLD,bw=4,shadow=(4,4,BLACK))
            T(dd,'?',SW/2,148,80,'press',72,GOLD,align='c',shadow=(4,4,BLACK))
            bignum(dd,SW/2,276,'1 À 1 000 000',CYAN,w=270,h=40,size=15)
            tagc(dd,SW/2,364,'UN NOMBRE SECRET',GOLD)
        elif key=='s2':
            insp(dd,90,GY,t,k=4.0)
            bignum(dd,214,150,'JE PARIE !',CORAL,w=170,h=48,size=14)
            T(dd,'?',236,214,60,'press',50,GOLD,align='c',shadow=(4,4,BLACK))
            tagc(dd,SW/2,364,'IL VA LE DEVINER',CORAL)
        elif key=='s3':
            insp(dd,70,GY,t,k=3.4)
            n=min(3,1+int(lt*2.2))
            for i in range(n): T(dd,'?',150+i*50,150+(i%2)*40,60,'press',44,[CORAL,GOLD,CYAN][i],align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'DES QUESTIONS',GOLD)
        elif key=='s4':
            bignum(dd,86,150,'OUI',GRN,w=116,h=80,size=30); bignum(dd,226,150,'NON',RED,w=116,h=80,size=30)
            insp(dd,SW/2,GY,t,k=2.6)
            tagc(dd,SW/2,364,'OUI OU NON SEULEMENT',CREAM)
        elif key=='s5':
            bignum(dd,SW/2,118,'PLUS GRAND QUE',CYAN,w=280,h=40,size=14)
            bignum(dd,SW/2,170,'500 000 ?',GOLD,w=240,h=64,size=22)
            if lt>1.6: bignum(dd,SW/2,254,'OUI',GRN,w=130,h=50,size=24)
            insp(dd,50,GY,t,k=2.2)
            tagc(dd,SW/2,364,'UNE QUESTION OUI / NON',GOLD)
        elif key=='s6':
            bignum(dd,SW/2,120,'1 000 ?',CORAL,w=190,h=50,size=20); bignum(dd,SW/2,184,'10 000 ?',CORAL,w=230,h=50,size=20)
            insp(dd,SW/2,GY,t,k=2.8)
            tagc(dd,SW/2,364,'DES MILLIERS ?',CORAL)
        elif key=='q':
            T(dd,'?',SW/2,118,80,'press',70,CORAL,align='c',shadow=(4,4,BLACK))
            bar(dd,226,1.0,'1 000 000',CYAN,hl=True)
            insp(dd,SW/2,GY,t,k=2.3)
            tagc(dd,SW/2,364,'COMBIEN DE QUESTIONS ?',CORAL)
        elif key=='s7':
            bar(dd,150,1.0,'1 000 000',CYAN,hl=True)
            stamp(dd,SW/2,236,'À COUP SÛR',GOLD,16)
            insp(dd,SW/2,GY,t,k=2.3)
            tagc(dd,SW/2,364,'GARANTI À 100 %',GOLD)
        elif key=='r0':
            insp(dd,64,GY,t,k=3.8)
            bignum(dd,212,150,'20',GOLD,w=150,h=100,size=60)
            star(dd,282,128,t,5); star(dd,150,120,t,4)
            tagc(dd,SW/2,364,'VINGT QUESTIONS',GOLD)
        elif key=='r1':
            box(dd,22,170,268,40,fill=CARD,border=GOLD,bw=3)
            box(dd,26,174,128,32,fill=CYAN); box(dd,158,174,128,32,fill=DIM)
            dd.line([(156*S,150*S),(156*S,230*S)],fill=GOLD,width=3*S)
            xmark_(dd,222,190,12,4,RED)
            bignum(dd,SW/2,248,'÷ 2',GOLD,w=120,h=50,size=26)
            tagc(dd,SW/2,364,'MOITIÉ MOINS DE CHOIX',GOLD)
        elif key=='r2':
            f=1.0-0.5*min(1,lt/1.0)
            bar(dd,170,f,'500 000' if lt>0.55 else '1 000 000',GOLD)
            T(dd,'÷ 2',SW/2,230,30,'press',24,CORAL,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'MOITIÉ : 500 000',GOLD)
        elif key=='r3':
            chain(dd,3,y0=126); tagc(dd,SW/2,364,'250 000',GOLD)
        elif key=='r4':
            chain(dd,4,y0=116); tagc(dd,SW/2,364,'125 000',GOLD)
        elif key=='r5':
            chain(dd,4,y0=116)
            T(dd,'…',SW/2,296,30,'press',26,CORAL,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'ET AINSI DE SUITE',CORAL)
        elif key=='r6':
            n=min(20,1+int(lt*9.5))
            for i in range(20):
                r,c=divmod(i,10); box(dd,24+c*27,130+r*30,24,24,fill=(GOLD if i<n else CARD),border=(DARK if i<n else EDGE),bw=2)
            if lt>2.0: bignum(dd,SW/2,222,'1',CORAL,w=110,h=70,size=40); lbl(dd,SW/2,300,'UN SEUL NOMBRE',CORAL,11)
            tagc(dd,SW/2,364,'APRÈS 20 QUESTIONS',GOLD)
        elif key=='r7':
            n=min(8,1+int(lt*5))
            for i in range(n): bignum(dd,32+i*35,140,'2',[GOLD,CYAN][i%2],w=30,h=36,size=16)
            T(dd,'…',SW/2,200,30,'press',26,CREAM,align='c')
            bignum(dd,SW/2,236,'20 FOIS',CORAL,w=190,h=44,size=18)
            tagc(dd,SW/2,364,'20 FOIS DE SUITE',GOLD)
        elif key=='r8':
            bignum(dd,SW/2,128,'1 048 576',GOLD,w=270,h=56,size=22)
            T(dd,'>',SW/2,196,30,'press',26,GRN,align='c',shadow=(3,3,BLACK))
            bignum(dd,SW/2,232,'1 000 000',CYAN,w=270,h=56,size=22)
            tagc(dd,SW/2,364,'PLUS D’UN MILLION',GOLD)
        elif key=='r9':
            bignum(dd,SW/2,118,'524 288',RED,w=250,h=52,size=22)
            T(dd,'<',SW/2,182,30,'press',26,RED,align='c',shadow=(3,3,BLACK))
            bignum(dd,SW/2,216,'1 000 000',CYAN,w=270,h=52,size=22)
            stamp(dd,SW/2,300,'PAS ASSEZ',RED,16)
            lbl(dd,SW/2,332,'19 QUESTIONS',CREAM,10)
            tagc(dd,SW/2,364,'IMPOSSIBLE AVEC 19',RED)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#028'
    def fn(lay,dd):
        box(dd,96,150,120,120,fill=CARD,border=GOLD,bw=4,shadow=(4,4,BLACK))
        T(dd,'?',SW/2,172,70,'press',64,GOLD,align='c',shadow=(4,4,BLACK))
        bignum(dd,SW/2,286,'1 À 1 000 000',CYAN,w=250,h=36,size=14)
        T(dd,'UN NOMBRE SECRET,',SW/2,10,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'COMBIEN DE QUESTIONS ?',SW/2,44,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DU NOMBRE SECRET"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#029')
