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

#
seeds = [0, 1, 2, 3, 4]

fig, axs = plt.subplots(2, 3, sharex='all', sharey='all', figsize=(8, 5))
		

for j in range(0, 3):
	fname = cwd + '/embeddings-normalized/w3-x50-y50-er-n1000-p02-seed0-' + str(seeds[j]) + '_norm'
	labels, xs, ys = np.loadtxt(fname=fname, comments='#', delimiter=' ', unpack=True)
	for i, label in enumerate(labels):
		x = xs[i]
		y = ys[i]
		labelz = int(label)
		axs[0, j].scatter(x, y, marker='o', color='red', s=5, alpha=0.5)
		axs[0, j].text(x, y, labelz, fontsize=6)
		axs[0, j].set_title('# walks 50 - seed 0 ' + str(seeds[j]))
	if j == 0:
		axs[0, j].set_ylabel('walk-lenght 50')

for j in range(0, 2):
	fname = cwd + '/embeddings-normalized/w3-x50-y50-er-n1000-p02-seed0-' + str(seeds[j+3]) + '_norm'
	labels, xs, ys = np.loadtxt(fname=fname, comments='#', delimiter=' ', unpack=True)
	for i, label in enumerate(labels):
		x = xs[i]
		y = ys[i]
		labelz = int(label)
		axs[1, j].scatter(x, y, marker='o', color='red', s=5, alpha=0.5)
		axs[1, j].text(x, y, labelz, fontsize=6)
		axs[1, j].set_title('# walks 50 - seed 0 ' + str(seeds[j+3]))
	if j == 0:
		axs[1, j].set_ylabel('walk-lenght 50')

plt.tight_layout()

name = 'visualizations/' + 'seeds-0.png'

plt.savefig(name, format='png')




