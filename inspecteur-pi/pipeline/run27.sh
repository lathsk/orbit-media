set -e
python3 build_e27.py > build27.log 2>&1
TOT=$(python3 -c "import json;print(int(json.load(open('e27_meta.json'))['total'])+1)")
sed "s/DUR=65.4/DUR=$TOT/;s/e26/e27/g" music_e26.py > music_e27.py && python3 music_e27.py
sed "s/e26/e27/g" mux_e26.sh > mux_e27.sh && bash mux_e27.sh >> build27.log 2>&1
echo FINISHED >> build27.log
