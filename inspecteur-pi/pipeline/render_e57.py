from render_e4x import *
import inspect, math
B.NUM='#057'
def sp(lt,a,b): return max(0.0,min(1.0,(lt-a)/(b-a)))
def blink(t): return int(t*2.5)%2==0
GREYP=dict(MPAL)
for _k in list(GREYP): GREYP[_k]='#3A4270'
PIR=[CANDP[3],CANDP[0],CANDP[1],CANDP[2],CANDP[5]]
FEET=296
def px(i): return 36+60*(i-1)
def gold(dd,cx,cy,r=6):
    disc(dd,cx,cy,r+2,DARK); disc(dd,cx,cy,r,GOLD); disc(dd,cx,cy,r*0.6,rgb('#FFF3B0'),None,0)
def pile(dd,cx,cy,n=14,sc=1.0):
    pts=[(0,0),(-9,2),(9,2),(-18,5),(18,5),(0,-8),(-9,-6),(9,-6),(-4,-15),(4,-15),(-14,-3),(14,-3),(0,6),(-22,9),(22,9),(-27,10),(27,10)]
    for dx,dy in sorted(pts[:n],key=lambda p:p[1]): gold(dd,cx+dx*sc,cy+dy*sc,6*sc)
def crown(dd,cx,top):
    box(dd,cx-9,top+6,18,6,fill=GOLD,border=DARK,bw=1)
    for dx in (-9,-1,7): box(dd,cx+dx,top,4,7,fill=GOLD,border=DARK,bw=1)
def pirates(dd,t,alive=(1,2,3,4,5),hl=(),amt=None,oui=None,chef=1,feet=FEET,amtcol=None,nums=True,ghost=True):
    for i in range(1,6):
        cx=px(i)
        if i in alive:
            if i in hl: box(dd,cx-27,feet-72,54,106,fill=CARD,border=GOLD,bw=3)
            pri(dd,cx,feet,t,k=4.0,pal=PIR[i-1],ph=i)
            if i==chef: crown(dd,cx,feet-14*4-10)
        elif ghost:
            pri(dd,cx,feet,t,k=4.0,pal=GREYP,still=True)
        if nums: T(dd,str(i),cx,feet+12,16,'press',12,(GOLD if i==chef else (CREAM if i in alive else DIM)),align='c')
        if amt and i in amt:
            v=amt[i]; c=(amtcol or {}).get(i, GOLD if v not in ('0',) else GREY)
            numcard(dd,cx,feet-104,v,c,11,dim=(i not in alive))
        if oui and i in oui:
            ok=oui[i]
            c=GRN if ok else RED
            box(dd,cx-24,feet-150,48,26,fill=CARD,border=c,bw=3,shadow=(3,3,BLACK)); T(dd,'OUI' if ok else 'NON',cx,feet-144,16,'press',11,c,align='c')
def water(dd,y=318,t=0.0):
    box(dd,0,y,SW,48,fill=rgb('#1B4F8A'))
    for k in range(8): box(dd,k*44+(t*20)%44-44,y,22,5,fill=rgb('#4DA3FF'))
HEADS={'s1':[('Cent pièces, ',GOLD),('cinq pirates',CORAL)],
 's2':[('5 pirates',CORAL),(' et ',CREAM),('100 pièces',GOLD)],
 's3':[('Le ',CREAM),('chef',GOLD),(' propose',CREAM)],
 's4':[('Tout le monde ',CREAM),('vote',CYAN)],
 's5':[('Moitié de ',CREAM),('oui',GRN),(' : adopté',CREAM)],
 's6':[('Sinon : ',CREAM),('à l’eau',CYAN),(' !',CREAM)],
 's7':[('Au pirate ',CREAM),('suivant',CORAL)],
 's8':[('Chacun veut un ',CREAM),('maximum d’or',GOLD)],
 's9':[('Gain égal : ',CREAM),('vote non',RED)],
 'q':[('Le chef garde ',CREAM),('combien',GOLD),(' ?',CREAM)],
 'r0':[('La réponse : ',CREAM),('98',GOLD)],
 'r1':[('On commence par ',CREAM),('la fin',CYAN)],
 'r2':[('Deux pirates',CORAL)],
 'r3':[('Trois pirates',CORAL)],
 'r4':[('Quatre pirates',CORAL)],
 'r5':[('Cinq pirates',CORAL)],
 'r6':[('Sinon ils n’ont ',CREAM),('rien',RED)],
 'r7':[('Le chef garde ',CREAM),('98',GOLD)],
 'r8':[('Le piège : ',CREAM),('partage égal',CORAL)],
 'r9':[('Enregistre-la !',CREAM)]}
STORY=('s1','s2','s3','s4','s5','s6','s7','s8','s9','q')
def scene_fn(key,t,lt,dur):
    def fn(lay,dd):
        cx=SW/2
        if key=='s1':
            pile(dd,cx,170,17,1.5); numcard(dd,cx,104,'100',GOLD,16)
            pirates(dd,t,hl=(1,))
            if blink(t): numcard(dd,px(1),FEET-100,'?',GOLD,11)
            tagc(dd,cx,364,'COMBIEN GARDE LE CHEF ?',GOLD)
        elif key=='s2':
            n=min(17,3+int(lt*8)); pile(dd,cx,170,n,1.5); numcard(dd,cx,104,'100 PIÈCES',GOLD,12)
            pirates(dd,t)
            tagc(dd,cx,364,'5 PIRATES, 100 PIÈCES D’OR',GOLD)
        elif key=='s3':
            pirates(dd,t,hl=(1,))
            pile(dd,cx,150,12,1.1)
            stamp(dd,cx,208,'MON PARTAGE !',CORAL,13)
            tagc(dd,cx,364,'LE CHEF PROPOSE UN PARTAGE',CORAL)
        elif key=='s4':
            votes={1:True,2:False,3:True,4:False,5:True}
            oui={i:v for j,(i,v) in enumerate(votes.items()) if lt>0.15+j*0.28}
            pirates(dd,t,oui=oui)
            tagc(dd,cx,364,'TOUT LE MONDE VOTE',CYAN)
        elif key=='s5':
            for j in range(5):
                x=cx-2*60+j*60; on=lt>0.1+j*0.25 and j<3
                box(dd,x-22,120,44,44,fill=(GRN if on else CARD),border=(GRN if on else EDGE),bw=3,shadow=(3,3,BLACK))
                if on: check(dd,x,140,12,5,DARK)
            box(dd,cx-2*60-22,176,2.5*60+44-22+0,6,fill=GOLD)
            T(dd,'MOITIÉ',cx-2*60-22+55,186,14,'silk7',11,GOLD,align='c')
            if lt>1.5: stamp(dd,cx,248,'OK, ADOPTE !',GRN,18)
            tagc(dd,cx,364,'AU MOINS LA MOITIÉ DE OUI',GRN)
        elif key=='s6':
            p=sp(lt,0.3,1.8)
            pirates(dd,t,alive=(2,3,4,5),nums=False,ghost=False)
            fy=FEET+p*95
            pri(dd,px(1),fy,t,k=4.0,pal=PIR[0],ph=1)
            water(dd,326,t)
            T(dd,'2',px(2),FEET+10,16,'press',12,CREAM,align='c'); T(dd,'3',px(3),FEET+10,16,'press',12,CREAM,align='c'); T(dd,'4',px(4),FEET+10,16,'press',12,CREAM,align='c'); T(dd,'5',px(5),FEET+10,16,'press',12,CREAM,align='c')
            if p>0.8:
                for dx in (-14,0,14): disc(dd,px(1)+dx,322-abs(dx)*0.6-(p-0.8)*20,4,CYAN)
                stamp(dd,cx,150,'SPLASH !',CYAN,16)
            tagc(dd,cx,364,'SINON, LE CHEF EST JETÉ À L’EAU',CYAN)
        elif key=='s7':
            pirates(dd,t,alive=(2,3,4,5),hl=(2,),chef=2)
            T(dd,'X',px(1),FEET-30,22,'press',16,DIM,align='c')
            stamp(dd,cx,190,'AU SUIVANT !',CORAL,14)
            tagc(dd,cx,364,'LE PIRATE SUIVANT PROPOSE',CORAL)
        elif key=='s8':
            pirates(dd,t)
            for i in range(1,6):
                for j in range(3): gold(dd,px(i)-12+j*12,FEET-96-((int(t*3)+i+j)%2)*4,5)
            pile(dd,cx,170,9,1.2)
            tagc(dd,cx,364,'CHACUN VEUT UN MAXIMUM D’OR',GOLD)
        elif key=='s9':
            numcard(dd,cx,112,'AVEC LUI : 0',CYAN,13); numcard(dd,cx,170,'SANS LUI : 0',CORAL,13)
            T(dd,'=',cx,228,30,'press',24,CREAM,align='c')
            if lt>1.0: stamp(dd,cx,290,'IL VOTE NON',RED,15)
            tagc(dd,cx,364,'GAIN ÉGAL : CHEF À L’EAU',RED)
        elif key=='q':
            pirates(dd,t,hl=(1,)); pile(dd,cx,160,17,1.5)
            if blink(t): stamp(dd,cx,222,'COMBIEN ?',GOLD,16)
            tagc(dd,cx,364,'ÉCRIS TA RÉPONSE EN COMMENTAIRE',CORAL)
        elif key=='r0':
            T(dd,'98',cx,120,100,'press',72,GOLD,align='c',shadow=(6,6,BLACK)); star(dd,30,120,t,6); star(dd,290,120,t+1,6)
            pile(dd,cx,248,17,1.4)
            tagc(dd,cx,364,'LA RÉPONSE : 98 PIÈCES',GOLD)
        elif key=='r1':
            pirates(dd,t,alive=(4,5),hl=(4,5),chef=0)
            stamp(dd,cx,190,'DU DERNIER AU PREMIER',CORAL,9)
            tagc(dd,cx,364,'ON COMMENCE PAR LA FIN',CYAN)
        elif key=='r2':
            pirates(dd,t,alive=(4,5),amt={4:'100',5:'0'},chef=4,hl=(4,))
            if lt>3.0: stamp(dd,cx,136,'SON VOTE SUFFIT',GRN,12)
            tagc(dd,cx,364,'À DEUX : LE 4 PREND TOUT',GOLD)
        elif key=='r3':
            pirates(dd,t,alive=(3,4,5),amt={3:'99',4:'0',5:'1'},chef=3,hl=(5,))
            tagc(dd,cx,364,'À TROIS : 1 PIÈCE AU 5',GOLD)
        elif key=='r4':
            pirates(dd,t,alive=(2,3,4,5),amt={2:'99',3:'0',4:'1',5:'0'},chef=2,hl=(4,))
            tagc(dd,cx,364,'À QUATRE : 1 PIÈCE AU 4',GOLD)
        elif key=='r5':
            pirates(dd,t,amt={1:'98',2:'0',3:'1',4:'0',5:'1'},hl=((3,5) if lt>1.8 else ()))
            tagc(dd,cx,364,'À CINQ : 1 PIÈCE AU 3 ET AU 5',GOLD)
        elif key=='r6':
            pirates(dd,t,amt={1:'98',2:'0',3:'1',4:'0',5:'1'},oui={1:True,3:True,5:True} if lt>1.0 else None)
            if lt>1.5: stamp(dd,cx,112,'3 OUI SUR 5 : OK !',GRN,11)
            tagc(dd,cx,364,'SINON ILS N’AURAIENT RIEN',CORAL)
        elif key=='r7':
            T(dd,'98',cx,104,100,'press',54,GOLD,align='c',shadow=(6,6,BLACK))
            pirates(dd,t,hl=(1,),amt={1:'98',2:'0',3:'1',4:'0',5:'1'})
            tagc(dd,cx,364,'LE CHEF GARDE 98 PIÈCES',GOLD)
        elif key=='r8':
            pirates(dd,t,amt={i:'20' for i in range(1,6)})
            if lt>0.4: xmark_(dd,cx,150,34,10,RED)
            tagc(dd,cx,364,'LE PIÈGE : CROIRE AU PARTAGE ÉGAL',CORAL)
        elif key=='r9':
            bx,by=cx-34,130; box(dd,bx,by,68,110,fill=GOLD,border=DARK,bw=3,shadow=(4,4,BLACK))
            dd.polygon([((bx+10)*S,(by+110)*S),((bx+58)*S,(by+110)*S),((bx+34)*S,(by+84)*S)],fill=rgb('#07090F'))
            T(dd,'98',cx,by+22,40,'press',28,DARK,align='c')
            if blink(t): star(dd,cx+80,150,t,7)
            tagc(dd,cx,364,'ENREGISTRE-LA POUR PLUS TARD',GOLD)
    return fn
story=frame_fn(__import__('sys').modules[__name__],STORY,HEADS)
answer=story
def cover(t):
    B.NUM='#057'
    def fn(lay,dd):
        cx=SW/2
        pile(dd,cx,150,17,1.6)
        pirates(dd,t,hl=(1,),nums=False)
        numcard(dd,px(1),FEET-100,'?',GOLD,11)
        T(dd,'5 PIRATES, 100 PIÈCES :',SW/2,14,36,'anton',22,CREAM,sp=1,align='c',shadow=(3,3,BLACK)); T(dd,'COMBIEN GARDE LE CHEF ?',SW/2,48,36,'anton',22,GOLD,sp=1,align='c',shadow=(3,3,BLACK))
        B.band(lay,SH-44,40); d2_=ImageDraw.Draw(lay); txt="LE PARTAGE DES PIRATES"; f=F('silk4',11); T(d2_,txt,SW/2-tw(txt,f,1)/2,SH-30,14,'silk4',11,CREAM,sp=1)
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
end=make_end2('#058','ENREGISTRE-LA POUR PLUS TARD')
