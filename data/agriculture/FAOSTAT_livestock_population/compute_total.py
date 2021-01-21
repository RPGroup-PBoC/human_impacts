#%%
import pandas as pd 
data = pd.read_csv('./processed/FAOSTAT_Livestock_population.csv')

# Exclude Beehives
data = data[data['animal'] != 'beehives']

# Group by year and compute the sum total
grouped = data.groupby(['year']).sum().reset_index()
grouped.to_csv('./processed/FAOSTAT_livestock_population_total.csv',
                index=False)

# %%
