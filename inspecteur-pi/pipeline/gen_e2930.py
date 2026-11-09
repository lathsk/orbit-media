import re,sys
src=open('build_e28.py').read()
def gen(n,st,an,chimes,nxt=None):
    s=src.replace('render_e28','render_e%s'%n).replace('ep28/voix/','ep%s/voix/'%n).replace('tmp_e28_','tmp_e%s_'%n).replace('voice_e28','voice_e%s'%n).replace('e28_meta','e%s_meta'%n).replace('video_e28','video_e%s'%n)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s,flags=re.S)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1,flags=re.S)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s,flags=re.S)
    s=s.replace("chime(T['r0']);chime(T['r6'])",";".join("chime(T['%s'])"%c for c in chimes))
    assert "chime(T['%s'])"%chimes[0] in s and 'render_e%s'%n in s
    open('build_e%s.py'%n,'w').write(s)
if sys.argv[1]=='29':
    st=[('s1',0.05),('s2',2.64),('s3',5.76),('s4',7.55),('s5',9.25),('s6',10.98),('s7',14.05),('s8',16.05),('s9',18.25),('q',19.55)]
    an=[('r0',0.0),('r1',2.2),('r2',5.88),('r3',11.8),('r4',14.18),('r5',16.7),('r6',20.0),('r7',22.16),('r8',25.22)]
    gen('29',st,an,['r0','r7'])

if sys.argv[1]=='30':
    st=[('s1',0.05),('s2',3.5),('s3',5.9),('s4',7.5),('s5',9.05),('s6',10.65),('s7',12.45),('q',15.1)]
    an=[('r0',0.0),('r1',3.7),('r2',6.12),('r3',12.28),('r4',13.94),('r5',17.7),('r6',19.85)]
    gen('30',st,an,['r0','r6'])
