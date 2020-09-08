#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz
colors = anthro.viz.plotting_style()

# Load the FAO population 
# load the data of livestock populations and examine only cattle
livestock_pop = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_Livestock_population.csv')
chicken = livestock_pop[livestock_pop['animal']=='chicken']

fig, ax = plt.subplots(1, 1, figsize=(3, 2))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlabel('year', fontsize=6)
ax.set_ylabel('standing population [billions]', fontsize=6)
ax.set_xlim([1961,2018])
ax.set_ylim([0, 28])
ax.set_yticks([0, 5, 10, 15, 20, 25])

# adjust the units
chicken['pop_Bhd']= chicken['population_Mhd'] / 1E3

ax.hlines(25, 1961, 2018, 'k', linestyle='--', label='estimate', lw=0.75)
ax.plot(chicken['year'], chicken['pop_Bhd'], '-o', color=colors['blue'],
        ms=1, lw=0.5, label='total population')
ax.legend(fontsize=6)
plt.savefig('../../../figures/barnyard_number/chicken_population_estimate.svg')


#%%


# %%
