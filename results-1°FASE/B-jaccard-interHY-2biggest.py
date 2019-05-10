#!/usr/bin/env python
#load file A-interHY-biggest-clusters-xdim.txt
#calculate jaccard index entre biggest clusters de dimensiones consecutivas

import numpy as np
import sys
import os
from matplotlib import pyplot as plt
from math import*
  
def jaccard_similarity(x, y):
	intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
	union_cardinality = len(set.union(*[set(x), set(y)]))
	return intersection_cardinality/float(union_cardinality)
  



cwd = os.getcwd() 

xl = ['2/10', '10/20', '20/50', '50/80', '80/100', '100/128', '128/300', '300/500']
xll = ['2', '10', '20', '50', '80', '100', '128', '300', '500']
lst = []
jaccards = []

J = open(cwd + "/B-inter-[biggest-1]-clusters-xdim_.txt", 'r')
for line in J:
	lst.append(list(map(int, line.split())))
J.close()

i = 0

while i + 1 < len(lst) - 2:
	jaccards.append(jaccard_similarity(lst[i], lst[i+1]))
	i += 1
	
fig = plt.figure(figsize=(6, 12)) #ANCHO/LARGO

plt.subplot(311)
plt.scatter(x=np.array(xl), y=np.array(jaccards), marker='o', color='red', s=100)
for i in range(len(jaccards)):
	plt.annotate(round(jaccards[i], 3), (xl[i], jaccards[i]+0.005))
plt.xlabel("d_{i,max-1}/d_{i+1,max-1}")
plt.ylabel("J_{MAX-1}")
plt.title('J_{MAX-1} entre d_{i,max-1}/d_{i+1,max-1} de INTER_H-Y')


# comparo clusters 2° más grandes tras aplicar community detection directa a la red (mismo algritmo, versión NetworkX vs igraph)
print(jaccard_similarity(lst[9], lst[10]))

# compara los clusters 2° más grandes de cada dimensión con la versión Networkx
jac_nx = []
for j in range(len(lst)-2):
	jac_nx.append(jaccard_similarity(lst[j], lst[9]))

plt.subplot(312)
plt.scatter(x=np.array(xll), y=np.array(jac_nx), marker='o', color='blue', s=100)
for i in range(len(jac_nx)):
	plt.annotate(round(jac_nx[i], 3), (xll[i], jac_nx[i]+0.005))
plt.xlabel("d_{i, max-1}/nx_{max-1}")
plt.ylabel("J_{MAX-1}")
plt.title('J_{MAX-1} entre d_{i, max-1}/nx_{max-1} de INTER_H-Y')


# compara los clusters más grandes de cada dimensión con la versión igraph
jac_i = []
for j in range(len(lst)-2):
	jac_i.append(jaccard_similarity(lst[j], lst[10]))

plt.subplot(313)
plt.scatter(x=np.array(xll), y=np.array(jac_i), marker='o', color='green', s=100)
for i in range(len(jac_i)):
	plt.annotate(round(jac_i[i], 3), (xll[i], jac_i[i]+0.005))
plt.xlabel("d_{i, max-1}/igraph_{max-1}")
plt.ylabel("J_{MAX-1}")
plt.title('J_{MAX-1} entre d_{i, max-1}/igraph_{max-1}" de INTER_H-Y')

plt.tight_layout()
plt.savefig(cwd + '/result-[biggest-1]-interHY.png', format='png')

