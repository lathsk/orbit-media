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
    assert 'e46' not in s
    open('build_e%s.py'%n,'w').write(s)
if sys.argv[1]=='47':
    st=[('s1',0.05),('s2',2.34),('s3',5.22),('s4',6.72),('s5',8.14),('s6',10.0),('s7',11.76),('s8',13.86),('q',17.84)]
    an=[('r0',0.0),('r1',2.92),('r2',5.06),('r3',7.92),('r4',9.64),('r5',11.98),('r6',13.96),('r7',15.76),('r8',18.48)]
    en=[('e0',0.0),('e1',2.28),('e2',4.92),('e3',5.80)]
    gen('47',st,an,en,['r0','r8'])
if sys.argv[1]=='48':
    st=[('s1',0.05),('s2',3.26),('s3',5.10),('s4',6.74),('s5',10.6),('s6',13.14),('s7',16.46),('q',18.76)]
    an=[('r0',0.0),('r1',2.62),('r2',5.4),('r3',6.9),('r4',8.74),('r5',10.24),('r6',11.86),('r7',14.86),('r8',16.92),('r9',20.04)]
    en=[('e0',0.0),('e1',2.28),('e2',4.60),('e3',5.38)]
    gen('48',st,an,en,['r0','r9'])
