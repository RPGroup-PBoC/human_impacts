#%%
import numpy as np 
import pandas as pd 
data = pd.read_csv('./source/FAOSTAT_livestock_population_continent_reduced.csv')
data.head()

data['population_Mhd'] = data['value'].values / 1E6
data.loc[data['unit'].str.contains('1000'), 'population_Mhd'] *= 1000
data.drop(columns=['unit', 'value'], inplace=True)
data = data[data['animal']!='Beehives']
data['animal'] = np.array([s.lower() for s in data['animal'].values])
data.loc[data['region']=='Caribbean', 'region'] = 'Northern America'
data.to_csv('./processed/FAOSTAT_livestock_population_continent.csv', index=False)
# %%
