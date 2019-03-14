

import pandas as pd
import sys
import os
import numpy as np

cwd = os.getcwd() 

# Red rattus norvegicus como ejemplo
fname = cwd + '/embeddings-normalized/w10-80walks-40l-d128-rattus_norvegicus_norm'
data = pd.read_csv(fname, delimiter=' ', header=None)

df = data.as_matrix()
X = df[::,1:]

from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, random_state=0)

X_2d = tsne.fit_transform(X)

from matplotlib import pyplot as plt
plt.figure(figsize=(6, 5))
for i in range(len(X_2d)):
	plt.scatter(X_2d[i, 0], X_2d[i, 1], s=2, c='red', alpha=0.5)

plt.savefig(str(cwd)+'/tsne-rattus-d128.pdf', format='pdf')


