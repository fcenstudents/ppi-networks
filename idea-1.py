# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
===========
Idea 1
Visualizar mediante scatterplots la media y la desviación estándar en x e y
de los embeddings según el número y longitud de caminos.
===========
"""
# matplotlib 2.2.3
# numpy 1.15.1
# pandas 0.23.4
# python 3.7.0

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

import os


cwd = os.getcwd() 

# walks
x = [1, 5, 10, 25, 50, 100]
# walk-lenght
y = [5, 10, 25, 50, 100]

J = open(str(cwd) + '/idea-1-' + 'er-n30-p02.txt', 'w') 

J.write("x y mean-x mean-y std-x std-y\n")

for i in x:
	for j in y:
		fname = cwd + '/deepwalk-embeddings/' + 'w3-x' + str(i) + '-y' + str(j) + '-er-n30-p02.txt'
		data = pd.read_csv(fname, header=0, delimiter=' ')
		J.write(str(i) + ' ' + str(j) + ' ' + str("{0:.3f}".format(data.mean()[0])) + ' ' + str("{0:.3f}".format(data.mean()[1])) + ' ' + str("{0:.3f}".format(data.std()[0])) + ' ' + str("{0:.3f}".format(data.std()[1])) + '\n')

J.close()


fname= cwd + '/idea-1-er-n30-p02.txt'

X, Y, xm, ym, xs, ys = np.loadtxt(fname=fname, comments='#', delimiter=' ', unpack=True, skiprows=1)

# scatterplot for the mean in x and y 
fig = plt.figure()

for i, k in enumerate(X):
    x = xm[i]
    y = ym[i]
    k = '(' + str(int(X[i])) + ',' + str(int(Y[i])) + ')'
    plt.scatter(x, y, marker='o', color='red')
    plt.text(x, y, k, fontsize=7)
    plt.title('x-y mean según (# walks, walk-lenght)')
    plt.xlabel('mean-x', fontsize=10) 
    plt.ylabel('mean-y', fontsize=10) 

plt.savefig(str(cwd) + '/visualizations/idea-1-mean.pdf', format='pdf')

# scatterplot for the std in x and y 

fig = plt.figure()

for i, k in enumerate(X):
    x = xs[i]
    y = ys[i]
    k = '(' + str(int(X[i])) + ',' + str(int(Y[i])) + ')'
    plt.scatter(x, y, marker='o', color='red')
    plt.text(x, y, k, fontsize=7)
    plt.title('x-y std según (# walks, walk-lenght)')
    plt.xlabel('std-x', fontsize=10) 
    plt.ylabel('std-y', fontsize=10) 

plt.savefig(str(cwd) + '/visualizations/idea-1-std.pdf', format='pdf')


# scatterplot for the mean/std in x and y 

fig = plt.figure()

for i, k in enumerate(X):
    x = float(xm[i])/float(xs[i])
    y = float(ym[i])/float(ym[i])
    k = '(' + str(int(X[i])) + ',' + str(int(Y[i])) + ')'
    plt.scatter(x, y, marker='o', color='blue')
    plt.text(x, y, k, fontsize=7)
    plt.title('x-y mean/std según (# walks, walk-lenght)')
    plt.xlabel('mean/std-x', fontsize=10) 
    plt.ylabel('mean/std-y', fontsize=10) 

plt.savefig(str(cwd) + '/visualizations/idea-1-mean-std.pdf', format='pdf')

