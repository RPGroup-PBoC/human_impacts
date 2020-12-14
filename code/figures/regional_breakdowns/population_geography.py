#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import anthro.viz
colors = anthro.viz.plotting_style()
region_colors, positions = anthro.viz.region_colors(positions=True)

# Load the total, rural, and urban populations
cats = pd.read_csv('../../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_rural_urban_population_by_region.csv')
totals = pd.read_csv('../../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_population_by_region.csv')

# Restrict to the 2018 values for both datasets.
cats = cats[cats['year']==2018]
totals = totals[totals['year']==2018]

# Incorporate central america into northern america as per the snaphsot.
totals.loc[totals['region']=='Central America', 'region'] = 'Northern America'
totals = totals.groupby(['region']).sum().reset_index()
cats.loc[cats['region']=='Central America', 'region'] = 'Northern America'
cats = cats.groupby(['category', 'region']).sum().reset_index()

# Compute the precentage breakdown for each.
total_pop = totals['population_Mhd'].sum()
totals['fraction'] = totals['population_Mhd'].values / total_pop
totals['color'] = [region_colors[k] for k in totals['region'].values]
cats['color'] = [region_colors[k] for k in cats['region'].values]

dfs = []
for g, d in cats.groupby(['category']):
    d = d.copy()
    tot = d['population_Mhd'].sum()
    d['fraction'] = d['population_Mhd'].values / tot
    dfs.append(d)
cats = pd.concat(dfs)

# %% Total donut
circ = plt.Circle((0, 0), 0.6, color='white')
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
totals.sort_values('population_Mhd', inplace=True)
ax.pie(totals['population_Mhd'], colors=totals['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/total_population_donut.svg')


# %% Rural donut
circ = plt.Circle((0, 0), 0.6, color='white')
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
rural = cats[cats['category']=='rural']
rural.sort_values('population_Mhd', inplace=True)
ax.pie(rural['population_Mhd'], colors=rural['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/rural_population_donut.svg')


# %% Urban donut
circ = plt.Circle((0, 0), 0.6, color='white')
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
urban = cats[cats['category']=='urban']
urban.sort_values('population_Mhd', inplace=True)
ax.pie(urban['population_Mhd'], colors=urban['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/urban_population_donut.svg')



# %%
