# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
===========
Embedding Normalization
===========

Standardization (or Z-score normalization) is the process where the features are rescaled so that they’ll have the properties of a standard normal distribution with μ=0 and σ=1, where μ is the mean (average) and σ is the standard deviation from the mean.

"""

# pandas 0.23.4
# python 3.7.0


cwd = os.getcwd() 

n_arg = sys.argv[1]

# walks
x = [1, 5, 10, 25, 50, 100]
# walk-lenght
y = [5, 10, 25, 50, 100]


for q in range(len(x)):
	for r in range(len(y)):
		fname= cwd + '/deepwalk-embeddings/' + 'w3-x' + str(x[q]) + '-y' + str(y[r]) + '-' + n_arg + '.txt'

		data = pd.read_csv(fname, header=0, delimiter=' ')

		data_scale = (data - data.mean()) / data.std()

		name = 'embeddings-normalized/'+ 'w3-x' + str(x[q]) + '-y' + str(y[r]) + '-' + n_arg + '_norm'

		pd.DataFrame.to_csv(data_scale, path_or_buf=name, sep=' ', float_format='%.8f', columns=None, header=False, index=True, index_label=True)
