#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.io
import anthro.viz
colors = anthro.viz.plotting_style()
regions = anthro.viz.region_colors(positions=False)

# Load the ag area data
rural = pd.read_csv('../../../data/land/FAOSTAT_agriculture_landuse/processed/FAOSTAT_agricultural_landuse_by_region.csv')
urban = pd.read_csv('../../../data/land/JRC_global_population_density/processed/JRC_regional_urban_area_geq5000.csv')
rural = rural[rural['year'] == 2015]
urban = urban[urban['year'] == 2015]

# Adjust for the redefinition of regions
rural.loc[rural['region']=='Northern America', 'region'] = 'North America'
rural.loc[rural['region']=='Central America', 'region'] = 'North America'
urban.loc[urban['region']=='Northern America', 'region'] = 'North America'
urban.loc[urban['region']=='Central America', 'region'] = 'North America'
urban = urban.groupby(['region']).sum().reset_index()
rural = rural.groupby(['region']).sum().reset_index()

#%%
# Add color information
rural['color'] = [regions[k] for k in rural['region'].values]
urban['color'] = [regions[k] for k in urban['region'].values]
# %% 
# Make the pie chart
rural.sort_values('area_km2', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(rural['area_km2'], colors=rural['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/agricultural_area_donut.svg')

urban.sort_values('total_area_km2', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(urban['total_area_km2'], colors=urban['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/urban_area_donut.svg')


# %%
# Compute the percentages
rural_area = rural['area_km2'].sum()
rural['percent'] = 100 * rural['area_km2'].values / rural_area
urban_area = urban['total_area_km2'].sum()
urban['percent'] = 100 * urban['total_area_km2'].values / urban_area
# %%
