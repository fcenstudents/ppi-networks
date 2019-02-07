#!/bin/bash
export PYTHONHASHSEED=10

# walk-lenght
X=(50)
# walks
Y=(50)

redes=(1000 1000 1000 1000 1000)


f='deepwalk-embeddings/w3-x50-y50-er-n1000-p02-seed0-'
r='.txt'

for i in {0..4}
do
	d=$f$i$r
	deepwalk --format "adjlist" --input "data/er-n1000-p02.txt" --max-memory-data-size 0 --number-walks 50 --representation-size 2 --walk-length 50 --window-size 3 --seed 0 --workers 4 --output $d
done


