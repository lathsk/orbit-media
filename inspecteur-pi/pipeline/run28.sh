set -e
python3 build_e28.py > build28.log 2>&1
TOT=$(python3 -c "import json;print(int(json.load(open('e28_meta.json'))['total'])+1)")
sed "s/DUR=65.4/DUR=$TOT/;s/e26/e28/g" music_e26.py > music_e28.py && python3 music_e28.py
sed "s/e26/e28/g" mux_e26.sh > mux_e28.sh && bash mux_e28.sh >> build28.log 2>&1
echo FINISHED >> build28.log
