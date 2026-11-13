from render_e2x import *
B.NUM='#038'
def tri(dd,pts,fill): dd.polygon([(x*S,y*S) for x,y in pts],fill=fill)
BRN=rgb('#7A4B2A'); BRN2=rgb('#C9B79A'); MANE=rgb('#2A1F18')
RIDER={'R':dict(MPAL,T='#FF7A59',P='#4A5078'),'C':dict(MPAL,T='#8FE3FF',P='#4A5078')}
for v in RIDER.values(): v['K']='#2A1F18'
SULT=dict(MPAL,T='#FFD23F',P='#8A3A2E',K='#EDEDED')
SAGE=dict(MPAL,T='#B08CE8',P='#6B4FA0',K='#F5F5F5')
TUN_R=CORAL; TUN_C=CYAN
def horse(dd,cx,feet,t,k=1.0,body=BRN,blank=GOLD,gait=0.0,face=1,rider=None,ring=None,ph=0.0):
    d=face
    def R(x,y,w,h,col):
        xx=cx+d*x*k-(w*k if d<0 else 0); box(dd,xx,feet+y*k,w*k,h*k,fill=col)
    def P(pts,col): tri(dd,[(cx+d*x*k,feet+y*k) for x,y in pts],col)
    sw=math.sin(t*(6+10*gait)+ph)*5*gait; lift=max(0,math.cos(t*(6+10*gait)+ph))*4*gait
    dark=lerpc(body,(0,0,0),0.35)
    for lx,ph2 in ((-19,0.0),(-11,math.pi),(11,math.pi*0.5),(19,math.pi*1.5)):
        s2=math.sin(t*(6+10*gait)+ph+ph2)*6*gait; l2=max(0,math.cos(t*(6+10*gait)+ph+ph2))*5*gait
        c=dark if lx in (-11,11) else body
        R(lx-3+s2,-22-l2,6,22,c); R(lx-3+s2,-5-l2,6,5,DARK)
    P([(-22,-42),(-32,-34),(-36,-14),(-30,-14),(-26,-30),(-22,-30)],MANE)
    R(-23,-44,46,26,body)
    R(-9,-44,18,12,blank); R(-9,-34,18,2,lerpc(blank,(0,0,0),0.3))
    P([(10,-42),(24,-44),(38,-66),(28,-72)],body)
    P([(24,-72),(38,-68),(50,-58),(46,-52),(34,-58),(26,-62)],body)
    P([(10,-42),(26,-72),(30,-72),(14,-42)],MANE)
    R(33,-70,4,4,DARK); R(27,-78,5,8,MANE)
    if ring: dd.ellipse([(cx-d*0-40*k)*S,(feet-86*k)*S,(cx+40*k)*S,(feet+4*k)*S],outline=ring,width=3*S)
    if rider:
        kk=k*2.1; b=math.sin(t*(6+10*gait))*1.5*gait
        sprite(dd,MAN[:10],RIDER[rider],cx-5*kk-2*k,feet-38*k-10*kk+b,kk,10)
def sky(dd,dusk=0.0):
    top=lerpc(rgb('#3A5FA8'),rgb('#120F2A'),dusk); bot=lerpc(rgb('#8FC0E8'),rgb('#E8704A'),dusk) if dusk<0.6 else lerpc(rgb('#E8704A'),rgb('#3A1F4A'),(dusk-0.6)/0.4)
    for i in range(14):
        box(dd,0,i*26,SW,26,fill=lerpc(top,bot,i/13))
def sun(dd,cx,cy,r=22,col=rgb('#FFE08A')):
    disc(dd,cx,cy,r+8,lerpc(col,rgb('#E8704A'),0.5)); disc(dd,cx,cy,r,col)
def dunes(dd,y=292,dusk=0.0):
    c1=lerpc(rgb('#C9A15A'),rgb('#3A2A3A'),dusk); c2=lerpc(rgb('#A8803F'),rgb('#2A1E2E'),dusk)
    tri(dd,[(0,y-24),(90,y-40),(200,y-12),(312,y-34),(312,396),(0,396)],c2)
    tri(dd,[(0,y+6),(110,y-6),(220,y+10),(312,y),(312,396),(0,396)],c1)
def palm(dd,x,y,k=1.0):
    box(dd,x-3*k,y-46*k,6*k,46*k,fill=rgb('#6B4A2E'))
    for dx,dy in ((-26,-8),(-14,-20),(14,-20),(26,-8),(0,-24)):
        tri(dd,[(x,y-46*k),(x+dx*k*0.5,y-46*k+dy*k*0.2-6*k),(x+dx*k,y-46*k-dy*k*0.3+10*k),(x+dx*k*0.5,y-46*k-2*k)],rgb('#3FA05A'))
def oasis(dd,x,y,k=1.0):
    dd.ellipse([(x-34*k)*S,(y-4*k)*S,(x+34*k)*S,(y+10*k)*S],fill=CYAN); palm(dd,x-18*k,y,k); palm(dd,x+18*k,y+2,k*0.8)
def desert(dd,dusk=0.0,sunpos=(250,150),y=292):
    sky(dd,dusk)
    if sunpos: sun(dd,sunpos[0],sunpos[1])
    dunes(dd,y,dusk)
def chest(dd,cx,y,k=1.0):
    box(dd,cx-28*k,y,56*k,34*k,fill=rgb('#8A5A3A'),border=DARK,bw=3); box(dd,cx-28*k,y-14*k,56*k,16*k,fill=rgb('#A8723F'),border=DARK,bw=3)
    box(dd,cx-5*k,y+6*k,10*k,12*k,fill=GOLD,border=DARK,bw=2)
    for i in range(5): disc(dd,cx-20*k+i*10*k,y-14*k,5*k,GOLD,DARK,1)
def flagline(dd,x,y0=150,y1=300):
    for i in range(int((y1-y0)/10)):
        for j in range(2): box(dd,x+j*10,y0+i*10,10,10,fill=CREAM if (i+j)%2==0 else DARK)
def dust(dd,x,y,t,n=5):
    for i in range(n):
        f=((t*2.5+i*0.2)%1.0); disc(dd,x-f*60-i*4,y-f*14,3+f*6,lerpc(rgb('#D9B77A'),rgb('#A8803F'),f))
def speed(dd,x0,x1,ys,t):
    for i,y in enumerate(ys):
        o=((t*4+i*0.37)%1.0)*40
        box(dd,x0+o,y,36,3,fill=lerpc(CREAM,rgb('#8FC0E8'),0.4))
def swap(dd,cx,y,t,col=GOLD):
    p=math.sin(t*4)*3
    arrow(dd,cx-50,cx+50,y-8+p,col,4); arrow(dd,cx+50,cx-50,y+10-p,col,4)
def arrow(dd,x1,x2,y,col,w=4):
    d=1 if x2>x1 else -1
    box(dd,min(x1,x2)+(0 if d>0 else 12),y-w/2,abs(x2-x1)-12,w,fill=col); tri(dd,[(x2,y),(x2-d*12,y-8),(x2-d*12,y+8)],col)
def man(dd,cx,feet,t,pal,k=3.0): sprite(dd,MAN,pal,cx-5*k,feet-14*k+math.sin(t*3)*1.2,k,10)
def sage(dd,cx,feet,t,k=3.2):
    man(dd,cx,feet,t,SAGE,k); box(dd,cx-3*k,feet-14*k+5.5*k,6*k,3*k,fill=rgb('#F5F5F5'))
    box(dd,cx+7*k,feet-22*k,2.5,22*k,fill=rgb('#6B4A2E')); disc(dd,cx+7*k+1,feet-22*k,4,GOLD)
def sultan(dd,cx,feet,t,k=3.2):
    man(dd,cx,feet,t,SULT,k); box(dd,cx-3*k,feet-14*k+5.5*k,6*k,3.5*k,fill=rgb('#EDEDED')); box(dd,cx-4*k,feet-14*k-1.5*k,8*k,3*k,fill=CORAL)
def bubble2(dd,x,y,w,h,txt,col=GOLD,size=16):
    box(dd,x,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,x+w/2,y+(h-size-4)/2,size+4,'press',size,col,align='c')
HEADS={'s1':[('Arriver le ',CREAM),('dernier',CORAL),(' !',CREAM)],
 's2':[('Deux fils, ',CREAM),('un héritage',GOLD)],
 's3':[('Course de ',CREAM),('chevaux',GOLD)],
 's4':[('Le cheval ',CREAM),('dernier',CORAL),(' gagne',CREAM)],
 's5':[('Chacun ',CREAM),('retient',CORAL),(' son cheval',CREAM)],
 's6':[('Ils s’arrêtent, le ',CREAM),('soleil',GOLD),(' se couche',CREAM)],
 's7':[('Un ',CREAM),('sage',CYAN),(' s’approche',CREAM)],
 's8':[('Les frères ',CREAM),('galopent',GOLD),(' !',CREAM)],
 'q':[('Que leur a dit le ',CREAM),('sage',CYAN),(' ?',CREAM)],
 'r0':[('Échangez ',CREAM),('vos chevaux',GOLD),(' !',CREAM)],
 'r1':[('Chacun monte le ',CREAM),('cheval',GOLD),(' de l’autre',CREAM)],
 'r2':[('Son propre cheval ',CREAM),('dernier',CORAL)],
 'r3':[('Donc ',CREAM),('premier',GRN),(' sur l’autre',CREAM)],
 'r4':[('Plus personne ',CREAM),('ne ralentit',CORAL)],
 'r5':[('À toute ',CREAM),('vitesse',GOLD),(' !',CREAM)],
 'r6':[('Le piège : ',CREAM),('ralentir',RED)],
 'r7':[('L’astuce : ',CREAM),('changer',GOLD),(' de monture',CREAM)],
 'r8':[('La course ',CREAM),('reprend',GRN),(' !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','q')
def pair(dd,t,x1,x2,feet,gait,swapped=False,k=0.95,face=1,ph=0.0):
    a,b=('C','R') if swapped else ('R','C')   # cavalier sur le cheval 1 (blanket coral) / cheval 2 (blanket cyan)
    horse(dd,x1,feet,t,k,body=BRN,blank=CORAL,gait=gait,face=face,rider=a,ph=ph)
    horse(dd,x2,feet,t,k,body=BRN2,blank=CYAN,gait=gait,face=face,rider=b,ph=ph+1.3)
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            desert(dd,0.0,None); chest(dd,SW/2,200,2.2); star(dd,50,150,t,5); star(dd,262,160,t+1,5); stamp(dd,SW/2,310,'LE DERNIER GAGNE',GOLD,14); tagc(dd,SW/2,364,'UNE FORTUNE À GAGNER',GOLD)
        elif key=='s2':
            desert(dd,0.0,(262,140)); sultan(dd,156,GY-30,t,3.4); chest(dd,52,GY-60,1.0)
            man(dd,252,GY-30,t,RIDER['R'],2.4); man(dd,276,GY-30,t,RIDER['C'],2.4) if False else None
            man(dd,208,GY-30,t,RIDER['C'],2.4); tagc(dd,SW/2,364,'DEUX FILS, UN SEUL HÉRITAGE',GOLD)
        elif key=='s3':
            desert(dd,0.0,(40,140)); oasis(dd,262,276,1.0)
            x=60+lt*10; pair(dd,t,x,x+100,300,0.8,k=0.8); tagc(dd,SW/2,364,'UNE COURSE JUSQU’À L’OASIS',CYAN)
        elif key=='s4':
            desert(dd,0.0,None); flagline(dd,258,170,300)
            horse(dd,244,300,t,0.8,body=BRN,blank=CORAL,gait=0.0,rider='R'); horse(dd,92,300,t,0.8,body=BRN2,blank=CYAN,gait=0.0,rider='C',ring=GOLD)
            lbl(dd,244,112,'1ER',CREAM,12); lbl(dd,92,112,'DERNIER',GOLD,12); chest(dd,92,152,0.6); tagc(dd,SW/2,364,'LE CHEVAL DERNIER GAGNE',GOLD)
        elif key=='s5':
            desert(dd,0.0,None); pair(dd,t,90,220,300,0.12,k=0.9)
            for cx in (90,220): arrow(dd,cx+30,cx-30,134,CORAL,4)
            stamp(dd,SW/2,196,'FREIN !',RED,16); tagc(dd,SW/2,364,'CHACUN RETIENT SON CHEVAL',CORAL)
        elif key=='s6':
            p=ease(lt/dur); desert(dd,0.1+0.9*p,(60,200+120*p)); pair(dd,t,90,220,306,0.0,k=0.9)
            T(dd,'Z',140,170,20,'press',14,CREAM,align='c') if False else None
            tagc(dd,SW/2,364,'ILS S’ARRÊTENT : LE SOLEIL SE COUCHE',GOLD)
        elif key=='s7':
            desert(dd,0.8,(250,310)); pair(dd,t,170,260,300,0.0,k=0.72)
            sx=min(70,-20+lt*60); sage(dd,sx,GY-26,t,3.0)
            bubble2(dd,sx+40,130,72,34,'...',CREAM,18); tagc(dd,SW/2,364,'UN SAGE LEUR CHUCHOTE UNE PHRASE',CYAN)
        elif key=='s8':
            desert(dd,0.0,(40,140)); oasis(dd,264,276,0.9); speed(dd,0,200,(150,176,200,226),t)
            pair(dd,t,110+(lt*10),220+(lt*10),300,1.0,k=0.8,ph=0.0); dust(dd,60,300,t); dust(dd,170,300,t+0.4)
            tagc(dd,SW/2,364,'LES DEUX FRÈRES PARTENT AU GALOP !',GOLD)
        elif key=='q':
            desert(dd,0.8,(250,310)); sage(dd,110,GY-26,t,3.8); bubble2(dd,170,124,110,120,'?',GOLD,70); tagc(dd,SW/2,364,'QUE LEUR A DIT LE SAGE ?',CORAL)
        elif key=='r0':
            desert(dd,0.0,(262,140)); pair(dd,t,90,220,300,0.0,k=0.9); swap(dd,SW/2,150,t); stamp(dd,SW/2,222,'ÉCHANGEZ !',GOLD,18); tagc(dd,SW/2,364,'ÉCHANGEZ VOS CHEVAUX',GOLD)
        elif key=='r1':
            desert(dd,0.0,(156,200)); ph=ease(lt/0.9)
            pair(dd,t,90,220,300,0.0,swapped=True,k=0.9)
            lbl(dd,90,112,'CHEVAL ROUGE',CORAL,10); lbl(dd,220,112,'CHEVAL BLEU',CYAN,10)
            tagc(dd,SW/2,364,'ON MONTE LE CHEVAL DE L’AUTRE',CREAM)
        elif key=='r2':
            desert(dd,0.0,None); flagline(dd,258,170,300)
            horse(dd,244,300,t,0.8,body=BRN,blank=CORAL,rider='C'); horse(dd,92,300,t,0.8,body=BRN2,blank=CYAN,rider='R',ring=GOLD)
            lbl(dd,92,112,'SON CHEVAL',GOLD,10); tagc(dd,SW/2,364,'SON CHEVAL DOIT FINIR DERNIER',CORAL)
        elif key=='r3':
            desert(dd,0.0,None); flagline(dd,258,170,300)
            horse(dd,244,300,t,0.8,body=BRN,blank=CORAL,rider='C',ring=GRN); horse(dd,92,300,t,0.8,body=BRN2,blank=CYAN,rider='R')
            lbl(dd,244,112,'LUI : PREMIER !',GRN,10); tagc(dd,SW/2,364,'IL DOIT DONC ARRIVER PREMIER',GRN)
        elif key=='r4':
            desert(dd,0.0,(156,215)); pair(dd,t,90,220,300,0.6,swapped=True,k=0.9)
            stamp(dd,SW/2,150,'PLUS DE FREIN',RED,13); tagc(dd,SW/2,364,'PLUS PERSONNE NE RALENTIT',CORAL)
        elif key=='r5':
            desert(dd,0.0,(40,140)); oasis(dd,264,276,0.9); speed(dd,0,200,(150,176,200,226),t)
            pair(dd,t,110,220,300,1.0,swapped=True,k=0.8); dust(dd,60,300,t); dust(dd,170,300,t+0.4); tagc(dd,SW/2,364,'À TOUTE VITESSE !',GOLD)
        elif key=='r6':
            desert(dd,0.0,None); pair(dd,t,90,220,300,0.1,k=0.9); xmark_(dd,SW/2,196,22,7,RED)
            stamp(dd,SW/2,128,'LE PIÈGE : RALENTIR',RED,13); tagc(dd,SW/2,364,'CROIRE QU’IL FALLAIT RALENTIR',RED)
        elif key=='r7':
            desert(dd,0.0,None); pair(dd,t,90,220,300,0.0,swapped=(int(t*1.5)%2==1),k=0.9); swap(dd,SW/2,150,t)
            star(dd,40,140,t,5); star(dd,272,150,t+1,5); stamp(dd,SW/2,222,'CHANGER DE MONTURE',GOLD,13); tagc(dd,SW/2,364,'L’ASTUCE : CHANGER DE MONTURE',GOLD)
        elif key=='r8':
            desert(dd,0.0,(40,140)); oasis(dd,264,276,0.9); flagline(dd,236,176,296); speed(dd,0,200,(150,176,200,226),t)
            pair(dd,t,90+lt*14,196+lt*14,300,1.0,swapped=True,k=0.78); dust(dd,40,300,t); dust(dd,146,300,t+0.4); tagc(dd,SW/2,364,'ET LA COURSE REPREND !',GRN)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#038'
    def fn(lay,dd):
        desert(dd,0.0,(250,150)); oasis(dd,262,276,0.8); speed(dd,0,160,(170,196,222),t)
        pair(dd,t,100,222,300,1.0,swapped=True,k=0.8); dust(dd,50,300,t); dust(dd,170,300,t+0.4)
        T(dd,'GAGNE EN ARRIVANT',SW/2,16,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'LE DERNIER ?',SW/2,52,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DE LA COURSE À L'ENVERS"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#039')
