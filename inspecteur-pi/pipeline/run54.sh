set -e
N=54
python3 build_e$N.py > build$N.log 2>&1
TOT=$(python3 -c "import json;print(int(json.load(open('e${N}_meta.json'))['total'])+1)")
sed "s/DUR=62/DUR=$TOT/;s/e52/e$N/g" music_e52.py > music_e$N.py && python3 music_e$N.py
bash mux_e$N.sh >> build$N.log 2>&1
echo FINISHED >> build$N.log
