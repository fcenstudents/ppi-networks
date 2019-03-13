# -*- coding: utf-8 -*-
#!/usr/bin/env python3


import networkx as nx
import sys

import os


cwd = os.getcwd() 

lst1 = ["er-n30-p02", "er-n100-p02", "er-n1000-p02", "sf-n100-m5-p29"]
lst2 = ["arab", "coli", "drosop", "elegans", "human", "inter_H-Y", "mus_musculus", "rattus_norvegicus", "yeast"]

for i in lst2:
	H = nx.read_edgelist(path=cwd+"/data/"+str(i)+".txt", delimiter=" ")
	print(nx.number_of_nodes(H))
	print(nx.number_of_edges(H))
