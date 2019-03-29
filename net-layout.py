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


cwd = os.getcwd() 


lst = ["rattus-norvegicus", "inter_H-Y"]

for i in lst:
	G = nx.read_adjlist(str(cwd) + '/data/' + str(i) + '.txt')
	#pos = nx.shell_layout(G)
	# nx.spring_layout(G), nx.rescale_layout(G), nx.random_layout(G), nx.kamada_kawai_layout(G)
	# nx.circular_layout(G), nx.bipartite_layout(G)
	#pos = nx.spectral_layout(G)
	pos = nx.random_layout(G)
	plt.figure(figsize=(25, 25))
	nx.draw(G, pos=pos, node_size=50, node_color='r', edge_color='r', width=0.40, with_labels=False, alpha=0.5)
	plt.axis('off')
	plt.savefig(str(cwd)+'/draw-'+str(i)+'.png', format="png")

