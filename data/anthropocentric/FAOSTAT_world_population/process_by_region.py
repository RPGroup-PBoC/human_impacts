#%%
import numpy as np 
import pandas as pd 
data = pd.read_csv('./source/FAOSTAT_population_by_region_reduced.csv')


# Aggregate 'Caribbean' into 'Northern America'
data.loc[data['region']=='Caribbean', 'region'] = 'Northern America'
grouped = data.groupby(['region', 'year']).sum().reset_index()
grouped.to_csv('./processed/FAOSTAT_population_by_region.csv', index=False)

# %%
