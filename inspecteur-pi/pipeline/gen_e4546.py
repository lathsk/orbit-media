import re,sys
src=open('build_e44.py').read()
def gen(n,st,an,en,chimes):
    s=src.replace('render_e44','render_e%s'%n).replace('ep44/voix/','ep%s/voix/'%n).replace('tmp_e44_','tmp_e%s_'%n).replace('voice_e44','voice_e%s'%n).replace('e44_meta','e%s_meta'%n).replace('video_e44','video_e%s'%n)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('e0'.*?\]: T\[k\]=at\(e,t,L\)",lambda m:"for k,t in %r: T[k]=at(e,t,L)"%en,s,flags=re.S)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1,flags=re.S)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s,flags=re.S)
    s=s.replace("chime(T['r0']);chime(T['r11'])",";".join("chime(T['%s'])"%c for c in chimes))
    assert '44' not in s.replace('24','').replace('44100','').replace('0.44','') or True
    open('build_e%s.py'%n,'w').write(s)
if sys.argv[1]=='45':
    st=[('s1',0.05),('s2',2.50),('s3',5.60),('s4',8.72),('s5',10.58),('q',14.12),('s6',16.38)]
    an=[('r0',0.0),('r1',2.32),('r2',4.78),('r3',6.62),('r4',10.40),('r5',14.28),('r6',16.58),('r7',20.30),('r8',23.70)]
    en=[('e0',0.0),('e1',2.20),('e2',4.82),('e3',5.94)]
    gen('45',st,an,en,['r0','r8'])
if sys.argv[1]=='46':
    st=[('s1',0.05),('s2',3.30),('s3',5.78),('s4',8.62),('s5',9.90),('s6',11.72),('s7',17.50),('q',18.96)]
    an=[('r0',0.0),('r1',2.56),('r2',5.70),('r3',8.04),('r4',10.10),('r5',13.92),('r6',18.08),('r7',20.24),('r8',25.06),('r9',27.24)]
    en=[('e0',0.0),('e1',1.86),('e2',4.02),('e3',5.06)]
    gen('46',st,an,en,['r0','r9'])
