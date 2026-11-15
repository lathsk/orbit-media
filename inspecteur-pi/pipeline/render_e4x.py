# Éléments communs aux épisodes #041 et #042
from render_e2x import *
def numcard(dd,cx,y,txt,col=GOLD,size=24,fill=None,dim=False):
    w=len(txt)*size+26; h=size+22
    c=DIM if dim else col
    box(dd,cx-w/2,y,w,h,fill=fill or CARD,border=c,bw=3,shadow=(3,3,BLACK))
    T(dd,txt,cx,y+11,size+4,'press',size,c,align='c')
    return h
def arrow_d(dd,x,y,h=16,col=CREAM):
    box(dd,x-2,y,5,h-6,fill=col); dd.polygon([((x-7)*S,(y+h-7)*S),((x+8)*S,(y+h-7)*S),((x+0.5)*S,(y+h)*S)],fill=col)
def arrow_r(dd,x,y,w=24,col=CREAM):
    box(dd,x,y-2,w-6,5,fill=col); dd.polygon([((x+w-7)*S,(y-7)*S),((x+w-7)*S,(y+8)*S),((x+w)*S,(y+0.5)*S)],fill=col)
def check(dd,cx,cy,r=14,w=5,col=GRN):
    dd.line([((cx-r)*S,cy*S),((cx-r*0.35)*S,(cy+r*0.7)*S)],fill=col,width=w*S)
    dd.line([((cx-r*0.35)*S,(cy+r*0.7)*S),((cx+r)*S,(cy-r*0.8)*S)],fill=col,width=w*S)
def minus(dd,cx,cy,w=30,col=CORAL): box(dd,cx-w/2,cy-3,w,7,fill=col)
def vline(dd,x1,x2,y,col=CREAM): box(dd,x1,y,x2-x1,4,fill=col)
def eqn(dd,a,b,res,size=24,y0=120,cres=CORAL,ca=GOLD,cb=CYAN,resdim=False):
    h=size+22
    numcard(dd,SW/2+10,y0,a,ca,size); numcard(dd,SW/2+10,y0+h+10,b,cb,size)
    minus(dd,32,y0+h+10+h/2,26)
    ly=y0+2*h+22; vline(dd,60,SW-20,ly)
    numcard(dd,SW/2+10,ly+14,res,cres,size+4,dim=resdim)
def chain(dd,vals,n,size=16,y0=116,last=None,labels=None):
    h=size+22; gap=20
    for i,v in enumerate(vals[:n]):
        y=y0+i*(h+gap)
        col=CREAM if i==0 else (CYAN if i%2 else CORAL)
        if last is not None and i==n-1 and i==len(vals)-1: col=GOLD
        numcard(dd,SW/2-20,y,v,col,size)
        if i<n-1: arrow_d(dd,SW/2-20,y+h+2,gap-2,CREAM)
        if labels and i<len(labels) and i<n and i>0: lbl(dd,262,y+h/2-9,labels[i],GREY,8)
def sorted_man(dd,cx,feet,t,pal,k=3.0):
    sprite(dd,MAN,pal,cx-5*k,feet-14*k+math.sin(t*3+cx)*1.0,k,10)
CANDP=[dict(MPAL,T=c) for c in ('#4DA3FF','#4CC36B','#B05CFF','#FF7A59','#FFD23F','#8FE3FF')]
