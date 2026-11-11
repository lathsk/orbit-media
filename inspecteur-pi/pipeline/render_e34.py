from render_e2x import *
B.NUM='#034'
TAN=rgb('#C9A15E'); TAN2=rgb('#A98448'); ASH=rgb('#6B5B6E')
HEADS={'s1':[('Un ',CREAM),('feu d’artifice !',GOLD)],
 's2':[('Départ dans ',CREAM),('45 minutes',CORAL)],
 's3':[('Ni ',CREAM),('montre,',GOLD),(' ni ',CREAM),('horloge',GOLD)],
 's4':[('Deux ',CREAM),('mèches',GOLD),(' + briquet',CREAM)],
 's5':[('Chaque mèche : ',CREAM),('1 heure',CORAL)],
 's6':[('Vitesse ',CREAM),('irrégulière',RED)],
 's7':[('Une moitié ',CREAM),('rapide',CORAL)],
 's8':[('L’autre ',CREAM),('très lente',CYAN)],
 's9':[('Couper',RED),(' ne sert à rien',CREAM)],
 's10':[('Pas ',CREAM),('la moitié',RED),(' du temps',CREAM)],
 'q':[('Mesurer ',CREAM),('45 minutes ?',GOLD)],
 'r0':[('Deux mèches, ',CREAM),('un briquet',GOLD)],
 'r1':[('Mèche 1 : ',CREAM),('deux bouts',CORAL)],
 'r2':[('Mèche 2 : ',CREAM),('un seul bout',CYAN)],
 'r3':[('En même ',CREAM),('temps',GOLD)],
 'r4':[('Mèche 1 : ',CREAM),('2 fois plus vite',CORAL)],
 'r5':[('Éteinte : ',CREAM),('30 minutes',GOLD)],
 'r6':[('Il reste ',CREAM),('30 minutes',CYAN)],
 'r7':[('On allume ',CREAM),('l’autre bout',CORAL)],
 'r8':[('Elles se ',CREAM),('rejoignent',GOLD)],
 'r9':[('30 + 15 = ',CREAM),('45 minutes !',GRN)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','q')
NF=44
def flame(dd,x,y,t,k=1.0,ph=0.0):
    j=math.sin(t*14+ph)*1.2
    box(dd,x-4*k,y-8*k+j,8*k,10*k,fill=RED); box(dd,x-3*k,y-13*k+j,6*k,9*k,fill=ORG); box(dd,x-1.5*k,y-17*k+j,3*k,7*k,fill=GOLD)
def fuse(dd,y,bl=0.0,br=0.0,t=0.0,fl=False,fr=False,x0=30,x1=282,name=None,col=None):
    w=(x1-x0)/NF
    for i in range(NF):
        f=(i+0.5)/NF; burnt=(f<bl) or (f>1-br)
        c=ASH if burnt else (TAN if i%2==0 else TAN2)
        if col is not None and not burnt: c=col if i%2==0 else lerpc(col,(0,0,0),0.18)
        box(dd,x0+i*w,y-6,w+0.6,12,fill=c)
    box(dd,x0-3,y-8,3,16,fill=DARK); box(dd,x1,y-8,3,16,fill=DARK)
    if fl: flame(dd,x0+max(bl,0)*(x1-x0),y-5,t,1.0)
    if fr: flame(dd,x1-max(br,0)*(x1-x0),y-5,t,1.0,ph=1.7)
    if name: T(dd,name,x0,y+10,14,'silk7',9,CREAM,sp=1)
def timer(dd,minutes,col=GOLD,y=100):
    m=int(minutes+1e-6); s=int(round((minutes-m)*60))%60
    txt='%02d:%02d'%(m,s); box(dd,SW/2-62,y,124,36,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,SW/2,y+7,26,'press',20,col,align='c')
def bar45(dd,minutes,y=330):
    box(dd,24,y,264,14,fill=CARD,border=EDGE,bw=2); w=int(260*min(1,minutes/45.0))
    if w>2: box(dd,26,y+2,w,10,fill=CORAL)
    for m,lab in ((0,'0'),(30,'30'),(45,'45')): T(dd,lab,26+int(260*m/45.0),y+16,12,'silk7',8,GREY,align='c')
def burst(dd,cx,cy,t,col,ph=0.0,R=34):
    p=((t*0.9+ph)%1.0); r=6+R*p
    for i in range(12):
        a=i*math.pi/6+ph*3; x=cx+r*math.cos(a); y=cy+r*math.sin(a)
        if p<0.85: box(dd,x-2,y-2,4,4,fill=col)
        box(dd,cx+(r*0.55)*math.cos(a)-1,cy+(r*0.55)*math.sin(a)-1,2,2,fill=lerpc(col,(255,255,255),0.5))
def lighter(dd,x,y,on,t):
    box(dd,x,y,18,30,fill=rgb('#8A93C0'),border=DARK,bw=2); box(dd,x+3,y-5,12,6,fill=rgb('#5A6BA8'),border=DARK,bw=1)
    if on: flame(dd,x+9,y-5,t,0.8)
def scissors(dd,cx,cy,col=RED):
    xmark_(dd,cx,cy,12,5,col)
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            burst(dd,80,170,t,GOLD,0.0); burst(dd,224,150,t,CORAL,0.35); burst(dd,156,226,t,CYAN,0.7,R=40)
            insp(dd,SW/2,GY,t,k=2.2); tagc(dd,SW/2,364,'LE FEU D’ARTIFICE',GOLD)
        elif key=='s2':
            timer(dd,45,CORAL,y=128); T(dd,'MIN',SW/2,176,16,'silk7',11,CREAM,align='c',sp=2) if False else None
            burst(dd,80,250,t,GOLD,0.2,R=26); burst(dd,232,250,t,CYAN,0.6,R=26); lbl(dd,SW/2,190,'DÉPART DANS EXACTEMENT',CORAL,10)
            tagc(dd,SW/2,364,'QUARANTE-CINQ MINUTES',CORAL)
        elif key=='s3':
            clock(dd,SW/2,196,52,10,10); xmark_(dd,SW/2,196,60,8,RED)
            tagc(dd,SW/2,364,'AUCUN MOYEN DE MESURER',RED)
        elif key=='s4':
            fuse(dd,170,t=t,name='MÈCHE 1'); fuse(dd,240,t=t,name='MÈCHE 2'); lighter(dd,SW/2-9,290,int(t*4)%2==0,t)
            tagc(dd,SW/2,364,'DEUX MÈCHES, UN BRIQUET',GOLD)
        elif key=='s5':
            fuse(dd,170,t=t,name='MÈCHE 1'); fuse(dd,240,t=t,name='MÈCHE 2')
            lbl(dd,SW/2,276,'CHACUNE BRÛLE 60 MINUTES',CORAL,11); tagc(dd,SW/2,364,'EXACTEMENT UNE HEURE',CORAL)
        elif key=='s6':
            fuse(dd,185,t=t,name='MÈCHE'); lbl(dd,SW/2,232,'PAS À VITESSE RÉGULIÈRE',RED,11)
            T(dd,'?',92,140,30,'press',24,GOLD,align='c'); T(dd,'?',220,140,30,'press',24,CYAN,align='c')
            tagc(dd,SW/2,364,'VITESSE IRRÉGULIÈRE',RED)
        elif key=='s7':
            p=min(1,lt/(dur*0.7)); fuse(dd,185,bl=p*0.5,t=t,fl=True,name='MÈCHE'); lbl(dd,92,232,'MOITIÉ RAPIDE',CORAL,10)
            T(dd,'>>>',92,150,18,'press',14,CORAL,align='c'); tagc(dd,SW/2,364,'UNE MOITIÉ BRÛLE VITE',CORAL)
        elif key=='s8':
            p=min(1,lt/(dur*0.9)); fuse(dd,185,bl=0.5+p*0.07,t=t,fl=True,name='MÈCHE'); lbl(dd,220,232,'MOITIÉ TRÈS LENTE',CYAN,10)
            T(dd,'>',220,150,18,'press',14,CYAN,align='c'); tagc(dd,SW/2,364,'L’AUTRE TRÈS LENTEMENT',CYAN)
        elif key=='s9':
            fuse(dd,185,t=t,name='MÈCHE'); scissors(dd,SW/2,190); dd.line([(SW/2*S,170*S),(SW/2*S,210*S)],fill=GOLD,width=2*S)
            lbl(dd,SW/2,236,'COUPER AU MILIEU ?',RED,11); tagc(dd,SW/2,364,'IMPOSSIBLE DE COUPER',RED)
        elif key=='s10':
            fuse(dd,185,bl=0.5,t=t,name='MÈCHE'); T(dd,'PAS 30 MIN',SW/2,230,18,'silk7',13,RED,align='c')
            T(dd,'?',SW/2,130,40,'press',32,GOLD,align='c',shadow=(3,3,BLACK)); tagc(dd,SW/2,364,'PAS LA MOITIÉ DU TEMPS',RED)
        elif key=='q':
            insp(dd,64,GY,t,k=2.4); T(dd,'45',SW/2+30,130,90,'press',70,GOLD,align='c',shadow=(5,5,BLACK)); T(dd,'MINUTES ?',SW/2+30,222,30,'press',20,CREAM,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'COMMENT MESURER 45 MIN ?',CORAL)
        elif key=='r0':
            fuse(dd,185,t=t,name='MÈCHE 1'); fuse(dd,270,t=t,name='MÈCHE 2'); lighter(dd,SW/2-9,300,True,t)
            tagc(dd,SW/2,364,'TOUT SE JOUE AU BRIQUET',GOLD)
        elif key=='r1':
            fuse(dd,185,t=t,fl=True,fr=True,name='MÈCHE 1'); fuse(dd,270,t=t,name='MÈCHE 2')
            lbl(dd,SW/2,222,'ALLUMÉE AUX DEUX BOUTS',CORAL,10); tagc(dd,SW/2,364,'LA 1RE : DES DEUX CÔTÉS',CORAL)
        elif key=='r2':
            fuse(dd,185,t=t,fl=True,fr=True,name='MÈCHE 1'); fuse(dd,270,t=t,fl=True,name='MÈCHE 2')
            lbl(dd,SW/2,302,'ALLUMÉE D’UN SEUL BOUT',CYAN,10); tagc(dd,SW/2,364,'LA 2E : D’UN SEUL CÔTÉ',CYAN)
        elif key=='r3':
            timer(dd,0,GOLD); fuse(dd,185,t=t,fl=True,fr=True,name='MÈCHE 1'); fuse(dd,270,t=t,fl=True,name='MÈCHE 2'); bar45(dd,0)
            tagc(dd,SW/2,364,'ON LANCE LE TEMPS',GOLD)
        elif key=='r4':
            p=min(1,lt/(dur*0.92)); m=30*p
            timer(dd,m,GOLD); fuse(dd,185,bl=p*0.5,br=p*0.5,t=t,fl=p<1,fr=p<1,name='MÈCHE 1'); fuse(dd,270,bl=p*0.5,t=t,fl=True,name='MÈCHE 2'); bar45(dd,m)
            tagc(dd,SW/2,364,'DEUX FLAMMES : 2 FOIS PLUS VITE',CORAL)
        elif key=='r5':
            timer(dd,30,GOLD); fuse(dd,185,bl=0.5,br=0.5,t=t,name='MÈCHE 1'); fuse(dd,270,bl=0.5,t=t,fl=True,name='MÈCHE 2'); bar45(dd,30)
            lbl(dd,SW/2,222,'MÈCHE 1 ÉTEINTE',GOLD,10); tagc(dd,SW/2,364,'EXACTEMENT 30 MINUTES',GOLD)
        elif key=='r6':
            timer(dd,30,GOLD); fuse(dd,185,bl=0.5,br=0.5,t=t,name='MÈCHE 1'); fuse(dd,270,bl=0.5,t=t,fl=True,name='MÈCHE 2',x0=30); bar45(dd,30)
            lbl(dd,220,298,'IL RESTE 30 MIN',CYAN,10); tagc(dd,SW/2,364,'30 MINUTES DE MÈCHE 2',CYAN)
        elif key=='r7':
            timer(dd,30,GOLD); fuse(dd,185,bl=0.5,br=0.5,t=t,name='MÈCHE 1'); fuse(dd,270,bl=0.5,t=t,fl=True,fr=(lt>0.45),name='MÈCHE 2'); bar45(dd,30)
            lbl(dd,SW/2,298,'ON ALLUME L’AUTRE BOUT',CORAL,10); tagc(dd,SW/2,364,'L’AUTRE BOUT DE LA MÈCHE 2',CORAL)
        elif key=='r8':
            p=min(1,lt/(dur*0.92)); m=30+15*p
            timer(dd,m,GOLD); fuse(dd,185,bl=0.5,br=0.5,t=t,name='MÈCHE 1'); fuse(dd,270,bl=0.5+p*0.25,br=p*0.25,t=t,fl=p<1,fr=p<1,name='MÈCHE 2'); bar45(dd,m)
            tagc(dd,SW/2,364,'ELLES SE RENCONTRENT : 15 MIN',GOLD)
        elif key=='r9':
            timer(dd,45,GRN); fuse(dd,185,bl=0.5,br=0.5,t=t,name='MÈCHE 1'); fuse(dd,270,bl=0.5,br=0.5,t=t,name='MÈCHE 2'); bar45(dd,45)
            burst(dd,70,140,t,GOLD,0.0,R=24) if False else None
            stamp(dd,SW/2,228,'30 + 15 = 45',GRN,14); star(dd,40,118,t,4); star(dd,272,118,t,4); tagc(dd,SW/2,364,'QUARANTE-CINQ MINUTES !',GRN)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#034'
    def fn(lay,dd):
        burst(dd,70,170,t,GOLD,0.0); burst(dd,244,160,t,CORAL,0.4); burst(dd,156,130,t,CYAN,0.7,R=30)
        fuse(dd,262,t=t,fl=True,fr=True); fuse(dd,296,t=t,fl=True); insp(dd,SW/2,350,t,k=1.4)
        T(dd,'2 MÈCHES, 45 MINUTES',SW/2,10,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'AUCUNE MONTRE !',SW/2,44,36,'anton',26,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DES DEUX MÈCHES"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#035')
