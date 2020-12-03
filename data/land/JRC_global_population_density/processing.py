#%%
import pandas as pd

# Load the processed data
data = pd.read_csv('./source/JRC_population_densities.csv')

# Move "caribbean" to "northern america"
data.loc[data['region'] == 'Caribbean', 'region'] = 'Northern America'

# Remove nans and zeros. 
data.dropna(inplace=True)
data = data[(data['population']!=0) & (data['total_area_km2']!=0)]

# Recompute the densities to resolve type issues. 
data['people_per_km2'] = data['population'].values / data['total_area_km2'].values

# Create the high-population areas 
threshold = 5E3 
urban = data[data['population'] >= threshold]
rural = data[data['population'] < threshold]

# save all three datasources. 
data.to_csv('./processed/JRC_population_density_tidy.csv', index=False)
urban.to_csv('./processed/JRC_urban_geq5k_density_tidy.csv', index=False)
rural.to_csv('./processed/JRC_rural_lt5k_density_tidy.csv', index=False)
# %%
