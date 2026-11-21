from render_e4x import *
import inspect
B.NUM='#053'
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-18: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
FX=[64,160,256]
def friends(dd,t,feet=300,cards=None,col=GOLD,size=12,dim=False):
    for i,x in enumerate(FX):
        sorted_man(dd,x,feet,t,CANDP[i],k=3.0)
        if cards: numcard(dd,x,feet-46-size-22,cards,[CORAL,CYAN,GOLD][i] if col is None else col,size,dim=dim)
def groom(dd,cx,feet,t): sorted_man(dd,cx,feet,t,CANDP[3],k=3.0)
def seg_bar(dd,segs,y=200,x0=36,wtot=248,h=46,total=None):
    tot=total or sum(v for v,_,_ in segs); x=x0
    for v,col,txt in segs:
        w=wtot*v/tot
        box(dd,x,y,w,h,fill=col,border=CREAM,bw=3)
        if txt and w>40: T(dd,txt,x+w/2,y+h/2-8,18,'press',14,BLACK,align='c')
        x+=w
    return x0,wtot,tot
def plus(dd,cx,cy,w=26,col=CREAM): box(dd,cx-w/2,cy-3,w,7,fill=col); box(dd,cx-3,cy-w/2,7,w,fill=col)
HEADS={'s1':[('Où est passé ',CREAM),('l’euro',GOLD),(' manquant ?',CREAM)],
 's2':[('Trois amis ',CREAM),('paient',GOLD),(' 10 € chacun',CREAM)],
 's3':[('30 €',GOLD),(' en tout',CREAM)],
 's4':[('La chambre ',CREAM),('coûte',CYAN),(' 25 €',GOLD)],
 's5':[('Le groom ',CREAM),('rapporte',CYAN),(' 5 €',GOLD)],
 's6':[('Il en garde ',CREAM),('2,',CORAL),(' rend ',CREAM),('1',CYAN)],
 's7':[('Chacun a payé ',CREAM),('9 €',GOLD)],
 's8':[('27 € + ',CREAM),('2 €',CORAL),(' = ',CREAM),('29 €',GOLD)],
 's9':[('Mais ils ont ',CREAM),('donné 30',CORAL)],
 'q':[('Où est passé ',CREAM),('l’euro',GOLD),(' ?',CREAM)],
 'r0':[('Aucun ',CREAM),('euro',GOLD),(' manquant',CORAL)],
 'r1':[('Le calcul ',CREAM),('est faux',CORAL)],
 'r2':[('Les amis ont payé ',CREAM),('27 €',GOLD)],
 'r3':[('27 € ',GOLD),('contiennent',CREAM),(' le groom',CORAL)],
 'r4':[('25',GOLD),(' chambre + ',CREAM),('2',CORAL),(' groom',CREAM)],
 'r5':[('On n’ajoute ',CREAM),('pas',CORAL),(' les 2 €',CREAM)],
 'r6':[('On les ',CREAM),('retire',CYAN),(' : 25 €',GOLD)],
 'r7':[('Pour retrouver ',CREAM),('30 €',GOLD)],
 'r8':[('25 €',GOLD),(' pour la chambre',CREAM)],
 'r9':[('Plus ',CREAM),('2 €',CORAL),(' pour le groom',CREAM)],
 'r10':[('Plus ',CREAM),('3 €',CYAN),(' rendus',CREAM)],
 'r11':[('Le piège : ',CREAM),('mauvaise',CORAL),(' addition',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            numcard(dd,cx,128,'30 €',GOLD,20); numcard(dd,cx,196,'29 €',CORAL,20)
            if blink(t): numcard(dd,cx,262,'1 € ?',CYAN,20)
            tagc(dd,cx,364,'OÙ EST PASSÉ L’EURO MANQUANT ?',GOLD)
        elif key=='s2':
            friends(dd,t,300,'10 €',col=None,size=12); tagc(dd,cx,364,'TROIS AMIS, 10 € CHACUN',GOLD)
        elif key=='s3':
            friends(dd,t,300,'10 €',col=None,size=12)
            p=sp(lt,0.2,0.9)
            if p>0.5: numcard(dd,cx,126,'= 30 €',GOLD,22)
            tagc(dd,cx,364,'10 + 10 + 10 = 30 €',GOLD)
        elif key=='s4':
            numcard(dd,cx,132,'PAYÉ : 30 €',CYAN,16,dim=True); arrow_d(dd,cx,190,20)
            numcard(dd,cx,216,'CHAMBRE : 25 €',GOLD,16); tagc(dd,cx,364,'LA CHAMBRE COÛTE 25 €',GOLD)
        elif key=='s5':
            numcard(dd,cx,124,'30 - 25 = 5 €',CYAN,16); groom(dd,cx,290,t); numcard(dd,cx+84,226,'5 €',GOLD,16)
            tagc(dd,cx,364,'LE GROOM RAPPORTE 5 €',CYAN)
        elif key=='s6':
            groom(dd,90,210,t); numcard(dd,226,150,'GARDE 2 €',CORAL,12)
            for i,x in enumerate(FX):
                sorted_man(dd,x,310,t,CANDP[i],k=3.0); numcard(dd,x,226,'+1 €',CYAN,11)
            tagc(dd,cx,364,'IL EN GARDE 2, RENDS 1 À CHACUN',CORAL)
        elif key=='s7':
            friends(dd,t,300,'9 €',col=None,size=12)
            if lt>0.6: numcard(dd,cx,126,'9 x 3 = 27 €',GOLD,16)
            tagc(dd,cx,364,'CHACUN A PAYÉ 9 €, SOIT 27 €',GOLD)
        elif key=='s8':
            numcard(dd,cx,118,'27 €',CYAN,20); plus(dd,60,200,26)
            numcard(dd,cx,176,'2 €',CORAL,20); vline(dd,60,SW-20,236)
            numcard(dd,cx,252,'29 €',GOLD,24); tagc(dd,cx,364,'27 € + 2 € = 29 €',GOLD)
        elif key=='s9':
            numcard(dd,cx,128,'DONNÉ : 30 €',GOLD,16); numcard(dd,cx,196,'COMPTÉ : 29 €',CORAL,16)
            if blink(t): stamp(dd,cx,290,'IL MANQUE 1 € ?',CORAL,14)
            tagc(dd,cx,364,'MAIS ILS AVAIENT DONNÉ 30 €',CORAL)
        elif key=='q':
            box(dd,cx-120,170,240,78,fill=CARD,border=GOLD,bw=4,shadow=(4,4,BLACK)); T(dd,'1 € ?',cx,190,40,'press',32,GOLD,align='c'); lbl(dd,cx,228,'OÙ EST-IL PASSÉ ?',CREAM,9)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'0€',cx,134,100,'press',80,GOLD,align='c',shadow=(6,6,BLACK)); star(dd,30,120,t,6); star(dd,290,120,t+1,6)
            stamp(dd,cx,300,'RIEN NE MANQUE !',CORAL,14); tagc(dd,cx,364,'AUCUN EURO NE MANQUE',GOLD)
        elif key=='r1':
            numcard(dd,cx,150,'27 + 2 = 29',CORAL,18);
            if lt>0.4: xmark_(dd,cx,172,60,9,RED)
            tagc(dd,cx,364,'LE CALCUL EST FAUX',CORAL)
        elif key=='r2':
            friends(dd,t,300,'9 €',col=None,size=12); numcard(dd,cx,126,'27 €',GOLD,22); tagc(dd,cx,364,'LES AMIS ONT PAYÉ 27 €',GOLD)
        elif key=='r3':
            numcard(dd,cx,124,'27 €',GOLD,22); arrow_d(dd,cx,176,20)
            seg_bar(dd,[(25,CYAN,''),(2,CORAL,'')],y=210,total=27)
            tagc(dd,cx,364,'27 € INCLUENT DÉJÀ LES 2 €',CORAL)
        elif key=='r4':
            seg_bar(dd,[(25,CYAN,'25'),(2,CORAL,'')],y=200,total=27)
            lbl(dd,36+248*25/27/2,256,'CHAMBRE',CYAN,9); lbl(dd,226,150,'GROOM : 2 €',CORAL,9)
            tagc(dd,cx,364,'25 € CHAMBRE + 2 € GROOM',GOLD)
        elif key=='r5':
            numcard(dd,cx,150,'27 + 2',CORAL,22)
            if lt>0.5: xmark_(dd,cx,174,50,9,RED)
            tagc(dd,cx,364,'ON N’AJOUTE PAS LES 2 €',CORAL)
        elif key=='r6':
            numcard(dd,cx,130,'27 - 2',CYAN,22); arrow_d(dd,cx,180,20)
            numcard(dd,cx,206,'= 25 €',GOLD,22);
            if lt>0.6: check(dd,cx+120,236,16,6)
            tagc(dd,cx,364,'ON LES RETIRE : 27 - 2 = 25',CYAN)
        elif key=='r7':
            T(dd,'30€',cx,150,80,'press',60,GOLD,align='c',shadow=(5,5,BLACK)); tagc(dd,cx,364,'POUR RETROUVER 30 €, ON COMPTE',GOLD)
        elif key=='r8':
            seg_bar(dd,[(25,CYAN,'25 €'),(5,DIM,'')],y=190,total=30); tagc(dd,cx,364,'25 € POUR LA CHAMBRE',CYAN)
        elif key=='r9':
            seg_bar(dd,[(25,CYAN,'25 €'),(2,CORAL,''),(3,DIM,'')],y=190,total=30); lbl(dd,226,150,'GROOM : 2 €',CORAL,9)
            tagc(dd,cx,364,'PLUS 2 € POUR LE GROOM',CORAL)
        elif key=='r10':
            seg_bar(dd,[(25,CYAN,'25 €'),(2,CORAL,''),(3,GRN,'3')],y=190,total=30); lbl(dd,236,150,'RENDUS : 3 €',GRN,9)
            tagc(dd,cx,364,'PLUS 3 € RENDUS AUX AMIS = 30 €',GRN)
        elif key=='r11':
            numcard(dd,cx,126,'27 €',CYAN,20); plus(dd,60,200,26)
            numcard(dd,cx,176,'2 €',CORAL,20)
            if blink(t): stamp(dd,cx,270,'SOMMES SANS LIEN',CORAL,14)
            tagc(dd,cx,364,'DES SOMMES SANS LIEN',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#053'
    def fn(lay,dd):
        cx=SW/2
        for i,x in enumerate(FX):
            sorted_man(dd,x,262,t,CANDP[i],k=3.0); numcard(dd,x,170,'10 €',[CORAL,CYAN,GOLD][i],12)
        numcard(dd,cx,112,'27 + 2 = 29 € ?',GOLD,14)
        stamp(dd,cx,306,'30 € PAYÉS',CORAL,14)
        T(dd,'OÙ EST PASSÉ',SW/2,14,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'L’EURO MANQUANT ?',SW/2,48,36,'anton',26,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="TROIS AMIS, UNE CHAMBRE, UN CALCUL"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')

def make_decide2():
    ns=dict(vars(R14))
    src=inspect.getsource(R14.decide).replace('COMMENTE TON PLAN','RÉPONDS EN COMMENTAIRE').replace("[('Écris ton idée en ',CREAM),('commentaire',CORAL),(' !',CREAM)]","[('Écris ta ',CREAM),('réponse',CORAL),(' en commentaire !',CREAM)]").replace('def decide','def decide_')
    exec(src,ns)
    return lambda n,t,ft=None: ns['decide_'](n,t,ft)
def make_end2(num_next,pill):
    ns=dict(vars(R14))
    src=inspect.getsource(R14.end).replace("bulb(d,262,150,True,k=1.3,t=t,gk=1.0)","star(d,262,176,t,8)").replace("'#010 >>'","'%s >>'"%num_next).replace("'PARTAGE LA VIDÉO À UN AMI'",repr(pill)).replace('def end','def end_')
    ns['star']=star
    exec(src,ns)
    return lambda level,t: ns['end_'](level,t)
decide=make_decide2()
end=make_end2('#054','ENREGISTRE-LA POUR PLUS TARD')
