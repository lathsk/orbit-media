import re,sys
src=open('build_e54.py').read()
def gen(n,Lh,Lr,st,an,en,chimes):
    s=src.replace('e54',f'e{n}')
    s=re.sub(r"L=0\.267; a=add\(load\('01_histoire',L\)",f"L={Lh}; a=add(load('01_histoire',L)",s)
    s=re.sub(r"L=0\.25; c_=add",f"L={Lr}; c_=add",s)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('e0'.*?\]: T\[k\]=at\(e,t,L\)",lambda m:"for k,t in %r: T[k]=at(e,t,L)"%en,s,flags=re.S)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1,flags=re.S)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s,flags=re.S)
    s=re.sub(r"chime\(T\['r0'\]\);chime\(T\['r7'\]\)",";".join("chime(T['%s'])"%c for c in chimes),s)
    open(f'build_e{n}.py','w').write(s)
en=[('e0',0.0),('e1',2.28),('e2',4.6),('e3',5.38)]
gen('55',0.26,0.18,
 [('s1',0.30),('s2',2.82),('s3',5.10),('s4',6.50),('s5',7.90),('s6',9.88),('s7',11.78),('q',14.28)],
 [('r0',0.20),('r1',2.52),('r2',6.18),('r3',9.26),('r4',11.78),('r5',15.70),('r6',18.84),('r7',21.90)],en,['r0','r4'])
gen('56',0.23,0.25,
 [('s1',0.30),('s2',2.60),('s3',3.88),('s4',6.74),('s5',9.78),('s6',12.76),('s7',15.68),('q',18.10)],
 [('r0',0.25),('r1',2.46),('r2',5.24),('r3',8.14),('r4',10.96),('r5',13.48),('r6',16.72),('r7',19.50)],en,['r0','r4'])
