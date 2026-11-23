from render_e4x import *
import inspect, math
B.NUM='#058'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
def ln(dd,p,q,col,w=3): dd.line([(p[0]*S,p[1]*S),(q[0]*S,q[1]*S)],fill=col,width=w*S)
STAR=(156,215); VIL=[(56,150),(256,150),(56,282),(256,282)]
PAL=[CANDP[0],CANDP[1],CANDP[2],CANDP[3]]
def crown(dd,cx,top):
    box(dd,cx-9,top+6,18,6,fill=GOLD,border=DARK,bw=1)
    for dx in (-9,-1,7): box(dd,cx+dx,top,4,7,fill=GOLD,border=DARK,bw=1)
def person(dd,x,y,t,pal,k=3.0,ph=0.0,hl=False,star_=False):
    if hl: box(dd,x-24,y-52,48,70,fill=CARD,border=GOLD,bw=3)
    pri(dd,x,y+16,t,k=k,pal=pal,ph=ph)
    if star_: crown(dd,x,y+16-14*k-8)
def village(dd,t,links=True,hlstar=False,hlvil=(),cards=None,linkcol=EDGE):
    if links:
        for v in VIL: ln(dd,STAR,v,linkcol,3)
    person(dd,STAR[0],STAR[1],t,CANDP[4],3.0,0,hl=hlstar,star_=True)
    for i,v in enumerate(VIL): person(dd,v[0],v[1],t,PAL[i],3.0,i+1,hl=(i in hlvil))
    if cards:
        for key,(txt,col) in cards.items():
            if key=='s': numcard(dd,STAR[0]+52,STAR[1]-8,txt,col,11)
            else:
                x,y=VIL[key]; numcard(dd,x+(0 if key%2==0 else 0),y+30,txt,col,11)
# generic village (histoire)
GN=[(50,150),(160,128),(262,160),(80,262),(190,246),(272,296)]
GE=[(0,1),(1,2),(0,3),(1,4),(3,4),(4,5),(2,5)]
def gen_village(dd,t,hl=None,friends=(),cards=None):
    for a,b in GE:
        col=GOLD if (hl is not None and (a==hl or b==hl)) else EDGE
        ln(dd,GN[a],GN[b],col,3)
    for i,(x,y) in enumerate(GN):
        pal=CANDP[(i+2)%6]
        if hl==i: pal=CANDP[5]
        person(dd,x,y,t,pal,2.6,i,hl=(i==hl or i in friends))
    if cards:
        for i,(txt,col) in cards.items(): numcard(dd,GN[i][0],GN[i][1]+26,txt,col,10)
HEADS={'s1':[('Tes amis ont ',CREAM),('plus d’amis',GOLD),(' que toi',CREAM)],
 's2':[('Vrai',GRN),(' ou ',CREAM),('faux',RED),(' ?',CREAM)],
 's3':[('Imagine un ',CREAM),('village',CORAL)],
 's4':[('Chacun compte ',CREAM),('ses amis',CYAN)],
 's5':[('Puis les amis de ',CREAM),('ses amis',GOLD)],
 's6':[('Il fait la ',CREAM),('moyenne',CORAL)],
 'q':[('Nos amis en ont ',CREAM),('plus',GOLD),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('vrai',GRN)],
 'r1':[('Un village de ',CREAM),('5',GOLD),(' personnes',CREAM)],
 'r2':[('Une ',CREAM),('star',GOLD),(' qui connaît tous',CREAM)],
 'r3':[('4 villageois',CORAL),(' : la star seule',CREAM)],
 'r4':[('Un ami chacun : ',CREAM),('la star',GOLD)],
 'r5':[('Nous : ',CREAM),('1,6 ami',CYAN)],
 'r6':[('Nos amis : ',CREAM),('3,4 amis',GOLD)],
 'r7':[('La star est ',CREAM),('plus croisée',CORAL)],
 'r8':[('Presque ',CREAM),('partout',GOLD)],
 'r9':[('Le piège : ',CREAM),('amis semblables',CORAL)],
 'r10':[('Envoie-la !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            person(dd,58,240,t,CANDP[5],3.8,0); T(dd,'TOI',58,284,16,'press',12,CYAN,align='c')
            numcard(dd,58,150,'? AMIS',CYAN,10)
            FR=[(206,190),(262,250),(206,310)]
            for (x,y) in FR: ln(dd,(98,245),(x,y),EDGE,3)
            for i,(x,y) in enumerate(FR): person(dd,x,y,t,CANDP[i],3.2,i+1)
            numcard(dd,266,128,'PLUS ?',CORAL,10)
            if blink(t): stamp(dd,cx,104,'VRAI OU FAUX ?',GOLD,11)
            tagc(dd,cx,364,'TES AMIS ONT PLUS D’AMIS QUE TOI',GOLD)
        elif key=='s2':
            box(dd,28,130,116,120,fill=CARD,border=GRN,bw=4,shadow=(4,4,BLACK)); T(dd,'VRAI',86,172,36,'press',24,GRN,align='c'); check(dd,86,222,16,6,GRN)
            box(dd,168,130,116,120,fill=CARD,border=RED,bw=4,shadow=(4,4,BLACK)); T(dd,'FAUX',226,172,36,'press',24,RED,align='c'); xmark_(dd,226,222,14,6,RED)
            if blink(t): T(dd,'?',cx,290,50,'press',40,GOLD,align='c')
            tagc(dd,cx,364,'VRAI OU FAUX ?',GOLD)
        elif key=='s3':
            gen_village(dd,t)
            tagc(dd,cx,364,'UN VILLAGE, DES AMIS',CORAL)
        elif key=='s4':
            gen_village(dd,t,hl=4,cards={4:('3 AMIS',CYAN)} if lt>1.2 else None)
            tagc(dd,cx,364,'ON COMPTE SES AMIS',CYAN)
        elif key=='s5':
            fr=[1,3,5]
            gen_village(dd,t,hl=4,friends=(1,3,5),cards={i:(['4','2','3'][j],GOLD) for j,i in enumerate(fr) if lt>0.5+j*0.6})
            tagc(dd,cx,364,'PUIS LES AMIS DE SES AMIS',GOLD)
        elif key=='s6':
            numcard(dd,cx,112,'4 + 2 + 3',GOLD,16)
            if lt>0.5: T(dd,'÷ 3',cx,172,30,'press',24,CREAM,align='c')
            if lt>1.1: stamp(dd,cx,252,'LA MOYENNE',CORAL,16)
            tagc(dd,cx,364,'ON FAIT LA MOYENNE',CORAL)
        elif key=='q':
            numcard(dd,86,130,'TOI',CYAN,14); numcard(dd,226,130,'AMIS',GOLD,14)
            T(dd,'<',cx,200,50,'press',40,CREAM,align='c') if blink(t) else T(dd,'?',cx,200,50,'press',40,GOLD,align='c')
            numcard(dd,86,230,'? AMIS',CYAN,10); numcard(dd,226,230,'?? AMIS',GOLD,10)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'VRAI',cx,150,80,'press',60,GRN,align='c',shadow=(6,6,BLACK)); star(dd,30,120,t,6); star(dd,290,120,t+1,6)
            check(dd,cx,270,26,9,GRN)
            tagc(dd,cx,364,'LA RÉPONSE : VRAI',GRN)
        elif key=='r1':
            village(dd,t,links=False)
            tagc(dd,cx,364,'UN VILLAGE DE 5 PERSONNES',CORAL)
        elif key=='r2':
            village(dd,t,links=lt>0.8,hlstar=True)
            if lt>0.8: T(dd,'STAR',STAR[0]+52,STAR[1]-14,16,'press',12,GOLD)
            tagc(dd,cx,364,'UNE STAR CONNAÎT TOUT LE MONDE',GOLD)
        elif key=='r3':
            village(dd,t,hlvil=(0,1,2,3))
            tagc(dd,cx,364,'4 VILLAGEOIS, UN SEUL AMI : LA STAR',CORAL)
        elif key=='r4':
            village(dd,t,hlvil=(0,1,2,3),cards={0:('1',CYAN),1:('1',CYAN),2:('1',CYAN),3:('1',CYAN)} if lt>0.3 else None)
            if lt>1.8:
                numcard(dd,STAR[0],STAR[1]+34,'4 AMIS',GOLD,11)
            tagc(dd,cx,364,'LA STAR A 4 AMIS',GOLD)
        elif key=='r5':
            for j,v in enumerate(['4','1','1','1','1']): numcard(dd,32+j*62,118,v,GOLD if j==0 else CYAN,12)
            T(dd,'÷ 5',cx,190,30,'press',24,CREAM,align='c')
            if lt>1.2: numcard(dd,cx,252,'1,6 AMI',CYAN,20)
            tagc(dd,cx,364,'MOYENNE DES VILLAGEOIS : 1,6',CYAN)
        elif key=='r6':
            for j,v in enumerate(['4','4','4','4','1']): numcard(dd,32+j*62,118,v,GOLD if j<4 else CYAN,12)
            T(dd,'÷ 5',cx,190,30,'press',24,CREAM,align='c')
            if lt>1.0: numcard(dd,cx,252,'3,4 AMIS',GOLD,20)
            tagc(dd,cx,364,'MOYENNE DE LEURS AMIS : 3,4',GOLD)
        elif key=='r7':
            village(dd,t,hlstar=True,linkcol=GOLD)
            if blink(t): stamp(dd,cx,356-30,'ON LA CROISE PLUS SOUVENT',CORAL,9)
            tagc(dd,cx,364,'UNE STAR EST L’AMIE DE BEAUCOUP',GOLD)
        elif key=='r8':
            for j,(txt,thr) in enumerate([('ÉCOLE',1.9),('VILLAGE',2.7),('RÉSEAU SOCIAL',3.2)]):
                y=118+j*62
                if lt>thr-1.6: 
                    box(dd,28,y,256,50,fill=CARD,border=GRN if lt>thr else EDGE,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx-14,y+16,18,'silk7',16,CREAM,align='c')
                    if lt>thr: check(dd,262,y+22,10,5,GRN)
            tagc(dd,cx,364,'PRESQUE TOUS LES GROUPES',GRN)
        elif key=='r9':
            person(dd,86,200,t,CANDP[5],3.6,0); person(dd,226,200,t,CANDP[3],3.6,1)
            T(dd,'=',cx,170,40,'press',32,CREAM,align='c')
            if lt>0.5: xmark_(dd,cx,176,26,8,RED)
            numcard(dd,86,100,'TOI',CYAN,12); numcard(dd,226,100,'TES AMIS',CORAL,12)
            tagc(dd,cx,364,'LE PIÈGE : TES AMIS TE RESSEMBLENT',CORAL)
        elif key=='r10':
            bx,by=cx-46,150; box(dd,bx,by,92,64,fill=CREAM,border=DARK,bw=3,shadow=(4,4,BLACK))
            dd.line([(bx*S,by*S),((bx+46)*S,(by+34)*S),((bx+92)*S,by*S)],fill=DARK,width=3*S)
            if blink(t): arrow_r(dd,cx-20,260,48,GOLD)
            tagc(dd,cx,364,'À QUELQU’UN QUI VA SE TROMPER',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#058'
    def fn(lay,dd):
        cx=SW/2
        village(dd,t)
        T(dd,'TES AMIS ONT PLUS',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'D’AMIS QUE TOI ?',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="VRAI OU FAUX ?"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#059','ENVOIE-LA À QUELQU’UN')
