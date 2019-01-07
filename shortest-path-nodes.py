#-*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
===========
Shortest Path between Nodes
===========

Se genera un archivo con una lista de las distancias más cortas entre nodos.

"""
# networkx 2.2
# numpy 1.15.1
# python 3.7.0


import networkx as nx
import numpy as np
import sys

import os

name = sys.argv[1]

cwd = os.getcwd() 

G = nx.read_adjlist(str(cwd) + '/data/' + str(name) + '.txt')

J = open(str(cwd) + '/s-path-nodes.txt', 'w') 

J.write('nodei nodej path-lenght\n')
	
p = nx.shortest_path_length(G)

k = []

for i in p:
	l = list(i[1].items())
	l.sort(key=lambda tup: int(tup[0]))
	k.append([i[0], l])

k.sort(key=lambda tup: int(tup[0]))

for i in k:
	for j in i[1]:
		if int(j[0]) > int(i[0]):
			J.write(str(i[0])+' '+str(j[0])+' '+str(j[1])+'\n')

J.close()
