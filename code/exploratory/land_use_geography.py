#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.io
import anthro.viz
colors = anthro.viz.plotting_style()

cont_colors = {'Africa':colors['light_green'], 'Northern America':colors['light_red'],                
               'Europe':'#4b4b4b', 'Central America':colors['purple'],
               'South America':colors['dark_brown'],
               'Asia':colors['blue'], 'Oceania':colors['dark_green']}
cont_positions = {k:i for i, k in enumerate(cont_colors.keys())}

# Load the ag area data
data = pd.read_csv('../../data/land/FAOSTAT_agriculture_landuse/processed/FAOSTAT_agricultural_landuse_by_region.csv')
data = data[data['year'] == 2018]
pop_data = pd.read_csv('../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_population_by_region.csv')
pop_data = pop_data[pop_data['year']==2018]

# Compute the area per capita (m^2)
data['area_m2'] = data['area_km2'] * 1E6
dfs = []
for g, d in data.groupby(['region']):
    d = d.copy()
    d['per_capita'] = d['area_km2'].values / (pop_data[pop_data['region']==g]['population_Mhd'].values[0] * 1E6)
    dfs.append(d)
data = pd.concat(dfs, sort=False)
data['percent'] = data['area_m2'].values / data['area_m2'].sum()
for k, v in cont_colors.items():
    data.loc[data['region']==k, 'color'] = v

# %% 
# Make the pie chart
data.sort_values('area_m2', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(data['area_m2'], colors=data['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('./ag_land_donut.svg')

# Make the percapita plot
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
# ax.set_ylim([3000, 95000])
ax.set_ylabel('km$^2$ per capita', fontsize=6)
for _, d in data.groupby(['region']):
    ax.plot(cont_positions[_], d['per_capita'], 'o', ms=3, color=d['color'].values[0])
    ax.vlines(cont_positions[_], 0, d['per_capita'], lw=0.5, color=d['color'].values[0])
plt.savefig('./ag_land_per_capita.svg')
# %%

