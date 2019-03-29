import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd
import os

cwd = os.getcwd() 

lst=["rattus-norvegicus", "inter_H-Y"]

for i in lst:

	fname=cwd+'/embeddings-normalized/w10-80walks-40l-d128-'+str(i)+'_norm'

	data = pd.read_csv(fname, header = None, sep=" ")

	#d20 vs. d50
	ax = data.plot.scatter(x=20, y=50, c='red',s=2)
	plt.title("slice de embedding d128")
	plt.savefig(str(cwd)+'/slice-'+str(i)+'-d128-1'+'.png', format='png')
	
	#d20 vs. d80
	ax = data.plot.scatter(x=20, y=80, c='red',s=2)
	plt.title("slice de embedding d128")
	plt.savefig(str(cwd)+'/slice-'+str(i)+'-d128-2'+'.png', format='png')
	
	#d20 vs. d100
	ax = data.plot.scatter(x=20, y=100, c='red',s=2)
	plt.title("slice de embedding d128")
	plt.savefig(str(cwd)+'/slice-'+str(i)+'-d128-3'+'.png', format='png')
	
	#d50 vs. d100
	ax = data.plot.scatter(x=50, y=100, c='red',s=2)
	plt.title("slice de embedding d128")
	plt.savefig(str(cwd)+'/slice-'+str(i)+'-d128-4'+'.png', format='png')
	
	#d80 vs. d100
	ax = data.plot.scatter(x=80, y=100, c='red',s=2)
	plt.title("slice de embedding d128")
	plt.savefig(str(cwd)+'/slice-'+str(i)+'-d128-5'+'.png', format='png')

