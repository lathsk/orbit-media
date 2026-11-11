set -e
for N in 33 34; do
python3 build_e$N.py > build$N.log 2>&1
TOT=$(python3 -c "import json;print(int(json.load(open('e${N}_meta.json'))['total'])+1)")
sed "s/DUR=63/DUR=$TOT/;s/e32/e$N/g" music_e32.py > music_e$N.py && python3 music_e$N.py
sed "s/e32/e$N/g" mux_e32.sh > mux_e$N.sh && bash mux_e$N.sh >> build$N.log 2>&1
echo FINISHED >> build$N.log
done
