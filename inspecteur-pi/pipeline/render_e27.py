from render_e2x import *
B.NUM='#027'
SHELL=rgb('#F6EBD9'); SHELLD=rgb('#C9B896'); YOLK=rgb('#FFB627')
BRICK=rgb('#3A4270'); BRICKD=rgb('#252C52'); WIN=rgb('#FFE08A'); WIND=rgb('#1A2040')
HEADS={'s1':[('Seulement ',CREAM),('deux œufs',GOLD)],
 's2':[('Un immeuble de ',CREAM),('100 étages',CORAL)],
 's3':[('Trouver l’étage ',CREAM),('limite',GOLD)],
 's4':[('L’œuf ',CREAM),('survit',GRN),(' : on relance',CREAM)],
 's5':[('L’œuf ',CREAM),('casse',RED),(' : perdu',CREAM)],
 's6':[('Seulement ',CREAM),('2 œufs',GOLD)],
 'q':[('Combien de ',CREAM),('lancers',CORAL),(' ?',CREAM)],
 's7':[('Même dans le ',CREAM),('pire des cas',RED)],
 'r0':[('Réponse : ',CREAM),('14',GOLD),(' lancers !',CREAM)],
 'r1':[('L’œuf n°1 monte ',CREAM),('par paliers',GOLD)],
 'r2':[('D’abord l’étage ',CREAM),('14',GOLD)],
 'r3':[('Puis l’étage ',CREAM),('27',GOLD)],
 'r4':[('Puis l’étage ',CREAM),('39',GOLD)],
 'r5':[('Le saut ',CREAM),('diminue',CORAL),(' à chaque fois',CREAM)],
 'r6':[('Dès que l’œuf n°1 ',CREAM),('casse',RED)],
 'r7':[('L’œuf n°2 vérifie ',CREAM),('un par un',GOLD)],
 'r8':[('Jamais plus de ',CREAM),('14',GOLD),(' lancers',CREAM)],
 'r9':[('14 + 13 + 12 … + 1 ',CREAM),('= 105',GOLD)]}
STORY=('s1','s2','s3','s4','s5','s6','q','s7')
PAL_=[14,27,39,50,60,69,77,84,90,95,99,100]

def egg(dd,cx,cy,k=1.0,hl=None,tag_=None):
    w=11*k; h=14*k
    if hl: dd.ellipse([(cx-w-4)*S,(cy-h-4)*S,(cx+w+4)*S,(cy+h+4)*S],outline=hl,width=3*S)
    dd.ellipse([(cx-w-2)*S,(cy-h-2)*S,(cx+w+2)*S,(cy+h+2)*S],fill=DARK)
    dd.ellipse([(cx-w)*S,(cy-h)*S,(cx+w)*S,(cy+h)*S],fill=SHELL)
    dd.ellipse([(cx-w*0.62)*S,(cy-h*0.7)*S,(cx-w*0.2)*S,(cy-h*0.25)*S],fill=rgb('#FFFFFF'))
    dd.arc([(cx-w)*S,(cy-h)*S,(cx+w)*S,(cy+h)*S],20,150,fill=SHELLD,width=3*S)
    if tag_: T(dd,tag_,cx,cy-5*k,14,'press',max(8,int(9*k)),DARK,align='c')
def broken(dd,cx,cy,k=1.0,gap=1.0):
    w=11*k; h=14*k
    # jaune
    dd.ellipse([(cx-6*k)*S,(cy+h*0.35)*S,(cx+6*k)*S,(cy+h*0.35+8*k)*S],fill=YOLK,outline=DARK,width=1*S)
    for sgn in (-1,1):
        x0=cx+sgn*(9*k*gap)
        dd.pieslice([(x0-w*0.9)*S,(cy-h*0.3)*S,(x0+w*0.9)*S,(cy+h*0.9)*S],0,180,fill=SHELL,outline=DARK,width=2*S)
        for q in range(4):
            xx=x0-w*0.9+q*(w*0.45); box(dd,xx,cy+h*0.30-(q%2)*3*k,w*0.45,4*k,fill=SHELL)
def tower(dd,x,y,w,h,rows,lit=(),cols=4,top_label=None,t=0.0):
    box(dd,x,y,w,h,fill=BRICK,border=DARK,bw=3,shadow=(3,3,BLACK))
    rh=(h-8)/rows
    for r in range(rows):
        for c in range(cols):
            wx=x+6+c*((w-12)/cols); wy=y+4+r*rh
            box(dd,wx+1,wy+1,(w-12)/cols-3,max(2,rh-3),fill=(WIN if r in lit else WIND))
def floorline(dd,x,w,y,col=GOLD):
    dd.line([(x*S,y*S),((x+w)*S,y*S)],fill=col,width=2*S)
def nline(dd,k,t,lt=0,hl=None,egg_at=None,cracked=None,labels=True,y=230):
    """droite des étages 0..100 : ticks de PAL_[:k]"""
    x0,x1=22,290
    X=lambda f: x0+(x1-x0)*f/100.0
    box(dd,x0,y,x1-x0,6,fill=EDGE)
    T(dd,'0',x0,y+14,12,'press',9,GREY,align='c'); T(dd,'100',x1,y+14,12,'press',9,GREY,align='c')
    prev=0
    for i in range(k):
        f=PAL_[i]; col=(GOLD if i==k-1 else CYAN)
        if cracked is not None and i==cracked: col=RED
        box(dd,X(f)-2,y-10,5,26,fill=col)
        if labels and (i<5 or i==k-1): T(dd,str(f),X(f),y-26-(i%2)*0,12,'press',9,col,align='c')
        prev=f
    return X

def bignum(dd,cx,y,txt,col=GOLD,w=120,h=64,size=32):
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=4,shadow=(4,4,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
def arc_jump(dd,xa,xb,yb,col,h=34):
    pts=[]
    for i in range(17):
        f=i/16; pts.append(((xa+(xb-xa)*f)*S,(yb-4*h*f*(1-f))*S))
    dd.line(pts,fill=col,width=2*S)

def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            egg(dd,92,212,2.6)
            egg(dd,220,212,2.6)
            T(dd,'2',SW/2,150,50,'press',44,GOLD,align='c',shadow=(3,3,BLACK)) if False else None
            bignum(dd,SW/2,116,'× 2',GOLD,w=110,h=52,size=26)
            box(dd,40,246,232,10,fill=rgb('#8A5A3A'),border=DARK,bw=2)
            insp(dd,SW/2,GY,t,k=2.0)
            tagc(dd,SW/2,364,'DEUX ŒUFS SEULEMENT',GOLD)
        elif key=='s2':
            tower(dd,74,106,164,238,20,lit=(3,7,12,15,18),cols=5)
            bignum(dd,SW/2,112,'100',GOLD,w=96,h=44,size=22)
            T(dd,'1',58,326,12,'press',9,CREAM,align='c')
            tagc(dd,SW/2,364,'100 ÉTAGES',CORAL)
        elif key=='s3':
            tower(dd,70,106,172,238,20,cols=5)
            ly=106+238*0.42
            box(dd,70,ly+3,172,238-(ly-106)-3,fill=None) 
            # moitié basse verte, haute rouge
            lay2=Image.new('RGBA',lay.size,(0,0,0,0)); od=ImageDraw.Draw(lay2)
            od.rectangle([71*S,107*S,241*S,ly*S],fill=(255,77,94,70))
            od.rectangle([71*S,ly*S,241*S,342*S],fill=(76,195,107,70))
            lay.paste(Image.alpha_composite(lay.convert('RGBA'),lay2).convert('RGB'))
            dd2=ImageDraw.Draw(lay)
            dd2.line([(62*S,ly*S),(250*S,ly*S)],fill=GOLD,width=3*S)
            T(dd2,'?',SW/2,ly-24,40,'press',34,GOLD,align='c',shadow=(3,3,BLACK))
            lbl(dd2,40,126,'CASSE',RED,9); lbl(dd2,40,300,'OK',GRN,9)
            tagc(dd2,SW/2,364,'TROUVER L’ÉTAGE LIMITE',GOLD)
        elif key=='s4':
            fy=int(20*abs(math.sin(lt*2.2)))
            box(dd,40,300,232,12,fill=rgb('#8A5A3A'),border=DARK,bw=2)
            egg(dd,SW/2,266-fy*3,2.4,GRN)
            dd.line([(60*S,170*S),(60*S,240*S)],fill=GRN,width=3*S); tri_down(dd,60,248,GRN,8)
            dd.polygon([(60*S,120*S),(48*S,140*S),(72*S,140*S)],fill=GRN)
            ok_stamp(dd,SW/2,150,'INTACT',GRN)
            lbl(dd,SW/2,326,'ON LE RAMASSE',CREAM,10) if False else None
            tagc(dd,SW/2,364,'L’ŒUF SURVIT',GRN)
        elif key=='s5':
            box(dd,40,300,232,12,fill=rgb('#8A5A3A'),border=DARK,bw=2)
            broken(dd,SW/2,262,3.2,1.0+min(1.0,lt*2)*0.8)
            cross(dd,SW/2,176,22,8,RED)
            stamp(dd,SW/2,134,'PERDU',RED,18)
            tagc(dd,SW/2,364,'L’ŒUF CASSE : PERDU',RED)
        elif key=='s6':
            egg(dd,92,200,2.8,CORAL,tag_='1'); egg(dd,220,200,2.8,CYAN,tag_='2')
            box(dd,40,262,232,10,fill=rgb('#8A5A3A'),border=DARK,bw=2)
            T(dd,'SEULEMENT',SW/2,118,24,'press',16,CREAM,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'SEULEMENT 2 ŒUFS',GOLD)
        elif key=='q':
            tower(dd,34,106,120,238,16,lit=(5,9),cols=3)
            insp(dd,232,GY,t,k=3.0)
            T(dd,'?',232,130,60,'press',50,CORAL,align='c',shadow=(4,4,BLACK))
            bignum(dd,232,208,'14 ?',GOLD,w=110,h=40,size=18) if False else None
            tagc(dd,SW/2,364,'COMBIEN DE LANCERS ?',CORAL)
        elif key=='s7':
            tower(dd,34,106,120,238,16,lit=(0,),cols=3)
            floorline(dd,24,140,106+238*0.06,RED)
            T(dd,'!',232,128,60,'press',50,RED,align='c',shadow=(4,4,BLACK))
            stamp(dd,232,230,'PIRE',RED,14); stamp(dd,232,268,'DES CAS',RED,12)
            tagc(dd,SW/2,364,'LE PIRE DES CAS',RED)
        elif key=='r0':
            insp(dd,64,GY,t,k=3.8)
            bignum(dd,212,150,'14',GOLD,w=150,h=100,size=60)
            star(dd,282,128,t,5); star(dd,150,120,t,4)
            tagc(dd,SW/2,364,'QUATORZE LANCERS',GOLD)
        elif key=='r1':
            # escalier : l'oeuf n°1 monte
            for i in range(6):
                box(dd,30+i*42,300-i*30,42,12+i*30,fill=BRICK,border=DARK,bw=2)
            n=min(5,int(lt*2.2)); egg(dd,51+n*42,300-n*30-22,1.2,CORAL,tag_='1')
            tagc(dd,SW/2,364,'L’ŒUF 1 MONTE PAR PALIERS',CORAL)
        elif key in ('r2','r3','r4'):
            k={'r2':1,'r3':2,'r4':3}[key]
            X=nline(dd,k,t,lt,y=250)
            fl=PAL_[k-1]
            prevf=PAL_[k-2] if k>1 else 0
            egg(dd,X(fl),204-int(8*abs(math.sin(lt*3))),1.3,CORAL,tag_='1')
            bignum(dd,SW/2,118,'ÉTAGE '+str(fl),GOLD,w=250,h=52,size=22)
            tagc(dd,SW/2,364,'ON LANCE AU %d%s'%(fl,'E'),GOLD)
        elif key=='r5':
            k=min(12,3+int(lt*3.0)); X=nline(dd,k,t,lt,y=262,labels=False)
            xs=[0]+PAL_
            for i in range(min(k,12)):
                arc_jump(dd,X(xs[i]),X(xs[i+1]),250,CORAL if i<3 else CYAN,h=18+max(0,14-i)*2)
            for i,v in enumerate(('+14','+13','+12')):
                if k>=i+1: T(dd,v,X((xs[i]+xs[i+1])/2),176+i*0,14,'press',10,GOLD,align='c')
            bignum(dd,SW/2,106,'SAUT − 1',CORAL,w=190,h=40,size=16) if False else None
            tagc(dd,SW/2,364,'LE SAUT DIMINUE',CORAL)
        elif key=='r6':
            X=nline(dd,3,t,lt,y=262,labels=True,cracked=2)
            broken(dd,X(39),214,1.5,1.0+min(1,lt*2)*0.6)
            cross(dd,X(39),158,16,6,RED)
            box(dd,X(27)+3,256,X(39)-X(27)-6,16,fill=None,border=GOLD,bw=2)
            T(dd,'?',(X(27)+X(39))/2,284,14,'press',12,GOLD,align='c')
            tagc(dd,SW/2,364,'L’ŒUF 1 SE CASSE AU 39',RED)
        elif key=='r7':
            n=min(11,int(lt*3.2))
            for i in range(11):
                col=GRN if i<n else (GOLD if i==n else EDGE)
                box(dd,22+i*24.5,230,22,22,fill=CARD,border=col,bw=3)
                if i<n: T(dd,'OK',22+i*24.5+11,236,10,'press',7,GRN,align='c')
            T(dd,'28',33,262,12,'press',9,CREAM,align='c'); T(dd,'38',33+10*24.5,262,12,'press',9,CREAM,align='c')
            egg(dd,33+min(n,10)*24.5,184,1.2,CYAN,tag_='2')
            bignum(dd,SW/2,108,'ÉTAGES 28 → 38'.replace(' → ',' À '),CYAN,w=270,h=40,size=14)
            tagc(dd,SW/2,364,'L’ŒUF 2 : UN PAR UN',CYAN)
        elif key=='r8':
            bignum(dd,SW/2,118,'3 + 11 = 14',GOLD,w=280,h=60,size=20)
            lbl(dd,SW/2,200,'3 LANCERS DE L’ŒUF 1',CORAL,10)
            lbl(dd,SW/2,228,'+ 11 LANCERS DE L’ŒUF 2',CYAN,10)
            nb2=bignum(dd,SW/2,262,'MAXIMUM : 14',GRN,w=250,h=44,size=15) 
            insp(dd,50,GY,t,k=2.0) if False else None
            tagc(dd,SW/2,364,'JAMAIS PLUS DE 14',GOLD)
        elif key=='r9':
            f=min(1.0,lt/2.0); n=int(14*f)+1 if f<1 else 14
            for i in range(min(14,n)):
                hh=(14-i)*13
                box(dd,22+i*19,330-hh,17,hh,fill=(GOLD if i%2==0 else CYAN),border=DARK,bw=1)
            T(dd,'14 + 13 + … + 1',SW/2,104,16,'press',12,CREAM,align='c')
            if f>=1: bignum(dd,236,128,'105',GOLD,w=92,h=44,size=22); lbl(dd,236,180,'> 100',GRN,11)
            tagc(dd,SW/2,364,'ÇA COUVRE LES 100 ÉTAGES',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#027'
    def fn(lay,dd):
        tower(dd,90,110,132,236,14,lit=(2,6,10),cols=4)
        egg(dd,SW/2,100,1.6)
        T(dd,'DEUX ŒUFS,',SW/2,10,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'100 ÉTAGES',SW/2,44,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        insp(dd,40,GY,t,k=2.2)
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DES DEUX ŒUFS"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#028')
