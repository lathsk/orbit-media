import re
src=open('build_e58.py').read()
def gen(n,Lh,Lr,st,an,chimes):
    s=src.replace('e58',f'e{n}').replace('ep58',f'ep{n}')
    s=re.sub(r"L=0\.053; a=add\(load\('01_histoire',L\)",f"L={Lh}; a=add(load('01_histoire',L)",s)
    s=re.sub(r"L=0\.239; c_=add",f"L={Lr}; c_=add",s)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s)
    s=s.replace("chime(T['r0']);chime(T['r5'])",";".join("chime(T['%s'])"%c for c in chimes))
    open(f'build_e{n}.py','w').write(s)
gen('59',0.23,0.31,
 [('s1',0.25),('s2',2.54),('s3',5.34),('q',7.84)],
 [('r0',0.31),('r1',2.30),('r2',8.02),('r3',10.02),('r4',14.72),('r5',18.06),('r6',21.14),('r7',24.26),('r8',26.14),('r9',27.76),('r10',32.04),('r11',36.34)],['r0','r5','r7'])
gen('60',0.25,0.12,
 [('s1',0.27),('s2',3.34),('s3',5.90),('s4',8.00),('s5',10.72),('q',11.94)],
 [('r0',0.14),('r1',2.26),('r2',5.78),('r3',7.56),('r4',9.20),('r5',11.12),('r6',15.46),('r7',19.04),('r8',21.88),('r9',25.66),('r10',28.68)],['r0','r5','r7'])
