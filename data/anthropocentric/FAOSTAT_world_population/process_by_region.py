# %%
import numpy as np
import pandas as pd
data = [pd.read_csv('./source/FAOSTAT_population_by_region_reduced.csv'),
        pd.read_csv('./source/FAOSTAT_rural_urban_population_by_region_reduced.csv')]


# Aggregate 'Caribbean' into 'Northern America'
fnames = ['FAOSTAT_population_by_region.csv',
          'FAOSTAT_rural_urban_population_by_region.csv']
for i, d in enumerate(data):
    d.loc[d['region'] == 'Caribbean', 'region'] = 'Northern America'
    if i == 0:
        groupby = ['region', 'year']
    elif i == 1:
        groupby = ['region', 'category', 'year']
    grouped = d.groupby(groupby).sum().reset_index()
    grouped.to_csv(f'./processed/{fnames[i]}', index=False)

# %%
# Generate the total global population
data = pd.read_csv(f'./processed/{fnames[0]}')
grouped = data.groupby(['year']).sum().reset_index()
grouped.to_csv('processed/FAOSTAT_total_population.csv', index=False)
