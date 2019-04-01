import pandas as pd
import sys
import os
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt

cwd = os.getcwd() 

lst1 = ["rattus-norvegicus", "inter_H-Y"]
lst2 = [2, 10, 20, 50, 80, 100, 128, 300, 500]

for k in lst1:
	for g in lst2:
		fname = cwd + '/embeddings-normalized/w10-80walks-40l-d' + str(g) + '-' + str(k) + '_norm'
		data = pd.read_csv(fname, delimiter=' ', header=None)
		df = data.as_matrix()
		X = df[::,1:]
		tsne = TSNE(n_components=2, random_state=0)
		X_2d = tsne.fit_transform(X)
		XD = pd.DataFrame(X_2d)
		result = pd.concat([data[0], XD], axis=1, sort=False)
		np.savetxt(cwd + '/tsne-2d/tsne-w10-80walks-40l-d' + str(g) + '-' + str(k) , result.values, fmt='%f')
		plt.figure(figsize=(6, 5))
		for i in range(len(X_2d)):
			plt.scatter(X_2d[i, 0], X_2d[i, 1], s=2, c='red', alpha=0.5)
		plt.title("d" + str(g))
		plt.savefig(str(cwd) + '/tsne-' + str(k) + '-d' + str(g) + '.png', format='png')
