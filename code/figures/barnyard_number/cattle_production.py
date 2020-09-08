#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import anthro.io 
import anthro.viz
colors = anthro.viz.plotting_style()

# Load the FAO data
data = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_product_produced/processed/FAOSTAT_livestock_and_product.csv')
cattle = data[data['category']=='cattle']
cattle.drop(columns=['category'], inplace=True)

# Compute the total and append.
tot = cattle.groupby(['year']).sum().reset_index()
tot['subcategory'] = 'total'
merged = pd.concat([cattle, tot], sort=False)

# Rescale the units to the estimate unit.
merged['kg_mass'] = merged['mass_produced_Mt'].values * 1E9 / 1E11

#%%
fig, ax = plt.subplots(1, 1, figsize=(3, 2))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlim([1961, 2018])
ax.set_ylim([0, 8.5])
ax.set_yticks([0, 2, 4, 6, 8])
ax.set_xlabel('year', fontsize=6)
ax.set_ylabel('mass of cattle product [10$^{11}$ kg]', fontsize=6)

beef = merged[merged['subcategory']=='beef']
dairy = merged[merged['subcategory']=='dairy (milk)']
total = merged[merged['subcategory']=='total']

ax.hlines(8, 1961, 2018, 'k', linestyle='--', lw=0.75, label='estimate')
ax.plot(beef['year'], beef['kg_mass'], '-o', ms=1, lw=0.5, label='beef',
       color=colors['red'])
ax.plot(dairy['year'], dairy['kg_mass'], '-o', ms=1, lw=0.5, label='dairy (milk)',
       color='white')
ax.plot(total['year'], total['kg_mass'], '-o', ms=1, lw=0.5, label='total',
       color=colors['dark_green'])
ax.legend(fontsize=6, loc=(0,  1.02), ncol=4, handlelength=0.75)
plt.savefig('../../../figures/barnyard_number/cattle_product_mass.svg')

# %%
# load the data of livestock populations and examine only cattle
livestock_pop = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_Livestock_population.csv')
cattle = livestock_pop[livestock_pop['animal']=='cattle']

# Adjust the units 
cattle['pop_bhd'] = cattle['population_Mhd'] * 1E6 / 1E9

fig, ax = plt.subplots(1, 1, figsize=(3, 2))

ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlabel('year', fontsize=6)
ax.set_ylabel('standing population [billions]', fontsize=6)
ax.set_ylim([0, 2])
ax.set_yticks([0.0, 0.5, 1.0, 1.5, 2])
ax.set_xlim([1961, 2018])
ax.hlines(1.3, 1961, 2018, 'k', linestyle='--', lw=0.75, 
             label='estimate')
ax.plot(cattle['year'], cattle['pop_bhd'], '-o', color=colors['blue'], 
        ms=1, lw=0.5, label='total population')
ax.legend(fontsize=6)
plt.savefig('../../../figures/barnyard_number/cattle_population.svg')
# %%
