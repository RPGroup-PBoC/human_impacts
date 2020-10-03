#%%
"""
This script computes the stripping ratio of coal as reported in Cooper et al. 2018
"""
import numpy as np
import pandas as pd 
data = pd.read_csv('./processed/Cooper2018_table1_sediment_mass.csv')

# Restrict to just the coal production and coal overburden
coal = data[data['quantity']=='coal production']
waste = data[data['quantity']=='coal waste/overburden']

strip = waste['value'].values / coal['value'].values
year = waste['year']
strip_df = pd.DataFrame(np.array([year, strip]).T, columns=['year', 'stripping_ratio'])
strip_df['year'] = strip_df['year'].astype(int)
strip_df.to_csv('./processed/Cooper2018_coal_stripping_ratio.csv', index=False)
# %%
