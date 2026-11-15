import re,sys
src=open('build_e40.py').read()
def gen(n,st,an,chimes):
    s=src.replace('render_e40','render_e%s'%n).replace('ep40/voix/','ep%s/voix/'%n).replace('tmp_e40_','tmp_e%s_'%n).replace('voice_e40','voice_e%s'%n).replace('e40_meta','e%s_meta'%n).replace('video_e40','video_e%s'%n)
    s=re.sub(r"for k,t in \[\('s1'.*?\]: T\[k\]=at\(a,t,L\)",lambda m:"for k,t in %r: T[k]=at(a,t,L)"%st,s,flags=re.S)
    s=re.sub(r"for k,t in \[\('r0'.*?\]: T\[k\]=at\(c_,t,L\)",lambda m:"for k,t in %r: T[k]=at(c_,t,L)"%an,s,flags=re.S)
    order=['cover']+[k for k,_ in st]+['dec','cd']+[k for k,_ in an]+['e0','e1','e2','e3']
    s=re.sub(r"order=\[.*?\]\n",lambda m:"order=%r\n"%order,s,count=1,flags=re.S)
    wh=[k for k,_ in st[1:]]+[k for k,_ in an[1:]]
    s=re.sub(r"for k in \['s2'.*?\]: whoosh",lambda m:"for k in %r: whoosh"%wh,s,flags=re.S)
    s=re.sub(r"chime\(T\['r0'\]\);chime\(T\['r8'\]\)",";".join("chime(T['%s'])"%c for c in chimes),s)
    assert 'e40' not in s,[l for l in s.split('\n') if 'e40' in l]
    open('build_e%s.py'%n,'w').write(s)
exec(open('timings_4142.py').read())
