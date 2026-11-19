import re,sys
src=open('build_e46.py').read()
def gen(n,st,an,en,chimes):
    s=src.replace('render_e46','render_e%s'%n).replace('ep46/voix/','ep%s/voix/'%n).replace('tmp_e46_','tmp_e%s_'%n).replace('voice_e46','voice_e%s'%n).replace('e46_meta','e%s_meta'%n).replace('video_e46','video_e%s'%n)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('e0'.*?\]: T\[k\]=at\(e,t,L\)",lambda m:"for k,t in %r: T[k]=at(e,t,L)"%en,s,flags=re.S)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1,flags=re.S)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s,flags=re.S)
    s=s.replace("chime(T['r0']);chime(T['r9'])",";".join("chime(T['%s'])"%c for c in chimes))
    s=s.replace("add(load('04_fin',L),0.9)","add(load('04_fin',L),2.0)").replace("add(load('03_reponse',L),0.5)","add(load('03_reponse',L),0.8)").replace("add(load('01_histoire',L),0.35)","add(load('01_histoire',L),0.55)")
    s=s.replace("L=0.0; a=add(load('01_histoire',L)","L=0.25; a=add(load('01_histoire',L)")
    assert 'e46' not in s
    open('build_e%s.py'%n,'w').write(s)
if sys.argv[1]=='49':
    st=[('s1',0.30),('s2',3.32),('s3',9.50),('s4',11.70),('s5',13.72),('q',16.62)]
    an=[('r0',0.0),('r1',3.64),('r2',6.10),('r3',11.48),('r4',15.08),('r5',20.14),('r6',23.46),('r7',27.24),('r8',31.04),('r9',34.70)]
    en=[('e0',0.0),('e1',2.28),('e2',4.92),('e3',5.80)]
    gen('49',st,an,en,['r0','r9'])
if sys.argv[1]=='50':
    st=[('s1',0.30),('s2',2.50),('s3',4.80),('s4',6.32),('s5',8.60),('s6',9.70),('s7',13.02),('q',17.26)]
    an=[('r0',0.0),('r1',2.14),('r2',5.0),('r3',7.0),('r4',11.48),('r5',13.80),('r6',16.84),('r7',19.32),('r8',25.7),('r9',27.85)]
    en=[('e0',0.0),('e1',2.28),('e2',4.60),('e3',5.38)]
    gen('50',st,an,en,['r0','r7'])
