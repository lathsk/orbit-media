from render_e4x import *
import inspect, math
B.NUM='#059'
WOOD=rgb('#B5763A'); WOOD2=rgb('#8A5527')
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
def bat(dd,cx,cy,w=150,col=None):
    """batte horizontale centrée en (cx,cy)"""
    col=col or WOOD; x0=cx-w/2
    box(dd,x0,cy-4,w*0.42,8,fill=col,border=DARK,bw=1)           # manche
    box(dd,x0-5,cy-7,7,14,fill=WOOD2,border=DARK,bw=1)            # pommeau
    box(dd,x0+w*0.40,cy-9,w*0.60,18,fill=col,border=DARK,bw=1)  # fût
    box(dd,x0+w*0.45,cy-6,w*0.50,3,fill=lerpc(col,(255,255,255),0.35))
def ball(dd,cx,cy,r=12):
    dd.ellipse([(cx-r-2)*S,(cy-r-2)*S,(cx+r+2)*S,(cy+r+2)*S],fill=DARK)
    dd.ellipse([(cx-r)*S,(cy-r)*S,(cx+r)*S,(cy+r)*S],fill=CREAM)
    dd.arc([(cx-r*0.7)*S,(cy-r*0.7)*S,(cx+r*0.7)*S,(cy+r*0.7)*S],200,320,fill=CORAL,width=2*S)
    dd.arc([(cx-r*0.7)*S,(cy-r*0.7)*S,(cx+r*0.7)*S,(cy+r*0.7)*S],20,140,fill=CORAL,width=2*S)
def seg(dd,x,y,w,h,col,txt,tcol=None,size=12):
    box(dd,x,y,w,h,fill=col,border=CREAM,bw=3)
    if txt: T(dd,txt,x+w/2,y+h/2-size/2-1,size+4,'press',size,tcol or DARK,align='c')
def brace(dd,x1,x2,y,col=CREAM):
    box(dd,x1,y,x2-x1,3,fill=col); box(dd,x1,y-6,3,9,fill=col); box(dd,x2-3,y-6,3,9,fill=col)
HEADS={'s1':[('Ta première ',CREAM),('réponse',GOLD),(' sera ',CREAM),('fausse',RED)],
 's2':[('Batte + balle : ',CREAM),('1,10 €',GOLD)],
 's3':[('La batte : ',CREAM),('1 € de plus',CYAN)],
 'q':[('Combien coûte ',CREAM),('la balle',CORAL),(' ?',CREAM)],
 'r0':[('La balle : ',CREAM),('5 centimes',GRN)],
 'r1':[('Les ',CREAM),('étudiants',CYAN),(' aussi !',CREAM)],
 'r2':[('Ton cerveau : ',CREAM),('0,10 €',RED)],
 'r3':[('Mais alors le total ',CREAM),('1,20 €',RED)],
 'r4':[('Batte = ',CREAM),('balle',CORAL),(' + ',CREAM),('1 €',CYAN)],
 'r5':[('2 balles',CORAL),(' + ',CREAM),('1 €',CYAN),(' = 1,10 €',GOLD)],
 'r6':[('On enlève ',CREAM),('l’euro',CYAN)],
 'r7':[('Une balle : ',CREAM),('5 centimes',GRN)],
 'r8':[('La batte : ',CREAM),('1,05 €',GOLD)],
 'r9':[('On ',CREAM),('vérifie',GRN)],
 'r10':[('Le piège : ',CREAM),('couper 1,10',CORAL)],
 'r11':[('Enregistre-la !',CREAM)]}
STORY=('s1','s2','s3','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            bat(dd,cx-20,170,170); ball(dd,cx+96,170,14)
            numcard(dd,cx,226,'1,10 €',GOLD,22)
            if blink(t): T(dd,'?',cx,292,40,'press',32,RED,align='c')
            tagc(dd,cx,364,'TA PREMIÈRE RÉPONSE EST FAUSSE',RED)
        elif key=='s2':
            bat(dd,cx-60,150,130); ball(dd,cx+60,150,14)
            T(dd,'+',cx,138,30,'press',24,CREAM,align='c')
            arrow_d(dd,cx,184,26,CREAM)
            numcard(dd,cx,222,'1,10 €',GOLD,24)
            tagc(dd,cx,364,'BATTE + BALLE = 1,10 € EN TOUT',GOLD)
        elif key=='s3':
            seg(dd,30,150,70,44,CORAL,'B',size=14); lbl(dd,65,124,'BALLE',CORAL,9)
            seg(dd,30,230,70,44,CORAL,'B',size=14)
            seg(dd,100,230,190,44,CYAN,'+ 1 €',size=16)
            lbl(dd,cx,290,'BATTE',CYAN,9)
            tagc(dd,cx,364,'LA BATTE COÛTE 1 € DE PLUS',CYAN)
        elif key=='q':
            bat(dd,cx-60,160,130); ball(dd,cx+80,160,14)
            if blink(t): numcard(dd,cx+80,206,'?',GOLD,20)
            lbl(dd,cx-60,184,'BATTE : 1 € DE PLUS',CYAN,8)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            ball(dd,cx,170,34)
            T(dd,'0,05 €',cx,240,44,'press',34,GRN,align='c',shadow=(4,4,BLACK))
            check(dd,cx+110,170,16,6,GRN)
            tagc(dd,cx,364,'LA BALLE COÛTE 5 CENTIMES',GRN)
        elif key=='r1':
            for i,x in enumerate((64,160,256)):
                sorted_man(dd,x,290,t,CANDP[i],k=3.0)
                numcard(dd,x,170,'0,10',[CORAL,CYAN,GOLD][i],11)
            T(dd,'UNIVERSITÉ',cx,112,16,'press',12,CREAM,align='c')
            tagc(dd,cx,364,'BEAUCOUP RÉPONDENT 10 CENTIMES',CORAL)
        elif key=='r2':
            ball(dd,cx,160,26)
            T(dd,'0,10 €',cx,214,40,'press',30,RED,align='c',shadow=(4,4,BLACK))
            if lt>0.6: xmark_(dd,cx+96,160,18,7,RED)
            tagc(dd,cx,364,'TON CERVEAU CRIE : 10 CENTIMES',RED)
        elif key=='r3':
            numcard(dd,cx,120,'BALLE 0,10 €',CORAL,13)
            if lt>0.5: numcard(dd,cx,176,'BATTE 1,10 €',CYAN,13)
            if lt>1.5:
                box(dd,36,226,248,4,fill=CREAM); numcard(dd,cx,240,'TOTAL 1,20 €',RED,13)
                xmark_(dd,cx+120,262,14,6,RED)
            tagc(dd,cx,364,'1,10 + 0,10 = 1,20 € : FAUX',RED)
        elif key=='r4':
            seg(dd,30,140,60,40,CORAL,'B',size=14); lbl(dd,60,118,'BALLE',CORAL,8)
            if lt>0.5:
                seg(dd,30,230,60,40,CORAL,'B',size=14)
                if lt>1.0: seg(dd,90,230,196,40,CYAN,'1 €',size=16)
                lbl(dd,cx,284,'BATTE = BALLE + 1 €',CYAN,9)
            tagc(dd,cx,364,'DESSINE-LE : BATTE = BALLE + 1 €',CYAN)
        elif key=='r5':
            seg(dd,24,150,56,40,CORAL,'B',size=14); seg(dd,80,150,56,40,CORAL,'B',size=14)
            if lt>0.5: seg(dd,136,150,150,40,CYAN,'1 €',size=16)
            brace(dd,24,286,210,GOLD)
            if lt>1.2: numcard(dd,cx,230,'1,10 €',GOLD,20)
            tagc(dd,cx,364,'2 BALLES + 1 € = 1,10 €',GOLD)
        elif key=='r6':
            seg(dd,24,150,56,40,CORAL,'B',size=14); seg(dd,80,150,56,40,CORAL,'B',size=14)
            if lt<1.0: seg(dd,136,150,150,40,CYAN,'1 €',size=16)
            else: seg(dd,136,150,150,40,CARD,'',size=14); xmark_(dd,211,170,16,6,RED)
            brace(dd,24,136,210,GOLD)
            if lt>1.2: numcard(dd,80,230,'0,10 €',GOLD,20)
            tagc(dd,cx,364,'IL RESTE 10 CENTIMES POUR 2 BALLES',GOLD)
        elif key=='r7':
            ball(dd,86,170,28); ball(dd,234,170,28)
            numcard(dd,86,222,'0,05',GRN,16); numcard(dd,234,222,'0,05',GRN,16)
            T(dd,'+',cx,160,40,'press',32,CREAM,align='c')
            tagc(dd,cx,364,'UNE BALLE = 5 CENTIMES',GRN)
        elif key=='r8':
            bat(dd,cx,170,230)
            numcard(dd,cx,214,'1,05 €',GOLD,22)
            tagc(dd,cx,364,'LA BATTE = 1,05 €',GOLD)
        elif key=='r9':
            numcard(dd,cx-12,118,'1,05 + 0,05 = 1,10',GRN,11)
            if lt>0.9: check(dd,cx+118,130,7,4,GRN)
            if lt>1.5:
                numcard(dd,cx-12,194,'1,05 - 0,05 = 1,00',GRN,11); check(dd,cx+118,206,7,4,GRN)
            tagc(dd,cx,364,'TOTAL 1,10 € ET ÉCART 1 €',GRN)
        elif key=='r10':
            numcard(dd,cx,118,'1,10 €',GOLD,22)
            arrow_d(dd,cx,176,24,CREAM)
            if lt>0.6:
                numcard(dd,86,214,'1 €',CYAN,16); numcard(dd,234,214,'0,10 €',CORAL,16)
                T(dd,'+',cx,226,30,'press',24,CREAM,align='c')
            if lt>1.6: xmark_(dd,cx,290,22,8,RED)
            tagc(dd,cx,364,'LE PIÈGE : COUPER 1,10 EN 1 + 0,10',CORAL)
        elif key=='r11':
            bx,by=cx-34,130; box(dd,bx,by,68,110,fill=GOLD,border=DARK,bw=3,shadow=(4,4,BLACK))
            dd.polygon([((bx+10)*S,(by+110)*S),((bx+58)*S,(by+110)*S),((bx+34)*S,(by+84)*S)],fill=rgb('#07090F'))
            T(dd,'5',cx,by+22,40,'press',28,DARK,align='c')
            if blink(t): star(dd,cx+80,150,t,7)
            tagc(dd,cx,364,'ENREGISTRE-LA POUR PLUS TARD',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#059'
    def fn(lay,dd):
        cx=SW/2
        bat(dd,cx-30,190,170); ball(dd,cx+100,190,15)
        numcard(dd,cx,232,'1,10 €',GOLD,22)
        T(dd,'TA PREMIÈRE RÉPONSE',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'SERA FAUSSE !',SW/2,48,36,'anton',24,RED,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="COMBIEN COÛTE LA BALLE ?"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#060','ENREGISTRE-LA POUR PLUS TARD')
