#!/bin/bash



f='deepwalk-embeddings/w10-80walks-40l-d128-'
b='.txt'


g='data/'



X=("arab" "coli" "drosop" "elegans" "human" "inter_H-Y" "mus_musculus" "rattus_norvegicus" "yeast")



for w in {0..9}
do
	d=$f${X[$w]}$b
	deepwalk --format "edgelist" --input $g${X[$w]}$b --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --seed 0 --workers 4 --output $d

done






