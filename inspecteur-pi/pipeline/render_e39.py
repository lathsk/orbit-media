from render_e2x import *
B.NUM='#039'
NOBLE=dict(MPAL); NOBLE.update({'T':'#B05CFF','P':'#4A3A6A','K':'#2A1F18'})
PIPS={1:[(0,0)],2:[(-1,-1),(1,1)],3:[(-1,-1),(0,0),(1,1)],4:[(-1,-1),(1,-1),(-1,1),(1,1)],5:[(-1,-1),(1,-1),(0,0),(-1,1),(1,1)],6:[(-1,-1),(1,-1),(-1,0),(1,0),(-1,1),(1,1)]}
def die(dd,cx,cy,s,n,col=CREAM,ring=None,rot=0.0):
    cy=cy+math.sin(rot)*3
    if ring: box(dd,cx-s/2-5,cy-s/2-5,s+10,s+10,fill=None,border=ring,bw=3)
    box(dd,cx-s/2,cy-s/2,s,s,fill=col,border=DARK,bw=3,shadow=(3,3,BLACK))
    for px,py in PIPS[n]: disc(dd,cx+px*s*0.27,cy+py*s*0.27,max(2,s*0.085),DARK)
def man(dd,cx,feet,t,pal,k=3.0): sprite(dd,MAN,pal,cx-5*k,feet-14*k+math.sin(t*3)*1.2,k,10)
def noble(dd,cx,feet,t,k=3.4,sad=False):
    k=k*1.45
    man(dd,cx,feet,t,NOBLE,k); box(dd,cx-5*k,feet-14*k-1.2*k,10*k,2.6*k,fill=rgb('#5A3A8A')); box(dd,cx+1*k,feet-14*k-4.4*k,2*k,3.4*k,fill=CORAL)
def pile(dd,cx,y,n,t=0.0):
    for i in range(n):
        r,c=divmod(i,6); x=cx-34+c*13+(r%2)*6; yy=y-r*9
        disc(dd,x,yy,8,GOLD,DARK,1)
def tri_(dd,pts,fill): dd.polygon([(x*S,y*S) for x,y in pts],fill=fill)
def bar(dd,x,y,w,h,frac,col,t=1.0):
    box(dd,x,y,w,h,fill=CARD,border=EDGE,bw=2); ww=(w-4)*frac*min(1,t)
    if ww>=1: box(dd,x+2,y+2,ww,h-4,fill=col)
HEADS={'s1':[('Une ',CREAM),('fortune',GOLD),(' avec un dé',CREAM)],
 's2':[('Un noble ',CREAM),('joueur',GOLD)],
 's3':[('Un dé, ',CREAM),('quatre',GOLD),(' lancers',CREAM)],
 's4':[('Il gagne ',CREAM),('souvent',GRN)],
 's5':[('Un pari ',CREAM),('pareil',CYAN),(' ?',CREAM)],
 's6':[('Deux dés, ',CREAM),('vingt-quatre',GOLD),(' lancers',CREAM)],
 's7':[('Son calcul ',CREAM),('semble parfait',GOLD)],
 's8':[('Six fois ',CREAM),('plus rare, ',RED),('six fois ',CREAM),('plus',GRN),(' de lancers',CREAM)],
 's9':[('Pourtant, il ',CREAM),('perd',RED),(' !',CREAM)],
 'q':[('Quel est le ',CREAM),('piège',CORAL),(' ?',CREAM)],
 'r0':[('Le premier ',CREAM),('gagne',GRN),(' et le second ',CREAM),('perd',RED)],
 'r1':[('Jamais de ',CREAM),('six',CORAL),(' ?',CREAM)],
 'r2':[('Cinq ',CREAM),('sixièmes, ',GOLD),('quatre fois',CREAM)],
 'r3':[('Environ ',CREAM),('48 %',CORAL)],
 'r4':[('Au moins un ',CREAM),('six',GOLD),(' : ',CREAM),('52 %',GRN)],
 'r5':[('Double six : ',CREAM),('35 sur 36',CYAN)],
 'r6':[('24 fois',GOLD),(' de suite',CREAM)],
 'r7':[('Double six : ',CREAM),('49 %',RED)],
 'r8':[('La ',CREAM),('règle de trois',RED),(' ?',CREAM)],
 'r9':[('Elles se ',CREAM),('multiplient',GOLD),(' !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            die(dd,SW/2,200,92,6,rot=t*3); star(dd,48,150,t,5); star(dd,264,160,t+1,5); pile(dd,SW/2,318,12); tagc(dd,SW/2,364,'UNE FORTUNE AVEC UN DÉ',GOLD)
        elif key=='s2':
            noble(dd,SW/2,GY-24,t,3.6); stamp(dd,SW/2,168,'AU 17E SIÈCLE',GOLD,14); die(dd,56,250,36,3); die(dd,256,250,36,5); tagc(dd,SW/2,364,'UN NOBLE JOUEUR',GOLD)
        elif key=='s3':
            seq=(2,5,6,3); n=min(4,int(lt/dur*4*1.3)+1)
            for i in range(n): die(dd,48+i*72,196,52,seq[i],ring=(GOLD if seq[i]==6 else None),rot=t*3+i)
            lbl(dd,SW/2,254,'UN DÉ x 4 LANCERS',CYAN,11); lbl(dd,SW/2,286,'AU MOINS UN 6',GOLD,12); tagc(dd,SW/2,364,'UN DÉ, QUATRE LANCERS',CYAN)
        elif key=='s4':
            noble(dd,86,GY-24,t,3.2); pile(dd,222,318,16); star(dd,230,170,t,5); stamp(dd,SW/2,150,'IL GAGNE SOUVENT',GRN,12); tagc(dd,SW/2,364,'IL S’ENRICHIT',GRN)
        elif key=='s5':
            die(dd,70,200,60,6); T(dd,'?',SW/2,150,60,'press',44,CORAL,align='c',shadow=(4,4,BLACK))
            die(dd,206,200,50,6); die(dd,266,200,50,6); lbl(dd,70,246,'1 DÉ',CREAM,11); lbl(dd,236,246,'2 DÉS',CREAM,11); tagc(dd,SW/2,364,'UN PARI PAREIL ?',CYAN)
        elif key=='s6':
            die(dd,100,190,70,6,rot=t*3); die(dd,212,190,70,6,rot=t*3+1); nb_=None
            stamp(dd,SW/2,274,'x 24 LANCERS',GOLD,16); lbl(dd,SW/2,310,'AU MOINS UN DOUBLE 6',CYAN,11); tagc(dd,SW/2,364,'DEUX DÉS, VINGT-QUATRE FOIS',GOLD)
        elif key=='s7':
            box(dd,26,138,260,60,fill=CARD,border=GOLD,bw=3,shadow=(3,3,BLACK)); T(dd,'4 x 6 = 24',SW/2,154,30,'press',24,GOLD,align='c')
            noble(dd,SW/2,GY-24,t,3.0); star(dd,52,260,t,4); star(dd,262,260,t+1,4); tagc(dd,SW/2,364,'SON CALCUL SEMBLE PARFAIT',GOLD)
        elif key=='s8':
            lbl(dd,SW/2,114,'UN SIX : 1 CHANCE SUR 6',CORAL,10); bar(dd,28,138,256,22,1/6,CORAL)
            lbl(dd,SW/2,172,'DOUBLE SIX : 1 SUR 36',RED,10); bar(dd,28,196,256,22,1/36,RED,t=min(1,lt/0.8)); lbl(dd,SW/2,230,'6 FOIS PLUS RARE',RED,11)
            T(dd,'LANCERS',SW/2,268,16,'press',12,CREAM,align='c'); T(dd,'4  ->  24',SW/2,292,24,'press',20,GRN,align='c',shadow=(3,3,BLACK)); lbl(dd,SW/2,326,'6 FOIS PLUS NOMBREUX',GRN,10)
            tagc(dd,SW/2,364,'RARE x6 ... LANCERS x6',GOLD)
        elif key=='s9':
            noble(dd,86,GY-24,t,3.2); pile(dd,226,318,4); stamp(dd,SW/2,150,'IL PERD !',RED,16); xmark_(dd,226,230,16,6,RED); tagc(dd,SW/2,364,'IL COMMENCE À PERDRE',RED)
        elif key=='q':
            noble(dd,86,GY-24,t,3.2); T(dd,'?',226,130,100,'press',80,GOLD,align='c',shadow=(5,5,BLACK)); die(dd,226,270,40,6); tagc(dd,SW/2,364,'QUEL EST LE PIÈGE ?',CORAL)
        elif key=='r0':
            for cx,col,txt,n,res,rc in ((80,GRN,'1 DÉ x 4',1,'GAGNE',GRN),(232,RED,'2 DÉS x 24',2,'PERD',RED)):
                box(dd,cx-62,128,124,150,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,144,20,'press',11,CREAM,align='c')
                if n==1: die(dd,cx,206,46,6)
                else: die(dd,cx-22,206,34,6); die(dd,cx+22,206,34,6)
                if lt>0.9: stamp(dd,cx,262,res,rc,13)
            tagc(dd,SW/2,364,'LE PREMIER GAGNE, LE SECOND PERD',GOLD)
        elif key=='r1':
            die(dd,SW/2,200,92,6); xmark_(dd,SW/2,200,50,10,RED); lbl(dd,SW/2,274,'AUCUN 6 EN 4 LANCERS',CORAL,10); tagc(dd,SW/2,364,'JAMAIS DE SIX ?',CORAL)
        elif key=='r2':
            n=min(4,int(lt/dur*4*1.4)+1)
            for i in range(n):
                x=26+i*70; box(dd,x,170,50,58,fill=CARD,border=GOLD,bw=3,shadow=(3,3,BLACK)); T(dd,'5/6',x+25,188,22,'press',12,GOLD,align='c')
                if i<3 and i<n-1: T(dd,'x',x+60,188,22,'press',12,CREAM,align='c')
            lbl(dd,SW/2,262,'5 CHANCES SUR 6, 4 FOIS',CYAN,10); tagc(dd,SW/2,364,'CINQ SIXIÈMES, QUATRE FOIS',GOLD)
        elif key=='r3':
            bar(dd,28,178,256,40,0.48,CORAL,t=min(1,lt/0.9)); T(dd,'48 %',SW/2,236,34,'press',28,CORAL,align='c',shadow=(3,3,BLACK)); lbl(dd,SW/2,128,'AUCUN 6 DU TOUT',CORAL,11); tagc(dd,SW/2,364,'ENVIRON 48 %',CORAL)
        elif key=='r4':
            bar(dd,28,178,256,40,0.52,GRN,t=min(1,lt/0.9)); T(dd,'52 %',SW/2,236,34,'press',28,GRN,align='c',shadow=(3,3,BLACK)); lbl(dd,SW/2,128,'AU MOINS UN 6',GOLD,11); star(dd,262,276,t,4); tagc(dd,SW/2,364,'AU MOINS UN SIX : 52 %',GRN)
        elif key=='r5':
            for i in range(6):
                for j in range(6):
                    hit=(i==5 and j==5); box(dd,66+j*30,118+i*30,28,28,fill=(CORAL if hit else rgb('#243060')),border=DARK,bw=1)
            lbl(dd,SW/2,306,'35 CHANCES SUR 36 DE RATER',CYAN,10); tagc(dd,SW/2,364,'TRENTE-CINQ SUR TRENTE-SIX',CYAN)
        elif key=='r6':
            box(dd,26,150,260,60,fill=CARD,border=CYAN,bw=3,shadow=(3,3,BLACK)); T(dd,'(35/36) x 24',SW/2,166,30,'press',20,CYAN,align='c')
            if lt>0.8: bar(dd,28,236,256,36,0.51,CYAN,t=min(1,(lt-0.8)/0.8)); T(dd,'51 %',SW/2,282,34,'press',26,CYAN,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'VINGT-QUATRE FOIS : 51 %',CYAN)
        elif key=='r7':
            bar(dd,28,178,256,40,0.49,RED,t=min(1,lt/0.9)); box(dd,28+2+(252)*0.5-1,170,3,56,fill=GOLD); T(dd,'50 %',28+2+126,146,16,'press',12,GOLD,align='c')
            T(dd,'49 %',SW/2,236,34,'press',28,RED,align='c',shadow=(3,3,BLACK)); lbl(dd,SW/2,118,'AU MOINS UN DOUBLE 6',GOLD,10); tagc(dd,SW/2,364,'ENVIRON 49 % : PERDANT',RED)
        elif key=='r8':
            box(dd,26,150,260,60,fill=CARD,border=RED,bw=3,shadow=(3,3,BLACK)); T(dd,'4 x 6 = 24',SW/2,166,30,'press',24,RED,align='c')
            if lt>0.5: box(dd,32,176,248,6,fill=RED)
            stamp(dd,SW/2,270,'RÈGLE DE TROIS',RED,14); tagc(dd,SW/2,364,'LE PIÈGE : LA RÈGLE DE TROIS',RED)
        elif key=='r9':
            box(dd,40,140,100,76,fill=CARD,border=RED,bw=3); T(dd,'+',90,150,40,'press',34,CREAM,align='c'); xmark_(dd,90,184,16,4,RED)
            box(dd,172,140,100,76,fill=CARD,border=GRN,bw=3); T(dd,'x',222,152,40,'press',32,GOLD,align='c')
            lbl(dd,90,230,'S’AJOUTENT',RED,10); lbl(dd,222,230,'SE MULTIPLIENT',GRN,9); star(dd,SW/2,290,t,5); tagc(dd,SW/2,364,'LES CHANCES SE MULTIPLIENT',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#039'
    def fn(lay,dd):
        die(dd,92,200,66,6,rot=t*2); die(dd,196,176,56,6,rot=t*2+1); die(dd,230,236,56,6,rot=t*2+2); star(dd,40,140,t,5); pile(dd,SW/2,330,10)
        T(dd,'UN DÉ GAGNE,',SW/2,16,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'DEUX DÉS PERDENT ?',SW/2,52,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DU PARI DU CHEVALIER"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#040')
