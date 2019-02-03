# -*- coding: utf-8 -*-
"""
SCALE-FREE NETWORKS

"""
# python 3.7.0

import sys
import os
from igraph import *

cwd = os.getcwd() 

# Creates a graph object
G = Graph()
G = G.Barabasi(n=100, m=5, outpref=False, directed=False, power=2.9, zero_appeal=1, implementation='psumtree', start_from=None)
# Gets edge-list
edge_list = G.get_edgelist()

# Saves edge-list in text file
F = open(cwd+'/data/sf-100-m5-p29.txt', 'w') 

for i in edge_list:
   F.write (str(i[0])+' '+str(i[1])+'\n')
F.close()

