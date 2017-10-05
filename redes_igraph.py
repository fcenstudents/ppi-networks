
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from igraph import *

# Genero grafo basado en el modelo de Barabási-Albert (scale-free)
# http://igraph.org/python/doc/igraph.GraphBase-class.html#Barabasi
G1 = Graph()
G1 = G1.Barabasi(n=10000, m=8, outpref=True, directed=True, power=3, zero_appeal=1, implementation="psumtree", start_from=None)

# Obtengo lista de adyacencia
ady_list_BA = G1.get_edgelist()

# Guardo lista de adyacencia en archivo .txt
F = open("BA.txt", "w") 

for i in ady_list_BA:
    F.write (str(i[0])+' '+str(i[1])+'\n')
   
F.close()



# Genero grafo basado en el modelo de Erdös-Renyi (random)
#Erdos_Renyi(n, p, m, directed=False, loops=False)
G2 = Graph()
G2 = G2.Erdos_Renyi(n=10000, p=0.05, directed=True, loops=False)

# Obtengo lista de adyacencia
ady_list_ER = G2.get_edgelist()

# Guardo lista de adyacencia en archivo .txt
F = open("ER.txt", "w") 

for i in ady_list_ER:
    F.write (str(i[0])+' '+str(i[1])+'\n')
   
F.close()



# Genero grafo basado en el modelo de Watts- Strogatz (small-world)
	
G3 = Graph()
G3 = G3.Watts_Strogatz(dim=1, size=10000, nei=10, p=0.01, loops=False, multiple=False)

# Obtengo lista de adyacencia
ady_list_WS = G3.get_edgelist()

# Guardo lista de adyacencia en archivo .txt
F = open("WS.txt", "w") 

for i in ady_list_WS:
    F.write (str(i[0])+' '+str(i[1])+'\n')
   
F.close()
