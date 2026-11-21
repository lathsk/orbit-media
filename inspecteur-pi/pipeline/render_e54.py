from render_e4x import *
import inspect, math
B.NUM='#054'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
def train(dd,x,y,face=1,col=CORAL):
    w=76
    box(dd,x,y,w,26,fill=col,border=DARK,bw=2)
    cabx=x if face==1 else x+w-24
    box(dd,cabx,y-14,24,16,fill=col,border=DARK,bw=2); box(dd,cabx+6,y-10,12,8,fill=CYAN)
    chx=x+w-18 if face==1 else x+10
    box(dd,chx,y-10,8,12,fill=DARK)
    box(dd,(x+w-4) if face==1 else x,y+6,4,8,fill=GOLD)
    for dx in (14,38,62): disc(dd,x+dx,y+29,6,DARK,GREY,1)
    box(dd,0,y+36,320,3,fill=GREY)
def fly(dd,x,y,t,k=1.0):
    wf=3 if int(t*14)%2==0 else 7
    dd.ellipse([(x-6*k)*S,(y-(2+wf)*k)*S,(x-0.5*k)*S,(y-1*k)*S],fill=CREAM,outline=GREY)
    dd.ellipse([(x+0.5*k)*S,(y-(2+wf)*k)*S,(x+6*k)*S,(y-1*k)*S],fill=CREAM,outline=GREY)
    dd.ellipse([(x-7*k)*S,(y-2*k)*S,(x+7*k)*S,(y+5*k)*S],fill=rgb('#2B2B35'),outline=CREAM,width=2*S)
    box(dd,x+3*k,y-1*k,3*k,3*k,fill=RED)
def larrow(dd,x,y,w=24,col=CREAM):
    box(dd,x+6,y-2,w-6,5,fill=col); dd.polygon([((x+7)*S,(y-7)*S),((x+7)*S,(y+8)*S),(x*S,(y+0.5)*S)],fill=col)
TY=250
def tri(u): u=u%2.0; return u if u<=1 else 2-u
def zig(dd,xa,xb,n=5,y0=150,y1=214,col=GREY,t=0.0):
    pts=[]
    for i in range(n+1):
        x=xa if i%2==0 else xb
        pts.append((x,y0+(y1-y0)*i/n))
    for a,b in zip(pts,pts[1:]): dotline(dd,a,b,col,t,2,12)
    return pts
def flypos(xa,xb,t,speed=0.9,y0=160,y1=214):
    u=tri(t*speed); return xa+(xb-xa)*u, y0+(y1-y0)*(0.5+0.5*math.sin(t*2.1))
HEADS={'s1':[('Une ',CREAM),('mouche,',GOLD),(' deux ',CREAM),('trains',CORAL)],
 's2':[('Deux trains à ',CREAM),('100 km',GOLD)],
 's3':[('Chacun roule à ',CREAM),('50 km/h',CYAN)],
 's4':[('Elle vole à ',CREAM),('75 km/h',GOLD)],
 's5':[('Elle fait ',CREAM),('demi-tour',CORAL)],
 's6':[('Et ça ',CREAM),('recommence',CYAN)],
 'q':[('Quelle ',CREAM),('distance',GOLD),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('75 km',GOLD)],
 'r1':[('Oublie les ',CREAM),('demi-tours',CORAL)],
 'r2':[('Ensemble : ',CREAM),('100 km/h',GOLD)],
 'r3':[('Ils se croisent en ',CREAM),('1 heure',CYAN)],
 'r4':[('La mouche vole ',CREAM),('1 heure',GOLD)],
 'r5':[('1 h',CYAN),(' x ',CREAM),('75 km/h',GOLD),(' = 75 km',CREAM)],
 'r6':[('Le piège : ',CREAM),('l’infini',CORAL)],
 'r7':[('Compte le ',CREAM),('temps',GOLD)]}
STORY=('s1','s2','s3','s4','s5','s6','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            train(dd,10,TY,1,CORAL); train(dd,234,TY,-1,CYAN)
            fx,fy=flypos(100,220,t,0.5,196,226); fly(dd,fx,fy,t,2.4)
            if blink(t): numcard(dd,cx,124,'? KM',GOLD,22)
            tagc(dd,cx,364,'COMBIEN DE KM POUR LA MOUCHE ?',GOLD)
        elif key=='s2':
            train(dd,10,TY,1,CORAL); train(dd,234,TY,-1,CYAN)
            dd.rectangle([86*S,214*S,234*S,217*S],fill=CREAM); dd.rectangle([86*S,206*S,89*S,225*S],fill=CREAM); dd.rectangle([231*S,206*S,234*S,225*S],fill=CREAM)
            numcard(dd,cx,150,'100 KM',GOLD,18); tagc(dd,cx,364,'DEUX TRAINS À 100 KM',GOLD)
        elif key=='s3':
            d=lt*6; train(dd,10+d,TY,1,CORAL); train(dd,234-d,TY,-1,CYAN)
            arrow_r(dd,100+d,226,40,CREAM); larrow(dd,180-d,226,40,CREAM)
            numcard(dd,62,160,'50 KM/H',CORAL,11); numcard(dd,258,160,'50 KM/H',CYAN,11)
            tagc(dd,cx,364,'ILS ROULENT L’UN VERS L’AUTRE',CYAN)
        elif key=='s4':
            train(dd,10,TY,1,CORAL); train(dd,234,TY,-1,CYAN)
            fx=92+sp(lt,0.2,2.5)*110; fly(dd,fx,214+math.sin(t*5)*3,t,2.4)
            numcard(dd,cx,130,'75 KM/H',GOLD,18); tagc(dd,cx,364,'UNE MOUCHE PART DU 1ER TRAIN',GOLD)
        elif key=='s5':
            train(dd,10,TY,1,CORAL); train(dd,234,TY,-1,CYAN)
            zig(dd,94,226,4,150,214,GREY,t); fx,fy=flypos(94,226,t,0.8,160,214); fly(dd,fx,fy,t,2.4)
            tagc(dd,cx,364,'ELLE FILE, FAIT DEMI-TOUR, REPART',CORAL)
        elif key=='s6':
            d=sp(lt,0.0,4.0)*52; train(dd,10+d,TY,1,CORAL); train(dd,234-d,TY,-1,CYAN)
            xa=94+d; xb=226-d; zig(dd,xa,xb,8,150,214,GREY,t); fx,fy=flypos(xa,xb,t,1.4,160,214); fly(dd,fx,fy,t,2.4)
            tagc(dd,cx,364,'ET ENCORE, JUSQU’À LA RENCONTRE',CYAN)
        elif key=='q':
            box(dd,cx-120,150,240,78,fill=CARD,border=GOLD,bw=4,shadow=(4,4,BLACK)); T(dd,'? KM',cx,170,40,'press',32,GOLD,align='c'); lbl(dd,cx,208,'DISTANCE DE LA MOUCHE',CREAM,8)
            fx,fy=flypos(70,250,t,0.7,260,300); fly(dd,fx,fy,t,1.8)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'75',cx-34,134,100,'press',80,GOLD,align='c',shadow=(6,6,BLACK)); T(dd,'KM',cx+96,170,60,'press',36,GOLD,align='c',shadow=(4,4,BLACK)); star(dd,30,120,t,6); star(dd,290,120,t+1,6)
            stamp(dd,cx,300,'TOUT SIMPLEMENT !',CORAL,14); tagc(dd,cx,364,'LA RÉPONSE : 75 KM',GOLD)
        elif key=='r1':
            zig(dd,70,250,6,130,250,GREY,t); fly(dd,160,190,t,2.4)
            if lt>0.4: xmark_(dd,cx,192,70,9,RED)
            tagc(dd,cx,364,'OUBLIE TOUS LES DEMI-TOURS',CORAL)
        elif key=='r2':
            d=lt*5; train(dd,10+d,TY,1,CORAL); train(dd,234-d,TY,-1,CYAN)
            numcard(dd,62,186,'50',CORAL,14); numcard(dd,258,186,'50',CYAN,14); plus(dd,160,200,24) if False else None
            numcard(dd,cx,130,'50 + 50 = 100 KM/H',GOLD,13); tagc(dd,cx,364,'ILS SE RAPPROCHENT À 100 KM/H',GOLD)
        elif key=='r3':
            numcard(dd,cx,122,'100 KM / 100 KM/H',CYAN,12)
            clock(dd,cx,226,40,hh=12,mm=60*sp(lt,0.3,3.0)); 
            if sp(lt,0.3,3.0)>0.99: numcard(dd,cx+112,206,'1 H',GOLD,16)
            tagc(dd,cx,364,'ILS SE CROISENT EN 1 HEURE',CYAN)
        elif key=='r4':
            numcard(dd,cx,122,'75 KM/H',GOLD,18)
            clock(dd,86,224,38,hh=12,mm=60*sp(lt,0.2,4.0)); fx,fy=flypos(170,290,t,0.9,190,250); fly(dd,fx,fy,t,2.0)
            tagc(dd,cx,364,'ELLE VOLE 1 H À 75 KM/H',GOLD)
        elif key=='r5':
            numcard(dd,cx,128,'1 H x 75 KM/H',CYAN,14); arrow_d(dd,cx,178,20)
            numcard(dd,cx,206,'= 75 KM',GOLD,24); tagc(dd,cx,364,'1 H À 75 KM/H = 75 KM',GOLD)
        elif key=='r6':
            zig(dd,70,250,8,130,250,GREY,t)
            if blink(t): stamp(dd,cx,190,'INUTILE !',CORAL,16)
            tagc(dd,cx,364,'PAS BESOIN DE TOUS LES TRAJETS',CORAL)
        elif key=='r7':
            clock(dd,cx,206,58,hh=12,mm=60*sp(lt,0.2,3.0)); numcard(dd,cx,130,'1 H',GOLD,18) if False else None
            tagc(dd,cx,364,'IL SUFFIT DE COMPTER LE TEMPS',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#054'
    def fn(lay,dd):
        cx=SW/2
        train(dd,10,TY-20,1,CORAL); train(dd,234,TY-20,-1,CYAN)
        zig(dd,94,226,4,150,200,GREY,t); fly(dd,160,176,t,3.0)
        numcard(dd,cx,106,'? KM',GOLD,16)
        T(dd,'UNE MOUCHE, DEUX TRAINS,',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'COMBIEN DE KILOMÈTRES ?',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="PLUS SIMPLE QUE TU CROIS"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#055','ENVOIE-LA À QUELQU’UN')
