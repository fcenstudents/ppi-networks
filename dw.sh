#!/bin/bash
export PYTHONHASHSEED=10

# walk-lenght
X=(5 10 25 50 100)
# walks
Y=(1 5 10 25 50 100)

redes=(500)

a='data/er-n'
b='-p02.txt'
f='deepwalk-embeddings/w3-x'
g='-y'
h='-er-n'

for i in {0..1}
do
	c=$a${redes[$i]}$b
	for w in {0..4}
	do
		for j in {0..5}
		do
		d=$f${Y[$j]}$g${X[$w]}$h${redes[$i]}$b
		deepwalk --format "adjlist" --input $c --max-memory-data-size 0 --number-walks ${Y[$j]} --representation-size 2 --walk-length ${X[$w]} --window-size 3 --workers 4 --output $d
		done
	done
done


