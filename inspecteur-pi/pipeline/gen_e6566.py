import re
src=open('build_e62.py').read().replace('ep62','epXX').replace('e62','eXX')
def gen(n,Lh,gh,Lr,gr,gfin,st,an,chimes):
    s=src.replace('epXX',f'ep{n}').replace('eXX',f'e{n}')
    s=re.sub(r"L=[\d.]+; a=add\(load\('01_histoire',L\),[\d.]+\)",f"L={Lh}; a=add(load('01_histoire',L),{gh})",s)
    s=re.sub(r"L=[\d.]+; c_=add\(load\('03_reponse',L\),[\d.]+\)",f"L={Lr}; c_=add(load('03_reponse',L),{gr})",s)
    s=re.sub(r"L=0\.0; e=add\(load\('04_fin',L\),[\d.]+\)",f"L=0.0; e=add(load('04_fin',L),{gfin})",s)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s)
    s=s.replace("chime(T['r0']);chime(T['r2']);chime(T['r7'])",";".join("chime(T['%s'])"%c for c in chimes))
    assert s.count("T[k]=at(")>=3
    open(f'build_e{n}.py','w').write(s)
gen('65',0.27,0.55,0.25,0.8,2.0,
 [('s1',0.29),('s2',3.32),('s3',5.32),('s4',6.62),('q',11.52)],
 [('r0',0.27),('r1',4.88),('r2',7.70),('r3',10.50),('r4',14.98),('r5',18.74),('r6',22.40),('r7',27.62)],['r0','r5','r7'])
gen('66',0.24,0.55,0.14,1.0,3.2,
 [('s1',0.26),('s2',2.26),('s3',4.30),('s4',7.48),('s5',9.06),('q',11.38)],
 [('r0',0.16),('r1',2.20),('r2',5.86),('r3',8.04),('r4',10.70),('r5',13.70),('r6',16.24),('r7',18.06),('r8',21.94),('r9',24.08)],['r0','r6','r9'])
