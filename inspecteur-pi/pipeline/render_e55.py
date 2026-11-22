from render_e4x import *
import inspect, math
B.NUM='#055'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
OX,OY,RR=44,330,205
def P(th): return (OX+RR*math.cos(th), OY-RR*math.sin(th))
def quarter(dd,col=CREAM):
    pts=[(OX,OY)]+[(OX+RR*math.cos(math.pi/2*i/60),OY-RR*math.sin(math.pi/2*i/60)) for i in range(61)]
    dd.polygon([(x*S,y*S) for x,y in pts],fill=CARD)
    dd.line([(x*S,y*S) for x,y in pts[1:]],fill=col,width=3*S)
    dd.line([(OX*S,OY*S),((OX+RR)*S,OY*S)],fill=col,width=3*S); dd.line([(OX*S,OY*S),(OX*S,(OY-RR)*S)],fill=col,width=3*S)
def ln(dd,p,q,col,w=4): dd.line([(p[0]*S,p[1]*S),(q[0]*S,q[1]*S)],fill=col,width=w*S)
def rect(dd,th,col=CORAL,w=4,fill=False):
    px,py=P(th); 
    if fill: dd.rectangle([OX*S,py*S,px*S,OY*S],fill=rgb('#2A2F4A'))
    dd.rectangle([OX*S,py*S,px*S,OY*S],outline=col,width=w*S)
    return px,py
def d1(dd,th,col=CYAN,w=5): px,py=P(th); ln(dd,(OX,OY),(px,py),col,w); disc(dd,px,py,6,col,DARK,2)
def d2(dd,th,col=GOLD,w=5): px,py=P(th); ln(dd,(px,OY),(OX,py),col,w); disc(dd,px,OY,5,col,DARK,2); disc(dd,OX,py,5,col,DARK,2)
def corner(dd,x,y,col=GOLD,r=8): disc(dd,x,y,r,col,DARK,2)
def tick(dd,p,q,col=CREAM):
    mx,my=(p[0]+q[0])/2,(p[1]+q[1])/2; dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); nx,ny=-dy/L,dx/L
    ln(dd,(mx-nx*8-dx/L*3,my-ny*8-dy/L*3),(mx+nx*8-dx/L*3,my+ny*8-dy/L*3),col,3); ln(dd,(mx-nx*8+dx/L*3,my-ny*8+dy/L*3),(mx+nx*8+dx/L*3,my+ny*8+dy/L*3),col,3)
TH=math.atan2(0.6,0.8)
HEADS={'s1':[('Zéro ',CREAM),('mesure',GOLD),(' donnée',CREAM)],
 's2':[('Un ',CREAM),('rectangle',CORAL),(' coincé',CREAM)],
 's3':[('Rayon : ',CREAM),('10 cm',GOLD)],
 's4':[('Un coin au ',CREAM),('centre',CYAN)],
 's5':[('Le coin opposé : ',CREAM),('le bord',GOLD)],
 's6':[('Large ou ',CREAM),('haut',CORAL),(' ?',CREAM)],
 's7':[('Largeur ',CREAM),('?',GOLD),(' Hauteur ',CREAM),('?',GOLD)],
 'q':[('L’autre ',CREAM),('diagonale',GOLD),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('10 cm',GOLD)],
 'r1':[('Deux diagonales ',CREAM),('égales',CYAN)],
 'r2':[('Du centre au ',CREAM),('bord',CYAN)],
 'r3':[('C’est un ',CREAM),('rayon',GOLD),(' : 10 cm',CREAM)],
 'r4':[('L’autre aussi : ',CREAM),('10 cm',GOLD)],
 'r5':[('On étire ? ',CREAM),('Pareil',CORAL)],
 'r6':[('Le piège : ',CREAM),('mesures inutiles',CORAL)],
 'r7':[('Enregistre-la !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            quarter(dd); rect(dd,TH,CORAL); d1(dd,TH,CYAN,3)
            if blink(t): numcard(dd,SW-62,150,'? CM',GOLD,12)
            tagc(dd,cx,364,'AUCUNE MESURE, UNE RÉPONSE',GOLD)
        elif key=='s2':
            quarter(dd); th=TH; 
            f=sp(lt,0.1,1.0); px,py=P(th); 
            dd.rectangle([OX*S,(OY-(OY-py)*f)*S,(OX+(px-OX)*f)*S,OY*S],outline=CORAL,width=4*S)
            tagc(dd,cx,364,'UN RECTANGLE COINCÉ DEDANS',CORAL)
        elif key=='s3':
            quarter(dd); rect(dd,TH,DIM,3)
            ln(dd,(OX,OY),(OX+RR,OY),GOLD,5); disc(dd,OX,OY,6,GOLD,DARK,2); disc(dd,OX+RR,OY,6,GOLD,DARK,2)
            numcard(dd,OX+RR/2,OY-62,'10 CM',GOLD,16)
            tagc(dd,cx,364,'RAYON DU QUART DE CERCLE : 10 CM',GOLD)
        elif key=='s4':
            quarter(dd); rect(dd,TH,CORAL)
            r=9+3*math.sin(t*8); disc(dd,OX,OY,r,CYAN,DARK,2)
            lbl(dd,OX+40,OY+14,'CENTRE',CYAN,8)
            tagc(dd,cx,364,'UN COIN TOUCHE LE CENTRE',CYAN)
        elif key=='s5':
            quarter(dd); rect(dd,TH,CORAL); px,py=P(TH); disc(dd,OX,OY,7,CYAN,DARK,2)
            r=9+3*math.sin(t*8); disc(dd,px,py,r,GOLD,DARK,2)
            lbl(dd,px+8,py-26,'BORD',GOLD,8)
            tagc(dd,cx,364,'LE COIN OPPOSÉ TOUCHE LE BORD',GOLD)
        elif key=='s6':
            quarter(dd); th=math.radians(50+30*math.sin(t*1.6)); rect(dd,th,CORAL,4,True)
            tagc(dd,cx,364,'LARGE OU HAUT : ON NE SAIT PAS',CORAL)
        elif key=='s7':
            quarter(dd); rect(dd,TH,CORAL,4,True); px,py=P(TH)
            if blink(t): numcard(dd,(OX+px)/2,OY+8,'?',GOLD,14); numcard(dd,OX+22,(OY+py)/2-4,'?',CYAN,14)
            tagc(dd,cx,364,'NI LARGEUR, NI HAUTEUR',CYAN)
        elif key=='q':
            quarter(dd); th=TH; rect(dd,th,DIM,3); d1(dd,th,DIM,3)
            if lt>1.6: d2(dd,th,GOLD,6); 
            else: d2(dd,th,GOLD,3)
            if blink(t): numcard(dd,SW-62,150,'? CM',GOLD,12)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'10',cx-44,134,100,'press',80,GOLD,align='c',shadow=(6,6,BLACK)); T(dd,'CM',cx+100,170,60,'press',36,GOLD,align='c',shadow=(4,4,BLACK)); star(dd,30,120,t,6); star(dd,290,120,t+1,6)
            stamp(dd,cx,300,'SANS AUCUNE MESURE !',CORAL,12); tagc(dd,cx,364,'LA RÉPONSE : 10 CM',GOLD)
        elif key=='r1':
            quarter(dd); rect(dd,TH,CORAL,3,True); px,py=P(TH)
            d1(dd,TH,CYAN,4); d2(dd,TH,GOLD,4); tick(dd,(OX,OY),(px,py)); tick(dd,(px,OY),(OX,py))
            if lt>0.8: stamp(dd,SW-70,140,'ÉGALES',CYAN,12)
            tagc(dd,cx,364,'LES DEUX DIAGONALES SONT ÉGALES',CYAN)
        elif key=='r2':
            quarter(dd); rect(dd,TH,DIM,3); f=sp(lt,0.2,1.4); px,py=P(TH)
            ln(dd,(OX,OY),(OX+(px-OX)*f,OY+(py-OY)*f),CYAN,6); disc(dd,OX,OY,6,CYAN,DARK,2)
            if f>0.99: disc(dd,px,py,8,CYAN,DARK,2)
            tagc(dd,cx,364,'UNE DIAGONALE VA DU CENTRE AU BORD',CYAN)
        elif key=='r3':
            quarter(dd); rect(dd,TH,DIM,3); d1(dd,TH,CYAN,6); px,py=P(TH)
            numcard(dd,SW-62,150,'= RAYON',GOLD,10)
            if lt>0.8: numcard(dd,(OX+px)/2-18,(OY+py)/2+22,'10 CM',GOLD,12)
            tagc(dd,cx,364,'C’EST UN RAYON : 10 CM',GOLD)
        elif key=='r4':
            quarter(dd); rect(dd,TH,DIM,3); d1(dd,TH,DIM,3); d2(dd,TH,GOLD,6); px,py=P(TH)
            numcard(dd,(px+OX)/2+50,(OY+py)/2+36,'10 CM',GOLD,12)
            tagc(dd,cx,364,'L’AUTRE AUSSI : 10 CM',GOLD)
        elif key=='r5':
            quarter(dd); th=math.radians(58+26*math.sin(lt*2.2)); rect(dd,th,CORAL,3,True); d2(dd,th,GOLD,5); d1(dd,th,CYAN,3)
            numcard(dd,SW-62,150,'10 CM',GOLD,12)
            tagc(dd,cx,364,'ON L’ÉTIRE : TOUJOURS 10 CM',CORAL)
        elif key=='r6':
            numcard(dd,86,150,'LARGEUR',CYAN,9); numcard(dd,226,150,'HAUTEUR',CYAN,9)
            if lt>0.4: xmark_(dd,86,222,22,6,RED); xmark_(dd,226,222,22,6,RED)
            stamp(dd,cx,276,'INUTILES !',CORAL,16)
            tagc(dd,cx,364,'PAS BESOIN DE LES CÔTÉS',CORAL)
        elif key=='r7':
            bx,by=cx-34,130; box(dd,bx,by,68,110,fill=GOLD,border=DARK,bw=3,shadow=(4,4,BLACK))
            dd.polygon([((bx+10)*S,(by+110)*S),((bx+58)*S,(by+110)*S),((bx+34)*S,(by+84)*S)],fill=rgb('#07090F'))
            T(dd,'10',cx,by+22,40,'press',28,DARK,align='c')
            if blink(t): star(dd,cx+80,150,t,7)
            tagc(dd,cx,364,'ENREGISTRE-LA POUR PLUS TARD',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#055'
    def fn(lay,dd):
        cx=SW/2
        quarter(dd); rect(dd,TH,CORAL,4,True); d1(dd,TH,CYAN,3); d2(dd,TH,GOLD,4)
        numcard(dd,SW-60,140,'? CM',GOLD,12)
        T(dd,'ZÉRO MESURE,',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'UNE SEULE RÉPONSE !',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="LA DIAGONALE QUI CACHE SON SECRET"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#056','ENREGISTRE-LA POUR PLUS TARD')
