import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

import pandas as pd
import sys
import os
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt

cwd = os.getcwd() 

lst1 = ["rattus-norvegicus", "inter_H-Y"]
lst2 = [2, 10, 20, 50, 80, 100, 128, 300, 500]

for k in lst1:
	for g in lst2:
		#fname = cwd + '/embeddings-normalized/w10-80walks-40l-d' + str(g) + '-' + str(k) + '_norm'
		fname = cwd + '/tsne-2d/tsne-w10-80walks-40l-d'+ str(g) + '-' + str(k)
		data = pd.read_csv(fname, delimiter=' ', header=None)
		df = data.values
		X = df[::, 1:]
		X = StandardScaler().fit_transform(X)
		# Compute DBSCAN
		db = DBSCAN(eps=0.3, min_samples=10).fit(X)
		# db = AgglomerativeClustering(n_clusters=5).fit(X)
		core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
		core_samples_mask[db.core_sample_indices_] = True
		# core_samples_mask[db.n_components_] = True
		labels = db.labels_
		dff = pd.DataFrame(labels)
		result = pd.concat([data[0], dff], axis=1, sort=False)
		result.columns = ['a', 'b']
		j = result.groupby(['b']).groups
		J = open(cwd + '/clustering-deepwalk+tsne/c-dbscan-tsne-w10-80walks-40l-d' + str(g) + '-' + str(k) + '.txt', 'w') 
		for q in list(j.keys()):
			J.write ('C' + str(q)+ '-' +str(len(list(j[q]))))
			for w in j[q]:
				J.write(' ' + str(w))
			J.write('\n')
		J.close()
		# Number of clusters in labels, ignoring noise if present.
		n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		n_noise_ = list(labels).count(-1)
		#print(db.core_sample_indices_)
		#print(np.shape(db.core_sample_indices_))
		print('Estimated number of clusters: %d' % n_clusters_)
		print('Estimated number of noise points: %d' % n_noise_)
		#print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
		#print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
		#print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
		#print("Adjusted Rand Index: %0.3f"
		#      % metrics.adjusted_rand_score(labels_true, labels))
		#print("Adjusted Mutual Information: %0.3f"
		#      % metrics.adjusted_mutual_info_score(labels_true, labels))
		#print("Silhouette Coefficient: %0.3f"
		#      % metrics.silhouette_score(X, labels))

		# #############################################################################
		# Plot result
		# Black removed and is used for noise instead.
		unique_labels = set(labels)
		colors = [plt.cm.Spectral(each)
          	for each in np.linspace(0, 1, len(unique_labels))]
		plt.figure(figsize=(6, 5))
		for u, col in zip(unique_labels, colors):
			if u == -1:
				# Black used for noise.
				col = [0, 0, 0, 1]
			class_member_mask = (labels == u)
			xy = X[class_member_mask & core_samples_mask]
			#plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
			#        markeredgecolor='k', markersize=14)
			plt.scatter(xy[:, 0], xy[:, 1], s=14, c=tuple(col), alpha=0.5)#, edgecolors='k')
			xy = X[class_member_mask & ~core_samples_mask]
			#plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
			#         markeredgecolor=None, markersize=2, alpha=0.5)
			plt.scatter(xy[:, 0], xy[:, 1], s=14, c=tuple(col), alpha=0.5)#, edgecolors='k')
		plt.title('Estimated number of clusters: %d' % n_clusters_)
		plt.savefig(str(cwd) + '/c-dbscan-tsne-w10-80walks-40l-d' + str(g) + '-' + str(k) + '.png', format='png')
