import re,sys
src=open('build_e30.py').read()
def gen(n,st,an,chimes):
    s=src.replace('render_e30','render_e%s'%n).replace('ep30/voix/','ep%s/voix/'%n).replace('tmp_e30_','tmp_e%s_'%n).replace('voice_e30','voice_e%s'%n).replace('e30_meta','e%s_meta'%n).replace('video_e30','video_e%s'%n)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s,flags=re.S)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1,flags=re.S)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s,flags=re.S)
    s=s.replace("chime(T['r0']);chime(T['r6'])",";".join("chime(T['%s'])"%c for c in chimes))
    assert "chime(T['%s'])"%chimes[0] in s and 'render_e%s'%n in s and 'e30' not in s
    open('build_e%s.py'%n,'w').write(s)
if sys.argv[1]=='31':
    st=[('s1',0.05),('s2',4.12),('s3',6.94),('s4',9.04),('s5',11.34),('s6',13.0),('s7',15.94),('s8',18.52),('s9',19.88),('s10',21.6),('s11',23.44),('q',25.08)]
    an=[('r0',0.0),('r1',2.22),('r2',5.12),('r3',9.22),('r4',11.08),('r5',12.98),('r6',15.84),('r7',19.3),('r8',20.9),('r9',24.78)]
    gen('31',st,an,['r0','r9'])

if sys.argv[1]=='32':
    st=[('s1',0.05),('s2',4.12),('s3',6.56),('s4',8.06),('s5',9.74),('s6',11.5),('s7',13.42),('s9',17.72),('s10',19.9),('s11',21.94),('q',24.54)]
    an=[('r0',0.0),('r1',2.76),('r2',6.7),('r3',8.3),('r4',9.5),('r5',12.46),('r6',14.0),('r7',15.12),('r8',17.98)]
    gen('32',st,an,['r0','r8'])
