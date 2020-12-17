#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.io
import anthro.viz
colors = anthro.viz.plotting_style()
regions, positions = anthro.viz.region_colors()

# Load the datasets
total = pd.read_csv('../../../data/energy/EIA_global_energy_consumption/processed/EIA_TotalConsumption.csv')
total = total[total['year']==2017]
renewables = pd.read_csv('../../../data/energy/EIA_global_energy_consumption/processed/EIA_RenewableGeneration.csv')
renewables = renewables[renewables['year']==2017]
fossils = pd.read_csv('../../../data/energy/EIA_global_energy_consumption/processed/EIA_FossilFuelConsumption.csv')
fossils = fossils[fossils['year']==2017]
nuclear = pd.read_csv('../../../data/energy/EIA_global_energy_consumption/processed/EIA_NuclearGeneration.csv')
nuclear = nuclear[nuclear['year']==2017]

for d in [total, renewables, fossils, nuclear]:
    d['color'] = [regions[k] for k in d['Country Group'].values]
    d['pos'] = [positions[k] for k in d['Country Group'].values]

total.head()
#%% Fossil fuel consumption
fossils.sort_values('Watts', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(fossils['Watts'], colors=fossils['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/fossil_fuel_consumption_donut.svg')

# Make the percapita plot
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_ylim([0, 10])
ax.set_ylabel('per capita\n[1000 W]', fontsize=6)
for g, d in fossils.groupby(['Country Group']):
    ax.plot(positions[g], int(d['Per Capita']) / 1E3, 'o', ms=3, color=regions[g])
    ax.vlines(positions[g], 0, int(d['Per Capita']) / 1E3, lw=0.5, color=regions[g])
ax.set_yticks([0, 3, 6, 9])
plt.savefig('../../../figures/regional_breakdowns/fossil_fuel_consumption_per_capita.svg')

#%% renewables
renewables.sort_values('Watts', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(renewables['Watts'], colors=renewables['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/renewables_consumption_donut.svg')

# Make the percapita plot
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_ylim([0, 0.8])
ax.set_ylabel('per capita\n[1000 W]', fontsize=6)
for g, d in renewables.groupby(['Country Group']):
    ax.plot(positions[g], int(d['Per Capita']) / 1E3, 'o', ms=3, color=regions[g])
    ax.vlines(positions[g], 0, int(d['Per Capita']) / 1E3, lw=0.5, color=regions[g])

ax.set_yticks([0, 0.25, 0.5, 0.75])
plt.savefig('../../../figures/regional_breakdowns/renewables_consumption_per_capita.svg')

#%% Nuclear
nuclear.sort_values('Watts', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(nuclear['Watts'], colors=nuclear['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/nuclear_generation_donut.svg')

# Make the percapita plot
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_ylim([0, 0.75])

ax.set_ylabel('per capita\n[1000 W]', fontsize=6)
for g, d in nuclear.groupby(['Country Group']):
    ax.plot(positions[g], int(d['Per Capita']) / 1E3, 'o', ms=3, color=regions[g])
    ax.vlines(positions[g], 0, int(d['Per Capita']) / 1E3, lw=0.5, color=regions[g])

# need to hardcode oceania in
ax.plot(5, 0, 'o', ms=3, color=regions['Oceania'])
ax.set_yticks([0, 0.25, 0.5, 0.75])
plt.savefig('../../../figures/regional_breakdowns/nuclear_generation_per_capita.svg')

#%% Total
total.sort_values('Watts', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(total['Watts'], colors=total['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/total_power_consumption_donut.svg')

# Make the percapita plot
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_ylim([0, 9])
ax.set_ylabel('per capita\n[1000 W]', fontsize=6)
for g, d in total.groupby(['Country Group']):
    ax.plot(positions[g], int(d['Per Capita']) / 1E3, 'o', ms=3, color=regions[g])
    ax.vlines(positions[g], 0, int(d['Per Capita']) / 1E3, lw=0.5, color=regions[g])
ax.set_yticks([0, 3, 6, 9])
plt.savefig('../../../figures/regional_breakdowns/total_consumption_per_capita.svg')

#%%
# Compute the percentages
total['percent'] = 100 * total['Watts'].values / total['Watts'].sum()
renewables['percent'] = 100 * renewables['Watts'].values / renewables['Watts'].sum()
nuclear['percent'] = 100 * nuclear['Watts'].values / nuclear['Watts'].sum()
fossils['percent'] = 100 * fossils['Watts'].values / fossils['Watts'].sum()

renewables
# %%
