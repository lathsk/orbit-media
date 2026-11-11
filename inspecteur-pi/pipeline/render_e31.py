from render_e2x import *
B.NUM='#031'
BLK=(16,16,24); SKIN=(241,195,155)
HEADS={'s1':[('Dix ',GOLD),('prisonniers',CREAM),(' en file',CREAM)],
 's2':[('Chapeau ',CREAM),('noir',GOLD),(' ou ',CREAM),('blanc',CYAN)],
 's3':[('Chacun voit ceux ',CREAM),('devant',GOLD),(' lui',CREAM)],
 's4':[('Mais ',CREAM),('jamais',CORAL),(' le sien',CREAM)],
 's5':[('On commence par le ',CREAM),('dernier',GOLD)],
 's6':[('Un ',CREAM),('seul',CORAL),(' cri : noir ou blanc',CREAM)],
 's7':[('Bon cri : ',CREAM),('sauvé',GRN)],
 's8':[('Mauvais cri : ',CREAM),('perdu',RED)],
 's9':[('Cette nuit : ',CREAM),('un code',GOLD)],
 's10':[('Ensuite : ',CREAM),('silence',CORAL)],
 's11':[('Ils entendent les ',CREAM),('cris',GOLD)],
 'q':[('Combien sauvés ',CREAM),('à coup sûr ?',GOLD)],
 'r0':[('Réponse : ',CREAM),('9',GRN),(' sur ',CREAM),('10',GOLD)],
 'r1':[('Le dernier compte les ',CREAM),('blancs',CYAN)],
 'r2':[('Pair',GOLD),(' = blanc, ',CREAM),('impair',CORAL),(' = noir',CREAM)],
 'r3':[('Lui joue à ',CREAM),('pile ou face',CORAL)],
 'r4':[('Mais il donne le ',CREAM),('code',GOLD)],
 'r5':[('Son voisin compte ',CREAM),('aussi',GOLD)],
 'r6':[('Parité ',CREAM),('différente',CORAL),(' : blanc',CREAM)],
 'r7':[('Sinon',CREAM),(' : ',CREAM),('noir',GOLD)],
 'r8':[('Chacun fait ',CREAM),('pareil',GOLD)],
 'r9':[('Un sacrifié, ',CREAM),('neuf sauvés',GRN)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','q')
HATS='BWBWBBWBWB'    # indice 0 = le dernier de la file (à gauche), 9 = le premier ; tous regardent vers la droite
FY=252
def X(i): return 21+i*30.4
def ol(dd,x,y,w,h,col,bw=2):
    box(dd,x,y,w,bw,fill=col); box(dd,x,y+h-bw,w,bw,fill=col); box(dd,x,y,bw,h,fill=col); box(dd,x+w-bw,y,bw,h,fill=col)
def hat(dd,cx,top,c,unk=False,hl=False):
    if unk:
        box(dd,cx-10,top-8,20,20,fill=CARD,border=GOLD,bw=2); T(dd,'?',cx,top-3,14,'press',12,GOLD,align='c'); return
    if c=='W': fill,bd=CREAM,DARK
    else: fill,bd=BLK,CREAM
    box(dd,cx-7,top,14,9,fill=fill,border=bd,bw=1); box(dd,cx-11,top+8,22,4,fill=fill,border=bd,bw=1)
    if hl: ol(dd,cx-14,top-5,28,22,GOLD,2)
def fig(dd,cx,c=None,unk=False,hl=False,hhl=False,dead=False,body=ORG):
    box(dd,cx-8,FY-8,7,8,fill=DARK); box(dd,cx+1,FY-8,7,8,fill=DARK)
    box(dd,cx-11,FY-34,22,26,fill=body if not dead else DIM,border=DARK,bw=1)
    box(dd,cx-11,FY-27,22,3,fill=DARK); box(dd,cx-11,FY-19,22,3,fill=DARK)
    box(dd,cx-8,FY-49,16,15,fill=SKIN,border=DARK,bw=1); box(dd,cx+2,FY-43,3,3,fill=DARK)
    if c or unk: hat(dd,cx,FY-58,c,unk,hhl)
    if hl: ol(dd,cx-16,FY-76,32,80,GOLD,2)
def row(dd,hats=HATS,hide=(),unk=(),hl=(),hhl=(),dead=(),n=10,upto=10):
    for i in range(n):
        if i>=upto: continue
        c=None if (hats is None or i in hide) else hats[i]
        fig(dd,X(i),c,unk=(i in unk),hl=(i in hl),hhl=(i in hhl),dead=(i in dead))
def bighat(dd,cx,c,y=112):
    fill,bd=(CREAM,DARK) if c=='W' else (BLK,CREAM)
    box(dd,cx-22,y,44,34,fill=fill,border=bd,bw=2,shadow=(3,3,BLACK)); box(dd,cx-36,y+30,72,10,fill=fill,border=bd,bw=2,shadow=(3,3,BLACK))
    T(dd,'NOIR' if c=='B' else 'BLANC',cx,y+50,14,'press',11,CREAM,align='c')
def sayb(dd,cx,y,txt,col=GOLD,w=96,h=34,size=13):
    cx=max(cx,24+w/2); cx=min(cx,SW-24-w/2)
    bubble(dd,cx-w/2,y,w,h,[txt],col,size)
    dd.polygon([((cx-5)*S,(y+h)*S),((cx+5)*S,(y+h)*S),(cx*S,(y+h+8)*S)],fill=col)
def bigc(dd,cx,y,txt,col=GOLD,w=120,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-22: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=4,shadow=(4,4,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
WH=[i for i,c in enumerate(HATS) if c=='W']   # [1,3,6,8]
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            row(dd,None,upto=min(10,1+int(lt*9))); lbl(dd,SW/2,120,'10 PRISONNIERS',GOLD,12)
            tagc(dd,SW/2,364,'UNE FILE INDIENNE',CYAN)
        elif key=='s2':
            bighat(dd,86,'B'); bighat(dd,226,'W'); row(dd,HATS,hide=[i for i in range(10) if lt<0.2+0.18*i]); tagc(dd,SW/2,364,'NOIR OU BLANC AU HASARD',GOLD)
        elif key=='s3':
            row(dd,HATS,hl=[3],hhl=range(4,10))
            lbl(dd,SW/2,128,'IL VOIT 6 CHAPEAUX',GOLD,12)
            tagc(dd,SW/2,364,'IL VOIT LES CHAPEAUX DEVANT',GOLD)
        elif key=='s4':
            row(dd,HATS,hl=[3],unk=[3]); sayb(dd,X(3),128,'LE MIEN ?',CORAL,w=140)
            tagc(dd,SW/2,364,'JAMAIS SON PROPRE CHAPEAU',CORAL)
        elif key=='s5':
            row(dd,HATS,hl=[0]); lbl(dd,X(0)+34,130,'LE DERNIER',GOLD,10)
            dd.polygon([((X(0)-6)*S,(FY-86)*S),((X(0)+6)*S,(FY-86)*S),(X(0)*S,(FY-78+math.sin(t*6)*2)*S)],fill=GOLD)
            tagc(dd,SW/2,364,'IL VOIT TOUS LES AUTRES',GOLD)
        elif key=='s6':
            row(dd,HATS,hl=[0]); w='NOIR ?' if int(lt*2.5)%2==0 else 'BLANC ?'
            sayb(dd,X(0)+36,150,w,GOLD,w=118,h=40,size=15); tagc(dd,SW/2,364,'UN SEUL CRI POUR CHACUN',CORAL)
        elif key=='s7':
            row(dd,HATS,hl=[0]); sayb(dd,X(0)+36,150,'BLANC !',GOLD,w=118,h=40,size=15) if False else None
            stamp(dd,SW/2,150,'SAUVÉ',GRN,18); tagc(dd,SW/2,364,'BON CRI = SAUVÉ',GRN)
        elif key=='s8':
            row(dd,HATS,hl=[0],dead=[0]); xmark_(dd,X(0),FY-20,13,4,RED)
            stamp(dd,SW/2,150,'PERDU',RED,18); tagc(dd,SW/2,364,'MAUVAIS CRI = FIN',RED)
        elif key=='s9':
            moon(dd,252,128,16); star(dd,60,120,t,3); star(dd,150,134,t,3)
            cl=[0,1,2,3];
            for k_,i in enumerate(range(10)): fig(dd,X(i),None)
            sayb(dd,SW/2,150,'ON FAIT UN CODE',GOLD,w=210,h=34,size=11); tagc(dd,SW/2,364,'ILS SE METTENT D’ACCORD',GOLD)
        elif key=='s10':
            row(dd,None)
            for i in (1,4,7): sayb(dd,X(i),150+(i%2)*6,'...',CREAM,w=44,h=26,size=12)
            stamp(dd,SW/2,118,'SILENCE',CORAL,14); tagc(dd,SW/2,364,'PLUS UN SEUL MOT',CORAL)
        elif key=='s11':
            row(dd,None)
            sayb(dd,X(0)+22,150,'NOIR !',CREAM,w=80,h=30,size=12)
            if lt>0.7: sayb(dd,X(2)+34,110,'BLANC !',GOLD,w=92,h=30,size=12)
            for i in range(3,10): dotline(dd,(X(0),FY-40),(X(i),FY-40),CYAN,t,n=3) if False else None
            tagc(dd,SW/2,364,'ILS ENTENDENT LES CRIS',GOLD)
        elif key=='q':
            row(dd,None,hl=[0]); bigc(dd,SW/2,110,'? / 10',GOLD,w=170,h=64,size=30)
            tagc(dd,SW/2,364,'COMBIEN À COUP SÛR ?',CORAL)
        elif key=='r0':
            bigc(dd,SW/2,120,'9 / 10',GRN,w=190,h=76,size=34); insp(dd,SW/2,GY,t,k=2.0)
            star(dd,276,130,t,5); star(dd,36,130,t,4); tagc(dd,SW/2,364,'NEUF SAUVÉS SUR DIX',GRN)
        elif key=='r1':
            n=sum(1 for j in range(4) if lt>0.35+0.4*j)
            row(dd,HATS,hl=[0],hhl=[WH[j] for j in range(n)]); bigc(dd,SW/2,120,'%d BLANC%s'%(n,'S' if n>1 else ''),CYAN,w=190,h=56,size=22)
            tagc(dd,SW/2,364,'IL COMPTE LES CHAPEAUX BLANCS',CYAN)
        elif key=='r2':
            bigc(dd,SW/2,110,'PAIR  >  BLANC',GOLD,w=250,h=52,size=18); bigc(dd,SW/2,184,'IMPAIR  >  NOIR',CORAL,w=250,h=52,size=18)
            lbl(dd,SW/2,262,'4 BLANCS = PAIR  >  BLANC',CREAM,10); tagc(dd,SW/2,364,'PAIR BLANC / IMPAIR NOIR',GOLD)
        elif key=='r3':
            row(dd,HATS,hl=[0]); sayb(dd,X(0)+36,140,'BLANC !',GOLD,w=118,h=40,size=15)
            stamp(dd,SW/2,300,'PILE OU FACE',CORAL,12); tagc(dd,SW/2,364,'IL RISQUE SA VIE',CORAL)
        elif key=='r4':
            row(dd,HATS,dead=[0] if lt>1.2 else []);
            if lt>1.2: xmark_(dd,X(0),FY-20,13,4,RED)
            bigc(dd,SW/2,112,'CODE : PAIR',GOLD,w=210,h=48,size=18); tagc(dd,SW/2,364,'TOUT LE MONDE A LE CODE',GOLD)
        elif key=='r5':
            n=sum(1 for j in (3,6,8) if lt>0.35+0.4*[3,6,8].index(j))
            row(dd,HATS,hide=[0],unk=[1],hl=[1],hhl=[j for j in (3,6,8)][:n])
            fig(dd,X(0),None,dead=True) if False else None
            bigc(dd,SW/2,112,'%d BLANC%s'%(n,'S' if n>1 else ''),CYAN,w=170,h=48,size=18); tagc(dd,SW/2,364,'IL COMPTE DEVANT LUI',CYAN)
        elif key=='r6':
            row(dd,HATS,hide=[0],unk=[1],hl=[1],hhl=[3,6,8]); bigc(dd,SW/2,100,'3 = IMPAIR',CORAL,w=200,h=34,size=16)
            bigc(dd,SW/2,140,'CODE : PAIR',GOLD,w=200,h=34,size=16)
            T(dd,'≠',SW/2,150,20,'press',16,CREAM,align='c') if False else None
            stamp(dd,SW/2,300,'CHAPEAU BLANC',CYAN,12); tagc(dd,SW/2,364,'DIFFÉRENT = BLANC',CYAN)
        elif key=='r7':
            bigc(dd,SW/2,108,'PAIR = PAIR',GOLD,w=200,h=40,size=16)
            row(dd,HATS,hide=[0],unk=[2],hl=[2],hhl=[3,6,8]); stamp(dd,SW/2,300,'CHAPEAU NOIR',GOLD,12)
            tagc(dd,SW/2,364,'IDENTIQUE = NOIR',GOLD)
        elif key=='r8':
            k=min(9,1+int(lt*2.2))
            row(dd,HATS,hl=[k]) ; bigc(dd,SW/2,110,'1, 2, 3 ...',CREAM,w=190,h=40,size=16)
            tagc(dd,SW/2,364,'ET AINSI DE SUITE',GOLD)
        elif key=='r9':
            row(dd,HATS,dead=[0]); xmark_(dd,X(0),FY-20,13,4,RED)
            for i in range(1,10): stamp(dd,X(i),FY-72-(i%2)*18,'OK',GRN,9) if False else None
            bigc(dd,SW/2,104,'1 PERDU',RED,w=170,h=38,size=16); bigc(dd,SW/2,148,'9 SAUVÉS',GRN,w=190,h=40,size=18)
            star(dd,276,120,t,4); tagc(dd,SW/2,364,'NEUF SAUVÉS À COUP SÛR',GRN)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#031'
    def fn(lay,dd):
        row(dd,HATS)
        T(dd,'DIX PRISONNIERS,',SW/2,10,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'COMBIEN SURVIVENT ?',SW/2,44,36,'anton',22,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DES CHAPEAUX"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#032')
