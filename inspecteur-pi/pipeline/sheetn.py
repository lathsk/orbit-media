import sys,importlib
from PIL import Image
n=sys.argv[1]; R=importlib.import_module('render_e'+n)
keys=sys.argv[2].split(','); out=sys.argv[3]; cols=int(sys.argv[4]) if len(sys.argv)>4 else 5
tt=float(sys.argv[5]) if len(sys.argv)>5 else 2.0
ims=[]
for k in keys:
    if k=='cover': im=R.cover(1.0)
    elif k=='dec': im=R.decide(5,1.0)
    elif k=='cd': im=R.decide(3,1.3,ft=0.3)
    elif k[0]=='e': im=R.end(int(k[1]),1.5)
    else:
        f=R.story if k in R.STORY else R.answer
        im=f(k,tt,(0.0,tt+1),{})
    ims.append(im.convert('RGB').resize((324,576)))
rows=(len(ims)+cols-1)//cols
S=Image.new('RGB',(cols*328,rows*580),'black')
for i,im in enumerate(ims): S.paste(im,((i%cols)*328,(i//cols)*580))
S.save(out)
