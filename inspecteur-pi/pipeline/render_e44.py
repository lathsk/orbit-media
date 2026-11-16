from render_e4x import *
B.NUM='#044'
def digits(dd,cx,y,s,size=22,cols=None,cross=None,hide=None,dim=()):
    n=len(s); w=size+14; gap=8; x0=cx-(n*w+(n-1)*gap)/2
    for i,ch in enumerate(s):
        x=x0+i*(w+gap); col=(cols[i] if cols else CREAM)
        if i in dim: col=DIM
        box(dd,x,y,w,w+14,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK))
        if hide is not None and i==hide: T(dd,'?',x+w/2,y+9,size+6,'press',size,GOLD,align='c')
        else: T(dd,ch,x+w/2,y+9,size+6,'press',size,col,align='c')
        if cross is not None and i==cross: xmark_(dd,x+w/2,y+(w+14)/2,w*0.55,5,RED)
    return x0
def eq(dd,a,b,res,y0=118,size=20,hide=False):
    digits(dd,SW/2+8,y0,a,size,[GOLD]*len(a)); digits(dd,SW/2+8,y0+66,b,size,[CYAN]*len(b))
    minus(dd,26,y0+66+24,26); vline(dd,54,SW-20,y0+66+66)
    if hide: digits(dd,SW/2+8,y0+66+78,res,size,[CORAL]*len(res),hide=None) 
    else: digits(dd,SW/2+8,y0+66+78,res,size,[CORAL]*len(res))
HEADS={'s1':[('L’inspecteur lit dans ',CREAM),('tes pensées',GOLD)],
 's2':[('Un nombre à ',CREAM),('4 chiffres',GOLD)],
 's3':[('On ',CREAM),('mélange',CORAL),(' ses chiffres',CREAM)],
 's4':[('Grand ',CREAM),('moins',CORAL),(' petit',CREAM)],
 's5':[('On ',CREAM),('barre',RED),(' un chiffre',CREAM)],
 's6':[('Mais ',CREAM),('pas un zéro',RED)],
 's7':[('On donne les chiffres ',CREAM),('restants',CYAN)],
 's8':[('Il devine ',CREAM),('aussitôt',GOLD)],
 'q':[('Comment ',CREAM),('fait-il',CORAL),(' ?',CREAM)],
 'r0':[('Le ',CREAM),('secret',GOLD)],
 'r1':[('Toujours un multiple de ',CREAM),('9',GOLD)],
 'r2':[('On mélange les ',CREAM),('chiffres',CORAL)],
 'r3':[('La différence : ',CREAM),('divisible par 9',GOLD)],
 'r4':[('Les multiples de ',CREAM),('9',GOLD)],
 'r5':[('Somme des chiffres : ',CREAM),('multiple de 9',GOLD)],
 'r6':[('Exemple : ',CREAM),('6483 - 3864',CYAN)],
 'r7':[('Ça fait ',CREAM),('2619',CORAL)],
 'r8':[('Il barre le ',CREAM),('6',RED)],
 'r9':[('Il reste ',CREAM),('2, 1 et 9',CYAN)],
 'r10':[('Pour arriver à ',CREAM),('18',GOLD)],
 'r11':[('Il complète : ',CREAM),('+ 6',GRN)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            sprite(dd,DET,DPAL,40,GY-20-24*4.2+math.sin(t*4)*1.5,4.2,20)
            box(dd,160,128,130,100,fill=CARD,border=GOLD,bw=3,shadow=(4,4,BLACK)); T(dd,'?!',225,150,50,'press',40,GOLD,align='c')
            for i in range(3): disc(dd,150-i*12,236+i*10,5-i,CREAM)
            tagc(dd,cx,364,'IL LIT DANS TES PENSÉES',GOLD)
        elif key=='s2':
            digits(dd,cx,170,'6483',28,[GOLD]*4); tagc(dd,cx,364,'UN NOMBRE À QUATRE CHIFFRES',GOLD)
        elif key=='s3':
            digits(dd,cx,128,'6483',22,[GOLD]*4); arrow_d(dd,cx,206,36,CORAL); digits(dd,cx,252,'3864',22,[CYAN]*4)
            lbl(dd,cx+90,214,'MÉLANGE',CORAL,9); tagc(dd,cx,364,'ON MÉLANGE LES CHIFFRES',CORAL)
        elif key=='s4':
            eq(dd,'6483','3864','????',y0=112,size=20); tagc(dd,cx,364,'LE GRAND MOINS LE PETIT',CORAL)
        elif key=='s5':
            digits(dd,cx,160,'2619',28,[CREAM]*4,cross=(1 if lt>0.6 else None)); tagc(dd,cx,364,'ON BARRE UN CHIFFRE',RED)
        elif key=='s6':
            T(dd,'0',cx,150,100,'press',80,CREAM,align='c',shadow=(6,6,BLACK)); xmark_(dd,cx,196,46,6,RED); stamp(dd,cx,300,'PAS UN ZÉRO',RED,13); tagc(dd,cx,364,'MAIS PAS UN ZÉRO',RED)
        elif key=='s7':
            digits(dd,cx-30,150,'219',26,[CYAN]*3); box(dd,SW-72,150,52,66,fill=CARD,border=DIM,bw=3); T(dd,'?',SW-46,162,40,'press',30,DIM,align='c')
            lbl(dd,cx-30,244,'CHIFFRES ANNONCÉS',CYAN,9); tagc(dd,cx,364,'ON DONNE LES CHIFFRES RESTANTS',CYAN)
        elif key=='s8':
            sprite(dd,DET,DPAL,40,GY-20-24*4.2+math.sin(t*4)*1.5,4.2,20)
            T(dd,'?',226,130,110,'press',90,GOLD,align='c',shadow=(5,5,BLACK)); star(dd,262,110,t,6); star(dd,170,240,t+1,5); tagc(dd,cx,364,'IL DEVINE AUSSITÔT',GOLD)
        elif key=='q':
            sprite(dd,DET,DPAL,24,GY-20-24*3.6+math.sin(t*4)*1.5,3.6,20)
            T(dd,'?',226,128,110,'press',90,GOLD,align='c',shadow=(5,5,BLACK)); stamp(dd,226,290,'COMMENT ?',CORAL,10); tagc(dd,cx,364,'COMMENT FAIT-IL ?',CORAL)
        elif key=='r0':
            T(dd,'!',cx,150,150,'press',120,GOLD,align='c',shadow=(7,7,BLACK)); star(dd,50,200,t,6); star(dd,262,200,t+1,6); stamp(dd,cx,320,'LE SECRET',GOLD,12); tagc(dd,cx,364,'LA RÉPONSE',GOLD)
        elif key=='r1':
            T(dd,'× 9',cx,150,110,'press',86,GOLD,align='c',shadow=(6,6,BLACK)); stamp(dd,cx,300,'2619 = 9 × 291',CYAN,10); tagc(dd,cx,364,'TOUJOURS UN MULTIPLE DE 9',GOLD)
        elif key=='r2':
            digits(dd,cx,128,'6483',22,[GOLD]*4); arrow_d(dd,cx,206,36,CORAL); digits(dd,cx,252,'3864',22,[CYAN]*4); tagc(dd,cx,364,'ON MÉLANGE LES CHIFFRES',CORAL)
        elif key=='r3':
            T(dd,'2619',cx,130,40,'press',32,CORAL,align='c',shadow=(3,3,BLACK)); vline(dd,70,SW-70,184,GOLD)
            T(dd,'= 9 × 291',cx,200,34,'press',24,CYAN,align='c',shadow=(3,3,BLACK)); check(dd,cx,290,26,8,GRN); tagc(dd,cx,364,'LA DIFFÉRENCE EST DIVISIBLE PAR 9',GOLD)
        elif key=='r4':
            for i,v in enumerate(('9','18','27','36','45')):
                numcard(dd,cx,112+i*48,v,[CREAM,CYAN,CORAL,GOLD,GRN][i],14)
            tagc(dd,cx,364,'UN MULTIPLE DE 9',GOLD)
        elif key=='r5':
            T(dd,'2+6+1+9',cx,140,40,'press',30,CREAM,align='c',shadow=(3,3,BLACK)); vline(dd,70,SW-70,196,GOLD)
            T(dd,'= 18',cx,214,60,'press',46,GOLD,align='c',shadow=(5,5,BLACK)); lbl(dd,cx,300,'18 = 2 × 9',CYAN,10); tagc(dd,cx,364,'SOMME DES CHIFFRES : MULTIPLE DE 9',GOLD)
        elif key=='r6':
            eq(dd,'6483','3864','????',y0=112,size=20); tagc(dd,cx,364,'SIX MILLE QUATRE CENT QUATRE-VINGT-TROIS...' if False else 'UN EXEMPLE',CYAN)
        elif key=='r7':
            eq(dd,'6483','3864','2619',y0=112,size=20); tagc(dd,cx,364,'ÇA FAIT 2619',CORAL)
        elif key=='r8':
            digits(dd,cx,150,'2619',28,[CREAM]*4,cross=(1 if lt>0.5 else None)); lbl(dd,cx,260,'ON BARRE LE 6',RED,10); tagc(dd,cx,364,'IL BARRE LE 6',RED)
        elif key=='r9':
            digits(dd,cx-30,130,'219',26,[CYAN]*3); box(dd,SW-72,130,52,66,fill=CARD,border=DIM,bw=3); T(dd,'?',SW-46,142,40,'press',30,DIM,align='c')
            if lt>1.0:
                vline(dd,70,SW-70,236,GOLD); T(dd,'2+1+9 = 12',cx,254,34,'press',24,GOLD,align='c',shadow=(3,3,BLACK))
            tagc(dd,cx,364,'IL RESTE 2, 1 ET 9 : TOTAL 12',CYAN)
        elif key=='r10':
            T(dd,'12',72,150,70,'press',54,CYAN,align='c',shadow=(4,4,BLACK)); arrow_r(dd,120,180,70,GOLD); T(dd,'18',250,150,70,'press',54,GOLD,align='c',shadow=(4,4,BLACK))
            stamp(dd,cx,270,('IL MANQUE 6' if lt>1.2 else 'IL MANQUE ?'),(GRN if lt>1.2 else CORAL),12); tagc(dd,cx,364,'POUR ARRIVER À 18',GOLD)
        elif key=='r11':
            T(dd,'12 + 6 = 18',cx,128,40,'press',26,CREAM,align='c',shadow=(3,3,BLACK))
            digits(dd,cx,190,'6',40,[GRN]); stamp(dd,cx,320,'LE CHIFFRE BARRÉ',GRN,11); tagc(dd,cx,364,'JUSQU’AU MULTIPLE DE 9 SUIVANT',GRN)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#044'
    def fn(lay,dd):
        digits(dd,SW/2,150,'2619',34,[CREAM]*4,cross=1)
        T(dd,'?',SW/2,250,100,'press',80,GOLD,align='c',shadow=(5,5,BLACK))
        T(dd,'JE DEVINE TON',SW/2,16,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'CHIFFRE BARRÉ',SW/2,52,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DU CHIFFRE BARRÉ"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#045')
