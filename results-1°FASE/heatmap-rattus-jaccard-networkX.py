
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
from math import*
import seaborn as sns
import pandas as pd

  
def jaccard_similarity(x, y):
	intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
	union_cardinality = len(set.union(*[set(x), set(y)]))
	return intersection_cardinality/float(union_cardinality)

### RED RATTUS
### De 155 clusters obtenidos por community detection (networkX) me quedé con 15 clsuters con más de #20 nodos

# defino labels de cluster de community detection networkX
cd_labels = []


cwd = os.getcwd() 

### necesito cargar cada uno de esos 15 clusters en una lista (levanto archivo con los 15 clusters)
lst_cd_i = []

J = open(cwd + "/C-rattus-CDet-networkX-18cl.txt", 'r')   
for line in J:
	lst_cd_i.append(list(map(int, line.split())))
J.close()

### ordeno la lista de forma de tener agrupar los clusters desde los más grandes a los más chicos

lst_cd_i.sort(key=len, reverse=True)

for i in range(1, 19):
	cd_labels.append('C'+str(i)+'-#'+str(len(lst_cd_i[i-1])))

### ahora implemento un loop sobre los archivos que contienen los clusters por dimensiones de DW+tSNE+DBSCAN

dim = [2, 10, 20, 50, 80, 100, 128, 300, 500]


fig = plt.figure(figsize=(15,18))

for j in range(len(dim)):
	fname = cwd + "/clustering-deepwalk+tsne/c-dbscan-tsne-w10-80walks-40l-d" + str(dim[j]) + "-rattus-norvegicus_.txt"
	lst = []
	J = open(fname, 'r')   
	for line in J:
		lst.append(list(map(int, line.split())))
	J.close()
	lst.sort(key=len, reverse=True)
	labels_d = []
	for t in range(1, len(lst)+1):
		labels_d.append('c'+str(t)+'-#'+str(len(lst[t-1])))
	jacc = np.zeros((len(lst_cd_i), len(lst)))
	intersection = np.zeros((len(lst_cd_i), len(lst)))
	for w in range(len(lst_cd_i)):
		for f in range(len(lst)):
			jacc[w, f] = jaccard_similarity(lst[f], lst_cd_i[w])
			intersection[w, f]= len(set.intersection(*[set(lst[f]), set(lst_cd_i[w])]))
	
	df = pd.DataFrame(jacc, columns=labels_d, index=cd_labels)
	dff = pd.DataFrame(intersection, columns=labels_d, index=cd_labels)
	plt.subplot(3,3,j+1)
	akws = {"ha": 'left',"va": 'bottom', "color":'r'}
	ax = sns.heatmap(dff, annot=True, alpha=0.0, annot_kws=akws, cbar=False, fmt='.0f')
	for t in ax.texts:
		trans = t.get_transform()
		offs = matplotlib.transforms.ScaledTranslation(-0.48, 0.48, matplotlib.transforms.IdentityTransform())
		t.set_transform( offs + trans )
	sns.heatmap(df, vmin=0, vmax=1, cmap="YlGnBu", annot=True, fmt='.2f')
	plt.yticks(rotation=0)
	plt.xticks(rotation=90)
	plt.title("J: CD networkX y DW+tSNE+DBSCAN (DIM "+str(dim[j])+") - RATTUS")

fig.tight_layout()
plt.savefig(cwd + '/result-heatmap-rattus-networkX_.png', format='png')
