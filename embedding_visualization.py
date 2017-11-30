
# -*- coding: utf-8 -*-

# python version == 2.7.13

import os
import glob
import matplotlib.pyplot as plt


print('\nChoose a network embedding:\n')

script_dir = os.path.dirname(__file__)
file_list = glob.glob(str(script_dir)+'/deepwalk_embeddings/'+'*.txt')

count = 0

if file_list == []:
    print('Empty.')
else:
    for name in file_list:
        count += 1
        print(str(count)+'. '+name+'\n')
    
    user_input = input('Name of the embedding file (type the number): ')
    user_input_dim = input('Embedding size (only 2 or 3): ')
    user_input_name = raw_input("Name of the network: ")

    if user_input_dim == 2:
        x = []
        y = []
        
        F = open(str(file_list[user_input-1]), 'r')
        
        while True:
            line = F.readline()
            if line:
                x_i, y_i = line.split()
                x.append(float(x_i))
                y.append(float(y_i))
            if not line: break
        
        F.close()
        
        
        print('\nSaving scatter plot without indicating properties of nodes...\n')
        
        plt.style.use('seaborn-whitegrid')
        
        fig, ax1 = plt.subplots(facecolor='white')
        ax1.scatter(x, y, s=25, alpha= .6, c='red')

        
        fig.tight_layout()
        
        plt.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'.png', facecolor='w', edgecolor='w')
 
    
        print('\nSaving scatter plot indicating properties of nodes...(Degree, Betweenness, Closeness, Eigenvector, Clustering Coefficient, Community Membership)')
        
        script_dir = os.path.dirname(__file__)
        file_list_p = glob.glob(str(script_dir)+'/properties_values_nodes/'+'*.txt')

        count = 0

        if file_list_p == []:
            print('Empty.')
        else:
            for name in file_list_p:
                count += 1
                print(str(count)+'. '+name+'\n')
    
        user_input_prop = input('Name of the file with the properties of the network (type the number): ')
        
        E = open(str(file_list_p[user_input_prop-1]), 'r')
        
        p_1 = []
        p_2 = []
        p_3 = []
        p_4 = []
        p_5 = []
        p_6 = []
        
        # Name of the properties
        line = E.readline()
        
        while True:
            line = E.readline()
            if line:
                p1, p2, p3, p4, p5, p6 = line.split()
                p_1.append(int(p1)) # Degree
                p_2.append(float(p2)) # Betweenness Centrality
                p_3.append(float(p3)) # Closeness Centrality
                p_4.append(float(p4)) # Clustering Coefficient
                p_5.append(float(p5)) # Eigenvector Centrality
                p_6.append(int(p6)) # Community Membership
                
            if not line: break
        
        E.close()
        
        # Plot style
        plt.style.use('seaborn-whitegrid')
    
        ### Degree
        fig1 = plt.figure()
        ax_1 = plt.subplot(111)
        z1 = ax_1.scatter(x, y, s=25, c=p_1, alpha= .6, cmap='winter', vmin=0, vmax=max(p_1))
        plt.colorbar(z1, ax=ax_1, label='Degree')
       
        fig1.tight_layout()

        fig1.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_degree.png', facecolor='w', edgecolor='w')  
        
    
        ### Betweenness
        fig2 = plt.figure()
        ax_2 = plt.subplot(111)
        z2 = ax_2.scatter(x, y, s=25, c=p_2, alpha= .6, cmap='winter', vmin=min(p_2), vmax=max(p_2))
        plt.colorbar(z2, ax=ax_2, label='Betweenness Centrality')
        
        fig2.tight_layout()

        fig2.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_betweenness.png', facecolor='w', edgecolor='w')
        
        
        ### Closeness
        fig3 = plt.figure()
        ax_3 = plt.subplot(111)
        z3 = ax_3.scatter(x, y, s=25, c=p_3, alpha= .6, cmap='winter', vmin=min(p_3), vmax=max(p_3))
        plt.colorbar(z3, ax=ax_3, label='Closeness Centrality')
        
        fig3.tight_layout()
        
        fig3.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_closeness.png', facecolor='w', edgecolor='w')
        
        
        ### Clustering
        fig4 = plt.figure()
        ax_4 = plt.subplot(111)
        z4 = ax_4.scatter(x, y, s=25, c=p_4, alpha= .6, cmap='winter', vmin=0, vmax=max(p_4))
        plt.colorbar(z4, ax=ax_4, label='Clustering Coefficient')
        
        fig4.tight_layout()
        
        fig4.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_clustering.png', facecolor='w', edgecolor='w')
        
        
        ### Eigenvector
        fig5 = plt.figure()
        ax_5 = plt.subplot(111)
        z5 = ax_5.scatter(x, y, s=25, c=p_5, alpha= .6, cmap='winter', vmin=min(p_5), vmax=max(p_5))
        plt.colorbar(z5, ax=ax_5, label='Eigenvector Centrality')
        
        fig5.tight_layout()
        
        fig5.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_eigenvector.png', facecolor='w', edgecolor='w')
        

        ### Membership
        fig6 = plt.figure()
        ax_6 = plt.subplot(111)
        z6 = ax_6.scatter(x, y, s=25, c=p_6, alpha= .6, cmap='winter', vmin=min(p_6), vmax=max(p_6))
        plt.colorbar(z6, ax=ax_6, label='Community Membership')
    
        fig6.tight_layout()
        
        fig6.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_membership.png', facecolor='w', edgecolor='w')
        
        
    elif user_input_dim == 3:
        
        x = []
        y = []
        z = []
        
        F = open(str(file_list[user_input-1]), 'r')
        
        while True:
            line = F.readline()
            if line:
                x_i, y_i, z_i = line.split()
                x.append(float(x_i))
                y.append(float(y_i))
                z.append(float(z_i))
            if not line: break
        
        F.close()
        
        
        print('\nSaving scatter plot without indicating properties of nodes...\n')
        
        plt.style.use('seaborn-whitegrid')
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, s=25, alpha= .6, c='red')        
        
        fig.tight_layout()
        
        plt.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'.png', facecolor='w', edgecolor='w')
        
        
        print('\nSaving scatter plot indicating properties of nodes...(Degree, Betweenness, Closeness, Eigenvector, Clustering Coefficient, Community Membership)')
        
        script_dir = os.path.dirname(__file__)
        file_list_p = glob.glob(str(script_dir)+'/properties_values_nodes/'+'*.txt')

        count = 0

        if file_list_p == []:
            print('Empty.')
        else:
            for name in file_list_p:
                count += 1
                print(str(count)+'. '+name+'\n')
    
        user_input_prop = input('Name of the file with the properties of the network (type the number): ')
        
        E = open(str(file_list_p[user_input_prop-1]), 'r')
        
        p_1 = []
        p_2 = []
        p_3 = []
        p_4 = []
        p_5 = []
        p_6 = []
        
        # Name of the properties
        line = E.readline()
        
        while True:
            line = E.readline()
            if line:
                p1, p2, p3, p4, p5, p6 = line.split()
                p_1.append(int(p1)) # Degree
                p_2.append(float(p2)) # Betweenness Centrality
                p_3.append(float(p3)) # Closeness Centrality
                p_4.append(float(p4)) # Clustering Coefficient
                p_5.append(float(p5)) # Eigenvector Centrality
                p_6.append(int(p6)) # Community Membership
                
            if not line: break
        
        E.close()
        
  
        ### Degree
        fig1 = plt.figure()
        ax_1 = fig1.add_subplot(111, projection='3d')
        z1 = ax_1.scatter(x, y, z, s=25, c=p_1, alpha= .6, cmap='winter', vmin=0, vmax=max(p_1))
        plt.colorbar(z1, ax=ax_1, label='Degree')
       
        fig1.tight_layout()

        fig1.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_degree.png', facecolor='w', edgecolor='w')  
        
    
        ### Betweenness
        fig2 = plt.figure()
        ax_2 = fig2.add_subplot(111, projection='3d')
        z2 = ax_2.scatter(x, y, z, s=25, c=p_2, alpha= .6, cmap='winter', vmin=min(p_2), vmax=max(p_2))
        plt.colorbar(z2, ax=ax_2, label='Betweenness Centrality')
        
        fig2.tight_layout()

        fig2.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_betweenness.png', facecolor='w', edgecolor='w')
        
        
        ### Closeness
        fig3 = plt.figure()
        ax_3 = fig3.add_subplot(111, projection='3d')
        z3 = ax_3.scatter(x, y, z, s=25, c=p_3, alpha= .6, cmap='winter', vmin=min(p_3), vmax=max(p_3))
        plt.colorbar(z3, ax=ax_3, label='Closeness Centrality')
        
        fig3.tight_layout()
        
        fig3.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_closeness.png', facecolor='w', edgecolor='w')
        
        
        ### Clustering
        fig4 = plt.figure()
        ax_4 = fig4.add_subplot(111, projection='3d')
        z4 = ax_4.scatter(x, y, z, s=25, c=p_4, alpha= .6, cmap='winter', vmin=0, vmax=max(p_4))
        plt.colorbar(z4, ax=ax_4, label='Clustering Coefficient')
        
        fig4.tight_layout()
        
        fig4.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_clustering.png', facecolor='w', edgecolor='w')
        
        
        ### Eigenvector
        fig5 = plt.figure()
        ax_5 = fig5.add_subplot(111, projection='3d')
        z5 = ax_5.scatter(x, y, z, s=25, c=p_5, alpha= .6, cmap='winter', vmin=min(p_5), vmax=max(p_5))
        plt.colorbar(z5, ax=ax_5, label='Eigenvector Centrality')
        
        fig5.tight_layout()
        
        fig5.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_eigenvector.png', facecolor='w', edgecolor='w')
        

        ### Membership
        fig6 = plt.figure()
        ax_6 = fig6.add_subplot(111, projection='3d')
        z6 = ax_6.scatter(x, y, z,  s=25, c=p_6, alpha= .6, cmap='winter', vmin=min(p_6), vmax=max(p_6))
        plt.colorbar(z6, ax=ax_6, label='Community Membership')
    
        fig6.tight_layout()
        
        fig6.savefig(str(script_dir)+'/embeddings_visualizations/dw_emb_'+str(user_input_name)+'_membership.png', facecolor='w', edgecolor='w')
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        