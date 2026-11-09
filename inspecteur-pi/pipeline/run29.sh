set -e
python3 build_e29.py > build29.log 2>&1
TOT=$(python3 -c "import json;print(int(json.load(open('e29_meta.json'))['total'])+1)")
sed "s/DUR=65.4/DUR=$TOT/;s/e26/e29/g" music_e26.py > music_e29.py && python3 music_e29.py
sed "s/e26/e29/g" mux_e26.sh > mux_e29.sh && bash mux_e29.sh >> build29.log 2>&1
echo FINISHED >> build29.log
