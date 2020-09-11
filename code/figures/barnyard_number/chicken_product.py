#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load the data for chicken product.
data = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_product_produced/processed/FAOSTAT_livestock_and_product.csv')
chicken = data[data['category']=='poultry']
chicken.drop(columns=['category'], inplace=True)

# Compute the total and append.
tot = chicken.groupby(['year']).sum().reset_index()
tot['subcategory'] = 'total'
merged = pd.concat([chicken, tot], sort=False)

# Rescale the units to the estimate unit.
merged['kg_mass'] = merged['mass_produced_Mt'].values * 1E9 / 1E11
merged

# %%
fig, ax = plt.subplots(1, 1, figsize=(3, 1.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_ylim([0, 2.25])
ax.set_yticks([0, 0.5, 1, 1.5, 2])
ax.set_xlim([1961, 2018])
ax.set_xlabel('year', fontsize=6)
ax.set_ylabel('mass of chicken\nproduct [10$^{11}$ kg]', fontsize=6)

poultry = merged[merged['subcategory']=='chicken']
egg = merged[merged['subcategory']=='egg']
total = merged[merged['subcategory']=='total']

ax.hlines(1.5, 1961, 2018, 'k', linestyle='--', lw=0.75, label='estimate')
ax.plot(poultry['year'], poultry['kg_mass'], '-o', ms=1, lw=0.5, label='poultry',
       color=colors['red'])
ax.plot(egg['year'], egg['kg_mass'], '-o', ms=1, lw=0.5, label='eggs',
       color='white')
ax.plot(total['year'], total['kg_mass'], '-o', ms=1, lw=0.5, label='total',
       color=colors['dark_green'])
ax.legend(fontsize=6, ncol=2, handlelength=0.75)
plt.savefig('../../../figures/barnyard_number/chicken_product_mass.svg')


# %%
