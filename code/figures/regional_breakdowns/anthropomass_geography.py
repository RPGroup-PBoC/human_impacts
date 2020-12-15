#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz
colors = anthro.viz.plotting_style()
regions, positions = anthro.viz.region_colors()
regions = {k.lower():v.lower() for k, v in regions.items()}
positions = {k.lower():v for k, v in positions.items()}

# Load the cement data
CONVERSION = 7 # mass of concrete is around 7 times the mass of cement (Monteiro et al 2017).
cement = pd.read_csv('../../../data/anthropocentric/USGS_cement_production/processed/USGS_cement_by_region.csv')
# Ensure there's only one value per region
cement = cement.groupby(['year', 'region', 'fao_locality']).sum().reset_index()
#%%
# load the population data
pop = pd.read_csv('../../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_world_population_by_country.csv')

# Include country population
dfs = []
for g, d in cement.groupby(['fao_locality', 'year']):
    _pop = pop[(pop['year']==g[1]) & (pop['region']==g[0])]['population_Mhd'].values[0] * 1E6
    d = d.copy()
    d['population'] = _pop
    dfs.append(d)
cement = pd.concat(dfs, sort=False) 

# Compute the cement per capita and average over the 5 years. 
cement['concrete_kg'] = cement['value'] * 1E6 * CONVERSION
cement['per_capita'] = (cement['concrete_kg'].values)/ cement['population'].values
cement = cement[cement['year']==2017]
cement.loc[cement['region']=='central america', 'region'] = 'north america'
cement.loc[cement['region']=='northern america', 'region'] = 'north america'
cement.loc[cement['region']=='asia', 'region'] = 'Asia'
cement = cement.groupby('region').sum().reset_index()

# Add colors and positional informatio
cement['color'] = [regions[k] for k in cement['region'].values]
cement['pos'] = [positions[k] for k in cement['region'].values]

#%% Donut for concrete
fig, ax = plt.subplots(1,1, figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
cement.sort_values('concrete_kg', inplace=True)
ax.pie(cement['concrete_kg'], colors=cement['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/concrete_regional_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([50, 100, 150, 200])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in cement.groupby(['pos', 'color']):
    ax.plot(int(g[0]), float(d['per_capita'].values[0]) / 1E3, 'o', ms=3, color=g[1])
    ax.vlines(int(g[0]), 0, float(d['per_capita'].values[0]) / 1E3, lw=0.5, color=g[1])
ax.set_ylim([0, 220])
plt.savefig('../../../figures/regional_breakdowns/concrete_regional_per_capita.svg')


#%%
# Compute the percentages
total_cement = cement['value'].sum()
cement['percent'] = 100 * cement['value'].values / total_cement
cement

#%% Steel
steel = pd.read_csv('../../../data/anthropocentric/WorldSteelAssoc_steel_production/processed/crude_steel_by_region.csv')

# Remove spurious nans and convert values to floats
steel.dropna(inplace=True)
steel['value'] = [float(str(k).replace(',', '')) for k in steel['value'].values]

# Restrict to one year
steel = steel[steel['year']==2018]

# Include country population
dfs = []
for g, d in steel.groupby(['fao_locality', 'year']):
    _pop = pop[(pop['year']==g[1]) & (pop['region']==g[0])]['population_Mhd'].values[0] * 1E6
    d = d.copy()
    d['population'] = _pop
    dfs.append(d)
steel = pd.concat(dfs, sort=False) 

# Update region definitions
steel.loc[steel['region']=='central america', 'region'] = 'north america'
steel.loc[steel['region']=='northern america', 'region'] = 'north america'

# Group and compute per capita
steel = steel.groupby(['region']).sum().reset_index()
steel['kg_per_capita'] = steel['value'].values * 1E6 / steel['population'].values

# Add colors and positional information.
steel['color'] = [regions[k] for k in steel['region'].values]
steel['pos'] = [positions[k] for k in steel['region'].values]

#%% Donut for steel 
fig, ax = plt.subplots(1,1, figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
steel.sort_values('value', inplace=True)
ax.pie(steel['value'], colors=steel['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/steel_regional_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 100, 200, 300, 400])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in steel.groupby(['pos', 'color']):
    ax.plot(int(g[0]), float(d['kg_per_capita'].values[0]), 'o', ms=3, color=g[1])
    ax.vlines(int(g[0]), 0, float(d['kg_per_capita'].values[0]), lw=0.5, color=g[1])
ax.set_ylim([0, 400])
plt.savefig('../../../figures/regional_breakdowns/steel_regional_per_capita.svg')


#%%
# Compute the percentages
total_steel = steel['value'].sum()
steel['percent'] = 100 * steel['value'].values / total_steel
steel
