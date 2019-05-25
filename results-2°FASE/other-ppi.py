# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import networkx as nx
import sys
import os
import matplotlib.pyplot as plt
import random
from igraph import *
import numpy as np


cwd = os.getcwd() 

lst = ["arab", "coli", "drosop", "elegans", "human", "inter_H-Y", "mus_musculus", "rattus-norvegicus", "yeast"]
#lst = ["rattus-norvegicus"]

J = open(str(cwd) + '/info-ppis.txt', 'w') 

for i in lst:
	J.write ('PPI: '+i+'\n')
	G = Graph.Read_Edgelist(str(cwd) + '/data/' + str(i) + '.txt', directed=False)
	G.simplify()
	J.write ('vcount: '+str(G.vcount())+'\n')
	J.write ('ecount: '+str(G.ecount())+'\n')
	J.write ('a-s-path: '+str(G.average_path_length(directed=False, unconn=True))+'\n')
	J.write ('diameter: '+str(G.diameter(directed=False, unconn=True, weights=None))+'\n')
	J.write ('c-clustering: '+str(G.transitivity_undirected(mode="nan"))+'\n')
	sump = 0.0
	p = G.degree()
	for j in p:
		sump += j/len(p)
	J.write ('a-degree: '+str(sump)+'\n')
	J.write ('adhesion: '+str(G.adhesion(source=-1, target=-1, checks=True))+'\n')
	J.write ('cohesion: '+str(G.cohesion(source=-1, target=-1, checks=True, neighbors="error"))+'\n')
	p = G.closeness(vertices=None, mode='ALL', cutoff=None, weights=None, normalized=True)
	sump = 0.0
	for j in p:
		sump += j/len(p)
	J.write ('a-closeness: '+str(sump)+'\n')
	p = G.betweenness(vertices=None, directed=False, cutoff=None, weights=None, nobigint=True)
	sump = 0.0
	for j in p:
		sump += j/len(p)
	J.write ('a-betweenness: '+str(sump*(1/np.max(p)))+'\n')
	J.write ('---------------------------------------'+'\n')
	J.write ('---------------------------------------'+'\n')

	db = G.degree_distribution(bin_width=1)
	l = list(db.bins())
	hy = []
	hx = []
	for j in l:
		if(j[0]>=0):
			hy.append(j[2])
			hx.append(j[0])
	
	maxFreq = max(hy)
	fig = plt.figure(figsize=(6, 6)) #ANCHO/LARGO
	plt.subplot(111)
	plt.scatter(x=np.array(hx), y=np.array(hy)*(1/maxFreq), marker='o', color='red', s=20)
	plt.ylim(-0.05, 1.05)
	plt.xlabel("Degree")
	plt.ylabel("Frequency")
	plt.title('Degree Distribution')
	plt.tight_layout()
	plt.savefig(cwd + '/z-dd-'+i+'.png', format='png')


J.close()

