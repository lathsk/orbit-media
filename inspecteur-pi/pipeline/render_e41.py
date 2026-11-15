from render_e4x import *
B.NUM='#041'
ORB=['1234','9081','2718','4096','7311','5050']
def orbit(dd,t,cx=156,cy=232,rx=110,ry=98,k=1.0,size=13,conv=0.0):
    for i,v in enumerate(ORB):
        a=i*math.pi/3+t*0.9
        x=cx+rx*(1-conv)*math.cos(a); y=cy+ry*(1-conv)*math.sin(a)
        w=len(v)*size+22; box(dd,x-w/2,y-(size+16)/2,w,size+16,fill=CARD,border=[CORAL,CYAN,GOLD][i%3],bw=2,shadow=(2,2,BLACK))
        T(dd,v,x,y-(size+4)/2+1,size+4,'press',size,CREAM,align='c')
def man(dd,cx,feet,t,pal,k=3.0): sprite(dd,MAN,pal,cx-5*k,feet-14*k+math.sin(t*3)*1.2,k,10)
HEADS={'s1':[('Un nombre ',CREAM),('magique',GOLD)],
 's2':[('Un ',CREAM),('tour de calcul',CYAN),(' étrange',CREAM)],
 's3':[('Un nombre à ',CREAM),('4 chiffres',GOLD)],
 's4':[('Pas tous ',CREAM),('identiques',RED)],
 's5':[('Du plus ',CREAM),('grand',GOLD),(' au plus ',CREAM),('petit',CYAN)],
 's6':[('Du plus ',CREAM),('petit',CYAN),(' au plus ',CREAM),('grand',GOLD)],
 's7':[('Grand ',GOLD),('moins ',CREAM),('petit',CYAN)],
 's8':[('Par exemple : ',CREAM),('3524',GOLD)],
 's9':[('Le plus grand : ',CREAM),('5432',GOLD)],
 's10':[('Le plus petit : ',CREAM),('2345',CYAN)],
 's11':[('Résultat : ',CREAM),('3087',CORAL)],
 's12':[('On ',CREAM),('recommence',GOLD)],
 's13':[('Quel que soit le ',CREAM),('départ',GOLD)],
 's14':[('Toujours le ',CREAM),('même nombre',GOLD)],
 'q':[('Quel est ce ',CREAM),('nombre',CORAL),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('6174',GOLD)],
 'r1':[('On part de ',CREAM),('3524',GOLD)],
 'r2':[('Étape un : ',CREAM),('3087',CORAL)],
 'r3':[('Puis ',CREAM),('8352',CYAN)],
 'r4':[('Puis ',CREAM),('6174',GOLD)],
 'r5':[('Et là, plus ',CREAM),('rien ne bouge',GOLD)],
 'r6':[('Essayons ',CREAM),('7641',GOLD),(' moins ',CREAM),('1467',CYAN)],
 'r7':[('Ça redonne ',CREAM),('6174',GOLD)],
 'r8':[('Il se mord ',CREAM),('la queue',CORAL)],
 'r9':[('Ce n’est pas de la ',CREAM),('chance',RED)],
 'r10':[('Sept étapes ',GOLD),('au plus',CREAM)],
 'r11':[('Tous les nombres ',CREAM),('y arrivent',GOLD)],
 'r12':[('Le nombre de ',CREAM),('Kaprekar',GOLD)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','q')
SC=[(54,70,'3'),(114,70,'5'),(174,70,'2'),(234,70,'4')]
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            orbit(dd,t); numcard(dd,cx,207,'????',GOLD,24); star(dd,40,128,t,5); star(dd,276,340,t+1,5); tagc(dd,cx,364,'UN NOMBRE MAGIQUE',GOLD)
        elif key=='s2':
            sprite(dd,DET,DPAL,56,GY-20-24*4.0+math.sin(t*4)*1.5,4.0,20)
            box(dd,150,140,142,132,fill=CARD,border=CORAL,bw=3,shadow=(4,4,BLACK))
            for i,(s,c) in enumerate((('+',CORAL),('-',CYAN),('x',GOLD),('=',GRN))): T(dd,s,175+(i%2)*62,158+(i//2)*54,36,'press',30,c,align='c',shadow=(3,3,BLACK))
            tagc(dd,cx,364,'UN TOUR DE CALCUL',CYAN)
        elif key=='s3':
            for i,(x,y,d) in enumerate(SC):
                box(dd,x-27,150,54,76,fill=CARD,border=GOLD,bw=3,shadow=(3,3,BLACK)); T(dd,d,x,170,40,'press',34,GOLD,align='c')
            lbl(dd,cx,118,'QUATRE CHIFFRES',CYAN,10); stamp(dd,cx,290,'4 CHIFFRES',GOLD,13); tagc(dd,cx,364,'UN NOMBRE À QUATRE CHIFFRES',GOLD)
        elif key=='s4':
            numcard(dd,cx-14,124,'1111',CREAM,22); xmark_(dd,262,148,15,5,RED)
            numcard(dd,cx-14,196,'7777',CREAM,22); xmark_(dd,262,220,15,5,RED)
            numcard(dd,cx-14,268,'3524',GOLD,22); check(dd,262,292,15,5,GRN)
            tagc(dd,cx,364,'PAS TOUS IDENTIQUES',RED)
        elif key=='s5':
            numcard(dd,cx,130,'3524',CREAM,28); arrow_d(dd,cx,210,26,GOLD)
            numcard(dd,cx,244,'5432',GOLD,28); lbl(dd,cx,318,'DU PLUS GRAND AU PLUS PETIT',GOLD,8); tagc(dd,cx,364,'LE NOMBRE LE PLUS GRAND',GOLD)
        elif key=='s6':
            numcard(dd,cx,130,'3524',CREAM,28); arrow_d(dd,cx,210,26,CYAN)
            numcard(dd,cx,244,'2345',CYAN,28); lbl(dd,cx,318,'DU PLUS PETIT AU PLUS GRAND',CYAN,8); tagc(dd,cx,364,'LE NOMBRE LE PLUS PETIT',CYAN)
        elif key=='s7':
            numcard(dd,cx+10,124,'5432',GOLD,24); numcard(dd,cx+10,194,'2345',CYAN,24); minus(dd,32,222,26)
            vline(dd,60,SW-20,262); T(dd,'?',cx+10,282,60,'press',40,CORAL,align='c',shadow=(4,4,BLACK))
            tagc(dd,cx,364,'GRAND MOINS PETIT',CORAL)
        elif key=='s8':
            numcard(dd,cx,190,'3524',GOLD,36); star(dd,40,150,t,5); star(dd,274,150,t+1,5); lbl(dd,cx,128,'EXEMPLE',CYAN,11); tagc(dd,cx,364,'PAR EXEMPLE 3524',GOLD)
        elif key=='s9':
            numcard(dd,cx,124,'3524',CREAM,18,dim=True); arrow_d(dd,cx,180,28,GOLD); numcard(dd,cx,222,'5432',GOLD,34); lbl(dd,cx,320,'LE PLUS GRAND',GOLD,10); tagc(dd,cx,364,'LE PLUS GRAND NOMBRE',GOLD)
        elif key=='s10':
            numcard(dd,cx+10,128,'5432',GOLD,24)
            minus(dd,32,222,26); numcard(dd,cx+10,198,'2345',CYAN,24); lbl(dd,cx,290,'MOINS LE PLUS PETIT',CYAN,10); tagc(dd,cx,364,'LE PLUS PETIT NOMBRE',CYAN)
        elif key=='s11':
            eqn(dd,'5432','2345','3087',22,120); tagc(dd,cx,364,'SOIT 3087',CORAL)
        elif key=='s12':
            numcard(dd,cx,122,'3087',CORAL,22); arrow_d(dd,cx,176,22,CREAM); numcard(dd,cx,206,'????',CYAN,22,dim=True); arrow_d(dd,cx,260,22,CREAM); numcard(dd,cx,290,'????',CORAL,22,dim=True)
            tagc(dd,cx,364,'ENCORE ET ENCORE',GOLD)
        elif key=='s13':
            P=[(54,140),(150,150),(250,138),(60,260),(160,250),(252,262)]
            for i,v in enumerate(ORB): numcard(dd,P[i][0]+(i%2)*4-2,P[i][1]+math.sin(t*3+i)*3,v,[CORAL,CYAN,GOLD][i%3],12)
            stamp(dd,cx,326,'N’IMPORTE QUEL NOMBRE',GOLD,10); tagc(dd,cx,364,'QUEL QUE SOIT TON NOMBRE DE DÉPART',GOLD)
        elif key=='s14':
            P=[(54,140),(150,150),(250,138),(60,260),(160,250),(252,262)]
            p=ease(lt/max(0.6,dur*0.85))
            for i,v in enumerate(ORB):
                x=P[i][0]+(cx-P[i][0])*p; y=P[i][1]+(222-P[i][1])*p
                if p<0.8: numcard(dd,x,y-18,v,[CORAL,CYAN,GOLD][i%3],12)
            numcard(dd,cx,198,'????',GOLD,28); stamp(dd,cx,326,'TOUJOURS LE MÊME',GOLD,11); tagc(dd,cx,364,'TOUJOURS SUR LE MÊME NOMBRE',GOLD)
        elif key=='q':
            sprite(dd,DET,DPAL,24,GY-20-24*3.6+math.sin(t*4)*1.5,3.6,20)
            T(dd,'?',226,128,110,'press',90,GOLD,align='c',shadow=(5,5,BLACK)); stamp(dd,226,290,'LEQUEL ?',CORAL,12); tagc(dd,cx,364,'QUEL EST CE NOMBRE ?',CORAL)
        elif key=='r0':
            numcard(dd,cx,176,'6174',GOLD,52); star(dd,36,150,t,6); star(dd,276,150,t+1,6); stamp(dd,cx,306,'LE NOMBRE MAGIQUE',GOLD,11); tagc(dd,cx,364,'LA RÉPONSE : 6174',GOLD)
        elif key=='r1':
            numcard(dd,cx,186,'3524',CREAM,36); stamp(dd,cx,128,'DÉPART',CYAN,13); tagc(dd,cx,364,'ON PART DE 3524',CREAM)
        elif key in ('r2','r3','r4'):
            n={'r2':2,'r3':3,'r4':4}[key]
            chain(dd,['3524','3087','8352','6174'],n,16,116,last=True,labels=['','ÉTAPE 1','ÉTAPE 2','ÉTAPE 3'])
            tagc(dd,cx,364,{'r2':'ÉTAPE UN : 3087','r3':'PUIS 8352','r4':'PUIS 6174'}[key],{'r2':CORAL,'r3':CYAN,'r4':GOLD}[key])
        elif key=='r5':
            numcard(dd,cx,176,'6174',GOLD,44); stamp(dd,cx,128,'ÇA NE BOUGE PLUS',GOLD,11)
            star(dd,48,300,t,5); star(dd,264,300,t+1,5)
            tagc(dd,cx,364,'PLUS RIEN NE BOUGE',GOLD)
        elif key in ('r6','r7'):
            eqn(dd,'7641','1467','6174' if key=='r7' else '????',22,120,cres=GOLD if key=='r7' else CORAL,resdim=(key=='r6'))
            tagc(dd,cx,364,'SEPT MILLE SIX CENT QUARANTE ET UN MOINS 1467' if False else ('ÇA REDONNE 6174' if key=='r7' else 'ESSAYONS AVEC 7641 - 1467'),GOLD if key=='r7' else CYAN)
        elif key=='r8':
            numcard(dd,cx,150,'6174',GOLD,34)
            pts=[(cx+84,172),(cx+120,172),(cx+120,262),(cx-120,262),(cx-120,172),(cx-90,172)]
            for a,b in zip(pts,pts[1:]): dotline(dd,a,b,CORAL,t,w=4,n=10)
            dd.polygon([((cx-92)*S,164*S),((cx-92)*S,180*S),((cx-80)*S,172*S)],fill=CORAL)
            stamp(dd,cx,300,'IL REVIENT À LUI-MÊME',CORAL,10); tagc(dd,cx,364,'IL SE MORD LA QUEUE',CORAL)
        elif key=='r9':
            box(dd,cx-44,170,88,88,fill=CREAM,border=DARK,bw=3,shadow=(4,4,BLACK))
            for (px,py) in ((-22,-22),(22,-22),(0,0),(-22,22),(22,22)): disc(dd,cx+px,214+py,8,DARK)
            xmark_(dd,cx,214,70,9,RED); stamp(dd,cx,306,'PAS DE HASARD',RED,12); tagc(dd,cx,364,'CE N’EST PAS DE LA CHANCE',RED)
        elif key=='r10':
            n=min(7,int(lt/dur*7*1.6)+1)
            for i in range(7):
                on=i<n; x=26+i*38
                box(dd,x,200,32,44,fill=CARD,border=(GOLD if on else EDGE),bw=3,shadow=(2,2,BLACK)); T(dd,str(i+1),x+16,212,20,'press',14,GOLD if on else GREY,align='c')
            T(dd,'7',cx,106,70,'press',54,GOLD,align='c',shadow=(5,5,BLACK)) if False else None
            stamp(dd,cx,140,'AU PLUS SEPT ÉTAPES',GOLD,11); numcard(dd,cx,274,'6174',GOLD,24) if n>=7 else None
            tagc(dd,cx,364,'EN SEPT ÉTAPES AU PLUS',GOLD)
        elif key=='r11':
            P=[(50,132),(156,122),(262,132),(40,250),(272,250),(100,300),(212,300)]
            vals=['1234','9081','2718','4096','7311','5050','8008']
            for i,v in enumerate(vals):
                dotline(dd,(P[i][0],P[i][1]+10),(cx,206),[CORAL,CYAN,GOLD][i%3],t+i*0.13,w=3,n=8)
            for i,v in enumerate(vals): numcard(dd,P[i][0],P[i][1]-10,v,[CORAL,CYAN,GOLD][i%3],11)
            numcard(dd,cx,184,'6174',GOLD,26); tagc(dd,cx,364,'TOUS LES NOMBRES ARRIVENT ICI',GOLD)
        elif key=='r12':
            numcard(dd,cx,128,'6174',GOLD,34); man(dd,100,GY-20,t,dict(MPAL,T='#4DA3FF'),4.2)
            box(dd,170,226,120,70,fill=CARD,border=GOLD,bw=3,shadow=(3,3,BLACK)); T(dd,'KAPREKAR',230,252,16,'press',11,GOLD,align='c'); T(dd,'MATHS',230,272,14,'press',9,CYAN,align='c')
            star(dd,262,180,t,5); tagc(dd,cx,364,'LE NOMBRE DE KAPREKAR',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#041'
    def fn(lay,dd):
        orbit(dd,t,cy=232); numcard(dd,SW/2,207,'????',GOLD,24); star(dd,36,150,t,5); star(dd,276,330,t+1,5)
        T(dd,'UN NOMBRE MAGIQUE',SW/2,16,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'QUEL EST-IL ?',SW/2,52,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DU NOMBRE MAGIQUE"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#042')
