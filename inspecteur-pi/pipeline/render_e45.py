from render_e4x import *
import inspect
B.NUM='#045'
BL=(14,352); PK=(156,160); BRr=(298,352)
HILL=rgb('#245C42'); HILLD=rgb('#173D2C'); HILLT=rgb('#3E8A5E')
def lp(f): return (BL[0]+(PK[0]-BL[0])*f, BL[1]+(PK[1]-BL[1])*f)
def rp(f): return (BRr[0]+(PK[0]-BRr[0])*f, BRr[1]+(PK[1]-BRr[1])*f)
NL=(-0.803*18,-0.594*18); NR=(0.803*18,-0.594*18)
def hill(dd,t=0.0,flag=True):
    dd.polygon([(BL[0]*S,BL[1]*S),(PK[0]*S,PK[1]*S),(BRr[0]*S,BRr[1]*S)],fill=HILL)
    dd.line([(BL[0]*S,BL[1]*S),(PK[0]*S,PK[1]*S),(BRr[0]*S,BRr[1]*S)],fill=HILLT,width=4*S)
    for (x,y) in ((90,320),(150,300),(210,325),(240,300),(60,335),(180,340)): box(dd,x,y,6,4,fill=HILLD)
    if flag:
        box(dd,PK[0]-1,PK[1]-34,3,34,fill=CREAM); dd.polygon([((PK[0]+2)*S,(PK[1]-34)*S),((PK[0]+22)*S,(PK[1]-28)*S),((PK[0]+2)*S,(PK[1]-22)*S)],fill=CORAL)
def aline(dd,p,q,col,w=4):
    dd.line([(p[0]*S,p[1]*S),(q[0]*S,q[1]*S)],fill=col,width=w*S)
    a=math.atan2(q[1]-p[1],q[0]-p[0]); L=11
    pts=[(q[0]+L*0.6*math.cos(a),q[1]+L*0.6*math.sin(a)),(q[0]-L*math.cos(a)+L*0.7*math.sin(a),q[1]-L*math.sin(a)-L*0.7*math.cos(a)),(q[0]-L*math.cos(a)-L*0.7*math.sin(a),q[1]-L*math.sin(a)+L*0.7*math.cos(a))]
    dd.polygon([(x*S,y*S) for x,y in pts],fill=col)
def up_arrow(dd,col=CYAN,a=0.18,b=0.85,k=1.0):
    aline(dd,(lp(a)[0]+NL[0]*k,lp(a)[1]+NL[1]*k),(lp(b)[0]+NL[0]*k,lp(b)[1]+NL[1]*k),col)
def down_arrow(dd,col=GOLD,a=0.85,b=0.18,k=1.0):
    aline(dd,(rp(a)[0]+NR[0]*k,rp(a)[1]+NR[1]*k),(rp(b)[0]+NR[0]*k,rp(b)[1]+NR[1]*k),col)
def insp_on(dd,f,t,k=2.2,side='l'):
    x,y=(lp(f) if side=='l' else rp(f)); sprite(dd,DET,DPAL,x-10*k,y-24*k+math.sin(t*4)*1.2,k,20)
def sign(dd,cx,cy,txt,r=30,col=RED,size=22):
    disc(dd,cx,cy,r+3,DARK); disc(dd,cx,cy,r,CREAM,col,5); T(dd,txt,cx,cy-size/2-2,size+4,'press',size,DARK,align='c')
def tbar(dd,x,y,w,h,frac,col,border=GOLD):
    box(dd,x,y,w,h,fill=CARD,border=border,bw=3)
    if frac>0: box(dd,x+3,y+3,(w-6)*min(1,frac),h-6,fill=col)
HEADS={'s1':[('Presque tous ',CREAM),('se trompent',RED)],
 's2':[('Une colline d’',CREAM),('1 km',GOLD)],
 's3':[('Montée à ',CREAM),('30 km/h',CYAN)],
 's4':[('Moyenne : ',CREAM),('60 km/h',GOLD)],
 's5':[('Sur tout l’',CREAM),('aller-retour',CORAL)],
 'q':[('À quelle ',CREAM),('vitesse',CORAL),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('impossible',RED)],
 'r1':[('Pas ',CREAM),('90 km/h',RED)],
 'r2':[('Aller-retour : ',CREAM),('2 km',GOLD)],
 'r3':[('À 60 de moyenne : ',CREAM),('2 min',GOLD)],
 'r4':[('Monter à 30 : ',CREAM),('2 min',CYAN)],
 'r5':[('Plus ',CREAM),('une seconde',RED)],
 'r6':[('Même à 90 : ',CREAM),('45',RED)]}
HEADS['s6']=[('Réfléchis ',CREAM),('bien',GOLD)]
HEADS['r7']=[('Jamais ',CREAM),('60',RED)]
HEADS['r8']=[('Moyenne : ',CREAM),('le temps',GOLD)]
STORY=('s1','s2','s3','s4','s5','q','s6')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            hill(dd,t); up_arrow(dd,CYAN,k=0.9); down_arrow(dd,GOLD,k=0.9)
            lbl(dd,50,226,'30 KM/H',CYAN,10); lbl(dd,262,226,'? KM/H',GOLD,10)
            stamp(dd,cx,112,'MOYENNE 60',CORAL,13); sprite(dd,DET,DPAL,6,352-24*2.4,2.4,20)
            tagc(dd,cx,364,'ÇA PIÈGE PRESQUE TOUT LE MONDE',RED)
        elif key=='s2':
            hill(dd,t); insp_on(dd,0.35+0.1*math.sin(t),t)
            aline(dd,(lp(0.02)[0]+NL[0]*0.9,lp(0.02)[1]+NL[1]*0.9),(lp(0.98)[0]+NL[0]*0.9,lp(0.98)[1]+NL[1]*0.9),GOLD,3)
            lbl(dd,40,222,'1 KM',GOLD,11); tagc(dd,cx,364,'UNE COLLINE D’UN KILOMÈTRE',GOLD)
        elif key=='s3':
            hill(dd,t); insp_on(dd,0.2+min(0.5,lt*0.15),t); up_arrow(dd,CYAN,k=0.9)
            sign(dd,cx,118,'30',30,RED,24); T(dd,'KM/H',cx,150,14,'press',10,CREAM,align='c')
            tagc(dd,cx,364,'EN MONTÉE : 30 KM/H',CYAN)
        elif key=='s4':
            disc(dd,cx,190,66,DARK); disc(dd,cx,190,62,CARD,GOLD,5)
            T(dd,'60',cx,160,64,'press',52,GOLD,align='c',shadow=(5,5,BLACK)); T(dd,'KM/H',cx,222,16,'press',12,CREAM,align='c')
            stamp(dd,cx,300,'VITESSE MOYENNE',CORAL,11); star(dd,48,130,t,6); star(dd,266,130,t+1,6)
            tagc(dd,cx,364,'MOYENNE VISÉE : 60 KM/H',GOLD)
        elif key=='s5':
            hill(dd,t); up_arrow(dd,CYAN,k=0.9); down_arrow(dd,GOLD,k=0.9)
            lbl(dd,48,226,'ALLER',CYAN,10); lbl(dd,264,226,'RETOUR',GOLD,10); stamp(dd,cx,112,'ALLER-RETOUR',CORAL,12)
            tagc(dd,cx,364,'MOYENNE SUR TOUT LE TRAJET',CORAL)
        elif key=='q':
            sprite(dd,DET,DPAL,14,352-24*3.4+math.sin(t*4)*1.5,3.4,20)
            T(dd,'?',216,120,120,'press',100,GOLD,align='c',shadow=(5,5,BLACK)); stamp(dd,216,262,'KM/H ?',CORAL,13)
            tagc(dd,cx,364,'À QUELLE VITESSE REDESCENDRE ?',CORAL)
        elif key=='r0':
            T(dd,'!',cx,130,150,'press',120,RED,align='c',shadow=(7,7,BLACK)); star(dd,48,210,t,6); star(dd,264,210,t+1,6)
            stamp(dd,cx,320,'IMPOSSIBLE',RED,14); tagc(dd,cx,364,'LA RÉPONSE',GOLD)
        elif key=='r1':
            numcard(dd,cx,150,'90',CREAM,40); T(dd,'KM/H',cx,246,16,'press',12,CREAM,align='c')
            if lt>1.3: xmark_(dd,cx,190,58,8,RED); stamp(dd,cx,310,'FAUX',RED,14)
            tagc(dd,cx,364,'LA RÉPONSE DE BEAUCOUP',RED)
        elif key=='r2':
            hill(dd,t,False); up_arrow(dd,CYAN,k=0.9); down_arrow(dd,GOLD,k=0.9)
            lbl(dd,48,226,'1 KM',CYAN,10); lbl(dd,264,226,'1 KM',GOLD,10); stamp(dd,cx,112,'= 2 KM',CORAL,14)
            tagc(dd,cx,364,'ALLER-RETOUR : 2 KILOMÈTRES',CORAL)
        elif key=='r3':
            T(dd,'2 KM À 60 KM/H',cx,112,22,'press',14,CREAM,align='c',shadow=(3,3,BLACK))
            tbar(dd,36,176,240,44,0,GOLD); T(dd,'TEMPS TOTAL',cx,240,16,'silk7',11,GOLD,align='c',sp=1)
            T(dd,'2 MIN',cx,264,50,'press',40,GOLD,align='c',shadow=(4,4,BLACK))
            tagc(dd,cx,364,'À 60 DE MOYENNE : 2 MINUTES',GOLD)
        elif key=='r4':
            T(dd,'1 KM À 30 KM/H',cx,112,22,'press',14,CREAM,align='c',shadow=(3,3,BLACK))
            tbar(dd,36,176,240,44,min(1,lt/1.6),CYAN); T(dd,'MONTÉE',cx,240,16,'silk7',11,CYAN,align='c',sp=1)
            T(dd,'2 MIN',cx,264,50,'press',40,CYAN,align='c',shadow=(4,4,BLACK))
            tagc(dd,cx,364,'LA MONTÉE PREND 2 MINUTES',CYAN)
        elif key=='r5':
            tbar(dd,36,130,240,44,1,CYAN,GOLD); T(dd,'TEMPS TOTAL UTILISÉ',cx,190,16,'silk7',11,CYAN,align='c',sp=1)
            stamp(dd,cx,262,'0 SECONDE RESTANTE',RED,12); T(dd,'REDESCENDRE ?',cx,300,20,'press',14,CREAM,align='c',shadow=(3,3,BLACK))
            tagc(dd,cx,364,'PLUS DE TEMPS POUR REDESCENDRE',RED)
        elif key=='s6':
            sprite(dd,DET,DPAL,14,352-24*3.4+math.sin(t*4)*1.5,3.4,20)
            T(dd,'?',216,120,100,'press',80,GOLD,align='c',shadow=(5,5,BLACK)); T(dd,'?',130,150,50,'press',40,CYAN,align='c',shadow=(3,3,BLACK))
            stamp(dd,216,262,'RÉFLÉCHIS BIEN',CORAL,11); tagc(dd,cx,364,'CE N’EST PAS SI SIMPLE',CORAL)
        elif key=='r7':
            y=120+min(1,lt/2.0)*80
            aline(dd,(cx,104),(cx,214),CORAL,5); disc(dd,cx,y+30,18,rgb('#8A93C0'),DARK,3)
            numcard(dd,cx,250,'60',RED,30); xmark_(dd,cx,284,40,6,RED) if lt>1.8 else None
            tagc(dd,cx,364,'MÊME EN CHUTE LIBRE : JAMAIS 60',RED)
        elif key=='r8':
            box(dd,24,120,210,66,fill=CARD,border=GRN,bw=3,shadow=(3,3,BLACK)); T(dd,'LE TEMPS',129,141,30,'press',22,GRN,align='c'); check(dd,268,153,16,6,GRN) if lt>0.8 else None
            box(dd,24,214,210,66,fill=CARD,border=RED,bw=3,shadow=(3,3,BLACK)); T(dd,'LES VITESSES',129,236,26,'press',15,RED,align='c')
            if lt>1.6: xmark_(dd,268,247,14,6,RED)
            tagc(dd,cx,364,'ON CALCULE AVEC LE TEMPS',GOLD)
        elif key=='r6':
            numcard(dd,cx,116,'90 KM/H',CREAM,22); arrow_d(dd,cx,176,40,CORAL)
            lbl(dd,cx+78,192,'EN DESCENTE',GREY,9); numcard(dd,cx,226,'45',RED,38); T(dd,'KM/H DE MOYENNE',cx,300,16,'press',11,RED,align='c')
            tagc(dd,cx,364,'À 90 : SEULEMENT 45 DE MOYENNE',RED)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#045'
    def fn(lay,dd):
        hill(dd,t); up_arrow(dd,CYAN,k=0.9); down_arrow(dd,GOLD,k=0.9)
        sign(dd,60,170,'30',30,RED,24); T(dd,'?',262,150,100,'press',80,GOLD,align='c',shadow=(5,5,BLACK))
        sprite(dd,DET,DPAL,6,352-24*2.4,2.4,20)
        T(dd,'IMPOSSIBLE DE',SW/2,16,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'FAIRE 60 DE MOYENNE',SW/2,52,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DE LA COLLINE"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#046','ENREGISTRE CETTE ÉNIGME')
