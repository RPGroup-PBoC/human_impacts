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



#%%
# Define the data for steel production as reported by Nicholas.
_conts = ['Asia', 'Africa', 'Northern America', 'Central America',
          'South America', 'Europe', 'Oceania']
_pos = [positions[k] for k in _conts]
_colors = [regions[k] for k in _conts]
totals = [1.36E12, 1.74E10, 1.00E11, 2.06E10, 4.49E10, 2.69E11, 6.34E9]
per_capita = [298, 14, 246, 117, 106, 360, 152]

# Set up the dataframe
steel = pd.DataFrame(np.array([_conts, _pos, _colors, totals, per_capita]).T,
            columns=['region', 'position', 'color', 'total', 'per_capita'])


# %%
# Donut for steel 
fig, ax = plt.subplots(1,1, figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
steel.sort_values('total', inplace=True)
ax.pie(steel['total'], colors=steel['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/steel_regional_donut.svg')

# Per Capita
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 100, 200, 300, 400])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in steel.groupby(['position', 'color']):
    ax.plot(int(g[0]), float(d['per_capita'].values[0]), 'o', ms=3, color=g[1])
    ax.vlines(int(g[0]), 0, float(d['per_capita'].values[0]), lw=0.5, color=g[1])
ax.set_ylim([0, 400])
plt.savefig('../../../figures/regional_breakdowns/steel_regional_per_capita.svg')
# %%
