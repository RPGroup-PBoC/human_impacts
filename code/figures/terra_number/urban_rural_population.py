#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load the FAO data 
data = pd.read_csv('../../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_rural_urban_population.csv')
# Compute the total population (sum of rural and urban) 
total = data.groupby(['year']).sum().reset_index()

# Set up the figure canvas and format axes
fig, ax = plt.subplots(1, 1, figsize=(4, 4))
ax.xaxis.set_tick_params(labelsize=8)
ax.yaxis.set_tick_params(labelsize=8)
ax.set_xlabel('year', fontsize=8)
ax.set_ylabel('population [billions]', fontsize=8)
ax.set_xlim([1950, 2018])

# Plot the total population
ax.plot(total['year'], total['population'] / 1E9, '-o', color=colors['dark_green'],
        label='total',ms=2, lw=0.5)

# Define colors for each category and plot
catcolors = {'rural':colors['red'], 'urban':colors['blue']}
for g, d in data.groupby(['category']):
    ax.plot(d['year'], d['population'] / 1E9, '-o', ms=2, lw=0.5, label=g,
            color=catcolors[g])
        
# Add legend and save
ax.legend(fontsize=8)
plt.savefig('../../../figures/terra_number/urban_rural_pop.pdf', bbox_inches='tight')
# %

# %%
