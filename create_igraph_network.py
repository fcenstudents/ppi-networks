
# -*- coding: utf-8 -*-

# python version == 2.7.13
# igraph version == 0.7.1

import os

from igraph import *


print('\nChoose a type of network to generate. Write:\n1 for Scale-Free\n2 for Random\n3 for Small-World')
user_input = input('Type: ')

# Creates a graph object
G = Graph()
    
if user_input == 1:
    print('\nCreating Scale-Free Network...')
    # Input parameters
    user_input_type = raw_input('Directed. True or False?: ')
    user_input_n = input('Number of nodes: ')
    user_input_m = input('Number of initial edges for each vertex: ')
    user_input_power = input('Power: ')
    # Generates a network based on the Barabási-Albert model
    G = G.Barabasi(n=user_input_n, m=user_input_m, outpref=False, directed=user_input_type, power=user_input_power, zero_appeal=1, implementation='psumtree', start_from=None)
    print('\nOK.\n')
   
elif user_input == 2:
    print('\nCreating Random Network...')
    # Input parameters
    user_input_type = raw_input('Directed. True or False?: ')
    user_input_n = input('Number of nodes: ')
    user_input_p = input('Probability of edges: ')
    # Generates a network based on the Erdös-Rényi model
    G = G.Erdos_Renyi(n=user_input_n, p=user_input_p, directed=user_input_type, loops=False)
    print('\nOK.\n')
   
elif user_input == 3:
    print('\nCreating Small-World Network...')
    # Input parameters
    user_input_type = raw_input('Directed. True or False?: ')
    user_input_n = input('Number of nodes: ')
    user_input_d = input('Dimension of the lattice: ')
    user_input_nei = input('Distance within which two vertices will be connected: ')
    user_input_p = input('Rewiring probability: ')
    # Generates a network based on the Watts-Strogatz model
    G = G.Watts_Strogatz(dim=user_input_d, size=user_input_n, nei=user_input_nei, p=user_input_p, loops=False, multiple=False) 
    print('\nOK.\n')
    
    
print('Obteining and saving edge-list in a text file...')

# Gets edge-list
edge_list = G.get_edgelist()

# Saves edge-list in text file
user_input_file = raw_input('Name of the network: ')

script_dir = os.path.dirname(__file__)

F = open(str(script_dir)+'/data/igraph-networks/'+str(user_input_file)+'.txt', 'w') 

for i in edge_list:
   F.write (str(i[0])+' '+str(i[1])+'\n')
F.close()

print('\nDONE.\n')
