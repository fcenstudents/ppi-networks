
import sys

import os
import deepwalk


cwd = os.getcwd() 

# walk-lenght
X = [5, 10, 25, 50, 100]
# walks
Y = [1, 5, 10, 25, 50, 100]

redes=[500, 1000]

for i in range(len(redes)):
	fnamei = cwd + '/data/er-n' + str(redes[i]) + '-p02.txt'
	print(fnamei)
	for w in range(0, len(X)):
		for j in range(0, len(Y)):
			fnameo = cwd + '/deepwalk-embeddings/w3-x'+str(Y[j])+'-y'+str(X[w])+'-er-n'+str(redes[i])+'-p02.txt'		
			deepwalk --format adjlist --input fnamei --max-memory-data-size 0 --number-walks Y[j] --representation-size 2 --walk-length X[w] --window-size 3 --workers 4 --output fnameo
			

