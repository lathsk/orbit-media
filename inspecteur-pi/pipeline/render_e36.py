from render_e2x import *
B.NUM='#036'
AMI=dict(MPAL); AMI.update({'T':'#3FBF7F','P':'#2A6B55','K':'#5A3A22'})
HEADS={'s1':[('Un ',CREAM),('café',GOLD),(' à payer',CREAM)],
 's2':[('Une pièce ',CREAM),('truquée',RED)],
 's3':[('Tirage ',CREAM),('équitable',GRN)],
 's4':[('Deux ',CREAM),('amis',GOLD),(' au café',CREAM)],
 's5':[('Une ',CREAM),('seule',GOLD),(' pièce',CREAM)],
 's6':[('Un côté ',CREAM),('sort plus',CORAL)],
 's7':[('Mais ',CREAM),('lequel ?',GOLD)],
 's8':[('Il choisit ',CREAM),('pile',GOLD)],
 's9':[('Il est ',CREAM),('désavantagé',RED)],
 's10':[('Comment ',CREAM),('faire ?',CORAL)],
 'q':[('Un tirage ',CREAM),('50 / 50 ?',GOLD)],
 'r0':[('Deux ',CREAM),('lancers',GOLD),(' de suite',CREAM)],
 'r1':[('Pile',GOLD),(' puis ',CREAM),('face',CYAN)],
 'r2':[('Face',CYAN),(' puis ',CREAM),('pile',GOLD)],
 'r3':[('Pareils : ',CREAM),('on recommence',CORAL)],
 'r4':[('Pourquoi ça ',CREAM),('marche ?',GOLD)],
 'r5':[('Pile : ',GOLD),('7 fois sur 10',CREAM)],
 'r6':[('Pile',GOLD),(' puis ',CREAM),('face',CYAN)],
 'r7':[('Face',CYAN),(' puis ',CREAM),('pile',GOLD)],
 'r8':[('Exactement ',CREAM),('pareil',GRN)],
 'r9':[('Même ',CREAM),('chance',GRN),(' pour tous',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','q')
def cup(dd,cx,cy,t,k=1.0):
    for i in range(3):
        yy=cy-34*k-((t*18+i*13)%26); box(dd,cx-12*k+i*12*k+math.sin(t*3+i)*2,yy,4*k,9*k,fill=rgb('#7A84B8'))
    box(dd,cx-30*k,cy+22*k,60*k,6*k,fill=rgb('#8A93C0'),border=DARK,bw=2)
    box(dd,cx-22*k,cy-22*k,44*k,44*k,fill=CREAM,border=DARK,bw=2); box(dd,cx-22*k,cy-22*k,44*k,10*k,fill=rgb('#5A3A22'),border=DARK,bw=1)
    box(dd,cx+22*k,cy-12*k,12*k,22*k,fill=None,border=CREAM,bw=4)
def person_pair(dd,t,k=2.6):
    insp(dd,78,GY,t,k=k); b=math.sin(t*3+1)*1.2; kk=k*1.65
    sprite(dd,MAN,AMI,234-5*kk,GY-14*kk+b,kk,10)
def coin_big(dd,cx,cy,r,ch,sq=1.0,ring=None): coin(dd,cx,cy,r,ch,squash=sq,ring=ring)
def prow(dd,y,seq,r=13,gap=29,hl=None,x0=None):
    n=len(seq); x0=SW/2-(n-1)*gap/2 if x0 is None else x0
    for i,c in enumerate(seq):
        coin(dd,x0+i*gap,y,r,c,ring=(GOLD if hl==i else None))
def frac(dd,cx,y,txt,col=CREAM,size=18):
    T(dd,txt,cx,y,size+6,'press',size,col,align='c',shadow=(2,2,BLACK))
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            cup(dd,SW/2,220,t,k=2.0); star(dd,52,150,t,4); tagc(dd,SW/2,364,'QUI PAIE LE CAFÉ ?',GOLD)
        elif key=='s2':
            sq=math.cos(t*3.0); coin_big(dd,SW/2,200,50,'P',sq=sq); stamp(dd,SW/2,300,'TRUQUÉE !',RED,16); tagc(dd,SW/2,364,'UNE PIÈCE TRUQUÉE',RED)
        elif key=='s3':
            for cx,col,ch in ((88,GOLD,'P'),(224,CYAN,'F')):
                box(dd,cx-58,150,116,100,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); frac(dd,cx,172,'50 %',col,20); coin(dd,cx,226,16,ch)
            stamp(dd,SW/2,296,'MÊME CHANCE',GRN,14); tagc(dd,SW/2,364,'UN TIRAGE ÉQUITABLE',GRN)
        elif key=='s4':
            person_pair(dd,t,k=2.6); cup(dd,78,150,t,k=0.8); cup(dd,234,150,t,k=0.8); tagc(dd,SW/2,364,'QUI VA PAYER ?',CORAL)
        elif key=='s5':
            table(dd,262); coin_big(dd,SW/2,222,32,'P'); lbl(dd,SW/2,130,'LA SEULE PIÈCE DISPONIBLE',CYAN,10)
            tagc(dd,SW/2,364,'UNE SEULE PIÈCE',CYAN)
        elif key=='s6':
            seq='PPFPPPFPPP'; n=min(len(seq),int(lt/dur*len(seq)*1.4)+1)
            for i in range(n): coin(dd,50+(i%5)*53,150+(i//5)*56,17,seq[i])
            lbl(dd,SW/2,290,'PLUS SOUVENT D’UN CÔTÉ',CORAL,10); tagc(dd,SW/2,364,'UN CÔTÉ TOMBE PLUS SOUVENT',CORAL)
        elif key=='s7':
            coin_big(dd,82,196,34,'P'); coin_big(dd,230,196,34,'F'); T(dd,'?',156,170,60,'press',48,GOLD,align='c',shadow=(4,4,BLACK))
            lbl(dd,82,252,'PILE ?',GOLD,11); lbl(dd,230,252,'FACE ?',CYAN,11); tagc(dd,SW/2,364,'PERSONNE NE SAIT LEQUEL',GOLD)
        elif key=='s8':
            insp(dd,86,GY,t,k=2.8); coin_big(dd,222,210,40,'P'); tagc(dd,SW/2,364,'IL CHOISIT PILE',GOLD)
        elif key=='s9':
            insp(dd,76,GY,t,k=2.0)
            T(dd,'PILE ?',210,120,18,'silk7',12,GOLD,align='c',sp=1); box(dd,150,146,124,18,fill=CARD,border=GOLD,bw=2); box(dd,152,148,46,14,fill=GOLD)
            T(dd,'FACE ?',210,196,18,'silk7',12,CYAN,align='c',sp=1); box(dd,150,222,124,18,fill=CARD,border=CYAN,bw=2); box(dd,152,224,100,14,fill=CYAN)
            stamp(dd,212,290,'DÉSAVANTAGÉ ?',RED,12); tagc(dd,SW/2,364,'DES CHANCES INÉGALES ?',RED)
        elif key=='s10':
            insp(dd,SW/2,GY,t,k=3.0); T(dd,'?',70,130,56,'press',44,CORAL,align='c',shadow=(3,3,BLACK)); T(dd,'?',244,130,56,'press',44,CYAN,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'COMMENT FAIRE ?',CORAL)
        elif key=='q':
            T(dd,'50/50',SW/2,120,60,'press',40,GOLD,align='c',shadow=(5,5,BLACK)); coin_big(dd,SW/2,236,34,'P'); stamp(dd,SW/2,306,'PIÈCE TRUQUÉE',RED,12)
            tagc(dd,SW/2,364,'AVEC CETTE PIÈCE TRUQUÉE',CORAL)
        elif key=='r0':
            for i,cx in enumerate((92,220)):
                box(dd,cx-50,140,100,100,fill=CARD,border=EDGE,bw=3); T(dd,str(i+1),cx,150,24,'press',18,GREY,align='c'); coin(dd,cx,206,24,'P' if i==0 else 'F') if lt>1.3+0.9*i else None
            lbl(dd,SW/2,270,'1 LANCER, PUIS 1 AUTRE',CYAN,10); tagc(dd,SW/2,364,'DEUX LANCERS DE SUITE',CYAN)
        elif key=='r1':
            prow(dd,170,'PF',r=28,gap=84); T(dd,'+',SW/2,152,32,'press',24,CREAM,align='c') if False else None
            insp(dd,84,GY,t,k=2.0); stamp(dd,206,290,'L’INSPECTEUR GAGNE',GOLD,10) if False else None
            stamp(dd,SW/2,250,'L’INSPECTEUR GAGNE',GOLD,11); star(dd,252,300,t,4); tagc(dd,SW/2,364,'L’INSPECTEUR GAGNE',GOLD)
        elif key=='r2':
            prow(dd,170,'FP',r=28,gap=84)
            stamp(dd,SW/2,250,'SON AMI GAGNE',GRN,12); sprite(dd,MAN,AMI,SW/2-5*3.4,GY-14*3.4+math.sin(t*3)*1.2,3.4,10); tagc(dd,SW/2,364,'SON AMI GAGNE',GRN)
        elif key=='r3':
            prow(dd,150,'PP',r=20,gap=48,x0=56) ; prow(dd,150,'FF',r=20,gap=48,x0=208)
            T(dd,'=',SW/2,128,30,'press',24,RED,align='c')  if False else None
            stamp(dd,SW/2,230,'ON IGNORE',RED,16); lbl(dd,SW/2,266,'ON RECOMMENCE',CORAL,12)
            tagc(dd,SW/2,364,'DEUX FOIS PAREIL : ON REJOUE',CORAL)
        elif key=='r4':
            insp(dd,76,GY,t,k=2.4); T(dd,'?',216,120,90,'press',70,GOLD,align='c',shadow=(5,5,BLACK)); tagc(dd,SW/2,364,'POURQUOI ÇA MARCHE ?',GOLD)
        elif key=='r5':
            box(dd,24,170,264,34,fill=CARD,border=EDGE,bw=2); w=int(260*0.7*min(1,lt/0.8+0.01)); box(dd,26,172,w,30,fill=GOLD)
            if lt>0.8: box(dd,26+182,172,78,30,fill=CYAN)
            T(dd,'PILE 7/10',26+90,142,16,'press',12,GOLD,align='c'); T(dd,'FACE 3/10',26+222,142,16,'press',12,CYAN,align='c')
            coin(dd,80,258,18,'P'); coin(dd,232,258,18,'F'); tagc(dd,SW/2,364,'PILE SORT 7 FOIS SUR 10',GOLD)
        elif key=='r6':
            prow(dd,160,'PF',r=24,gap=96); frac(dd,SW/2-72,208,'7/10',GOLD,15); frac(dd,SW/2+72,208,'3/10',CYAN,15); frac(dd,SW/2,206,'x',CREAM,18)
            if lt>0.9: stamp(dd,SW/2,276,'= 21 %',GOLD,20)
            tagc(dd,SW/2,364,'7/10 FOIS 3/10',GOLD)
        elif key=='r7':
            prow(dd,160,'FP',r=24,gap=96); frac(dd,SW/2-72,208,'3/10',CYAN,15); frac(dd,SW/2+72,208,'7/10',GOLD,15); frac(dd,SW/2,206,'x',CREAM,18)
            if lt>0.9: stamp(dd,SW/2,276,'= 21 %',CYAN,20)
            tagc(dd,SW/2,364,'3/10 FOIS 7/10',CYAN)
        elif key=='r8':
            box(dd,20,140,120,90,fill=CARD,border=GOLD,bw=3); frac(dd,80,168,'21 %',GOLD,24); prow(dd,214,'PF',r=11,gap=34,x0=64)
            box(dd,172,140,120,90,fill=CARD,border=CYAN,bw=3); frac(dd,232,168,'21 %',CYAN,24); prow(dd,214,'FP',r=11,gap=34,x0=216)
            T(dd,'=',SW/2,170,40,'press',32,GRN,align='c',shadow=(3,3,BLACK)); tagc(dd,SW/2,364,'EXACTEMENT PAREIL',GRN)
        elif key=='r9':
            person_pair(dd,t,k=2.4); stamp(dd,SW/2,150,'50 / 50',GRN,24); star(dd,44,210,t,4); star(dd,268,210,t,4); tagc(dd,SW/2,364,'LA MÊME CHANCE POUR LES DEUX',GRN)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#036'
    def fn(lay,dd):
        coin_big(dd,70,190,28,'P',sq=math.cos(t*2)); coin_big(dd,SW/2,150,34,'F',sq=math.cos(t*2+1)); coin_big(dd,242,190,28,'P',sq=math.cos(t*2+2))
        person_pair(dd,t,k=2.0)
        T(dd,'UNE PIÈCE TRUQUÉE',SW/2,16,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'TIRAGE 50 / 50 ?',SW/2,52,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DE LA PIÈCE TRUQUÉE"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#037')
