# -*- coding: utf-8 -*-
#!/usr/bin/env python3


# matplotlib 2.2.3
# networkx 2.2
# python 3.7.0

import sys

import os
import networkx as nx
import matplotlib.pyplot as plt
import random
import matplotlib.cm as cm
from igraph import *
import numpy as np

from networkx.algorithms import community

# igraph ofrece muchos algoritmos de clustering mientras que Networkx solo tres o cuatro.
# tienen en común alrededor de tres, entre ellos fastgready y optimal modularity.

cwd = os.getcwd() 


lst = ["inter_H-Y", "rattus-norvegicus"]


for i in lst:
	G = Graph.Read_Edgelist(str(cwd) + '/data/' + str(i) + '.txt', directed=False)
	#print(G.ecount())
	# If there are multiple edges or loops, it simplifies the graph
	G.simplify()
	#print(G.ecount())
	"""
	C = G.community_multilevel()
	p = C.membership
	print(len(p))
	J = open(cwd+'/com-multilevel-inter_H-Y.txt', 'w') 
	J.write ('#communities= '+str(len(p))+'\n')
	for i in range(len(p)):
		J.write ('C'+str(i+1)+' '+str(p[i])+'\n')
	J.close()
	"""
	####################################################
	### PUEDE SER
	C = G.community_fastgreedy() # VertexDendrogram, 1052 elements, 991 merges
	p = C.as_clustering() # #Cuts dendrogram at the given level (optimal) and returns a VertexClustering object.
	#print(p.sizes())
	#print(len(p))
	J = open(cwd+'/network-communities/com-fastgreedy-'+str(i)+'_I.txt', 'w') 
	J.write ('# '+str(len(p))+' communities; '+str(G.vcount())+' elements \n')
	for q in range(len(p)):
		J.write ('C'+str(q+1)+'-'+str(len(p[q])))
		for w in p[q]:
			J.write(' '+str(w))
		J.write('\n')
	J.close()
	"""
	for i in range(len(p)):
		J.write ('C'+str(i+1)+' '+str(p[i])+'\n')
	J.close()
	"""
	####################################################
	"""
	C = G.community_edge_betweenness(directed=False)
	p = C.as_clustering() #Cuts dendrogram at the given level (optimal) and returns a VertexClustering object.
	print(len(p))
	J = open(cwd+'/network-communities/com-edge_betweenness-inter_H-Y.txt', 'w') 
	J.write ('#communities= '+str(len(p))+'\n')
	for i in range(len(p)):
		J.write ('C'+str(i+1)+' '+str(p[i])+'\n')
	J.close()
	"""
	####################################################
	"""
	# Mucho tiempo de cómputo...
	C = G.community_optimal_modularity()
	p = C.membership
	print(len(p))
	J = open(cwd+'/network-communities/com-optimal_modularity-inter_H-Y.txt', 'w') 
	J.write ('#communities= '+str(len(p))+'\n')
	for i in range(G.vcount()):
		J.write (str(i+1)+' '+str(p[i])+'\n')
	J.close()
	"""
	####################################################
	""" (PUEDE SER)
	C = G.community_walktrap()
	p = C.as_clustering()
	print(len(p))
	J = open(cwd+'/network-communities/com-walktrap-inter_H-Y.txt', 'w') 
	J.write ('#communities= '+str(len(p))+'\n')
	for i in range(len(p)):
		J.write ('C'+str(i+1)+' '+str(p[i])+'\n')
	J.close()
	"""
	####################################################
	"""
	### no trabaja con nodos aislados
	C = G.community_spinglass(spins=300)   
	p = C.membership
	print(len(p))
	J = open(cwd+'/network-communities/com-spinglass-inter_H-Y.txt', 'w') 
	J.write ('#communities= '+str(len(p))+'\n')
	for i in range(G.vcount()):
		J.write (str(i+1)+' '+str(p[i])+'\n')
	J.close()
	"""
	####################################################
	"""
	C = G.community_infomap()
	p = C.membership
	print(len(p))
	J = open(cwd+'/network-communities/com-infomap-inter_H-Y.txt', 'w') 
	J.write ('#communities= '+str(len(p))+'\n')
	for i in range(G.vcount()):
		J.write (str(i+1)+' '+str(p[i])+'\n')
	J.close()
	"""
	####################################################
	"""
	C = G.community_label_propagation()
	p = C.membership
	print(len(p))
	J = open(cwd+'/network-communities/com-label_propagation-inter_H-Y.txt', 'w') 
	J.write ('#communities= '+str(len(p))+'\n')
	for i in range(G.vcount()):
		J.write (str(i+1)+' '+str(p[i])+'\n')
	J.close()
	"""
	####################################################
	"""
	C = G.community_leading_eigenvector()
	p = C.membership
	print(len(p))
	J = open(cwd+'/network-communities/com-leading_eigenvector-inter_H-Y.txt', 'w') 
	J.write ('#communities= '+str(len(p))+'\n')
	for i in range(G.vcount()):
		J.write (str(i+1)+' '+str(p[i])+'\n')
	J.close()
	"""
	####################################################
	####################################################
	####################################################
	
	G = nx.read_adjlist(str(cwd) + '/data/' + str(i) + '.txt')
	#print(G.number_of_edges())
	#m = community.girvan_newman(G) #991
	m = community.greedy_modularity_communities(G)
	c = list(m)
	print(len(c))
	for u in c:
		print(len(u))
	J = open(cwd+'/network-communities/com-fastgreedy-'+str(i)+'_NX.txt', 'w') 
	J.write ('# '+str(len(c))+' communities; '+str(G.number_of_nodes())+' elements \n')
	for q in range(len(c)):
		J.write ('C'+str(q+1)+'-'+str(len(c[q])))
		for w in c[q]:
			J.write(' '+str(w))
		J.write('\n')
	J.close()

	####################################################
	####################################################
	####################################################

	#pos = nx.shell_layout(G)
	# nx.spring_layout(G), nx.rescale_layout(G), nx.random_layout(G), nx.kamada_kawai_layout(G)
	# nx.circular_layout(G), nx.bipartite_layout(G), nx.spectral_layout(G)

	pos = nx.random_layout(G)
	plt.figure(figsize=(25, 25))
	nx.draw(G, pos=pos, edge_color='k', width=0.40, with_labels=False, alpha=0.5)
	plt.axis('off')
	colors = cm.rainbow(np.linspace(0, 1, len(c)))
	#For each community list, draw the nodes, giving it a specific color.
	z = zip(c, colors)
	if (i == 'inter_H-Y'):
		for y, c in z:
			if len(list(y)) > 20:
				#print(list(y))
				#print('\n')
				nx.draw_networkx_nodes(G, pos=pos, nodelist=list(y), node_color='r', alpha=0.5, node_size=100)
			if len(list(y)) <= 20:
				nx.draw_networkx_nodes(G, pos=pos, nodelist=list(y), node_color='b', alpha=0.5, node_size=100)
		plt.savefig(str(cwd)+'/draw-com-nx-'+str(i)+'.png', format="png")
	if (i == 'rattus-norvegicus'):
		for y, c in z:
			if len(list(y)) > 60:
				#print(list(y))
				#print('\n')
				nx.draw_networkx_nodes(G, pos=pos, nodelist=list(y), node_color='r', alpha=0.5, node_size=100)
			if len(list(y)) <= 60:
				nx.draw_networkx_nodes(G, pos=pos, nodelist=list(y), node_color='b', alpha=0.5, node_size=100)
		plt.savefig(str(cwd)+'/draw-com-nx-'+str(i)+'.png', format="png")

