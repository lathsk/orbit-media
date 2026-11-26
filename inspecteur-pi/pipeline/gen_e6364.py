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
gen('63',0.27,0.9,0.30,0.8,3.0,
 [('s1',0.29),('s2',1.98),('s3',4.08),('s4',6.5),('s5',8.16),('s6',10.88),('q',12.36)],
 [('r0',0.30),('r1',2.36),('r2',3.8),('r3',5.4),('r4',9.12),('r5',11.76),('r6',14.68),('r7',17.04),('r8',20.06),('r9',22.12),('r10',25.16)],['r0','r5','r8'])
gen('64',0.31,0.55,0.15,0.8,2.0,
 [('s1',0.33),('s2',4.62),('s3',8.06),('s4',11.74),('q',16.66)],
 [('r0',0.15),('r1',2.84),('r2',5.94),('r3',8.74),('r4',10.74),('r5',15.22),('r6',18.62),('r7',20.72),('r8',22.24)],['r0','r4','r7'])
