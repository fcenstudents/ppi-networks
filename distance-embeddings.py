# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
===========
Euclidean Distance between Nodes
===========

Se genera un archivo con una lista de las distancias euclideanas entre nodos
en los embeddings.

"""
# networkx 2.2
# numpy 1.15.1
# pandas 0.23.4
# python 3.7.0


import networkx as nx
import numpy as np
import pandas as pd
import sys

import os


# walks
x = [1, 5, 10, 25, 50, 100]
# walk-lenght
y = [5, 10, 25, 50, 100]

cwd = os.getcwd() 

for q in range(len(x)):
	for r in range(len(y)):
		name= cwd + '/embeddings-normalized/' + 'w3-x' + str(x[q]) + '-y' + str(y[r]) + '-er-n30-p02_norm'
		label, X, Y = np.loadtxt(fname=name, comments='#', delimiter=' ', unpack=True, skiprows=0)
		J = open(str(cwd) + '/distances-embeddings/dist-' + 'w3-x' + str(x[q]) + '-y' + str(y[r]) + '.txt', 'w') 
		J.write('nodei nodej distance\n')
		lst = []
		for h in range(len(X)):
			lst.append([label[h], [X[h], Y[h]]])
		lst.sort(key=lambda tup: int(tup[0]))
		for i in lst:
			xo1 = i[1][0]
			xo2 = i[1][1]
			for j in lst:
				if int(j[0]) > int(i[0]):
					x1 = j[1][0]
					x2 = j[1][1]
					d = np.sqrt((xo1 - x1)**2 + (xo2 - x2)**2)
					J.write(str(int(i[0])) + ' ' + str(int(j[0])) + ' ' + str('{0:.3f}'.format(d)) + '\n')
		J.close()




