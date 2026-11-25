import re
src=open('build_e60.py').read()
def gen(n,Lh,Lr,st,an,chimes):
    s=src.replace('e60',f'e{n}').replace('ep60',f'ep{n}')
    s=re.sub(r"L=0\.25; a=add\(load\('01_histoire',L\)",f"L={Lh}; a=add(load('01_histoire',L)",s)
    s=re.sub(r"L=0\.12; c_=add",f"L={Lr}; c_=add",s)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s)
    s=s.replace("chime(T['r0']);chime(T['r5']);chime(T['r7'])",";".join("chime(T['%s'])"%c for c in chimes))
    open(f'build_e{n}.py','w').write(s)
gen('61',0.11,0.30,
 [('s1',0.13),('s2',2.32),('s3',4.14),('s4',6.84),('s5',10.04),('q',13.42)],
 [('r0',0.32),('r1',2.92),('r2',4.92),('r3',6.36),('r4',8.9),('r5',12.06),('r6',15.78),('r7',19.38),('r8',21.74),('r9',25.84)],['r0','r5','r6'])
gen('62',0.23,0.13,
 [('s1',0.25),('s2',2.40),('s3',5.66),('s4',7.34),('s5',9.80),('q',11.84)],
 [('r0',0.15),('r1',3.04),('r2',7.48),('r3',10.16),('r4',12.0),('r5',13.98),('r6',15.98),('r7',21.52),('r8',26.22),('r9',29.5)],['r0','r2','r7'])
