import re
src=open('build_e56.py').read()
def gen(n,Lh,Lr,st,an,en,chimes):
    s=src.replace('e56',f'e{n}').replace('ep56',f'ep{n}')
    s=s.replace("L=0.23; a=add(load('01_histoire',L)",f"L={Lh}; a=add(load('01_histoire',L)")
    s=s.replace("L=0.25; c_=add",f"L={Lr}; c_=add")
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('e0'.*?\]: T\[k\]=at\(e,t,L\)",lambda m:"for k,t in %r: T[k]=at(e,t,L)"%en,s,flags=re.S)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1,flags=re.S)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s,flags=re.S)
    s=s.replace("chime(T['r0']);chime(T['r4'])",";".join("chime(T['%s'])"%c for c in chimes))
    open(f'build_e{n}.py','w').write(s)
en=[('e0',0.0),('e1',2.0),('e2',2.75),('e3',3.80)]
gen('57',0.283,0.278,
 [('s1',0.30),('s2',3.64),('s3',6.32),('s4',8.08),('s5',9.0),('s6',11.9),('s7',13.66),('s8',15.74),('s9',17.86),('q',20.32)],
 [('r0',0.30),('r1',2.94),('r2',5.30),('r3',10.0),('r4',13.84),('r5',16.58),('r6',20.30),('r7',22.54),('r8',24.66),('r9',27.02)],en,['r0','r5','r7'])
gen('58',0.053,0.239,
 [('s1',0.08),('s2',2.06),('s3',3.26),('s4',4.38),('s5',6.12),('s6',9.6),('q',11.3)],
 [('r0',0.26),('r1',2.04),('r2',3.94),('r3',5.56),('r4',7.76),('r5',11.26),('r6',13.18),('r7',15.24),('r8',19.98),('r9',24.64),('r10',27.08)],en,['r0','r5'])
