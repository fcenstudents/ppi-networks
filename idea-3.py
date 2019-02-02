# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
===========
Idea 3
===========

Se genera un archivo pdf con una figura que contiene heatmap
de correlaciones entre distancias euclideanas y shortest path

"""
# matplotlib 2.2.3
# numpy 1.15.1
# seaborn 0.9.0
# python 3.7.0


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys

import os

cwd = os.getcwd() 

# file with shortest path between nodes
fname1 = cwd + '/s-path-nodes-er-n100-p02.txt'

# walks
x = [1, 5, 10, 25, 50, 100]
# walk-lenght
y = [5, 10, 25, 50, 100]

ni0, nj0, d0 = np.loadtxt(fname=fname1, comments='#', delimiter=' ', unpack=True, skiprows=1)

data1 = np.ndarray(shape=(len(y), len(x)), dtype=float, order='C')

for q in range(len(x)):
	for r in range(len(y)):
		fname2 = cwd + '/distances-embeddings/dist-w3-x' + str(x[q]) + '-y' + str(y[r]) + 'er-n100-p02.txt'
		ni, nj, d = np.loadtxt(fname=fname2, comments='#', delimiter=' ', unpack=True, skiprows=1)
		data1[r, q] = float(np.corrcoef(d0, d)[0, 1])

# generamos un heatmap de las correlaciones entre las distancias para la idea 3
fig = plt.figure() 

ax = sns.heatmap(data1, vmin=-1.0, vmax=1.0, xticklabels=x, yticklabels=y, annot=True, cmap=sns.color_palette("RdBu_r", 21))
plt.title('correlation shortest-path vs euclidean distance')
plt.xlabel('# walks')
plt.ylabel('walk-lenght')
name = cwd + '/visualizations/idea-3-er-n100-p02_prueba.pdf'

figure = ax.get_figure()   
 
figure.savefig(name)


