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

import sys
import os
import pandas as pd

name_arg = sys.argv[1]

cwd = os.getcwd() 

fname=cwd+'/deepwalk-embeddings/'+name_arg+'.txt'

data = pd.read_csv(fname, header=0, delimiter=' ')

data_scale = (data - data.mean()) / data.std()

name = 'embeddings-normalized/'+ name_arg + '_norm.txt'

pd.DataFrame.to_csv(data_scale, path_or_buf=name, sep=' ', float_format='%.8f', columns=None, header=False, index=True, index_label=True)

