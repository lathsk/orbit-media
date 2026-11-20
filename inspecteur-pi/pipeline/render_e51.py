from render_e4x import *
import inspect
B.NUM='#051'
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-18: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')


def bar(dd,cx,val,col,w=76,sc=1.25,base=330,label=None,dim=False,border=CREAM):
    h=val*sc
    box(dd,cx-w/2,base-h,w,h,fill=(rgb('#2A3050') if dim else col),border=border,bw=3,shadow=(3,3,BLACK))
    if label: numcard(dd,cx,base-h-44,label,col,14)
def ghost(dd,cx,val,w=76,sc=1.25,base=330,col=GREY):
    h=val*sc; box(dd,cx-w/2,base-h,w,3,fill=col)
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
HEADS={'s1':[('Plus ',CREAM),('50 %,',CORAL),(' puis ',CREAM),('moins 50',CYAN)],
 's2':[('Un ',CREAM),('manteau',GOLD),(' à ',CREAM),('100 €',GOLD)],
 's3':[('Le prix ',CREAM),('monte',CORAL),(' de 50 %',CREAM)],
 's4':[('Puis ',CREAM),('soldes',CYAN),(' : ',CREAM),('-50 %',CYAN)],
 's5':[('Tous disent ',CREAM),('100 €',GOLD)],
 's6':[('Mais ',CREAM),('est-ce vrai',CORAL),(' ?',CREAM)],
 'q':[('Quel est le ',CREAM),('prix final',GOLD),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('75 €',GOLD)],
 'r1':[('D’abord ',CREAM),('100 + 50 %',CORAL)],
 'r2':[('Ça fait ',CREAM),('150 €',GOLD)],
 'r3':[('Ensuite ',CREAM),('moins 50 %',CYAN)],
 'r4':[('Mais de ',CREAM),('150,',GOLD),(' pas de ',CREAM),('100',GREY)],
 'r5':[('La moitié de 150 : ',CREAM),('75',GOLD)],
 'r6':[('Donc ',CREAM),('25 € de moins',CORAL)],
 'r7':[('Pas le ',CREAM),('même prix',GOLD),(' de base',CREAM)],
 'r8':[('Pour revenir : ',CREAM),('+ un tiers',CYAN)]}
STORY=('s1','s2','s3','s4','s5','s6','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            numcard(dd,cx,118,'+50 %',CORAL,20); arrow_d(dd,cx,164,20)
            numcard(dd,cx,186,'-50 %',CYAN,20); arrow_d(dd,cx,232,20)
            numcard(dd,cx,254,'= ?',GOLD if int(t*2.5)%2==0 else CREAM,20)
            tagc(dd,cx,364,'PLUS 50 % PUIS MOINS 50 %',GOLD)
        elif key=='s2':
            bar(dd,cx,100,GOLD,label='100 €'); tagc(dd,cx,364,'UN MANTEAU À 100 €',GOLD)
        elif key=='s3':
            p=sp(lt,0.3,1.6); v=100+50*p
            bar(dd,cx,v,CORAL,label='%d €'%round(v)); ghost(dd,cx,100)
            T(dd,'+50 %',cx+100,200,24,'press',16,CORAL,align='c'); tagc(dd,cx,364,'LE PRIX AUGMENTE DE 50 %',CORAL)
        elif key=='s4':
            bar(dd,cx,150,CYAN,dim=True,border=CYAN,label='? €')
            T(dd,'-50 %',cx,330-150*1.25/2-8,20,'press',12,CYAN,align='c')
            T(dd,'-50 %',cx+100,200,24,'press',16,CYAN,align='c'); tagc(dd,cx,364,'PUIS SOLDES : MOINS 50 %',CYAN)
        elif key=='s5':
            bar(dd,cx,100,GOLD,dim=True,border=GREY); numcard(dd,cx,150,'100 € ?',GOLD,22)
            tagc(dd,cx,364,'PRESQUE TOUS DISENT 100 €',GOLD)
        elif key=='s6':
            bar(dd,cx,100,GOLD,dim=True,border=GREY)
            if int(t*2.5)%2==0: numcard(dd,cx,150,'VRAI ?',CORAL,24)
            tagc(dd,cx,364,'EST-CE VRAIMENT LE CAS ?',CORAL)
        elif key=='q':
            box(dd,cx-120,170,240,78,fill=CARD,border=GOLD,bw=4,shadow=(4,4,BLACK)); T(dd,'? €',cx,190,40,'press',32,GOLD,align='c'); lbl(dd,cx,228,'PRIX FINAL',CREAM,10)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'75',cx-24,134,100,'press',80,GOLD,align='c',shadow=(6,6,BLACK)); T(dd,'€',cx+100,160,60,'press',44,GOLD,align='c',shadow=(4,4,BLACK)); star(dd,30,120,t,6); star(dd,290,120,t+1,6)
            stamp(dd,cx,300,'ET PAS 100 !',CORAL,14); tagc(dd,cx,364,'LA RÉPONSE : 75 €',GOLD)
        elif key=='r1':
            bar(dd,70,100,GOLD,w=64,label='100 €'); arrow_r(dd,140,250,40,CREAM)
            p=sp(lt,0.5,1.6); bar(dd,250,100+50*p,CORAL,w=64,label='%d €'%round(100+50*p)) 
            T(dd,'+50 %',160,222,24,'press',11,CORAL,align='c'); tagc(dd,cx,364,'100 € + 50 %',CORAL)
        elif key=='r2':
            bar(dd,cx,150,CORAL,label='150 €'); ghost(dd,cx,100); lbl(dd,cx+90,226,'100',GREY,10)
            tagc(dd,cx,364,'ÇA FAIT 150 €',GOLD)
        elif key=='r3':
            bar(dd,cx,150,CORAL,label='150 €'); h=75*1.25
            box(dd,cx-38,330-150*1.25,76,h,fill=CYAN,border=CREAM,bw=3)
            T(dd,'-50 %',cx,330-150*1.25+h/2-8,20,'press',12,BLACK,align='c'); tagc(dd,cx,364,'ENSUITE MOINS 50 %',CYAN)
        elif key=='r4':
            bar(dd,cx,150,CORAL,label='150 €'); ghost(dd,cx,100,col=GOLD)
            T(dd,'PAS DE 100 !',cx+0,210,24,'press',14,GOLD,align='c') if int(t*2.5)%2==0 else None
            tagc(dd,cx,364,'50 % DE 150 €, PAS DE 100 €',CYAN)
        elif key=='r5':
            bar(dd,70,150,CORAL,w=64,label='150 €',dim=True); arrow_r(dd,140,250,40,CREAM)
            p=sp(lt,0.4,1.6); bar(dd,250,150-75*p,CYAN,w=64,label=('75 €' if p>0.99 else '? €'))
            T(dd,'/ 2',160,222,24,'press',12,CYAN,align='c'); tagc(dd,cx,364,'LA MOITIÉ DE 150, C’EST 75',GOLD)
        elif key=='r6':
            bar(dd,70,100,GOLD,w=64,label='100 €',dim=True); bar(dd,250,75,CYAN,w=64,label='75 €')
            box(dd,250-32,330-100*1.25,64,25*1.25,fill=None,border=CORAL,bw=3); T(dd,'-25 €',226,330-100*1.25-34,24,'press',16,CORAL,align='c') if False else None
            numcard(dd,cx,250,'-25 €',CORAL,12); tagc(dd,cx,364,'25 € DE MOINS QU’AU DÉPART',CORAL)
        elif key=='r7':
            numcard(dd,cx,124,'+50 % de 100 €',CORAL,14); T(dd,'PAS PAREIL',cx,172,24,'press',14,CORAL,align='c')
            numcard(dd,cx,206,'-50 % de 150 €',CYAN,14); tagc(dd,cx,364,'PAS LE MÊME PRIX DE BASE',GOLD)
        elif key=='r8':
            bar(dd,cx,75,CYAN,label=None); p=sp(lt,0.6,1.6)
            if p>0.25: box(dd,cx-38,330-(75+25*p)*1.25,76,25*p*1.25,fill=GOLD,border=CREAM,bw=3)
            numcard(dd,cx,330-100*1.25-44,'100 €' if p>0.99 else '75 €',GOLD,14)
            T(dd,'+ 1/3',cx+104,200,24,'press',16,GOLD,align='c'); tagc(dd,cx,364,'REMONTER D’UN TIERS',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#051'
    def fn(lay,dd):
        cx=SW/2
        numcard(dd,cx,106,'+50 %',CORAL,22); arrow_d(dd,cx,158,20)
        numcard(dd,cx,180,'-50 %',CYAN,22); arrow_d(dd,cx,232,20); numcard(dd,cx,254,'= 100 € ?',GOLD,22)
        T(dd,'PLUS 50 %, PUIS',SW/2,14,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'MOINS 50 % ?',SW/2,48,36,'anton',28,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="PRESQUE TOUS SE TROMPENT"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#052','ENREGISTRE-LA POUR PLUS TARD')
