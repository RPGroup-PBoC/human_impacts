#%%
import pandas as pd 
data = pd.read_csv('./source/FAOSTAT_livestock_population_source.csv')

# Convert units
data.loc[data['Unit'].str.contains('1000 Head'), 'Value'] *= 1000
data['Value'] /= 1E6

# Reduce to necessary
data = data[['Area', 'Item', 'Year', 'Value']]
data.rename(columns={'Area':'country', 
                     'Item': 'animal', 
                     'Value':'population_Mhd',
                     'Year': 'year'},
                     inplace=True)
# Compute globla totals
totals = data.groupby(['year', 'animal']).sum().reset_index()
totals['animal'] = totals['animal'].str.lower()
totals.to_csv('processed/FAOSTAT_livestock_population.csv', index=False)
# %%

# Process continent data
data = pd.read_csv('./source/FAOSTAT_livestock_population_region.csv')
data.loc[data['Unit'].str.contains('1000 Head'), 'Value'] *= 1000
data['Value'] /= 1E6

# Reduce to necessary
data = data[['Area', 'Item', 'Year', 'Value']]
data.rename(columns={'Area':'region', 
                     'Item': 'animal', 
                     'Value':'population_Mhd',
                     'Year': 'year'},
                     inplace=True)
# Compute globla totals
totals = data.groupby(['year', 'region', 'animal']).sum().reset_index()
totals['animal'] = totals['animal'].str.lower()
totals.to_csv('processed/FAOSTAT_livestock_population_continent.csv', index=False)



# %%
