
# -*- coding: utf-8 -*-

# python version == 2.7.13
# gensim version == 0.10.1
# deepwalk version == 1.0.2
# cython version == 0.27.1
# igraph version == 0.7.1

import os
import glob

from deepwalk import graph
from gensim.models import Word2Vec
from igraph import *
from numpy import savetxt, concatenate, double
from random import Random


print('\nChoose a network:\n')

script_dir = os.path.dirname(__file__)
file_list_i = glob.glob(str(script_dir)+str('/data/igraph-networks/')+'*.txt')
file_list_ppi = glob.glob(str(script_dir)+str('/data/ppi-networks/edge_lists_ints/')+'*.txt')

file_list = file_list_i + file_list_ppi

count = 0

if file_list == []:
    print('Empty.\n')
else:
    for name in file_list:
        count += 1
        print(str(count)+'. '+name+'\n')
    
    user_input = input('Name of the network file (type number): ')
    user_input_type = raw_input('Type of network undirected. True or False?: ')
    
    # Creates a graph object
    G = Graph()
    
    if user_input_type == str(False):
        # Loads an edge-list from a text file
        G = G.Read_Edgelist(str(file_list[user_input-1]), directed=True)
    elif user_input_type == str(True):
        G = G.Read_Edgelist(str(file_list[user_input-1]), directed=False)
    
    # Check if there are multiple edges and loops
    s = G.is_simple()
    
    # If there are multiple edges or loops, it simplifies the graph
    if s == False:
        # loops == False if not, nodes with only interaction with itself obtain error in deepwalk
        G.simplify(loops=False)
        # Gets edge-list
        edge_list = G.get_edgelist()
        # Creates a temporal file for the simplified version of the original network
        F = open(str(script_dir)+'/data/'+'temp.txt', 'w') 

        for i in edge_list:
            F.write (str(i[0])+' '+str(i[1])+'\n')
        
        F.close()
        
        print('\nLoading Network...')
        G = graph.load_edgelist(str(script_dir)+'/data/'+'temp.txt', undirected=user_input_type)
        print('OK.\n')
        
        # Deletes temporal file
        os.remove(str(script_dir)+'/data/'+'temp.txt')
        
    elif s == True:
        print('\nLoading Network...')
        G = graph.load_edgelist(file_list[user_input-1], undirected=user_input_type)
        print('OK.\n')


    print('\nSpecify the values of deepwalk parameters...')
    
    user_input_np = input('Number of paths: ')
    user_input_pl = input('Path length: ')
    user_input_size = input('Embedding size: ')
    user_input_win = input('Window size: ')
    user_input_mc = input("Min_count (0 default value): ")
    user_input_w = input("Workers (1 for no parallelization): ")
    user_input_name_f = raw_input('Name of the network: ')
    print('OK.')

    
    # Generates num_paths walks of length <= path_length in each vertex
    # note: alpha 'restart probability'
    print('\nWalking...')
    walks = graph.build_deepwalk_corpus(G, num_paths=user_input_np, path_length=user_input_pl, alpha=0, rand=Random(0))
    print('OK.')

    # Creates embedding of size = size
    # note: 1 worker = no parallelization
    print('\nTraining...')
    model = Word2Vec(walks, size = user_input_size, window = user_input_win, min_count = user_input_mc, workers = user_input_w)
    print('OK.')
    
    # module --> array
    a = [model[0]]   

    for i in range(1, G.order()):
        k = concatenate((a, [model[i]]), axis=0)
        a = k
        
    script_dir = os.path.dirname(__file__)
    
    print('\nSaving embedding...')
    # Saves embedding
    savetxt(str(script_dir)+'/deepwalk_embeddings/'+'dw-embedding_'+str(user_input_name_f)+'_'+str(user_input_size)+'s_'+str(user_input_np)+'p_'+str(user_input_pl)+'pl_'+str(user_input_win)+'w.txt', double(k), fmt='%.5f')
    print('DONE.\n')