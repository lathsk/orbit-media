import re,sys
src=open('build_e38.py').read()
def gen(n,st,an,chimes):
    s=src.replace('render_e38','render_e%s'%n).replace('ep38/voix/','ep%s/voix/'%n).replace('tmp_e38_','tmp_e%s_'%n).replace('voice_e38','voice_e%s'%n).replace('e38_meta','e%s_meta'%n).replace('video_e38','video_e%s'%n)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s,flags=re.S)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1,flags=re.S)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s,flags=re.S)
    s=s.replace("chime(T['r0']);chime(T['r8'])",";".join("chime(T['%s'])"%c for c in chimes))
    assert 'e38' not in s,[l for l in s.split('\n') if 'e38' in l]
    open('build_e%s.py'%n,'w').write(s)
if sys.argv[1]=='39':
    st=[('s1',0.05),('s2',4.90),('s3',8.36),('s4',11.94),('s5',14.28),('s6',16.54),('s7',20.88),('s8',22.60),('s9',26.48),('q',28.54)]
    an=[('r0',0.0),('r1',3.90),('r2',7.48),('r3',10.02),('r4',11.30),('r5',14.54),('r6',19.52),('r7',22.90),('r8',26.22),('r9',28.12)]
    gen('39',st,an,['r0','r9'])
if sys.argv[1]=='40':
    st=[('s1',0.05),('s2',3.42),('s3',6.08),('s4',8.16),('s5',10.94),('s6',12.58),('s7',16.26),('q',18.26)]
    an=[('r0',0.0),('r1',3.46),('r2',5.22),('r3',8.78),('r4',11.80),('r5',14.54),('r6',16.58),('r7',18.46),('r8',21.72)]
    gen('40',st,an,['r0','r8'])
