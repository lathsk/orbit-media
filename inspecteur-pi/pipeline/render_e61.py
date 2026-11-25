from render_e4x import *
import inspect, math
B.NUM='#061'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
CW,CH=58,84
def card(dd,cx,cy,txt,face=True,col=None,dim=False,hl=None,k=1.0,bob=0.0):
    w=CW*k; h=CH*k; y=cy-h/2+bob
    if face:
        bd=hl or (DIM if dim else DARK)
        box(dd,cx-w/2,y,w,h,fill=(CREAM if not dim else rgb('#8A8478')),border=bd,bw=3 if hl else 2,shadow=(3,3,BLACK))
        sz=int(34*k)
        T(dd,txt,cx,y+h/2-sz/2-2,sz+4,'press',sz,col or DARK,align='c')
    else:
        box(dd,cx-w/2,y,w,h,fill=CARD,border=hl or CORAL,bw=3,shadow=(3,3,BLACK))
        box(dd,cx-w/2+6,y+6,w-12,h-12,fill=rgb('#1B2347'),border=EDGE,bw=1)
        sz=int(30*k)
        T(dd,txt,cx,y+h/2-sz/2-2,sz+4,'press',sz,hl or CORAL,align='c')
XS=[52,124,196,268]; FACES=['E','K','4','7']
def four(dd,y=230,faces=True,hl=(),dim=(),t=0.0,n=4,k=1.0,txts=None):
    for i in range(n):
        card(dd,XS[i],y,(txts or FACES)[i] if faces else '?',face=faces,hl=(GRN if i in hl else None),dim=(i in dim),bob=(math.sin(t*3+i)*2 if not hl else 0),k=k)
def bookmark(dd,cx,cy,col=GOLD):
    box(dd,cx-22,cy-34,44,56,fill=col,border=DARK,bw=3)
    dd.polygon([((cx-22)*S,(cy+22)*S),((cx+22)*S,(cy+22)*S),(cx*S,(cy+2)*S)],fill=rgb('#07090F'))
    dd.polygon([((cx-19)*S,(cy+22)*S),((cx+19)*S,(cy+22)*S),(cx*S,(cy+4)*S)],fill=CARD)
HEADS={'s1':[('9 personnes sur 10 ',CREAM),('se trompent',RED),(' ici',CREAM)],
 's2':[('4 cartes',GOLD),(' sur la table',CREAM)],
 's3':[('Une ',CREAM),('lettre',CYAN),(' d’un côté, un ',CREAM),('nombre',CORAL),(' de l’autre',CREAM)],
 's4':[('Tu vois : ',CREAM),('E, K, 4',GOLD),(' et ',CREAM),('7',GOLD)],
 's5':[('La règle : ',CREAM),('voyelle',CORAL),(' = ',CREAM),('pair',CYAN)],
 'q':[('Cartes à ',CREAM),('retourner',CORAL),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('E',GRN),(' et ',CREAM),('7',GRN)],
 'r1':[('Beaucoup disent ',CREAM),('E et 4',RED)],
 'r2':[('Le ',CREAM),('4',GOLD),(' est ',CREAM),('inutile',RED)],
 'r3':[('Une ',CREAM),('consonne',CYAN),(' derrière : ',CREAM),('ça passe',GRN)],
 'r4':[('Le ',CREAM),('K',GOLD),(' : hors sujet',CREAM)],
 'r5':[('Le ',CREAM),('E',GOLD),(' doit cacher un ',CREAM),('pair',CYAN)],
 'r6':[('Le ',CREAM),('7',GOLD),(' : voyelle derrière ?',CREAM)],
 'r7':[('Retourne ',CREAM),('E',GRN),(' et ',CREAM),('7',GRN)],
 'r8':[('Cherche à ',CREAM),('casser',GOLD),(' la règle',CREAM)],
 'r9':[('Enregistre-la !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            four(dd,236,True,t=t)
            numcard(dd,cx,118,'9 SUR 10',RED,22)
            tagc(dd,cx,364,'NEUF SUR DIX SE TROMPENT',RED)
        elif key=='s2':
            for i in range(4):
                if lt>0.15+i*0.25: card(dd,XS[i],230,FACES[i],True,bob=math.sin(t*3+i)*2)
            tagc(dd,cx,364,'QUATRE CARTES SUR LA TABLE',GOLD)
        elif key=='s3':
            card(dd,86,220,'E',True,k=1.35); arrow_r(dd,134,222,44,CREAM); card(dd,226,220,'4',False,k=1.35,hl=CYAN)
            lbl(dd,86,292,'LETTRE',CYAN,9); lbl(dd,226,292,'NOMBRE',CORAL,9)
            tagc(dd,cx,364,'UNE LETTRE, UN NOMBRE',CYAN)
        elif key=='s4':
            four(dd,226,True,t=t)
            tagc(dd,cx,364,'TU VOIS : E, K, 4 ET 7',GOLD)
        elif key=='s5':
            numcard(dd,cx,124,'VOYELLE',CORAL,18); lbl(dd,cx,176,'A  E  I  O  U',GREY,9)
            arrow_d(dd,cx,196,30,CREAM)
            numcard(dd,cx,236,'NOMBRE PAIR',CYAN,18); lbl(dd,cx,286,'2  4  6  8',GREY,9)
            tagc(dd,cx,364,'DERRIÈRE UNE VOYELLE : UN PAIR',CORAL)
        elif key=='q':
            four(dd,212,True,hl=(),t=t)
            numcard(dd,cx,112,'? ? ?',GOLD,14) if False else None
            lbl(dd,cx,290,'LESQUELLES RETOURNER ?',GOLD,10)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            four(dd,226,True,hl=(0,3),dim=(1,2))
            check(dd,XS[0],310,16,6,GRN); check(dd,XS[3],310,16,6,GRN)
            star(dd,30,130,t,6); star(dd,284,130,t+1,6)
            tagc(dd,cx,364,'LA RÉPONSE : E ET 7',GRN)
        elif key=='r1':
            four(dd,226,True,t=t,dim=(1,3))
            for i in (0,2): box(dd,XS[i]-CW/2-4,226-CH/2-4,CW+8,6,fill=RED)
            xmark_(dd,XS[2],310,14,6,RED)
            tagc(dd,cx,364,'BEAUCOUP DISENT : E ET 4',RED)
        elif key=='r2':
            card(dd,cx,214,'4',True,k=1.5)
            if lt>0.3 and blink(t): stamp(dd,cx,320,'INUTILE',RED,14)
            tagc(dd,cx,364,'LE 4 EST INUTILE',RED)
        elif key=='r3':
            card(dd,80,214,'4',True,k=1.2); arrow_r(dd,128,216,44,CREAM)
            card(dd,234,214,'B' if lt<1.2 else 'K',True,k=1.2,col=CORAL,hl=GRN)
            lbl(dd,234,276,'CONSONNE',CORAL,9)
            if lt>0.5: check(dd,cx,320,16,6,GRN)
            tagc(dd,cx,364,'UNE CONSONNE NE CASSE RIEN',GRN)
        elif key=='r4':
            card(dd,cx-60,204,'K',True,k=1.5); arrow_r(dd,cx+4,206,40,CREAM)
            numcard(dd,cx+86,190,'?',GREY,20)
            lbl(dd,cx,290,'LA RÈGLE NE DIT RIEN',CREAM,10)
            tagc(dd,cx,364,'RIEN SUR LES CONSONNES',GOLD)
        elif key=='r5':
            card(dd,76,206,'E',True,k=1.4); arrow_r(dd,124,208,40,CREAM)
            card(dd,236,206,'?' if lt<1.4 else '2',lt>=1.4,k=1.4,hl=CYAN,col=DARK)
            lbl(dd,236,276,'DOIT ÊTRE PAIR',CYAN,9)
            if blink(t): stamp(dd,cx,320,'ON LE RETOURNE',GOLD,10)
            tagc(dd,cx,364,'LE E : ON LE RETOURNE',GOLD)
        elif key=='r6':
            card(dd,76,206,'7',True,k=1.4); arrow_r(dd,124,208,40,CREAM)
            card(dd,236,206,'? ' if lt<1.2 else 'A',lt>=1.2,k=1.4,hl=RED,col=CORAL)
            if lt>1.2:
                xmark_(dd,cx,324,14,6,RED)
                lbl(dd,cx,284,'7 N’EST PAS PAIR',RED,10)
            tagc(dd,cx,364,'VOYELLE DERRIÈRE : RÈGLE FAUSSE',RED)
        elif key=='r7':
            four(dd,226,True,hl=(0,3),dim=(1,2))
            for i in (0,3): arrow_d(dd,XS[i],284,22,GRN)
            tagc(dd,cx,364,'RETOURNE LE E ET LE 7',GRN)
        elif key=='r8':
            numcard(dd,cx,132,'CONFIRMER',GREY,16,dim=True); xmark_(dd,cx+118,152,14,6,RED)
            numcard(dd,cx,222,'CASSER',GOLD,24)
            if blink(t): star(dd,36,248,t,6); star(dd,276,248,t+1,6)
            tagc(dd,cx,364,'LE PIÈGE : CHERCHER À CONFIRMER',CORAL)
        elif key=='r9':
            bookmark(dd,cx,210)
            if blink(t): arrow_d(dd,cx,262,30,GOLD)
            tagc(dd,cx,364,'POUR LA REFAIRE PLUS TARD',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#061'
    def fn(lay,dd):
        cx=SW/2
        four(dd,214,True,t=0.0)
        T(dd,'9 SUR 10 SE TROMPENT',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'LES 4 CARTES',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="QUELLES CARTES RETOURNER ?"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#062','ENREGISTRE-LA POUR PLUS TARD')
