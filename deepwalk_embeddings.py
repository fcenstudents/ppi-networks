
# -*- coding: utf-8 -*-

# Python version == 2.7.13
# gensim version == 0.10.1
# deepwalk version == 1.0.2
# cython version == 0.27.1

import numpy as np

from deepwalk import graph
from random import Random
from gensim.models import Word2Vec


# Cargo lista de conexiones de la red BA
print("Loading Barabási-Albert Network...")
G = graph.load_edgelist('BA.txt', undirected=False)
print("OK\n")


# Check sólo por las dudas...
#print (G.check_self_loops())
#print (G.order())
#print (G.number_of_edges())


# Genero caminos aleatorios truncados (10 por nodo y de longitud a lo sumo 10)
# nota: alpha 'probabilidad de recommienzo'
print("Walking...")
walks = graph.build_deepwalk_corpus(G, num_paths=10, path_length=10, alpha=0, rand=Random(0))
print("OK\n")

# Obtengo embedding dimensión N x size
# nota: 1 worker = no parallelization
print("Training...")
model = Word2Vec(walks, size = 100, window = 5, min_count = 3, workers = 1)
print("OK\n")


# module --> array
a = [model[0]]
count = 0

for x in model:
    count += 1
    if count > 1:
        k = np.concatenate((a, [x]), axis=0)
        a = k


# Guardo embedding
np.savetxt('BA_embedding.txt', np.double(k), fmt='%.5f')
