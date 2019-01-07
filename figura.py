# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
===========
Embedding Visualization
===========
"""
# matplotlib 2.2.3
# numpy 1.15.1
# python 3.7.0

import matplotlib.pyplot as plt
import numpy as np
import sys

import os

cwd = os.getcwd() 

# walk-lenght
X = [5, 10, 25, 50, 100]
# walks
Y = [1, 5, 10, 25, 50, 100]

fig, axs = plt.subplots(len(X), len(Y), sharex='all', sharey='all', figsize=(9, 8))

for w in range(0, len(X)):
	for j in range(0, len(Y)):
		fname = cwd + '/embeddings-normalized/' + 'w3-x' + str(Y[j]) + '-y' + str(X[w]) + '-er-n30-p02_norm'
		labels, xs, ys = np.loadtxt(fname=fname, comments='#', delimiter=' ', unpack=True)
		for i, label in enumerate(labels):
		    	x = xs[i]
    			y = ys[i]
    			labelz = int(label)
    			axs[w, j].scatter(x, y, marker='o', color='red', s=4)
    			axs[w, j].text(x, y, labelz, fontsize=5)
		if w == 0:
			axs[w, j].set_title('# walks ' + str(Y[j]))
		if j == 0:
			axs[w, j].set_ylabel('walk-lenght ' + str(X[w]))


plt.tight_layout()

name = 'visualizations/' + 'fig-embeddings.pdf'

plt.savefig(name, format='pdf')
