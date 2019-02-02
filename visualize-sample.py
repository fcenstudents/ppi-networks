# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
===========
Embedding Visualization (SAMPLE)
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
# walks-number
Y = [1, 5, 10, 25, 50, 100]

fig, axs = plt.subplots(len(X), len(Y), sharex='all', sharey='all', figsize=(9, 8))

sm = np.random.randint(low=0, high=100, size=5, dtype='l')

for w in range(0, len(X)):
	for j in range(0, len(Y)):
		lst = []
		fname = cwd + '/embeddings-normalized/' + 'w3-x'+str(Y[j])+'-y'+str(X[w])+'-er-n100-p02_norm'
		labels, xs, ys = np.loadtxt(fname=fname, comments='#', delimiter=' ', unpack=True)
		for i in range(len(labels)):
			lst.append([labels[i], xs[i], ys[i]])
		lst.sort(key=lambda tup: int(tup[0]))
		for i in sm:
			x = lst[i][1]
			y = lst[i][2]
			labelz = int(lst[i][0])
			axs[w, j].scatter(x, y, marker='o', color='red', s=4, alpha=0.5)
			axs[w, j].text(x, y, labelz, fontsize=5)
		if w == 0:
			axs[w, j].set_title('# walks ' + str(Y[j]))
		if j == 0:
			axs[w, j].set_ylabel('walk-lenght ' + str(X[w]))


plt.tight_layout()

name = 'visualizations/' + 'idea-6-er-n100-p02-sample.png'

plt.savefig(name, format='png')
