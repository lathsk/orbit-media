from render_e2x import *
B.NUM='#032'
APL=RED; ORGF=ORG
HEADS={'s1':[('Un ',CREAM),('voleur',CORAL),(' mélange tout',CREAM)],
 's2':[('Un ',CREAM),('seul fruit',GOLD),(' pour réparer',CREAM)],
 's3':[('Trois ',CREAM),('caisses',GOLD)],
 's4':[('Une caisse de ',CREAM),('pommes',RED)],
 's5':[('Une caisse ',CREAM),('d’oranges',ORG)],
 's6':[('Une caisse ',CREAM),('mélange',CYAN)],
 's7':[('Il remet les ',CREAM),('étiquettes',GOLD)],
 's9':[('Aucune',CORAL),(' n’est correcte',CREAM)],
 's10':[('Piocher ',CREAM),('un seul',GOLD),(' fruit',CREAM)],
 's11':[('Dans ',CREAM),('une seule',CORAL),(' caisse',CREAM)],
 'q':[('Quelle ',CREAM),('caisse',GOLD),(' choisir ?',CREAM)],
 'r0':[('Caisse ',CREAM),('« mélange »',CYAN)],
 'r1':[('Un seul ',CREAM),('type',GOLD),(' de fruit',CREAM)],
 'r2':[('Il sort une ',CREAM),('pomme',RED)],
 'r3':[('C’est la caisse des ',CREAM),('pommes',RED)],
 'r4':[('« Oranges » : ',CREAM),('pas d’oranges',CORAL)],
 'r5':[('Ni de ',CREAM),('pommes, ',RED),('déjà trouvées',CREAM)],
 'r6':[('Donc c’est le ',CREAM),('mélange',CYAN)],
 'r7':[('Il reste : les ',CREAM),('oranges',ORG)],
 'r8':[('Tout est ',CREAM),('réparé !',GRN)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s9','s10','s11','q')
CX=[52,156,260]; Y=176
def ol(dd,x,y,w,h,col,bw=2):
    box(dd,x,y,w,bw,fill=col); box(dd,x,y+h-bw,w,bw,fill=col); box(dd,x,y,bw,h,fill=col); box(dd,x+w-bw,y,bw,h,fill=col)
def fruit(dd,cx,cy,kind,r=9):
    if kind=='A':
        disc(dd,cx,cy,r+1,DARK); disc(dd,cx,cy,r,APL); box(dd,cx-r*0.5,cy-r*0.5,r*0.45,r*0.45,fill=lerpc(APL,(255,255,255),0.5)); box(dd,cx-1,cy-r-3,2,4,fill=DARK); box(dd,cx+1,cy-r-3,r*0.5,3,fill=GRN)
    else:
        disc(dd,cx,cy,r+1,DARK); disc(dd,cx,cy,r,ORGF); box(dd,cx-r*0.5,cy-r*0.5,r*0.45,r*0.45,fill=lerpc(ORGF,(255,255,255),0.5)); box(dd,cx-1,cy-r-2,3,3,fill=GRN)
def plate(dd,cx,y,txt,col=CREAM):
    s=11
    while s>6 and tw(txt,F('silk7',s),1)>62: s-=1
    box(dd,cx-35,y,70,24,fill=col,border=DARK,bw=2); T(dd,txt,cx-tw(txt,F('silk7',s),1)/2,y+(24-s-4)/2+1,s+4,'silk7',s,DARK,sp=1)
def crate(dd,i,txt=None,pcol=CREAM,content=None,hl=False,xo=False,big=None):
    cx=CX[i]
    if content:
        for j in range(4):
            fk={'A':'A','O':'O','M':('A' if j%2==0 else 'O')}[content]
            fruit(dd,cx-30+j*20,Y-1,fk)
    box(dd,cx-42,Y+6,84,64,fill=rgb('#C9A15E'),border=rgb('#6B4A2E'),bw=3,shadow=(3,3,BLACK))
    box(dd,cx-42,Y+22,84,3,fill=rgb('#6B4A2E')); box(dd,cx-42,Y+52,84,3,fill=rgb('#6B4A2E'))
    box(dd,cx-46,Y,92,9,fill=rgb('#8A6A3A'),border=rgb('#4A3220'),bw=2)
    plate(dd,cx,Y+28,txt if txt else '?',pcol)
    if hl: ol(dd,cx-48,Y-24,96,100,GOLD,3)
    if xo: xmark_(dd,cx,Y+40,16,5,RED)
LAB=['POMMES','ORANGES','MÉLANGE']   # étiquettes (toutes fausses) ; contenu réel : oranges, mélange, pommes
REAL=['O','M','A']
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            for i in range(3): crate(dd,i)
            braq(dd,SW/2,GY,t,k=5.0); tagc(dd,SW/2,364,'LES ÉTIQUETTES SONT MÉLANGÉES',CORAL)
        elif key=='s2':
            fruit(dd,92,150,'A',r=24); fruit(dd,220,150,'O',r=24)
            bigc(dd,SW/2,206,'1 SEUL FRUIT',GOLD,w=240,h=52,size=20); insp(dd,SW/2,GY,t,k=2.0)
            tagc(dd,SW/2,364,'UN SEUL FRUIT POUR TOUT RÉPARER',GOLD)
        elif key=='s3':
            for i in range(3): crate(dd,i)
            lbl(dd,SW/2,128,'3 CAISSES',GOLD,12); tagc(dd,SW/2,364,'TROIS CAISSES',GOLD)
        elif key=='s4':
            for i in range(3): crate(dd,i,content=('A' if i==2 else None),hl=(i==2))
            lbl(dd,SW/2,128,'QUE DES POMMES',RED,11); tagc(dd,SW/2,364,'UNE CAISSE DE POMMES',RED)
        elif key=='s5':
            for i in range(3): crate(dd,i,content=REAL[i] if i!=1 else None,hl=(i==0))
            lbl(dd,SW/2,128,'QUE DES ORANGES',ORG,11); tagc(dd,SW/2,364,'UNE CAISSE D’ORANGES',ORG)
        elif key=='s6':
            for i in range(3): crate(dd,i,content=REAL[i],hl=(i==1))
            lbl(dd,SW/2,128,'LES DEUX MÉLANGÉS',CYAN,10); tagc(dd,SW/2,364,'UNE CAISSE MÉLANGE',CYAN)
        elif key=='s7':
            for i in range(3): crate(dd,i,txt=(LAB[i] if lt>[2.0,2.6,3.2][i] else None))
            braq(dd,SW/2,GY,t,k=5.0); tagc(dd,SW/2,364,'POMMES, ORANGES, MÉLANGE',GOLD)
        elif key=='s9':
            for i in range(3): crate(dd,i,txt=LAB[i],xo=(lt>0.3+0.35*i))
            lbl(dd,SW/2,128,'AUCUNE EST BONNE',RED,12); tagc(dd,SW/2,364,'ÉTIQUETTES TOUTES FAUSSES',RED)
        elif key=='s10':
            for i in range(3): crate(dd,i,txt=LAB[i])
            fruit(dd,CX[1],110+math.sin(t*5)*3,'A',r=14); dd.polygon([((CX[1]-6)*S,134*S),((CX[1]+6)*S,134*S),(CX[1]*S,146*S)],fill=GOLD)
            lbl(dd,SW/2,300,'1 FRUIT = 1 INDICE',GOLD,10); tagc(dd,SW/2,364,'UN SEUL FRUIT',GOLD)
        elif key=='s11':
            k=int(lt*2.4)%3
            for i in range(3): crate(dd,i,txt=LAB[i],hl=(i==k))
            lbl(dd,SW/2,300,'UNE SEULE CAISSE',CORAL,10); tagc(dd,SW/2,364,'DANS UNE SEULE CAISSE',CORAL)
        elif key=='q':
            for i in range(3): crate(dd,i,txt=LAB[i])
            for i in range(3): T(dd,'?',CX[i],110,36,'press',28,GOLD,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'QUELLE CAISSE ?',CORAL)
        elif key=='r0':
            for i in range(3): crate(dd,i,txt=LAB[i],hl=(i==2))
            star(dd,CX[2],120,t,5); tagc(dd,SW/2,364,'LA CAISSE MARQUÉE MÉLANGE',CYAN)
        elif key=='r1':
            for i in range(3): crate(dd,i,txt=LAB[i],xo=(i==2),hl=(i==2))
            lbl(dd,SW/2,120,'PAS UN VRAI MÉLANGE',CORAL,11); lbl(dd,SW/2,300,'UN SEUL TYPE DE FRUIT',GOLD,10)
            tagc(dd,SW/2,364,'ÉTIQUETTE FAUSSE',CORAL)
        elif key=='r2':
            for i in range(3): crate(dd,i,txt=LAB[i],hl=(i==2))
            fruit(dd,CX[2],110+math.sin(t*5)*3,'A',r=16); lbl(dd,SW/2,300,'UNE POMME !',RED,12)
            tagc(dd,SW/2,364,'IL SORT UNE POMME',RED)
        elif key=='r3':
            for i in range(3): crate(dd,i,txt=('POMMES' if i==2 else LAB[i]),pcol=(GRN if i==2 else CREAM),content=('A' if i==2 else None),hl=(i==2))
            tagc(dd,SW/2,364,'C’EST LA CAISSE DES POMMES',RED)
        elif key=='r4':
            for i in range(3): crate(dd,i,txt=('POMMES' if i==2 else LAB[i]),pcol=(GRN if i==2 else CREAM),xo=False,hl=(i==1))
            fruit(dd,CX[1],110,'O',r=14); xmark_(dd,CX[1],110,18,5,RED)
            tagc(dd,SW/2,364,'PAS D’ORANGES ICI',CORAL)
        elif key=='r5':
            for i in range(3): crate(dd,i,txt=('POMMES' if i==2 else LAB[i]),pcol=(GRN if i==2 else CREAM),hl=(i==1))
            fruit(dd,CX[1]-22,110,'O',r=13); xmark_(dd,CX[1]-22,110,17,5,RED)
            if lt>0.8: fruit(dd,CX[1]+22,110,'A',r=13); xmark_(dd,CX[1]+22,110,17,5,RED)
            tagc(dd,SW/2,364,'NI D’ORANGES, NI DE POMMES',CORAL)
        elif key=='r6':
            for i in range(3): crate(dd,i,txt=('MÉLANGE' if i==1 else 'POMMES' if i==2 else LAB[i]),pcol=(GRN if i>0 else CREAM),content=('M' if i==1 else 'A' if i==2 else None),hl=(i==1))
            tagc(dd,SW/2,364,'C’EST LE MÉLANGE',CYAN)
        elif key=='r7':
            for i in range(3): crate(dd,i,txt=('ORANGES' if i==0 else 'MÉLANGE' if i==1 else 'POMMES'),pcol=(GRN if i>0 else CREAM),content=('O' if i==0 else 'M' if i==1 else 'A'),hl=(i==0))
            tagc(dd,SW/2,364,'LA DERNIÈRE : LES ORANGES',ORG)
        elif key=='r8':
            for i in range(3): crate(dd,i,txt=['ORANGES','MÉLANGE','POMMES'][i],pcol=GRN,content=REAL[i])
            stamp(dd,SW/2,128,'RÉPARÉ',GRN,18); star(dd,36,130,t,4); star(dd,276,130,t,4); insp(dd,SW/2,GY,t,k=2.0)
            tagc(dd,SW/2,364,'UN SEUL FRUIT SUFFIT',GRN)
    return fn
def bigc(dd,cx,y,txt,col=GOLD,w=120,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-22: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=4,shadow=(4,4,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#032'
    def fn(lay,dd):
        for i in range(3): crate(dd,i,txt=LAB[i])
        fruit(dd,CX[1],120,'A',r=18)
        T(dd,'TOUTES LES ÉTIQUETTES',SW/2,10,36,'anton',22,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'SONT FAUSSES !',SW/2,44,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DES TROIS CAISSES"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#033')
