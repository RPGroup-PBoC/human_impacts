#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.io 
import anthro.viz
import pycountry
colors = anthro.viz.plotting_style()
regions, positions = anthro.viz.region_colors()

# Load the datasets from AQUASTAT
ag = pd.read_csv('../../../data/water/AQUASTAT_water_use/processed/agricultural_water_withdrawal_region.csv')
ag_pop = pd.read_csv('../../../data/water/AQUASTAT_water_use/processed/agriculture_population.csv')
ind = pd.read_csv('../../../data/water/AQUASTAT_water_use/processed/industrial_water_withdrawal_region.csv')
ind_pop = pd.read_csv('../../../data/water/AQUASTAT_water_use/processed/industrial_population.csv')
mun = pd.read_csv('../../../data/water/AQUASTAT_water_use/processed/municipal_water_withdrawal_region.csv')
mun_pop = pd.read_csv('../../../data/water/AQUASTAT_water_use/processed/municipal_population.csv')

# For each, add colors and compute the per capita
merged = []
for w, p, t in zip([ag, ind, mun], [ag_pop, ind_pop, mun_pop], ['agricultural', 'industrial', 'municipal']):
    # Group by each region and sum to get total withdrawal and year
    p = p.groupby(['region']).sum().reset_index()
    p.loc[p['region']=='Central America', 'region'] = 'Northern America'
    p = p.groupby(['region']).sum().reset_index()
    w.loc[w['region']=='Central America', 'region'] = 'Northern America'
    w = w.groupby(['region']).sum().reset_index()
    # Merge 
    m = w.merge(p, on='region')
    m['category'] = t
    m.rename(columns={'water_withdrawal_10^9_m^3/year': 'water_withdrawal_m3',
                       'population_1000_inhab':'population'}, inplace=True)

    # Compute the per capita
    m['water_withdrawal_m3'] = m['water_withdrawal_m3'] * 1E9
    m['population'] *= 1E3
    m['per_capita'] = m['water_withdrawal_m3'].values / m['population'].values
    m['color'] = [regions[k] for k in m['region'].values]
    merged.append(m)

water = pd.concat(merged, sort=False)
water.drop(columns=['Unnamed: 0'], inplace=True)

#%% Agriculture 
ag = water[water['category']=='agricultural']
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
ag.sort_values('water_withdrawal_m3', inplace=True)
ax.pie(ag['water_withdrawal_m3'], colors=ag['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/agricultural_water_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([100, 200, 300, 400, 500])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in ag.groupby(['region']):
    ax.plot(positions[g], d['per_capita'].values[0], 'o', ms=3, color=regions[g])
    ax.vlines(positions[g], 0, d['per_capita'].values[0], lw=0.5, color=regions[g])
ax.set_ylim([50, 550])
plt.savefig('../../../figures/regional_breakdowns/agricultural_water_per_capita.svg')

#%% Industry
ind = water[water['category']=='industrial']
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
ind.sort_values('water_withdrawal_m3', inplace=True)
ax.pie(ind['water_withdrawal_m3'], colors=ind['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/industrial_water_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 150, 300, 450, 600])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in ind.groupby(['region']):
    ax.plot(positions[g], d['per_capita'].values[0], 'o', ms=3, color=regions[g])
    ax.vlines(positions[g], 0, d['per_capita'].values[0], lw=0.5, color=regions[g])
ax.set_ylim([0, 650 ])
plt.savefig('../../../figures/regional_breakdowns/industrial_water_per_capita.svg')


#%% Municipal
mun = water[water['category']=='municipal']
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
mun.sort_values('water_withdrawal_m3', inplace=True)
ax.pie(mun['water_withdrawal_m3'], colors=mun['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/municipal_water_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 50, 100, 150, 200])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in mun.groupby(['region']):
    ax.plot(positions[g], d['per_capita'].values[0], 'o', ms=3, color=regions[g])
    ax.vlines(positions[g], 0, d['per_capita'].values[0], lw=0.5, color=regions[g])
ax.set_ylim([0, 200])
plt.savefig('../../../figures/regional_breakdowns/municipal_water_per_capita.svg')

#%% 
# Compute the percentages
ag['percent'] = 100 * ag['water_withdrawal_m3'].values / ag['water_withdrawal_m3'].sum()
ind['percent'] = 100 * ind['water_withdrawal_m3'].values / ind['water_withdrawal_m3'].sum()
mun['percent'] = 100 * mun['water_withdrawal_m3'].values / mun['water_withdrawal_m3'].sum()

# %%
