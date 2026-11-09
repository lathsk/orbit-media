set -e
python3 build_e30.py > build30.log 2>&1
TOT=$(python3 -c "import json;print(int(json.load(open('e30_meta.json'))['total'])+1)")
sed "s/DUR=65.4/DUR=$TOT/;s/e26/e30/g" music_e26.py > music_e30.py && python3 music_e30.py
sed "s/e26/e30/g" mux_e26.sh > mux_e30.sh && bash mux_e30.sh >> build30.log 2>&1
echo FINISHED >> build30.log
