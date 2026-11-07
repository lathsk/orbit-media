from render_e2x import *
B.NUM='#026'
SKIN=rgb('#F1C39B'); HAIRC=rgb('#6B4A2E'); PINK=rgb('#FF8FB8')
GCOL=[CORAL,CYAN,GOLD,rgb('#B05CFF'),GRN]
HEADS={'s1':[('Deux ',CREAM),('invités',GOLD),(' fêtent le ',CREAM),('même jour',CORAL)],
 's2':[('Des ',CREAM),('invités',GOLD),(' dans la salle',CREAM)],
 's3':[('Chacun est né un ',CREAM),('jour au hasard',GOLD)],
 's4':[('L’année : ',CREAM),('365 jours',CYAN)],
 's5':[('Des ',CREAM),('centaines',CORAL),(' d’invités ?',CREAM)],
 'q':[('Combien d’',CREAM),('invités',GOLD),(' pour ',CREAM),('50 %',CORAL),(' ?',CREAM)],
 'r0':[('Réponse : ',CREAM),('23',GOLD),(' seulement !',CREAM)],
 'r1':[('Avec ',CREAM),('23',GOLD),(' invités',CREAM)],
 'r2':[('253',GOLD),(' paires possibles',CREAM)],
 'r3':[('Une ',CREAM),('petite chance',GOLD),(' par paire',CREAM)],
 'r4':[('Toutes ces chances ',CREAM),('s’additionnent',GOLD)],
 'r5':[('Résultat : ',CREAM),('50,7 %',GOLD)],
 'r6':[('Avec ',CREAM),('57',GOLD),(' invités : ',CREAM),('99 %',CORAL)],
 'r7':[('Avec ',CREAM),('70',GOLD),(' : presque ',CREAM),('certain',CORAL)],
 'r8':[('Le cerveau compte les ',CREAM),('personnes',GOLD)],
 'r9':[('Il oublie les ',CREAM),('paires',CORAL),(' !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','q')

def person(dd,x,y,col=CORAL,k=1.0,hat=False):
    box(dd,x,y,6*k,5*k,fill=SKIN); box(dd,x,y-1.5*k,6*k,2.5*k,fill=HAIRC); box(dd,x-1*k,y+5*k,8*k,7*k,fill=col)
    if hat:
        dd.polygon([((x+3*k)*S,(y-9*k)*S),((x-0.5*k)*S,(y-1.5*k)*S),((x+6.5*k)*S,(y-1.5*k)*S)],fill=PINK,outline=DARK)
def cake(dd,cx,y,k=1.0,t=0.0):
    box(dd,cx-30*k,y+22*k,60*k,22*k,fill=rgb('#C8743E'),border=DARK,bw=2)
    box(dd,cx-24*k,y+8*k,48*k,16*k,fill=PINK,border=DARK,bw=2)
    box(dd,cx-24*k,y+8*k,48*k,5*k,fill=CREAM)
    for dx in (-14,0,14):
        box(dd,cx+(dx-1.5)*k,y-4*k,3*k,12*k,fill=CYAN,border=DARK,bw=1)
        fl=2*math.sin(t*9+dx)
        box(dd,cx+(dx-1.5)*k,y-10*k+fl*0.3,3*k,5*k,fill=GOLD)
def calcard(dd,cx,y,txt,col=GOLD,w=64,h=46,hl=False):
    box(dd,cx-w/2,y,w,h,fill=CREAM,border=(GOLD if hl else DARK),bw=(3 if hl else 2),shadow=(3,3,BLACK))
    box(dd,cx-w/2,y,w,12,fill=RED,border=DARK,bw=2)
    T(dd,txt,cx,y+22,14,'press',10,DARK,align='c')
def gauge(dd,x,y,w,frac,col=GOLD,hl=True):
    box(dd,x,y,w,26,fill=CARD,border=EDGE,bw=3)
    if frac>0.005: box(dd,x+3,y+3,(w-6)*frac,20,fill=col)
    box(dd,x+w/2-1,y-6,3,38,fill=CREAM)
def bignum(dd,cx,y,txt,col=GOLD,w=120,h=64,size=32):
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=4,shadow=(4,4,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
def circle_pts(n,cx,cy,r):
    return [(cx+r*math.sin(2*math.pi*i/n),cy-r*math.cos(2*math.pi*i/n)) for i in range(n)]
def circle_people(dd,n,cx,cy,r,k=1.6,hl=()):
    for i,(x,y) in enumerate(circle_pts(n,cx,cy,r)):
        person(dd,x-3*k,y-8*k,GCOL[i%5],k)
def pair_lines(dd,n,cx,cy,r,frac=1.0,col=GOLD):
    pts=circle_pts(n,cx,cy,r); L=[(i,j) for i in range(n) for j in range(i+1,n)]
    for i,j in L[:int(len(L)*frac)]:
        dd.line([(pts[i][0]*S,pts[i][1]*S),(pts[j][0]*S,pts[j][1]*S)],fill=col,width=1*S)
def crowd(dd,x0,y0,cols,rows,gx=17,gy=22,k=1.0,hat=False):
    for r_ in range(rows):
        for c_ in range(cols): person(dd,x0+c_*gx,y0+r_*gy,GCOL[(r_*3+c_)%5],k,hat=hat)

def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            box(dd,0,GY-6,SW,8,fill=rgb('#2C3766'))
            for i in range(9): box(dd,18+i*34,108+(i%2)*6,10,10,fill=GCOL[i%5])
            dd.line([(10*S,112*S),((SW-10)*S,112*S)],fill=CREAM,width=2*S)
            crowd(dd,30,210,9,2,gx=28,gy=40,k=1.8,hat=True)
            cake(dd,SW/2,140,1.0,t)
            tagc(dd,SW/2,364,'LE MÊME ANNIVERSAIRE ?',GOLD)
        elif key=='s2':
            crowd(dd,26,112,15,9,gx=19,gy=24,k=1.0,hat=True)
            tagc(dd,SW/2,364,'LES INVITÉS',GOLD)
        elif key=='s3':
            n=min(5,1+int(lt*2.4))
            ds=['14/03','02/06','27/10','09/08','31/01']
            for i in range(n):
                x=34+i*61
                person(dd,x-2,130+(i%2)*10,GCOL[i%5],2.2,hat=True)
                calcard(dd,x+2,200+(i%2)*10,ds[i],w=56,hl=(i==n-1))
            tagc(dd,SW/2,364,'UN JOUR AU HASARD',CORAL)
        elif key=='s4':
            n=min(365,int(lt*260)+1)
            for i in range(n):
                r,c=divmod(i,28); box(dd,30+c*9.5,120+r*9.5,7,7,fill=(GOLD if i==364 else rgb('#4A5486')))
            if lt>1.0: bignum(dd,SW/2,268,'365',GOLD,w=150,h=56,size=30)
            tagc(dd,SW/2,364,'365 JOURS',CYAN)
        elif key=='s5':
            crowd(dd,10,106,17,10,gx=17,gy=23,k=0.8,hat=True)
            if lt>0.5: bignum(dd,SW/2,196,'200 ? 300 ?',CORAL,w=260,h=56,size=20)
            tagc(dd,SW/2,364,'DES CENTAINES ?',CORAL)
        elif key=='q':
            cake(dd,SW/2,120,1.0,t)
            T(dd,'?',60,150,50,'press',44,CORAL,align='c',shadow=(3,3,BLACK)); T(dd,'?',252,150,50,'press',44,GOLD,align='c',shadow=(3,3,BLACK))
            gauge(dd,36,260,240,0.5,CORAL)
            lbl(dd,SW/2,304,'1 CHANCE SUR 2',CREAM,11)
            tagc(dd,SW/2,364,'COMBIEN D’INVITÉS ?',CORAL)
        elif key=='r0':
            insp(dd,64,GY,t,k=3.8)
            bignum(dd,206,150,'23',GOLD,w=150,h=100,size=60)
            star(dd,282,128,t,5); star(dd,150,120,t,4)
            tagc(dd,SW/2,364,'VINGT-TROIS SEULEMENT',GOLD)
        elif key=='r1':
            circle_people(dd,23,SW/2,210,98,k=1.5)
            T(dd,'23',SW/2,192,40,'press',30,GOLD,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'23 INVITÉS',GOLD)
        elif key=='r2':
            circle_people(dd,23,SW/2,210,98,k=1.5)
            pair_lines(dd,23,SW/2,210,98,min(1.0,lt/1.4))
            if lt>1.2: bignum(dd,SW/2,190,'253',GOLD,w=110,h=44,size=22)
            tagc(dd,SW/2,364,'253 PAIRES',GOLD)
        elif key=='r3':
            person(dd,60,160,CORAL,4.0,hat=True); person(dd,222,160,CYAN,4.0,hat=True)
            dotline(dd,(100,190),(214,190),GOLD,t,n=12)
            T(dd,'=',156,168,30,'press',24,GOLD,align='c') if False else None
            lbl(dd,SW/2,244,'1 CHANCE SUR 365',GOLD,11)
            tagc(dd,SW/2,364,'UNE PETITE CHANCE',CYAN)
        elif key=='r4':
            f=min(1.0,lt/2.2)*0.507
            gauge(dd,36,210,240,f,GOLD)
            for i in range(8): box(dd,40+i*30,150+(i%2)*6,12,12,fill=GCOL[i%5])
            T(dd,'+ + + + +',SW/2,120,16,'press',12,CORAL,align='c')
            lbl(dd,SW/2,262,('%.1f %%'%(f*100)).replace('.',','),GOLD,12)
            tagc(dd,SW/2,364,'ELLES S’ADDITIONNENT',GOLD)
        elif key=='r5':
            gauge(dd,36,230,240,0.507,GOLD)
            bignum(dd,SW/2,130,'50,7 %',GOLD,w=200,h=64,size=30)
            lbl(dd,SW/2,282,'23 INVITÉS',CYAN,11)
            star(dd,40,150,t,4); star(dd,272,150,t,4)
            tagc(dd,SW/2,364,'PLUS D’UNE CHANCE SUR 2',GOLD)
        elif key=='r6':
            gauge(dd,36,230,240,0.99,CORAL)
            bignum(dd,SW/2,130,'99 %',CORAL,w=170,h=64,size=32)
            lbl(dd,SW/2,282,'57 INVITÉS',CYAN,11)
            tagc(dd,SW/2,364,'57 INVITÉS',CORAL)
        elif key=='r7':
            gauge(dd,36,230,240,0.999,RED)
            bignum(dd,SW/2,130,'99,9 %',RED,w=210,h=64,size=30)
            lbl(dd,SW/2,282,'70 INVITÉS',CYAN,11)
            tagc(dd,SW/2,364,'PRESQUE CERTAIN',RED)
        elif key=='r8':
            circle_people(dd,23,SW/2,200,92,k=1.4)
            n=int(min(23,lt*6)); T(dd,str(n),SW/2,182,40,'press',30,CREAM,align='c',shadow=(3,3,BLACK))
            tagc(dd,SW/2,364,'ON COMPTE LES PERSONNES',CYAN)
        elif key=='r9':
            circle_people(dd,23,SW/2,210,98,k=1.5)
            pair_lines(dd,23,SW/2,210,98,1.0,rgb('#B05CFF'))
            ok_stamp(dd,SW/2,206,'PAIRES',GOLD)
            tagc(dd,SW/2,364,'ET OUBLIE LES PAIRES',CORAL)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#026'
    def fn(lay,dd):
        crowd(dd,30,230,9,2,gx=28,gy=40,k=1.8,hat=True)
        cake(dd,SW/2,150,1.1,t)
        T(dd,'DANS UNE SALLE,',SW/2,10,36,'anton',28,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'MÊME ANNIVERSAIRE ?',SW/2,44,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DES ANNIVERSAIRES"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#027')
