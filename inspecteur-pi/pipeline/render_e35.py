from render_e2x import *
B.NUM='#035'
WATER=rgb('#1F5FA8'); WATER2=rgb('#2D7BD0'); WSURF=rgb('#8FE3FF'); STONE=rgb('#8A8FA3'); STONED=rgb('#585D74'); STONEL=rgb('#BCC1D4')
VOL=rgb('#174A8C'); SAND=rgb('#5A4630'); SANDD=rgb('#3E3022')
WL0=232; WL1=250
HEADS={'s1':[('Le ',CREAM),('niveau',GOLD),(' du lac ?',CREAM)],
 's2':[('Seul sur une ',CREAM),('barque',GOLD)],
 's3':[('Une ',CREAM),('énorme pierre',CORAL),(' à bord',CREAM)],
 's4':[('Une ',CREAM),('règle',CYAN),(' sur la rive',CREAM)],
 's5':[('Il ',CREAM),('pousse',CORAL),(' la pierre',CREAM)],
 's6':[('Plouf !',GOLD),(' Elle coule',CREAM)],
 's7':[('La pierre est ',CREAM),('dans l’eau',CYAN)],
 'q':[('Monte',CORAL),(' ou ',CREAM),('descend ?',CYAN)],
 'r0':[('Le niveau ',CREAM),('descend !',GRN)],
 'r1':[('La pierre ',CREAM),('pèse',CORAL)],
 'r2':[('La barque ',CREAM),('s’enfonce',CORAL)],
 'r3':[('Eau poussée = ',CREAM),('pierre',GOLD)],
 'r4':[('Pierre ',CREAM),('plus lourde',GOLD)],
 'r5':[('Beaucoup',CYAN),(' plus d’eau',CREAM)],
 'r6':[('Une pierre de ',CREAM),('1000 kg',GOLD)],
 'r7':[('Barque : ',CREAM),('1000 litres',CYAN)],
 'r8':[('Au fond : ',CREAM),('370 litres',RED)],
 'r9':[('Le lac ',CREAM),('baisse !',GRN)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','q')
def water(dd,wl,t,x0=24,x1=250,bot=346):
    box(dd,x0,wl,x1-x0,bot-wl,fill=WATER)
    for i in range(0,x1-x0,16):
        yy=wl+3+((i//16)%2)*5; box(dd,x0+i+4,yy,10,2,fill=WATER2)
    box(dd,x0,wl,x1-x0,3,fill=WSURF)
    for k in range(5):
        xx=x0+((k*53+t*14)%(x1-x0-12)); box(dd,xx,wl-2,10,2,fill=WSURF)
def shore(dd,wl,orig=None,hl=False,mark=True):
    box(dd,250,150,62,196,fill=SAND); box(dd,250,150,62,4,fill=SANDD)
    box(dd,262,122,26,222,fill=CREAM,border=(GOLD if hl else DARK),bw=(3 if hl else 2))
    for i in range(14):
        yy=130+i*15; w=14 if i%2==0 else 8; box(dd,262+26-w-2,yy,w,2,fill=DARK)
    if orig is not None: box(dd,24,orig,226,1.5,fill=GOLD)
    if mark:
        dd.polygon([(256*S,wl*S),(266*S,(wl-6)*S),(266*S,(wl+6)*S)],fill=CORAL)
def stone(dd,cx,cy,k=1.0,lab=None):
    pts=[(-16,6),(-12,-6),(-3,-11),(8,-10),(15,-2),(16,6),(8,10),(-8,10)]
    dd.polygon([((cx+x*k)*S,(cy+y*k)*S) for x,y in pts],fill=STONED)
    pts2=[(-14,4),(-10,-5),(-2,-9),(7,-8),(13,-2),(14,4),(6,8),(-7,8)]
    dd.polygon([((cx+x*k-1)*S,(cy+y*k-1)*S) for x,y in pts2],fill=STONE)
    box(dd,cx-7*k,cy-6*k,8*k,3*k,fill=STONEL); box(dd,cx+3*k,cy-1*k,5*k,2*k,fill=STONEL)
    if lab: T(dd,lab,cx,cy-4,12,'press',9,DARK,align='c')
def boat(dd,cx,wl,t,sink=0.0,bob=True):
    y=wl+(math.sin(t*2)*1.3 if bob else 0)+sink-3   # y = niveau de la ligne de flottaison
    top=y-18
    for i in range(30):
        yy=top+i; half=50-16*(i/30.0); sub=yy>=wl
        c=lerpc(WOODD,WATER,0.55) if sub else WOODD
        box(dd,cx-half,yy,2*half,1.2,fill=c)
    box(dd,cx-52,top-2,104,4,fill=WOOD,border=DARK,bw=1)
    box(dd,cx-40,top+11,80,2,fill=lerpc(WOODD,(0,0,0),0.25))
    box(dd,cx-52,wl,104,2,fill=WSURF)
    return top
def lake(dd,t,wl,orig=None,hl=False,mark=True):
    water(dd,wl,t); shore(dd,wl,orig,hl,mark)
def arrow_down(dd,x,y,col=CORAL,k=7,h=22):
    box(dd,x-3,y,6,h,fill=col); dd.polygon([((x-k)*S,(y+h)*S),((x+k)*S,(y+h)*S),(x*S,(y+h+k+3)*S)],fill=col)
def arrow_up(dd,x,y,col=CORAL,k=7,h=22):
    box(dd,x-3,y+k+3,6,h,fill=col); dd.polygon([((x-k)*S,(y+k+3)*S),((x+k)*S,(y+k+3)*S),(x*S,y*S)],fill=col)
def cube(dd,cx,by,s,col=WATER2,lab=None,lcol=CREAM,edge=WSURF):
    box(dd,cx-s/2,by-s,s,s,fill=col,border=edge,bw=2)
    if lab: T(dd,lab,cx,by-s/2-6,12,'press',9,lcol,align='c')
def balance(dd,cx,y,tilt,left,right):
    """tilt>0 : côté gauche plus bas. left/right : fonctions (cx,cy) dessinant le contenu posé sur le plateau"""
    box(dd,cx-6,y+10,12,110,fill=STEEL); box(dd,cx-34,y+118,68,8,fill=STEEL,border=DARK,bw=2)
    dy=tilt*16; L=(cx-80,y+dy); R=(cx+80,y-dy)
    dd.line([(L[0]*S,L[1]*S),(R[0]*S,R[1]*S)],fill=STEEL,width=5*S)
    disc(dd,cx,y,6,GOLD,DARK,2)
    for (px,py),fn in ((L,left),(R,right)):
        dd.line([((px-34)*S,(py+36)*S),(px*S,py*S)],fill=STEEL,width=2*S); dd.line([((px+34)*S,(py+36)*S),(px*S,py*S)],fill=STEEL,width=2*S)
        box(dd,px-38,py+36,76,6,fill=STEEL,border=DARK,bw=2)
        fn(px,py+36)
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            lake(dd,t,WL0); b=boat(dd,120,WL0,t); insp(dd,96,b,t,k=1.4); stone(dd,150,b-8,1.0)
            T(dd,'?',SW/2-20,100,40,'press',32,GOLD,align='c',shadow=(3,3,BLACK)); tagc(dd,SW/2,364,'LE NIVEAU DU LAC',GOLD)
        elif key=='s2':
            lake(dd,t,WL0); b=boat(dd,128,WL0,t); insp(dd,128,b,t,k=2.2); tagc(dd,SW/2,364,'SEUL, AU MILIEU DU LAC',CYAN)
        elif key=='s3':
            lake(dd,t,WL0+4,mark=False); b=boat(dd,128,WL0+4,t,sink=3); insp(dd,86,b,t,k=1.5); stone(dd,156,b-18,1.9)
            lbl(dd,SW/2-20,128,'UNE ÉNORME PIERRE',CORAL,11); tagc(dd,SW/2,364,'UNE ÉNORME PIERRE À BORD',CORAL)
        elif key=='s4':
            lake(dd,t,WL0,hl=(int(t*3)%2==0)); b=boat(dd,110,WL0,t); insp(dd,86,b,t,k=1.3); stone(dd,134,b-9,1.0)
            lbl(dd,208,104,'LA RÈGLE',CYAN,10); tagc(dd,SW/2,364,'UNE RÈGLE GRADUÉE SUR LA RIVE',CYAN)
        elif key=='s5':
            p=min(1,lt/(dur*0.8)); sx=150+p*72
            lake(dd,t,WL0); b=boat(dd,120,WL0,t); insp(dd,86,b,t,k=1.5); stone(dd,sx,b-9-(math.sin(p*math.pi)*10),1.0)
            T(dd,'>>>',190,110,18,'press',14,CORAL,align='c'); tagc(dd,SW/2,364,'IL POUSSE LA PIERRE',CORAL)
        elif key=='s6':
            p=min(1,lt/(dur*0.85)); wl=WL0
            lake(dd,t,wl,mark=True); b=boat(dd,100,wl,t); insp(dd,76,b,t,k=1.5)
            sy=(wl-24)+p*(330-(wl-24)); sx=222
            stone(dd,sx,sy,1.0)
            if lt<0.9:
                for i in range(7): a=i*0.6+0.3; box(dd,sx+math.cos(a*2)*(10+lt*40),wl-4-abs(math.sin(a))*(12+lt*30),4,4,fill=WSURF)
            if lt>0.1 and p<0.7: stamp(dd,SW/2-30,150,'PLOUF !',GOLD,16)
            for i in range(3): box(dd,sx-6+i*6,sy-14-((t*30+i*17)%22),3,3,fill=WSURF) if sy>wl+10 else None
            tagc(dd,SW/2,364,'ELLE COULE TOUT AU FOND',CYAN)
        elif key=='s7':
            lake(dd,t,WL0,orig=None,mark=False); b=boat(dd,100,WL0,t); insp(dd,76,b,t,k=1.5); stone(dd,206,338,1.0)
            T(dd,'?',SW/2-6,104,52,'press',44,GOLD,align='c',shadow=(4,4,BLACK))
            dd.polygon([(256*S,WL0*S),(266*S,(WL0-6)*S),(266*S,(WL0+6)*S)],fill=GOLD); tagc(dd,SW/2,364,'ET LE NIVEAU DU LAC ?',GOLD)
        elif key=='q':
            opts=[('MONTE',CORAL,'▲'),('DESCEND',CYAN,'▼'),('NE BOUGE PAS',GOLD,'=')]
            for i,(lab,col,ic) in enumerate(opts):
                y=112+i*70; on=(int(t*1.4)%3==i)
                box(dd,36,y,240,56,fill=CARD,border=col,bw=(4 if on else 2),shadow=(3,3,BLACK))
                if ic=='▲': dd.polygon([(60*S,(y+40)*S),(84*S,(y+40)*S),(72*S,(y+14)*S)],fill=col)
                elif ic=='▼': dd.polygon([(60*S,(y+14)*S),(84*S,(y+14)*S),(72*S,(y+40)*S)],fill=col)
                else: box(dd,60,y+18,24,5,fill=col); box(dd,60,y+30,24,5,fill=col)
                T(dd,lab,184,y+20,18,'press',14,col,align='c')
            tagc(dd,SW/2,364,'MONTE, DESCEND OU RESTE ?',CORAL)
        elif key=='r0':
            lake(dd,t,WL1,orig=WL0); b=boat(dd,100,WL1,t); insp(dd,76,b,t,k=1.5); stone(dd,206,338,1.0)
            arrow_down(dd,224,WL0-34,GRN,h=18); lbl(dd,130,150,'TRAIT DORÉ = AVANT',GOLD,10)
            tagc(dd,SW/2,364,'LE NIVEAU DU LAC BAISSE',GRN)
        elif key=='r1':
            lake(dd,t,WL0,mark=False); b=boat(dd,128,WL0,t); insp(dd,86,b,t,k=1.4); stone(dd,158,b-8,1.0)
            arrow_down(dd,158,b-86,CORAL,h=34); T(dd,'POIDS',158,b-108,16,'silk7',11,CORAL,align='c',sp=1)
            tagc(dd,SW/2,364,'LA PIERRE PÈSE SUR LA BARQUE',CORAL)
        elif key=='r2':
            p=min(1,lt/(dur*0.6)); wl=WL0; b=boat(dd,128,wl,t,sink=4*p,bob=False) if False else None
            lake(dd,t,wl,mark=False); b=boat(dd,128,wl,t,sink=10*p); insp(dd,86,b,t,k=1.4); stone(dd,158,b-8,1.0)
            hh=int(8+22*p); box(dd,82,wl+8,92,hh+14,fill=VOL,border=CYAN,bw=2) ; lbl(dd,128,wl+hh+30,'EAU POUSSÉE',CYAN,10)
            arrow_down(dd,128,wl-12-20,CORAL,h=0,k=0) if False else None
            tagc(dd,SW/2,364,'ELLE POUSSE DE L’EAU',CYAN)
        elif key=='r3':
            balance(dd,SW/2,150,0.0,lambda x,y:stone(dd,x,y-12,0.9),lambda x,y:cube(dd,x,y,28,lab=None))
            lbl(dd,SW/2-80,252,'PIERRE',STONEL,10); lbl(dd,SW/2+80,252,'EAU POUSSÉE',CYAN,10)
            T(dd,'=',SW/2,106,36,'press',30,GOLD,align='c',shadow=(3,3,BLACK)); tagc(dd,SW/2,364,'MÊME POIDS',GOLD)
        elif key=='r4':
            tl=min(1,lt/0.6)
            balance(dd,SW/2,150,0.9*tl,lambda x,y:cube(dd,x,y,34,col=STONE,edge=STONEL),lambda x,y:cube(dd,x,y,34))
            lbl(dd,SW/2-80,252,'PIERRE',STONEL,10); lbl(dd,SW/2+80,252,'EAU',CYAN,10)
            lbl(dd,SW/2,96,'MÊME VOLUME',GOLD,11); tagc(dd,SW/2,364,'À VOLUME ÉGAL : PIERRE PLUS LOURDE',RED) if False else tagc(dd,SW/2,364,'LA PIERRE EST PLUS LOURDE',RED)
        elif key=='r5':
            tl=min(1,lt/0.6)
            balance(dd,SW/2,150,0.0,lambda x,y:cube(dd,x,y,24,col=STONE,edge=STONEL),lambda x,y:cube(dd,x,y,56))
            lbl(dd,SW/2-80,252,'PIERRE',STONEL,10); lbl(dd,SW/2+80,252,'EAU',CYAN,10)
            T(dd,'=',SW/2,106,36,'press',30,GOLD,align='c',shadow=(3,3,BLACK)); tagc(dd,SW/2,364,'BEAUCOUP PLUS D’EAU',CYAN)
        elif key=='r6':
            stone(dd,SW/2,196,3.4); T(dd,'1000 KG',SW/2,232,28,'press',20,GOLD,align='c',shadow=(3,3,BLACK)) if False else None
            stamp(dd,SW/2,290,'1000 KG',GOLD,18); tagc(dd,SW/2,364,'UNE PIERRE DE MILLE KILOS',GOLD)
        elif key=='r7':
            wl=WL0; lake(dd,t,wl,mark=False); b=boat(dd,128,wl,t,sink=14); insp(dd,86,b,t,k=1.4); stone(dd,158,b-8,1.0)
            box(dd,66,wl+10,124,74,fill=VOL,border=CYAN,bw=2); T(dd,'1000 L',128,wl+36,24,'press',18,CREAM,align='c',shadow=(2,2,BLACK))
            tagc(dd,SW/2,364,'DANS LA BARQUE : 1000 LITRES',CYAN)
        elif key=='r8':
            wl=WL1; lake(dd,t,wl,orig=WL0,mark=False); b=boat(dd,92,wl,t); insp(dd,68,b,t,k=1.4)
            stone(dd,206,326,1.0); box(dd,172,292,68,50,fill=VOL,border=CYAN,bw=2); T(dd,'370 L',206,299,16,'press',12,CREAM,align='c',shadow=(2,2,BLACK)); stone(dd,206,330,0.7)
            tagc(dd,SW/2,364,'AU FOND : SEULEMENT 370 L',RED)
        elif key=='r9':
            lake(dd,t,WL1,orig=WL0); b=boat(dd,100,WL1,t); insp(dd,76,b,t,k=1.5); stone(dd,206,338,1.0)
            arrow_down(dd,224,WL0-34,GRN,h=18); stamp(dd,SW/2-6,150,'LE NIVEAU BAISSE',GRN,12); star(dd,40,118,t,4)
            tagc(dd,SW/2,364,'LA RÉPONSE : ÇA DESCEND !',GRN)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#035'
    def fn(lay,dd):
        water(dd,236,t,x0=24,x1=288,bot=300); b=boat(dd,156,236,t); insp(dd,126,b,t,k=1.4); stone(dd,192,b-9,1.1)
        arrow_down(dd,60,180,GRN,h=14); arrow_up(dd,252,180,CORAL,h=14)
        T(dd,'UNE PIERRE À L’EAU',SW/2,70,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'LE LAC MONTE ?',SW/2,106,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DE LA BARQUE"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#036')
