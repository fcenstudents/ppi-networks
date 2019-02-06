# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
===========
Erdos Renyi
===========

Create an G{n,p} random graph with n nodes and link probability p
undirected, unweighted, simple (no loops and no multiple edges)
"""
# networkx 2.2
# python 3.7.0

import sys
import os
import networkx as nx
import random

n_arg = sys.argv[1]
p_arg = sys.argv[2]
name_arg = sys.argv[3]

cwd = os.getcwd() 

# Generates a network based on the Erdos Renyi model
G = nx.erdos_renyi_graph(n=int(n_arg), p=float(p_arg), directed=False)

# Saves adjlist in a text file
nx.write_adjlist(G, str(cwd)+'/data/'+str(name_arg)+'.txt')
