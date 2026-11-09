from render_e2x import *
B.NUM='#030'
HEADS={'s1':[('Un ',CREAM),('marchand',GOLD),(' et une ',CREAM),('balance',CYAN)],
 's2':[('Peser ',CREAM),('n’importe',GOLD),(' quelle masse',CREAM)],
 's3':[('De ',CREAM),('1',GOLD),(' à ',CREAM),('40 kg',GOLD)],
 's4':[('Seulement ',CREAM),('quatre',CORAL),(' poids',CREAM)],
 's5':[('Poids sur les ',CREAM),('deux',GOLD),(' plateaux',CREAM)],
 's6':[('Même du côté de la ',CREAM),('marchandise',CORAL)],
 's7':[('6 ou 7',CORAL),(' poids ?',CREAM)],
 'q':[('Quels ',CREAM),('4 poids',GOLD),(' choisir ?',CREAM)],
 'r0':[('Réponse : ',CREAM),('1, 3, 9',GOLD),(' et ',CREAM),('27',GRN),(' kg',CREAM)],
 'r1':[('Chaque poids : ',CREAM),('× 3',GOLD)],
 'r2':[('Peser ',CREAM),('2 kg',CORAL)],
 'r3':[('3',GOLD),(' - ',CREAM),('1',CYAN),(' = ',CREAM),('2',CORAL)],
 'r4':[('Peser ',CREAM),('5 kg',CORAL)],
 'r5':[('9',CORAL),(' - ',CREAM),('4',CYAN),(' = ',CREAM),('5',GOLD)],
 'r6':[('1 + 3 + 9 + 27',GOLD),(' = ',CREAM),('40',GRN)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','q')
WC={1:CYAN,3:GOLD,9:CORAL,27:GRN}
def bignum(dd,cx,y,txt,col=GOLD,w=120,h=64,size=32):
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=4,shadow=(4,4,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')
def item(dd,x,y,it):
    txt,col=it
    w=34 if len(txt)<3 else 42
    box(dd,x-w/2,y,w,30,fill=CARD,border=col,bw=3,shadow=(2,2,BLACK)); T(dd,txt,x,y+(8 if len(txt)<3 else 10),16,'press',(11 if len(txt)<3 else 9),col,align='c')
def balance(dd,L,R,cx=SW/2,by=140,py=240):
    box(dd,cx-8,by,16,py-by+58,fill=DIM)
    box(dd,cx-30,py+56,60,10,fill=DIM,border=DARK,bw=2)
    box(dd,cx-108,by-4,216,8,fill=CREAM,border=DARK,bw=2)
    for side,items in ((-1,L),(1,R)):
        x=cx+side*84; ax=cx+side*98
        dd.line([(ax*S,(by+4)*S),((x-48)*S,py*S)],fill=CREAM,width=2*S); dd.line([(ax*S,(by+4)*S),((x+48)*S,py*S)],fill=CREAM,width=2*S)
        box(dd,x-52,py,104,8,fill=CREAM,border=DARK,bw=2)
        if len(items)<3:
            n=len(items); gap=42
            x0=x-(n-1)*gap/2
            for i,it in enumerate(items): item(dd,x0+i*gap,py-32,it)
        else:
            item(dd,x-21,py-32,items[0]); item(dd,x+21,py-32,items[1]); item(dd,x-21,py-66,items[2])
def W(n): return (str(n),WC[n])
G=lambda t: (t,CORAL)
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        if key=='s1':
            balance(dd,[],[]); tagc(dd,SW/2,364,'UNE BALANCE À 2 PLATEAUX',CYAN)
        elif key=='s2':
            balance(dd,[G('?KG')],[]); tagc(dd,SW/2,364,'N’IMPORTE QUELLE MASSE',GOLD)
        elif key=='s3':
            bignum(dd,SW/2,130,'1 À 40 KG',GOLD,w=260,h=70,size=26)
            for i,v in enumerate((1,2,3,'…',40)): bignum(dd,40+i*58,230,str(v),[CYAN,CORAL,GOLD,CREAM,GRN][i],w=48,h=44,size=14)
            tagc(dd,SW/2,364,'DE UN À QUARANTE',GOLD)
        elif key=='s4':
            for i in range(4): bignum(dd,52+i*69,150,'?',[CYAN,GOLD,CORAL,GRN][i],w=58,h=70,size=30)
            lbl(dd,SW/2,250,'SEULEMENT 4 POIDS',CREAM,12)
            insp(dd,SW/2,GY,t,k=2.0)
            tagc(dd,SW/2,364,'QUATRE POIDS',CORAL)
        elif key=='s5':
            balance(dd,[W(3)],[W(9)]); tagc(dd,SW/2,364,'POIDS DES DEUX CÔTÉS',GOLD)
        elif key=='s6':
            balance(dd,[G('2KG'),W(1)],[W(3)]); tagc(dd,SW/2,364,'AVEC LA MARCHANDISE',CORAL)
        elif key=='s7':
            n=min(7,2+int(lt*2.2))
            for i in range(7):
                if i<n: bignum(dd,SW/2-(n-1)*21+i*42,150,'?',[CYAN,GOLD,CORAL,GRN][i%4],w=36,h=60,size=22)
            insp(dd,SW/2,GY,t,k=2.3)
            tagc(dd,SW/2,364,'6 OU 7 POIDS ?',CORAL)
        elif key=='q':
            for i in range(4): bignum(dd,52+i*69,130,'?',[CYAN,GOLD,CORAL,GRN][i],w=58,h=70,size=30)
            bignum(dd,SW/2,230,'JUSQU’À 40 KG',CYAN,w=250,h=42,size=14)
            insp(dd,SW/2,GY,t,k=2.0)
            tagc(dd,SW/2,364,'QUELS QUATRE POIDS ?',CORAL)
        elif key=='r0':
            insp(dd,SW/2,GY,t,k=2.0)
            for i,v in enumerate((1,3,9,27)):
                if lt>=[1.0,1.4,1.9,2.4][i]: bignum(dd,52+i*69,150,str(v),WC[v],w=58,h=70,size=22)
            star(dd,282,128,t,5); star(dd,40,120,t,4)
            tagc(dd,SW/2,364,'1 - 3 - 9 - 27 KG',GOLD)
        elif key=='r1':
            for i,v in enumerate((1,3,9,27)):
                bignum(dd,40+i*76,170,str(v),WC[v],w=58,h=64,size=22)
                if i<3: T(dd,'×3',40+i*76+38,130,20,'press',14,CREAM,align='c')
            lbl(dd,SW/2,270,'CHAQUE POIDS = 3 × LE PRÉCÉDENT',CREAM,10)
            tagc(dd,SW/2,364,'TRIPLE DU PRÉCÉDENT',GOLD)
        elif key=='r2':
            balance(dd,[G('2KG'),W(1)],[W(3)]); tagc(dd,SW/2,364,'2 KG + 1 KG = 3 KG',GOLD)
        elif key=='r3':
            bignum(dd,SW/2,130,'3 - 1 = 2',GOLD,w=260,h=70,size=26)
            balance(dd,[G('2KG'),W(1)],[W(3)],by=250,py=300) if False else None
            lbl(dd,SW/2,230,'DEUX KILOS',CORAL,12)
            tagc(dd,SW/2,364,'3 MOINS 1 ÉGALE 2',GOLD)
        elif key=='r4':
            balance(dd,[G('5KG'),W(3),W(1)],[W(9)]); tagc(dd,SW/2,364,'5 KG + 3 + 1 = 9',GOLD)
        elif key=='r5':
            bignum(dd,SW/2,130,'9 - 4 = 5',GOLD,w=260,h=70,size=26)
            lbl(dd,SW/2,230,'CINQ KILOS',CORAL,12)
            tagc(dd,SW/2,364,'9 MOINS 4 ÉGALE 5',GOLD)
        elif key=='r6':
            for i,v in enumerate((1,3,9,27)): bignum(dd,52+i*69,130,str(v),WC[v],w=58,h=64,size=22)
            bignum(dd,SW/2,230,'= 40 KG',GOLD,w=210,h=56,size=24)
            star(dd,282,210,t,4)
            tagc(dd,SW/2,364,'TOUT JUSQU’À 40 KG',GRN)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#030'
    def fn(lay,dd):
        balance(dd,[('?',CYAN),('?',GOLD)],[('?',CORAL),('?',GRN)],by=168,py=250)
        T(dd,'4 POIDS, UNE BALANCE,',SW/2,10,36,'anton',24,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'TOUT PESER JUSQU’À 40 KG ?',SW/2,44,36,'anton',22,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="L'ÉNIGME DES QUATRE POIDS"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
    return B.frame_with(B.make_scene(fn,t),'ÉNIGME DU JOUR')
decide=make_decide()
end=make_end('#031')
