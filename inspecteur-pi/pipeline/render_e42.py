from render_e4x import *
B.NUM='#042'
def cand(dd,cx,feet,t,pal,k=3.0,still=False):
    sprite(dd,MAN,pal,cx-5*k,feet-14*k+(0 if still else math.sin(t*3+cx)*1.2),k,10)
def grid(dd,n_dim=0,gold=None,cyan_from=None,y0=94,sp=26,x0=36):
    for idx in range(100):
        r,c=divmod(idx,10)
        col=ORG
        if idx<n_dim: col=DIM
        if cyan_from is not None and idx>=cyan_from: col=CYAN
        icon(dd,x0+c*sp,y0+r*22,col,hl=(GOLD if idx==gold else None))
SILP={k:'#0B0D14' for k in 'KSsTPB'}; SILP.update({'E':'#FFD23F'})
HEADS={'s1':[('100 ',GOLD),('candidats',CREAM)],
 's2':[('L’inspecteur cherche un ',CREAM),('assistant',GOLD)],
 's3':[('Ils passent ',CREAM),('un par un',CORAL)],
 's4':[('Dans un ordre ',CREAM),('aléatoire',CYAN)],
 's5':[('Après chaque entretien : ',CREAM),('oui ou non',GOLD)],
 's6':[('Un refus est ',CREAM),('définitif',RED)],
 's7':[('Dès qu’il dit ',CREAM),('oui',GRN),(' : fini',CREAM)],
 's8':[('Il compare avec les ',CREAM),('déjà vus',CYAN)],
 's9':[('Mais pas ceux qui ',CREAM),('arrivent après',CORAL)],
 's10':[('Au hasard : ',CREAM),('1 chance sur 100',RED)],
 'q':[('Quelle ',CREAM),('stratégie',CORAL),(' ?',CREAM)],
 'r0':[('La ',CREAM),('réponse',GOLD)],
 'r1':[('Refuser les ',CREAM),('37 premiers',CORAL)],
 'r2':[('Quoi qu’il ',CREAM),('arrive',RED)],
 'r3':[('Retenir le ',CREAM),('meilleur',GOLD),(' d’entre eux',CREAM)],
 'r4':[('Ensuite : ',CREAM),('les suivants',CYAN)],
 'r5':[('Le ',CREAM),('premier',GOLD),(' qui ',CREAM),('bat tous',GRN)],
 'r6':[('Réussite : ',CREAM),('37 %',GRN)],
 'r7':[('Contre ',CREAM),('1 %',RED),(' au hasard',CREAM)],
 'r8':[('Pourquoi ',CREAM),('37',GOLD),(' ?',CREAM)],
 'r9':[('100 divisé par ',CREAM),('2,718',GOLD)],
 'r10':[('Refuser ',CREAM),('trop peu',RED)],
 'r11':[('Refuser ',CREAM),('trop',RED),(' : trop tard',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','q')
def row20(dd,n_dim,pick=None,best=None,y=210):
    for i in range(20):
        x=16+i*14.2
        col=DIM if i<n_dim else CREAM
        if best is not None and i==best: col=GOLD
        if pick is not None and i==pick: col=GRN
        box(dd,x,y,11,30,fill=col,border=DARK,bw=1)
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            n=min(100,int(lt*55)); 
            for idx in range(n):
                r,c=divmod(idx,10); icon(dd,36+c*26,112+r*22,ORG,hl=(GOLD if (idx==63 and lt>2.0) else None))
            tagc(dd,cx,364,'UNE SEULE CHANCE',GOLD)
        elif key=='s2':
            sprite(dd,DET,DPAL,50,GY-20-24*4.2+math.sin(t*4)*1.5,4.2,20)
            box(dd,150,130,140,118,fill=CARD,border=GOLD,bw=3,shadow=(4,4,BLACK)); T(dd,'ASSISTANT',220,150,16,'press',11,GOLD,align='c'); T(dd,'RECHERCHÉ',220,176,16,'press',11,CREAM,align='c'); T(dd,'?',220,200,40,'press',32,CORAL,align='c')
            tagc(dd,cx,364,'IL CHERCHE UN ASSISTANT',GOLD)
        elif key=='s3':
            sprite(dd,DET,DPAL,230,GY-20-24*3.4,3.4,20)
            for i in range(5):
                x=40+i*44-((t*14)%44)
                if x>40: pass
                cand(dd,x+20,GY-20,t,CANDP[i%6],3.0)
            lbl(dd,110,124,'LA FILE D’ATTENTE',CYAN,9); tagc(dd,cx,364,'ILS PASSENT UN PAR UN',CORAL)
        elif key=='s4':
            seq=[5,2,8,1,7,3,6,4]; import random as rd; rr=rd.Random(int(t*2)); rr.shuffle(seq)
            for i,v in enumerate(seq):
                x=22+(i%4)*72; y=140+(i//4)*84
                box(dd,x,y,60,70,fill=CARD,border=[CORAL,CYAN,GOLD,GRN][i%4],bw=3,shadow=(3,3,BLACK)); T(dd,str(v),x+30,y+20,36,'press',28,CREAM,align='c')
            stamp(dd,cx,326,'ORDRE ALÉATOIRE',CYAN,11); tagc(dd,cx,364,'DANS UN ORDRE ALÉATOIRE',CYAN)
        elif key=='s5':
            sprite(dd,DET,DPAL,100,GY-20-24*3.2+math.sin(t*4)*1.5,3.2,20)
            box(dd,22,150,120,60,fill=GRN,border=DARK,bw=3,shadow=(3,3,BLACK)); T(dd,'OUI',82,166,30,'press',22,DARK,align='c')
            box(dd,170,150,120,60,fill=RED,border=DARK,bw=3,shadow=(3,3,BLACK)); T(dd,'NON',230,166,30,'press',22,DARK,align='c')
            lbl(dd,cx,118,'TOUT DE SUITE',GOLD,10); tagc(dd,cx,364,'OUI OU NON TOUT DE SUITE',GOLD)
        elif key=='s6':
            cand(dd,96,GY-20,t,CANDP[0],4.4,still=True); xmark_(dd,96,206,32,8,RED)
            stamp(dd,226,200,'NON',RED,22); stamp(dd,226,270,'ADIEU',RED,12); tagc(dd,cx,364,'UN REFUS EST DÉFINITIF',RED)
        elif key=='s7':
            for i in range(3): cand(dd,60+i*86,GY-20,t,dict(CANDP[i+1],T='#3A4270'),3.0,still=True)
            cand(dd,156,GY-26,t,CANDP[1],4.6); check(dd,156,196,24,7,GRN); stamp(dd,cx,128,'OUI = FIN',GRN,13); tagc(dd,cx,364,'DÈS QU’IL DIT OUI C’EST TERMINÉ',GRN)
        elif key=='s8':
            lbl(dd,100,122,'DÉJÀ VUS',CYAN,10)
            for i in range(3): cand(dd,36+i*52,GY-60,t,CANDP[i],2.8,still=True)
            cand(dd,250,GY-20,t,CANDP[4],4.2)
            arrow_r(dd,176,250,40,CYAN); lbl(dd,250,122,'CELUI-CI',GOLD,10); tagc(dd,cx,364,'IL COMPARE AVEC LES DÉJÀ VUS',CYAN)
        elif key=='s9':
            for i in range(4): 
                cand(dd,50+i*70,GY-20,t,SILP,3.2,still=True); T(dd,'?',50+i*70,170,40,'press',30,GOLD,align='c',shadow=(3,3,BLACK))
            lbl(dd,cx,118,'PAS ENCORE VUS',CORAL,10); tagc(dd,cx,364,'IL NE CONNAÎT PAS CEUX D’APRÈS',CORAL)
        elif key=='s10':
            T(dd,'1/100',cx,170,60,'press',50,RED,align='c',shadow=(5,5,BLACK)); stamp(dd,cx,290,'1 CHANCE SUR 100',RED,12); tagc(dd,cx,364,'CHOISIR AU HASARD',RED)
        elif key=='q':
            sprite(dd,DET,DPAL,24,GY-20-24*3.6+math.sin(t*4)*1.5,3.6,20)
            T(dd,'?',226,128,110,'press',90,GOLD,align='c',shadow=(5,5,BLACK)); stamp(dd,226,290,'LAQUELLE ?',CORAL,10); tagc(dd,cx,364,'QUELLE STRATÉGIE ?',CORAL)
        elif key=='r0':
            T(dd,'!',cx,150,150,'press',120,GOLD,align='c',shadow=(7,7,BLACK)); star(dd,50,200,t,6); star(dd,262,200,t+1,6); stamp(dd,cx,320,'LA STRATÉGIE',GOLD,12); tagc(dd,cx,364,'LA RÉPONSE',GOLD)
        elif key=='r1':
            n=min(37,int(lt/dur*37*1.5)+1); grid(dd,n_dim=n)
            tagc(dd,cx,364,'REFUSER LES 37 PREMIERS',CORAL)
        elif key=='r2':
            grid(dd,n_dim=37); stamp(dd,cx,326,'TOUS REFUSÉS',RED,12); tagc(dd,cx,364,'QUOI QU’IL ARRIVE',RED)
        elif key=='r3':
            grid(dd,n_dim=37,gold=21); lbl(dd,cx,324,'LE MEILLEUR DES 37',GOLD,10); tagc(dd,cx,364,'LE MEILLEUR D’ENTRE EUX',GOLD)
        elif key=='r4':
            grid(dd,n_dim=37,gold=21,cyan_from=37); lbl(dd,cx,324,'LES SUIVANTS',CYAN,10); tagc(dd,cx,364,'ENSUITE LES SUIVANTS',CYAN)
        elif key=='r5':
            base=316
            box(dd,26,base,262,4,fill=EDGE)
            hs=[70,96,62,160]; cols=[DIM,DIM,DIM,GRN]
            for i,h in enumerate(hs): box(dd,52+i*58,base-h,40,h,fill=cols[i],border=DARK,bw=2)
            for i in range(24): box(dd,26+i*11,base-120,6,3,fill=GOLD)
            lbl(dd,80,base-150,'RECORD',GOLD,9); stamp(dd,52+3*58+20,base-186,'OUI !',GRN,12); tagc(dd,cx,364,'LE PREMIER QUI BAT LE RECORD',GRN)
        elif key in ('r6','r7'):
            barrow(dd,0,'NOTRE MÉTHODE','37 %',0.37,GRN,hl=True)
            if key=='r7': barrow(dd,1,'AU HASARD','1 %',0.01,RED)
            T(dd,'37 %',cx,230,50,'press',40,GRN,align='c',shadow=(4,4,BLACK))
            tagc(dd,cx,364,'37 % CONTRE 1 %' if key=='r7' else 'RÉUSSITE : 37 %',GRN if key=='r6' else GOLD)
        elif key=='r8':
            T(dd,'37',cx-34,150,110,'press',86,GOLD,align='c',shadow=(6,6,BLACK)); T(dd,'?',cx+84,150,110,'press',86,CORAL,align='c',shadow=(6,6,BLACK)); tagc(dd,cx,364,'POURQUOI 37 ?',GOLD)
        elif key=='r9':
            T(dd,'100',cx,126,40,'press',34,CREAM,align='c',shadow=(3,3,BLACK)); vline(dd,70,SW-70,176,GOLD); T(dd,'2,718',cx,190,34,'press',30,CYAN,align='c',shadow=(3,3,BLACK))
            T(dd,'= 37',cx,246,50,'press',40,GOLD,align='c',shadow=(4,4,BLACK))
            if lt>2.9: lbl(dd,cx,318,'UN NOMBRE CÉLÈBRE',CYAN,10)
            tagc(dd,cx,364,'ENVIRON 100 DIVISÉ PAR 2,718',GOLD)
        elif key=='r10':
            row20(dd,5,pick=5); lbl(dd,cx,150,'TROP PEU REFUSÉ',RED,10); stamp(dd,cx,290,'CHOISI TROP VITE',RED,11); tagc(dd,cx,364,'TU CHOISIS TROP VITE',RED)
        elif key=='r11':
            row20(dd,17,best=7); lbl(dd,cx,150,'LE MEILLEUR EST DÉJÀ PASSÉ',GOLD,9); stamp(dd,cx,290,'TROP TARD',RED,13); tagc(dd,cx,364,'LE MEILLEUR EST DÉJÀ PASSÉ',RED)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#042'
    def fn(lay,dd):
        for idx in range(100):
            r,c=divmod(idx,10); icon(dd,36+c*26,112+r*22,ORG,hl=(GOLD if idx==63 else None))
        T(dd,'100 CANDIDATS,',SW/2,16,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'UNE SEULE CHANCE',SW/2,52,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DES CENT CANDIDATS"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#043')
