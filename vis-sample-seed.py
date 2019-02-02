import matplotlib.pyplot as plt
import numpy as np
import sys

import os

cwd = os.getcwd() 
#
seeds = [0, 1, 2, 3, 4]

fig, axs = plt.subplots(2, 3, sharex='all', sharey='all', figsize=(8, 5))
		
sm = np.random.randint(low=0, high=1000, size=5, dtype='l')


for j in range(0, 3):
	lst = []
	fname = cwd + '/embeddings-normalized/w3-x50-y50-er-n1000-p02-seed0-' + str(seeds[j]) + '_norm'
	labels, xs, ys = np.loadtxt(fname=fname, comments='#', delimiter=' ', unpack=True)
	for i in range(len(labels)):
		lst.append([labels[i], xs[i], ys[i]])
		lst.sort(key=lambda tup: int(tup[0]))
	for i in sm:
		x = lst[i][1]
		y = lst[i][2]
		labelz = int(lst[i][0])
		axs[0, j].scatter(x, y, marker='o', color='red', s=4, alpha=0.5)
		axs[0, j].text(x, y, labelz, fontsize=5)
		axs[0, j].set_title('# walks 50 seed 0')
	if j == 0:
		axs[0, j].set_ylabel('walk-lenght 50 seed 0')

for j in range(0, 2):
	lst = []
	fname = cwd + '/embeddings-normalized/w3-x50-y50-er-n1000-p02-seed0-' + str(seeds[j+3]) + '_norm'
	labels, xs, ys = np.loadtxt(fname=fname, comments='#', delimiter=' ', unpack=True)
	for i in range(len(labels)):
		lst.append([labels[i], xs[i], ys[i]])
		lst.sort(key=lambda tup: int(tup[0]))
	for i in sm:
		x = lst[i][1]
		y = lst[i][2]
		labelz = int(lst[i][0])
		axs[1, j].scatter(x, y, marker='o', color='red', s=4, alpha=0.5)
		axs[1, j].text(x, y, labelz, fontsize=5)
		axs[1, j].set_title('# walks 50 seed 0')
	if j == 0:
		axs[1, j].set_ylabel('walk-lenght 50 seed 0')

plt.tight_layout()

name = 'visualizations/' + 'seeds-0-sample.png'

plt.savefig(name, format='png')

