# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
===========
Idea 2
===========

Se genera un archivo pdf con una figura que contiene scatterplots de
shortest path y distancias euclineanas entre nodos según las
distintas combinaciones de parámetros.

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
fname1 = cwd + '/s-path-nodes.txt'

# walks
x = [1, 5, 10, 25, 50, 100]
# walk-lenght
y = [5, 10, 25, 50, 100]

fig, axs = plt.subplots(len(y), len(x), sharex='all', sharey='all', figsize=(9, 8))

ni0, nj0, d0 = np.loadtxt(fname=fname1, comments='#', delimiter=' ', unpack=True, skiprows=1)


data = np.ndarray(shape=(len(y), len(x)), dtype=float, order='F')

for q in range(len(x)):
	for r in range(len(y)):
		fname2 = cwd + '/distances-embeddings/dist-w3-x' + str(x[q]) + '-y' + str(y[r]) + '.txt'
		ni, nj, d = np.loadtxt(fname=fname2, comments='#', delimiter=' ', unpack=True, skiprows=1)
		for i, dist in enumerate(d):
			label = '(' + str(ni[i]) + ',' + str(nj[i]) + ')'
			diste = float(dist)
			distsp = float(d0[i])
			axs[r, q].scatter(diste, distsp, marker='o', color='red', s=4, alpha=0.3)
			#axs[q, r].text(diste, distsp, label, fontsize=5)
			if r == 0:
				axs[r, q].set_title('# walks ' + str(x[q]) + '\neuclidean-dist')
			if q == 0:
				axs[r, q].set_ylabel('walk-lenght ' + str(y[r]) + '\nshortest-path')
		f = float(np.corrcoef(d0, d)[0, 1])
		data[r, q] = f

plt.tight_layout()

name = cwd + '/visualizations/idea-2.png'

plt.savefig(name, format='png')

# generamos un heatmap de las correlaciones entre las distancias para la idea 3
fig = plt.figure() 

ax = sns.heatmap(data, vmin=-1.0, vmax=1.0, xticklabels=x, yticklabels=y, annot=True, cmap=sns.color_palette("RdBu_r", 21))
plt.title('correlation shortest-path vs euclidean distance')
plt.xlabel('# walks')
plt.ylabel('walk-lenght')
name = cwd + '/visualizations/idea-3.png'

figure = ax.get_figure()   
 
figure.savefig(name)
