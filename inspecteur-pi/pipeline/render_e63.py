from render_e4x import *
import inspect, math
B.NUM='#063'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
POT=rgb('#C9965A'); POTD=rgb('#8A5E2E'); WAT=CYAN; DRY=GOLD
def disc_(dd,cx,cy,rx,ry,fill,border=DARK,bw=2):
    dd.ellipse([(cx-rx)*S,(cy-ry)*S,(cx+rx)*S,(cy+ry)*S],fill=fill,outline=border,width=bw*S)
def potato(dd,cx,cy,r=16,k=0,dim=False):
    c=rgb('#5a5f73') if dim else POT
    disc_(dd,cx,cy,r*1.15,r*0.85,c)
    for dx,dy in ((-0.4,-0.2),(0.3,0.15),(0.0,-0.45)):
        dd.ellipse([(cx+dx*r-1.5)*S,(cy+dy*r-1.5)*S,(cx+dx*r+1.5)*S,(cy+dy*r+1.5)*S],fill=POTD)
def pile(dd,cx,cy,n=10,r=14,t=0.0,dim=False):
    pos=[(-34,0),(0,0),(34,0),(-17,-22),(17,-22),(0,-44),(-52,-20),(52,-20),(-34,-42),(34,-42),(-17,-64),(17,-64)]
    for i in range(min(n,len(pos))):
        dx,dy=pos[i]; potato(dd,cx+dx,cy+dy+math.sin(t*3+i)*0.8,r,dim=dim)
def bar(dd,cx,y,w=252,h=34,frac_dry=0.01,wlab=None,dlab=None,hl=False):
    x0=cx-w/2
    box(dd,x0-3,y-3,w+6,h+6,fill=DARK,border=CREAM,bw=2)
    dw=max(4,w*frac_dry)
    box(dd,x0,y,w-dw,h,fill=WAT); box(dd,x0+w-dw,y,dw,h,fill=DRY)
    if wlab: T(dd,wlab,x0+(w-dw)/2,y+h/2-8,16,'press',12,DARK,align='c')
def drop(dd,cx,cy,r=6,col=CYAN):
    dd.polygon([(cx*S,(cy-r*1.6)*S),((cx-r)*S,cy*S),((cx+r)*S,cy*S)],fill=col); disc_(dd,cx,cy,r,r,col,border=col,bw=0)
def bookmark(dd,cx,cy,col=GOLD):
    box(dd,cx-22,cy-34,44,56,fill=col,border=DARK,bw=3)
    dd.polygon([((cx-22)*S,(cy+22)*S),((cx+22)*S,(cy+22)*S),(cx*S,(cy+2)*S)],fill=rgb('#07090F'))
    dd.polygon([((cx-19)*S,(cy+22)*S),((cx+19)*S,(cy+22)*S),(cx*S,(cy+4)*S)],fill=CARD)
HEADS={'s1':[('Un seul ',CREAM),('pour cent',GOLD),(' change tout',CREAM)],
 's2':[('100 kg',GOLD),(' de pommes de terre',CREAM)],
 's3':[('99 %',CYAN),(' d’eau',CREAM)],
 's4':[('On les laisse ',CREAM),('sécher',GOLD)],
 's5':[('Maintenant : ',CREAM),('98 %',CYAN),(' d’eau',CREAM)],
 's6':[('Seulement ',CREAM),('1 point',RED),(' de moins',CREAM)],
 'q':[('Combien ',CREAM),('pèsent-elles',GOLD),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('50 kg',GRN)],
 'r1':[('Pas ',CREAM),('99',RED),(' kilos',CREAM)],
 'r2':[('Regarde la ',CREAM),('matière sèche',GOLD)],
 'r3':[('Dans ',CREAM),('100 kg',CYAN),(' : 1 % = ',CREAM),('1 kg',GOLD)],
 'r4':[('Ce ',CREAM),('kilo',GOLD),(' ne disparaît pas',CREAM)],
 'r5':[('À la fin : ',CREAM),('2 %',GOLD),(' du total',CREAM)],
 'r6':[('Il reste ',CREAM),('98 %',CYAN),(' d’eau',CREAM)],
 'r7':[('1 kg',GOLD),(' = ',CREAM),('2 %',CYAN),(' de ',CREAM),('50 kg',GRN)],
 'r8':[('Poids ',CREAM),('divisé par 2',CORAL)],
 'r9':[('Le piège : ',CREAM),('l’eau',RED)],
 'r10':[('Enregistre-la !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            numcard(dd,76,122,'99 %',CYAN,18); arrow_r(dd,118,140,40,CREAM); numcard(dd,236,122,'98 %',CYAN,18)
            numcard(dd,76,222,'100 KG',GOLD,16); arrow_r(dd,130,240,40,CREAM); numcard(dd,240,222,'? KG',RED,18)
            tagc(dd,cx,364,'UN SEUL POUR CENT CHANGE TOUT',GOLD)
        elif key=='s2':
            pile(dd,cx,262,10,16,t)
            numcard(dd,cx,128,'100 KG',GOLD,22)
            tagc(dd,cx,364,'CENT KILOS DE POMMES DE TERRE',GOLD)
        elif key=='s3':
            bar(dd,cx,190,252,34,0.01,'EAU : 99 KG')
            lbl(dd,cx,150,'99 % D’EAU',CYAN,12)
            arrow_d(dd,cx+118,232,22,GOLD); lbl(dd,cx+60,262,'MATIÈRE SÈCHE : 1 KG',GOLD,8)
            tagc(dd,cx,364,'99 % D’EAU',CYAN)
        elif key=='s4':
            sun(dd,58,142,16,t)
            pile(dd,cx+14,300,6,15,t)
            for i in range(5):
                p=((t*0.9)+i*0.2)%1.0; drop(dd,120+i*34,260-p*110,5+0*i)
            tagc(dd,cx,364,'ON LES LAISSE SÉCHER AU SOLEIL',GOLD)
        elif key=='s5':
            bar(dd,cx,190,252,34,0.02,'EAU : 98 %')
            lbl(dd,cx,150,'98 % D’EAU',CYAN,12)
            tagc(dd,cx,364,'MAINTENANT : 98 % D’EAU',CYAN)
        elif key=='s6':
            numcard(dd,86,150,'99 %',DIM,22,dim=True); xmark_(dd,86,174,10,5,RED) if False else None
            arrow_r(dd,140,168,40,CREAM); numcard(dd,238,150,'98 %',CYAN,22)
            lbl(dd,cx,248,'SEULEMENT 1 POINT',RED,12)
            tagc(dd,cx,364,'SEULEMENT UN POINT DE MOINS',RED)
        elif key=='q':
            pile(dd,cx,300,6,13,t)
            numcard(dd,cx,128,'? KG',GOLD,30)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            if lt<0.85:
                numcard(dd,cx,150,'? KG',GOLD,30)
            else:
                numcard(dd,cx,150,'50 KG',GRN,30)
                star(dd,34,130,t,6); star(dd,282,130,t+1,6)
                pile(dd,cx,300,3,15,t)
            tagc(dd,cx,364,'LA RÉPONSE : 50 KILOS',GRN)
        elif key=='r1':
            numcard(dd,cx,168,'99 KG',RED,28); xmark_(dd,cx,190,70,6,RED)
            tagc(dd,cx,364,'PAS 99 KILOS',RED)
        elif key=='r2':
            bar(dd,cx,180,252,34,0.01,None)
            arrow_d(dd,cx+118,220,26,GOLD); lbl(dd,cx+10,262,'MATIÈRE SÈCHE',GOLD,12)
            if blink(t): star(dd,40,140,t,6)
            tagc(dd,cx,364,'REGARDE LA MATIÈRE SÈCHE',GOLD)
        elif key=='r3':
            u=14; x0=cx-5*u; y0=112
            for i in range(10):
                for j in range(10):
                    g=(i==9 and j==9)
                    box(dd,x0+j*u,y0+i*u,u-2,u-2,fill=(GOLD if g else rgb('#1f5f7a')))
            lbl(dd,cx-60,y0+10*u+16,'100 KG',CYAN,10); lbl(dd,cx+60,y0+10*u+16,'1 % = 1 KG',GOLD,10)
            tagc(dd,cx,364,'1 % DE 100 KG = 1 KILO',GOLD)
        elif key=='r4':
            box(dd,cx-22,250,44,44,fill=GOLD,border=DARK,bw=3); lbl(dd,cx,304,'1 KG',GOLD,12)
            for i in range(6):
                p=((t*0.8)+i*0.17)%1.0; drop(dd,60+i*38,230-p*110,5)
            lbl(dd,cx,128,'L’EAU S’ÉVAPORE',CYAN,10)
            tagc(dd,cx,364,'LE KILO RESTE, L’EAU PART',GOLD)
        elif key=='r5':
            bar(dd,cx,176,252,34,0.02,None)
            numcard(dd,cx,118,'1 KG = 2 %',GOLD,16)
            arrow_d(dd,cx+114,216,24,GOLD); lbl(dd,cx,262,'DU POIDS TOTAL',CREAM,10)
            tagc(dd,cx,364,'À LA FIN : 2 % DU TOTAL',GOLD)
        elif key=='r6':
            bar(dd,cx,176,252,34,0.02,'EAU : 98 %')
            lbl(dd,cx,136,'IL RESTE 98 % D’EAU',CYAN,10)
            tagc(dd,cx,364,'IL RESTE 98 % D’EAU',CYAN)
        elif key=='r7':
            numcard(dd,cx,130,'1 KG',GOLD,22); lbl(dd,cx,190,'=',CREAM,20)
            numcard(dd,cx,214,'2 % DE 50 KG',GRN,18)
            tagc(dd,cx,364,'1 KILO, C’EST 2 % DE 50 KILOS',GRN)
        elif key=='r8':
            numcard(dd,70,150,'100',DIM,24,dim=True); arrow_r(dd,118,170,44,CREAM); numcard(dd,240,150,'50',GRN,24)
            if blink(t) or lt<0.6: stamp(dd,cx,260,'DIVISÉ PAR 2',CORAL,14)
            pile(dd,cx,330,2,11,t) if False else None
            tagc(dd,cx,364,'LE POIDS EST DIVISÉ PAR DEUX',CORAL)
        elif key=='r9':
            drop(dd,84,170,16); xmark_(dd,84,180,30,6,RED); lbl(dd,84,236,'L’EAU',RED,10)
            box(dd,206,156,44,44,fill=GOLD,border=DARK,bw=3); check(dd,228,230,14,6,GRN); lbl(dd,228,262,'MATIÈRE SÈCHE',GOLD,8)
            tagc(dd,cx,364,'LE PIÈGE : REGARDER L’EAU',RED)
        elif key=='r10':
            bookmark(dd,cx,210)
            if blink(t): arrow_d(dd,cx,262,30,GOLD)
            tagc(dd,cx,364,'POUR LA REFAIRE PLUS TARD',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#063'
    def fn(lay,dd):
        cx=SW/2
        pile(dd,cx,318,6,15,0.0)
        numcard(dd,76,138,'99 %',CYAN,16); arrow_r(dd,120,154,40,CREAM); numcard(dd,238,138,'98 %',CYAN,16)
        numcard(dd,cx,200,'? KG',GOLD,22)
        T(dd,'UN SEUL POUR CENT',SW/2,14,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'CHANGE TOUT',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="COMBIEN PÈSENT LES PATATES ?"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#064','ENREGISTRE-LA POUR PLUS TARD')
