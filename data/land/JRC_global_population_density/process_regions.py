#%%
import numpy as np 
import pandas as pd

# Load the tidy densities
data = pd.read_csv('./processed/JRC_population_density_tidy.csv')

# Create a dictionary mapping coarse-grained regions
regions = data['region'].unique()

n_am = ['Northern America', 'Caribbean']
europe = ['Northern Europe', 'Western Europe', 'Eastern Europe', 'Southern Europe']
africa = ['Western Africa', 'Northern Africa', 'Southern Africa',
        'Eastern Africa', 'Middle Africa']
asia = ['Western Asia', 'South-Central Asia', 'Eastern Asia', 'South-Eastern Asia']
oceania = ['Melanesia', 'Polynesia', 'Australia/New Zealand']
for coarse, fine  in zip(['Northern America', 'Europe', 'Africa', 'Asia', 'Oceania'],
                        [n_am, europe, africa, asia, oceania]):
   for v in fine:
       data.loc[data['region']==v, 'region'] = coarse


# Define the thresholds as Florczyk et al. does.
threshold_pop = 5E3
threshold_density = 300
urban = data[(data['population'] >= threshold_pop) & (data['people_per_km2'] >= threshold_density)]


# Compute the total area for each
urban = urban.groupby(['region', 'year']).sum().reset_index()
urban = urban[['region', 'year', 'population', 'total_area_km2']]
urban.to_csv('./processed/JRC_regional_urban_area_geq5000.csv', index=False)
# %%
