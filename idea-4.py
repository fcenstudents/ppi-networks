# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
===========
Idea 4. SEEDS
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

# seeds
seeds = [0, 3, 10, 25, 106, 500]

fig, axs = plt.subplots(2, 3, sharex='all', sharey='all', figsize=(8, 5))
		

for j in range(0, 3):
	fname = cwd + '/embeddings-normalized/w3-x5-y10-seed' + str(seeds[j]) + '-er-n30-p02_norm'
	labels, xs, ys = np.loadtxt(fname=fname, comments='#', delimiter=' ', unpack=True)
	for i, label in enumerate(labels):
		x = xs[i]
		y = ys[i]
		labelz = int(label)
		axs[0, j].scatter(x, y, marker='o', color='red', s=5, alpha=0.5)
		axs[0, j].text(x, y, labelz, fontsize=6)
		axs[0, j].set_title('# walks 5 - seed ' + str(seeds[j]))
	if j == 0:
		axs[0, j].set_ylabel('walk-lenght 10')

for j in range(0, 3):
	fname = cwd + '/embeddings-normalized/w3-x5-y10-seed' + str(seeds[j+3]) + '-er-n30-p02_norm'
	labels, xs, ys = np.loadtxt(fname=fname, comments='#', delimiter=' ', unpack=True)
	for i, label in enumerate(labels):
		x = xs[i]
		y = ys[i]
		labelz = int(label)
		axs[1, j].scatter(x, y, marker='o', color='red', s=5, alpha=0.5)
		axs[1, j].text(x, y, labelz, fontsize=6)
		axs[1, j].set_title('# walks 5 - seed ' + str(seeds[j+3]))
	if j == 0:
		axs[1, j].set_ylabel('walk-lenght 10')

plt.tight_layout()

name = 'visualizations/' + 'idea-4-seeds.pdf'

plt.savefig(name, format='pdf')




