import re,sys
src=open('build_e42.py').read()
def gen(n,st,an,chimes):
    s=src.replace('render_e42','render_e%s'%n).replace('ep42/voix/','ep%s/voix/'%n).replace('tmp_e42_','tmp_e%s_'%n).replace('voice_e42','voice_e%s'%n).replace('e42_meta','e%s_meta'%n).replace('video_e42','video_e%s'%n)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s,flags=re.S)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1,flags=re.S)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s,flags=re.S)
    s=s.replace("chime(T['r0']);chime(T['r11'])",";".join("chime(T['%s'])"%c for c in chimes))
    assert 'e42' not in s,[l for l in s.split('\n') if 'e42' in l]
    open('build_e%s.py'%n,'w').write(s)
if sys.argv[1]=='43':
    st=[('s1',0.05),('s2',4.88),('s3',7.96),('s4',11.80),('s5',13.80),('s6',16.08),('s7',18.24),('q',21.32)]
    an=[('r0',0.0),('r1',1.44),('r2',2.82),('r3',4.22),('r4',6.08),('r5',7.58),('r6',9.98),('r7',11.98),('r8',13.42),('r9',15.02),('r10',16.44),('r11',17.56)]
    gen('43',st,an,['r0','r11'])
if sys.argv[1]=='44':
    st=[('s1',0.05),('s2',2.88),('s3',4.78),('s4',7.24),('s5',9.14),('s6',10.90),('s7',11.94),('s8',14.36),('q',16.90)]
    an=[('r0',0.0),('r1',1.2),('r2',4.1),('r3',5.98),('r4',8.14),('r5',9.78),('r6',12.75),('r7',17.26),('r8',19.48),('r9',20.74),('r10',23.68),('r11',26.0)]
    gen('44',st,an,['r0','r11'])
