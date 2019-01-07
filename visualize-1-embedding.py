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


name_arg = sys.argv[1]

cwd = os.getcwd() 

fname = cwd + '/embeddings-normalized/' + name_arg

labels, xs, ys = np.loadtxt(fname=fname, comments='#', delimiter=' ', unpack=True)

fig = plt.figure()

for i, label in enumerate(labels):
    x = xs[i]
    y = ys[i]
    labelz = int(label)
    plt.scatter(x, y, marker='x', color='red')
    plt.text(x, y, labelz, fontsize=9)

name = 'visualizations/' + name_arg + '.pdf'

plt.savefig(name, format='pdf')



