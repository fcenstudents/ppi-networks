
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

cwd = os.getcwd() 


### ahora implemento un loop sobre los archivos que contienen los clusters por dimensiones de DW+tSNE+DBSCAN

dim = [2, 10, 20, 50, 80, 100, 128, 300, 500]


fig = plt.figure(figsize=(15,18))

for j in range(len(dim)-1):
	fnamei = cwd + "/clustering-deepwalk+tsne/c-dbscan-tsne-w10-80walks-40l-d" + str(dim[j]) + "-rattus-norvegicus_.txt"
	fnameii = cwd + "/clustering-deepwalk+tsne/c-dbscan-tsne-w10-80walks-40l-d" + str(dim[j+1]) + "-rattus-norvegicus_.txt"
	lsti = []
	lstii = []
	J = open(fnamei, 'r')   
	for line in J:
		lsti.append(list(map(int, line.split())))
	J.close()
	lsti.sort(key=len, reverse=True)
	J = open(fnameii, 'r')   
	for line in J:
		lstii.append(list(map(int, line.split())))
	J.close()
	lstii.sort(key=len, reverse=True)
	labelsi = []
	labelsii = []
	for t in range(1, len(lsti)+1):
		labelsi.append('c'+str(t)+'-d'+str(dim[j])+'-#'+str(len(lsti[t-1])))
	for s in range(1, len(lstii)+1):
		labelsii.append('c'+str(s)+'-d'+str(dim[j+1])+'-#'+str(len(lstii[s-1])))
	jacc = np.zeros((len(lsti), len(lstii)))
	intersection = np.zeros((len(lsti), len(lstii)))
	for w in range(len(lsti)):
		for f in range(len(lstii)):
			jacc[w, f] = jaccard_similarity(lstii[f], lsti[w])
			intersection[w, f]= len(set.intersection(*[set(lstii[f]), set(lsti[w])]))
	
	df = pd.DataFrame(jacc, columns=labelsii, index=labelsi)
	dff = pd.DataFrame(intersection, columns=labelsii, index=labelsi)
	plt.subplot(2,4,j+1)
	akws = {"ha": 'left',"va": 'bottom', "color":'r'}
	ax = sns.heatmap(dff, annot=True, alpha=0.0, annot_kws=akws, cbar=False, fmt='.0f')
	for t in ax.texts:
		trans = t.get_transform()
		offs = matplotlib.transforms.ScaledTranslation(-0.48, 0.48, matplotlib.transforms.IdentityTransform())
		t.set_transform( offs + trans )
	sns.heatmap(df, vmin=0, vmax=1, cmap="YlGnBu", annot=True, fmt='.2f')
	plt.yticks(rotation=0) 
	plt.xticks(rotation=90) 
	plt.title("J: DIM "+str(dim[j])+' vs. '+str(dim[j+1])+" - RATTUS")

fig.tight_layout()
plt.savefig(cwd + '/result-heatmap-rattus-DW+tSNE+DBScan_.png', format='png')
