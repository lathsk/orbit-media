from render_e2x import *
B.NUM='#040'
CHEF=dict(MPAL); CHEF.update({'T':'#F5F5F5','P':'#4A5078','K':'#2A1F18'})
SPONGE=rgb('#E8B86D'); SPONGE2=rgb('#B58A4A'); ICING=rgb('#F5A3B8'); STEELC=rgb('#C9CFE4')
def tri_(dd,pts,fill): dd.polygon([(x*S,y*S) for x,y in pts],fill=fill)
def ln(dd,x1,y1,x2,y2,col,w=2): dd.line([(x1*S,y1*S),(x2*S,y2*S)],fill=col,width=int(w*S))
def man(dd,cx,feet,t,pal,k=3.0): sprite(dd,MAN,pal,cx-5*k,feet-14*k+math.sin(t*3)*1.2,k,10)
def chef(dd,cx,feet,t,k=4.4):
    man(dd,cx,feet,t,CHEF,k); box(dd,cx-4*k,feet-14*k-3.2*k,8*k,3.6*k,fill=rgb('#FFFFFF'),border=DARK,bw=1); box(dd,cx-5*k,feet-14*k+0.2*k,10*k,0.8*k,fill=rgb('#FFFFFF'))
def cube(dd,x,y,s,grid=0,front=SPONGE,top=ICING,side=SPONGE2,edge=DARK,gcol=None,alpha=True):
    d=s*0.38
    tri_(dd,[(x,y),(x+d,y-d),(x+s+d,y-d),(x+s,y)],top)
    tri_(dd,[(x+s,y),(x+s+d,y-d),(x+s+d,y+s-d),(x+s,y+s)],side)
    box(dd,x,y,s,s,fill=front)
    gc=gcol or edge
    if grid:
        for i in range(1,grid):
            f=i/grid
            ln(dd,x+s*f,y,x+s*f,y+s,gc,1.4); ln(dd,x,y+s*f,x+s,y+s*f,gc,1.4)
            ln(dd,x+s+d*f,y-d*f,x+s+d*f,y+s-d*f,gc,1.4); ln(dd,x+s,y+s*f,x+s+d,y+s*f-d,gc,1.4)
            ln(dd,x+s*f,y,x+s*f+d,y-d,gc,1.4); ln(dd,x+d*f,y-d*f,x+s+d*f,y-d*f,gc,1.4)
    for (a,b,c,e) in ((x,y,x+s,y),(x,y+s,x+s,y+s),(x,y,x,y+s),(x+s,y,x+s,y+s),(x,y,x+d,y-d),(x+s,y,x+s+d,y-d),(x+d,y-d,x+s+d,y-d),(x+s+d,y-d,x+s+d,y+s-d),(x+s,y+s,x+s+d,y+s-d)):
        ln(dd,a,b,c,e,edge,2)
def wire(dd,x,y,s,col=CYAN):
    d=s*0.38
    pts=[(x,y),(x+s,y),(x,y+s),(x+s,y+s),(x+d,y-d),(x+s+d,y-d),(x+s+d,y+s-d)]
    for a,b in (((x,y),(x+s,y)),((x,y),(x,y+s)),((x+s,y),(x+s,y+s)),((x,y+s),(x+s,y+s)),((x,y),(x+d,y-d)),((x+s,y),(x+s+d,y-d)),((x+d,y-d),(x+s+d,y-d)),((x+s+d,y-d),(x+s+d,y+s-d)),((x+s,y+s),(x+s+d,y+s-d))):
        ln(dd,a[0],a[1],b[0],b[1],col,2)
    # arêtes cachées (pointillés)
    for a,b in (((x+d,y-d),(x+d,y+s-d)),((x+d,y+s-d),(x+s+d,y+s-d)),((x,y+s),(x+d,y+s-d))):
        for i in range(8):
            f1=i/8; f2=(i+0.5)/8; ln(dd,a[0]+(b[0]-a[0])*f1,a[1]+(b[1]-a[1])*f1,a[0]+(b[0]-a[0])*f2,a[1]+(b[1]-a[1])*f2,col,1.5)
def center_cube(dd,x,y,s,col=GOLD):
    d=s*0.38; c=s/3; cd=d/3
    ox=x+c+cd; oy=y+c-cd
    cube(dd,ox,oy,c,0,front=col,top=lerpc(col,(255,255,255),0.45),side=lerpc(col,(0,0,0),0.35))
def knife(dd,x,y,k=1.0,ang=0):
    tri_(dd,[(x,y),(x+8*k,y),(x+8*k,y+54*k),(x,y+60*k)],STEELC); box(dd,x+8*k,y,3*k,54*k,fill=rgb('#8A93C0'))
    box(dd,x-2*k,y-26*k,12*k,26*k,fill=rgb('#6B4A2E'),border=DARK,bw=1)
def lerpc(a,b,p): return tuple(int(a[i]+(b[i]-a[i])*p) for i in range(3))
HEADS={'s1':[('Un ',CREAM),('gâteau, ',GOLD),('un ',CREAM),('couteau',CYAN)],
 's2':[('Un ',CREAM),('pâtissier',GOLD),(' et son cube',CREAM)],
 's3':[('27',GOLD),(' petits cubes ',CREAM),('identiques',CYAN)],
 's4':[('Deux coups ',CREAM),('par direction',GOLD)],
 's5':[('Six',GOLD),(' coups en tout',CREAM)],
 's6':[('Mais il est ',CREAM),('malin',CORAL)],
 's7':[('Un coup, ',CREAM),('plusieurs morceaux',GOLD)],
 'q':[('Combien de coups ',CREAM),('au minimum',CORAL),(' ?',CREAM)],
 'r0':[('Pas un de moins : ',CREAM),('six',GOLD),(' !',CREAM)],
 'r1':[('Le petit cube du ',CREAM),('centre',GOLD)],
 'r2':[('Caché ',CREAM),('au cœur',CYAN)],
 'r3':[('Il a ',CREAM),('six faces',GOLD)],
 'r4':[('Un coup, ',CREAM),('une face',CORAL)],
 'r5':[('Donc ',CREAM),('six coups',GOLD),(' au moins',CREAM)],
 'r6':[('Déplacer ',CREAM),('ne change rien',RED)],
 'r7':[('Le piège : ',CREAM),('économiser',RED)],
 'r8':[('Le centre en ',CREAM),('exige six',GOLD)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            cube(dd,70,170,110); knife(dd,236,200,1.2); star(dd,44,150,t,5); star(dd,262,140,t+1,5); stamp(dd,SW/2,310,'UN GÂTEAU CUBE',GOLD,13); tagc(dd,SW/2,364,'UN GÂTEAU, UN COUTEAU',GOLD)
        elif key=='s2':
            chef(dd,86,GY-20,t,4.6); cube(dd,150,230,80); tagc(dd,SW/2,364,'LE PÂTISSIER ET SON GÂTEAU',GOLD)
        elif key=='s3':
            cube(dd,86,184,100,grid=3,gcol=DARK); T(dd,'27',SW/2,296,60,'press',44,GOLD,align='c',shadow=(4,4,BLACK)); lbl(dd,SW/2,116,'3 x 3 x 3',CYAN,12); tagc(dd,SW/2,364,'VINGT-SEPT PETITS CUBES',CYAN)
        elif key=='s4':
            s=110; x,y=80,170; d=s*0.38
            cube(dd,x,y,s)
            for i in (1,2):
                ln(dd,x+s*i/3,y,x+s*i/3,y+s,CORAL,4); ln(dd,x+s*i/3,y,x+s*i/3+d,y-d,CORAL,4)
                ln(dd,x,y+s*i/3,x+s,y+s*i/3,CYAN,4); ln(dd,x+s,y+s*i/3,x+s+d,y+s*i/3-d,CYAN,4)
                ln(dd,x+d*i/3,y-d*i/3,x+s+d*i/3,y-d*i/3,GOLD,4); ln(dd,x+s+d*i/3,y-d*i/3,x+s+d*i/3,y+s-d*i/3,GOLD,4)
            lbl(dd,70,300,'2 COUPS',CORAL,10); lbl(dd,156,300,'2 COUPS',CYAN,10); lbl(dd,242,300,'2 COUPS',GOLD,10); tagc(dd,SW/2,364,'DEUX COUPS PAR DIRECTION',GOLD)
        elif key=='s5':
            for i,(txt,col) in enumerate((('2',CORAL),('+',CREAM),('2',CYAN),('+',CREAM),('2',GOLD),('=',CREAM),('6',GRN))):
                T(dd,txt,34+i*40,176,50,'press',34,col,align='c',shadow=(3,3,BLACK))
            stamp(dd,SW/2,270,'SIX COUPS EN TOUT',GRN,13); tagc(dd,SW/2,364,'SOIT SIX COUPS EN TOUT',GRN)
        elif key=='s6':
            chef(dd,86,GY-20,t,4.4); box(dd,170,130,110,60,fill=CARD,border=GOLD,bw=3,shadow=(3,3,BLACK)); T(dd,'!',225,138,50,'press',40,GOLD,align='c')
            for i in range(3): cube(dd,150+i*44,300,32); 
            for i in range(2): cube(dd,170+i*44,236,32)
            box(dd,226,258,5,26,fill=GOLD); tri_(dd,[(228.5,252),(220,262),(237,262)],GOLD); tagc(dd,SW/2,364,'MAIS IL EST MALIN',CORAL)
        elif key=='s7':
            for r in range(2):
                for c in range(3): cube(dd,70+c*54,250-r*50 if r==0 else 200,34)
            ln(dd,72,150,72,300,CORAL,4) if False else None
            p=int(lt*6)%2; knife(dd,SW/2-4,118+p*4,1.1); box(dd,60,214,196,4,fill=CORAL)
            stamp(dd,SW/2,312,'EN UN SEUL COUP ?',CORAL,12); tagc(dd,SW/2,364,'PLUSIEURS MORCEAUX D’UN COUP',CORAL)
        elif key=='q':
            chef(dd,76,GY-20,t,4.0); T(dd,'?',226,128,110,'press',90,GOLD,align='c',shadow=(5,5,BLACK)); stamp(dd,226,290,'MOINS DE 6 ?',CORAL,11); tagc(dd,SW/2,364,'COMBIEN DE COUPS AU MINIMUM ?',CORAL)
        elif key=='r0':
            T(dd,'6',SW/2,126,170,'press',140,GOLD,align='c',shadow=(8,8,BLACK)); cube(dd,110,300,60,grid=3,gcol=DARK) if False else None
            stamp(dd,SW/2,300,'PAS UN DE MOINS',GOLD,13); star(dd,46,200,t,5); star(dd,266,200,t+1,5); tagc(dd,SW/2,364,'SIX COUPS, PAS UN DE MOINS',GOLD)
        elif key=='r1':
            wire(dd,76,176,110,CYAN); center_cube(dd,76,176,110); lbl(dd,SW/2,128,'LE CUBE DU CENTRE',GOLD,11); tagc(dd,SW/2,364,'LE PETIT CUBE DU CENTRE',GOLD)
        elif key=='r2':
            cube(dd,76,176,110,grid=3,gcol=DARK); T(dd,'?',SW/2,206,80,'press',64,DARK,align='c')
            lbl(dd,SW/2,128,'CACHÉ DANS LE GÂTEAU',CYAN,10); stamp(dd,SW/2,310,'AUCUNE FACE VISIBLE',RED,11); tagc(dd,SW/2,364,'CACHÉ AU CŒUR DU GÂTEAU',CYAN)
        elif key=='r3':
            cube(dd,106,176,100,0,front=GOLD,top=lerpc(GOLD,(255,255,255),0.45),side=lerpc(GOLD,(0,0,0),0.35))
            n=min(6,int(lt/dur*6*1.5)+1)
            for i in range(n): box(dd,24+i*44,290,38,38,fill=CARD,border=GOLD,bw=3,shadow=(2,2,BLACK)); T(dd,str(i+1),24+i*44+19,300,22,'press',16,GOLD,align='c')
            lbl(dd,SW/2,114,'6 FACES À CRÉER',GOLD,11); tagc(dd,SW/2,364,'IL A SIX FACES',GOLD)
        elif key=='r4':
            cube(dd,60,190,90,0,front=GOLD,top=lerpc(GOLD,(255,255,255),0.45),side=lerpc(GOLD,(0,0,0),0.35)); ln(dd,60+45,170,60+45,300,CORAL,5)
            knife(dd,200,170+int(math.sin(t*5)*4),1.2); stamp(dd,SW/2,326,'1 COUP = 1 FACE',CORAL,13); lbl(dd,SW/2,128,'LE COUTEAU CRÉE LES FACES',CORAL,10); tagc(dd,SW/2,364,'UN COUP, UNE SEULE FACE',CORAL)
        elif key=='r5':
            n=min(6,int(lt/dur*6*1.6)+1)
            for i in range(6):
                on=i<n; box(dd,26+(i%3)*92,138+(i//3)*84,76,66,fill=CARD,border=(GOLD if on else EDGE),bw=3,shadow=(3,3,BLACK))
                if on: knife(dd,26+(i%3)*92+34,138+(i//3)*84+18,0.5); 
                T(dd,str(i+1),26+(i%3)*92+38,138+(i//3)*84+4,14,'press',11,GOLD if on else GREY,align='c')
            stamp(dd,SW/2,326,'6 FACES = 6 COUPS',GOLD,12); tagc(dd,SW/2,364,'IL FAUT AU MOINS SIX COUPS',GOLD)
        elif key=='r6':
            for r in range(2):
                for c in range(3): cube(dd,66+c*54,250 if r==0 else 200,34)
            T(dd,'<->',SW/2,140,26,'press',20,CREAM,align='c'); xmark_(dd,250,150,16,5,RED); stamp(dd,SW/2,318,'DÉPLACER : INUTILE',RED,12); tagc(dd,SW/2,364,'DÉPLACER NE CHANGE RIEN',RED)
        elif key=='r7':
            for i in range(5): disc(dd,60+i*48,210,16,GOLD,DARK,2)
            box(dd,34,206,244,7,fill=RED); lbl(dd,SW/2,128,'EMPILER = ÉCONOMISER ?',RED,10); stamp(dd,SW/2,300,'FAUX !',RED,16); tagc(dd,SW/2,364,'LE PIÈGE : CROIRE ÉCONOMISER',RED)
        elif key=='r8':
            cube(dd,60,190,90,0,front=GOLD,top=lerpc(GOLD,(255,255,255),0.45),side=lerpc(GOLD,(0,0,0),0.35)); T(dd,'6',236,176,100,'press',80,GOLD,align='c',shadow=(6,6,BLACK))
            star(dd,260,130,t,5); star(dd,44,150,t+1,5); stamp(dd,SW/2,326,'TOUJOURS SIX',GOLD,13); tagc(dd,SW/2,364,'LE CENTRE EXIGE SIX COUPS',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#040'
    def fn(lay,dd):
        cube(dd,70,190,120,grid=3,gcol=DARK); knife(dd,232,190,1.3); star(dd,44,150,t,5); star(dd,264,300,t+1,5)
        T(dd,'27 MORCEAUX,',SW/2,16,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'COMBIEN DE COUPS ?',SW/2,52,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DU GÂTEAU CUBE"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#041')
