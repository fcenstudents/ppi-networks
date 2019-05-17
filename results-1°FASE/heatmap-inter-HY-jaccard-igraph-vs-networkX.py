
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

### RED INTER HY
### De 90 clusters obtenidos por community detection (igraph) me quedé con 15 clsuters con más de #20 nodos
### De 85 clusters obtenidos por community detection (NX) me quedé con 15 clsuters con más de #20 nodos

# defino labels de cluster de community detection igraph
cd_labels_i = []
for i in range(1, 16):
	cd_labels_i.append('C'+str(i)+'-i')

cwd = os.getcwd() 

### necesito cargar cada uno de esos 15 clusters en una lista (levanto archivo con los 15 clusters)
lst_cd_i = []

J = open(cwd + "/C-interHY-CDet-igraph-15cl.txt", 'r')   
for line in J:
	lst_cd_i.append(list(map(int, line.split())))
J.close()

### ordeno la lista de forma de tener agrupar los clusters desde los más grandes a los más chicos

lst_cd_i.sort(key=len, reverse=True)



# defino labels de cluster de community detection networkX
cd_labels_nx = []
for i in range(1, 16):
	cd_labels_nx.append('C'+str(i)+'-nx')


### necesito cargar cada uno de esos 15 clusters en una lista (levanto archivo con los 15 clusters)
lst_cd_nx = []

J = open(cwd + "/C-interHY-CDet-networkX-15cl.txt", 'r')   
for line in J:
	lst_cd_nx.append(list(map(int, line.split())))
J.close()

### ordeno la lista de forma de tener agrupar los clusters desde los más grandes a los más chicos

lst_cd_nx.sort(key=len, reverse=True)


### para el jaccard

jacc = np.zeros((len(lst_cd_i), len(lst_cd_nx)))

### figura
fig = plt.figure(figsize=(15,18))

for w in range(len(lst_cd_i)):
	for f in range(len(lst_cd_nx)):
		jacc[w, f] = jaccard_similarity(lst_cd_nx[f], lst_cd_i[w])
	
df = pd.DataFrame(jacc, columns=cd_labels_nx, index=cd_labels_i)
plt.subplot(1,1,1)
sns.heatmap(df, vmin=0, vmax=1, cmap="YlGnBu", annot=True, fmt='.2f')
plt.yticks(rotation=0) 
plt.title("J: CD igraph vs CD networkX - INTER-HY")

fig.tight_layout()
plt.savefig(cwd + '/result-heatmap-interHY-igraph-vs-networkX.png', format='png')
