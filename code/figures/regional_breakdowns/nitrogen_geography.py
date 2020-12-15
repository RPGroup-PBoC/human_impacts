#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz
import anthro.io
colors = anthro.viz.plotting_style()
regions, positions = anthro.viz.region_colors()
mapper = anthro.io.region_mapper()

# Load the FAOSTAT data
data = pd.read_csv('../../../data/atmosphere_biogeochemistry/FAOSTAT_ammonia/processed/FAOSTAT_nitrogen_tidy.csv')
data.loc[data['locality']=='Carribean', 'locality'] = 'Northern America'
pop = pd.read_csv('../../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_population_by_region.csv')
pop = pop[pop['year']==2018]

#%%
# Add population data to the dataframe.
for k, v in zip(pop['region'], pop['population_Mhd']):
    data.loc[data['locality'] == k, 'population'] = v * 1E6

# Compute per capita
data['locality'] = [mapper[k] for k in data['locality'].values]
data = data.groupby(['element', 'locality']).sum().reset_index()
data['per_capita'] = data['value'].values * 1E3 / data['population'].values
data['color'] = [regions[k] for k in data['locality'].values]
data

#%% Production Figure
prod_df = data[data['element']=='Production']

circ = plt.Circle((0, 0), 0.6, color='white')
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
prod_df.sort_values('value', inplace=True)
ax.pie(prod_df['value'], colors=prod_df['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/nitrogenous_fertilizer_production_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 10, 20, 30, 40])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in prod_df.groupby(['locality', 'color']):
    ax.plot(positions[g[0]], d['per_capita'].values[0], 'o', ms=3, color=g[1])
    ax.vlines(positions[g[0]], 0, d['per_capita'].values[0], lw=0.5, color=g[1])
ax.set_ylim([0, 40])
plt.savefig('../../../figures/regional_breakdowns/nitrogenous_fertilizer_production_per_capita.svg')



#%% Consumption Figure
ag_df = data[data['element']=='Agricultural Use']

circ = plt.Circle((0, 0), 0.6, color='white')
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
ag_df.sort_values('value', inplace=True)
ax.pie(ag_df['value'], colors=ag_df['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/nitrogenous_fertilizer_consumption_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 10, 20, 30, 40, 50])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in ag_df.groupby(['locality', 'color']):
    ax.plot(positions[g[0]], d['per_capita'].values[0], 'o', ms=3, color=g[1])
    ax.vlines(positions[g[0]], 0, d['per_capita'].values[0], lw=0.5, color=g[1])
ax.set_ylim([0, 50])
plt.savefig('../../../figures/regional_breakdowns/nitrogenous_fertilizer_consumption_per_capita.svg')

#%%  Compute the breakdown
prod_df['percent'] = 100 * prod_df['value'] / prod_df['value'].sum()
ag_df['percent'] = 100 * ag_df['value'] / ag_df['value'].sum()
prod_df
# %%
