from render_e4x import *
import inspect
B.NUM='#052'
def nb(dd,cx,y,txt,col=GOLD,w=64,h=64,size=32):
    while size>8 and tw(txt,F('press',size),0)>w-18: size-=1
    box(dd,cx-w/2,y,w,h,fill=CARD,border=col,bw=3,shadow=(3,3,BLACK)); T(dd,txt,cx,y+(h-size-4)/2+2,size+4,'press',size,col,align='c')



def kid(dd,cx,y,ch,col,sz=52,dim=False,cross=False):
    c=GREY if dim else col
    box(dd,cx-sz/2,y,sz,sz,fill=CARD,border=c,bw=3,shadow=(3,3,BLACK))
    T(dd,ch,cx,y+(sz-26)/2+2,sz*0.6,'press',26,c,align='c')
    if cross:
        dd.line([((cx-sz/2+4)*S,(y+4)*S),((cx+sz/2-4)*S,(y+sz-4)*S)],fill=CORAL,width=5*S)
        dd.line([((cx+sz/2-4)*S,(y+4)*S),((cx-sz/2+4)*S,(y+sz-4)*S)],fill=CORAL,width=5*S)
def pair(dd,y,a,b,dim=False,cross=False,hl=None,cx=None):
    cx=SW/2 if cx is None else cx
    ca={'F':CORAL,'G':CYAN,'?':GOLD}
    kid(dd,cx-40,y,a,ca[a],dim=dim,cross=cross); kid(dd,cx+40,y,b,ca[b],dim=dim,cross=cross)
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
HEADS={'s1':[('Deux ',CREAM),('enfants',GOLD),(' : ',CREAM),('une fille',CORAL)],
 's2':[('Une ',CREAM),('famille,',GOLD),(' deux enfants',CREAM)],
 's3':[('Il sait ',CREAM),('une seule chose',CYAN)],
 's4':[('Pas ',CREAM),('deux garçons',CYAN)],
 's5':[('Au moins ',CREAM),('une fille',CORAL)],
 's6':[('Tous disent : ',CREAM),('1 sur 2',GOLD)],
 's7':[('Mais est-ce ',CREAM),('juste',CORAL),(' ?',CREAM)],
 'q':[('Chance de ',CREAM),('deux filles',CORAL),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('1 sur 3',GOLD)],
 'r1':[('Les enfants ',CREAM),('dans l’ordre',CYAN)],
 'r2':[('Quatre ',CREAM),('familles',GOLD),(' possibles',CREAM)],
 'r3':[('FF, FG, ',CORAL),('GF, GG',CYAN)],
 'r4':[('Mais ',CREAM),('pas GG',CORAL)],
 'r5':[('Il reste ',CREAM),('trois familles',GOLD)],
 'r6':[('Une seule a ',CREAM),('deux filles',CORAL)],
 'r7':[('Donc ',CREAM),('1 sur 3',GOLD),(', pas 1 sur 2',GREY)],
 'r8':[('FG et GF : ',CREAM),('deux cas',CYAN)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','q')
ROWS=[('F','F',CORAL),('F','G',GOLD),('G','F',CYAN),('G','G',GREY)]
def fam(dd,i,y,dim=False,cross=False,hl=False):
    a,b,_=ROWS[i]; pair(dd,y,a,b,dim=dim,cross=cross)
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            pair(dd,150,'F','?'); T(dd,'?',cx+40,150,10,'press',1,CREAM) if False else None
            tagc(dd,cx,364,'DEUX ENFANTS, UNE FILLE',CORAL)
        elif key=='s2':
            pair(dd,150,'?','?'); tagc(dd,cx,364,'UNE FAMILLE, DEUX ENFANTS',GOLD)
        elif key=='s3':
            pair(dd,150,'?','?'); tagc(dd,cx,364,'IL SAIT UNE SEULE CHOSE',CYAN)
        elif key=='s4':
            pair(dd,150,'G','G',cross=lt>0.5); tagc(dd,cx,364,'CE NE SONT PAS DEUX GARÇONS',CYAN)
        elif key=='s5':
            a,b=('F','?') if int(t*2.5)%2==0 else ('?','F'); pair(dd,150,a,b); tagc(dd,cx,364,'AU MOINS UNE FILLE',CORAL)
        elif key=='s6':
            pair(dd,120,'F','?'); numcard(dd,cx,214,'1 SUR 2 ?',GOLD,22); tagc(dd,cx,364,'PRESQUE TOUS : 1 CHANCE SUR 2',GOLD)
        elif key=='s7':
            pair(dd,120,'F','?',dim=True)
            if int(t*2.5)%2==0: numcard(dd,cx,214,'JUSTE ?',CORAL,24)
            tagc(dd,cx,364,'MAIS EST-CE VRAIMENT JUSTE ?',CORAL)
        elif key=='q':
            pair(dd,120,'F','F',dim=False); numcard(dd,cx,214,'? SUR ?',GOLD,24)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'1/3',cx,134,100,'press',80,GOLD,align='c',shadow=(6,6,BLACK)); star(dd,30,120,t,6); star(dd,290,120,t+1,6)
            stamp(dd,cx,300,'ET PAS 1/2 !',CORAL,14); tagc(dd,cx,364,'LA RÉPONSE : 1 CHANCE SUR 3',GOLD)
        elif key=='r1':
            pair(dd,150,'?','?'); lbl(dd,cx-40,214,'AÎNÉ',CORAL,10); lbl(dd,cx+40,214,'CADET',CYAN,10)
            tagc(dd,cx,364,'DANS L’ORDRE : AÎNÉ, CADET',CYAN)
        elif key=='r2':
            for i in range(4):
                if lt>=0.15+0.35*i: fam(dd,i,112+i*58)
            tagc(dd,cx,364,'QUATRE FAMILLES POSSIBLES',GOLD)
        elif key=='r3':
            for i in range(4): fam(dd,i,112+i*58)
            tagc(dd,cx,364,'FILLE ET GARÇON : 4 CAS',CYAN)
        elif key=='r4':
            for i in range(3): fam(dd,i,112+i*58)
            fam(dd,3,112+3*58,cross=lt>0.5)
            tagc(dd,cx,364,'PAS GARÇON-GARÇON',CORAL)
        elif key=='r5':
            for i in range(3): fam(dd,i,112+i*58)
            fam(dd,3,112+3*58,dim=True,cross=True)
            numcard(dd,SW-32,200,'3',GOLD,22); tagc(dd,cx,364,'IL RESTE TROIS FAMILLES',GOLD)
        elif key=='r6':
            fam(dd,0,112); fam(dd,1,170,dim=True); fam(dd,2,228,dim=True); fam(dd,3,286,dim=True,cross=True)
            dd.rectangle([(cx-76)*S,106*S,(cx+76)*S,170*S],outline=GOLD,width=4*S); numcard(dd,SW-48,200,'1/3',GOLD,14); tagc(dd,cx,364,'UNE SEULE A DEUX FILLES',GOLD)
        elif key=='r7':
            T(dd,'1/3',cx,134,100,'press',80,GOLD,align='c',shadow=(6,6,BLACK))
            numcard(dd,cx,250,'PAS 1/2',GREY,20,dim=True); tagc(dd,cx,364,'1 SUR 3, PAS 1 SUR 2',GOLD)
        elif key=='r8':
            fam(dd,1,150); T(dd,'ET',cx,214,24,'press',12,CREAM,align='c') if False else None
            pair(dd,230,'G','F'); lbl(dd,cx,214,'ET',CREAM,12)
            tagc(dd,cx,364,'FG ET GF : DEUX CAS DIFFÉRENTS',CYAN)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#052'
    def fn(lay,dd):
        cx=SW/2
        pair(dd,150,'F','?')
        T(dd,'DEUX ENFANTS,',SW/2,14,36,'anton',26,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'UNE FILLE. ET L’AUTRE ?',SW/2,48,36,'anton',24,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2=ImageDraw.Draw(lay); txt="PRESQUE TOUS RÉPONDENT 1 SUR 2"; f=F('silk4',11); T(d2,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#053','ENVOIE-LA À QUELQU’UN')
