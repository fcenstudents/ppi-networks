
# -*- coding: utf-8 -*-

# python version == 2.7.13
# igraph version == 0.7.1

import os
import glob

from igraph import *

print('\nChoose a network to analyze:\n')

script_dir = os.path.dirname(__file__)
file_list_i = glob.glob(str(script_dir)+str('/data/igraph-networks/')+'*.txt')
file_list_ppi = glob.glob(str(script_dir)+str('/data/ppi-networks/edge_lists_ints/')+'*.txt')

file_list = file_list_i + file_list_ppi

count = 0

if file_list == []:
    print('Empty, no edge-lists.')
else:
    for name in file_list:
        count += 1
        print(str(count)+'. '+name+'\n')
        
    # Creates a graph object
    G = Graph()
    
    user_input = input('Edge-list file (type the number): ')
    user_input_type = raw_input('Type of network directed. True or False?: ')
    
    # Loads an edge-list from a text file
    G = G.Read_Edgelist(str(file_list[user_input-1]), directed=user_input_type)
    
    # Check if there are multiple edges and loops
    s = G.is_simple()
    
    # If there are multiple edges or loops, it simplifies the graph
    if s == False:
        G.simplify()

    # Degree
    p1 = G.degree()
    # Betweenness Centrality
    p2 = G.betweenness(directed=user_input_type)
    # Closeness Centrality
    p3 = G.closeness()
    # Clustering Coefficient
    p4 = G.transitivity_local_undirected(mode='zero')
    # Eigenvector Centrality
    p5 = G.eigenvector_centrality(directed=user_input_type)
    # Communieties
    #C = G.community_infomap()
    C = G.community_leading_eigenvector()
    p6 = C.membership
        
    """
    Other communities algorithms:
    
    C = G.community_multilevel() 
    C = G.community_fastgreedy() 
    C = G.community_edge_betweenness()
    C = G.community_optimal_modularity()
    C = G.community_walktrap() 
    C = G.community_spinglass() 
    C = G.community_infomap()
    C = G.community_label_propagation() 
    C = G.community_leading_eigenvector()

    """
    print('OK.')  
    
    print('\nCalculating properties of the network and saving information in text files...')
        
    user_input_file_name = raw_input('Name of the network: ')
    script_dir = os.path.dirname(__file__)
        
    # Saves information of the network in a text file
    E = open(str(script_dir)+str('/information_networks/')+'info_'+str(user_input_file_name)+'.txt', 'w') 
    E.write ('Name = '+str(user_input_file_name)+'-network\n')
    
    if user_input_type == str(False):
        E.write ('Type = undirected\n')
    elif user_input_type == str(True):
        E.write ('Type = directed\n')
    
    if s == True:
        E.write ('Is simple? (no multiple edges and loops) = '+str(s)+'\n')
    elif s == False:
        E.write ('Is simple? (no multiple edges and loops) = '+str(s)+'. Then, simplified\n')
        
    E.write ('Nodes = '+str(G.vcount())+'\n') 
    E.write ('Edges = '+str(G.ecount())+'\n') 
    E.write ('Average Degree = '+str(float(sum(G.degree()))/float(G.vcount()))+'\n') 
    E.write ('Diameter = '+str(G.diameter(directed=user_input_type))+'\n') 
    E.write ('Average Path Length = '+str(G.average_path_length(directed=bool(user_input_type)))+'\n')
    E.write ('Clustering Coefficient = '+str(G.transitivity_undirected(mode='zero'))+'\n')
    E.write ('Density = '+str(G.density())+'\n') 
    E.write ('Modularity = '+str(C.modularity)+'\n')
    E.write ('Communities = '+str(C.summary())+' using community_leading_eigenvector (igraph)\n')
    E.close()
        
    print('\nDONE.\n')
    
    # Saving properties values for each node
    J = open(str(script_dir)+str('/properties_values_nodes/')+'prop_'+str(user_input_file_name)+'.txt', 'w') 
    J.write (str('Degree')+' '+str('Betweenness')+' '+str('Closeness')+' '+str('Clustering')+' '+str('Eigenvector')+' '+str('Membership')+'\n')
    for i in range(int(G.vcount())):
        J.write (str(p1[i])+' '+'{0:.8f}'.format(p2[i])+' '+'{0:.8f}'.format(p3[i])+' '+'{0:.8f}'.format(p4[i])+' '+'{0:.8f}'.format(p5[i])+' '+str(p6[i])+'\n')
    J.close()
    
