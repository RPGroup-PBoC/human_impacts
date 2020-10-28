#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load the data from Qin 2019
data = pd.read_csv('../../../data/water/Qin2019_water_use/processed/Qin2019_category_volume_1980-2016.csv')

domestic = data[data['category']=='domestic_municipal']
domestic['volume_L'] = domestic['volume_km3'] * 1E9 * 1E3
domestic['scaled_vol'] = domestic['volume_L'] / 1E14
# %%
fig, ax = plt.subplots(1, 1, figsize=(2.5,2))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlabel('year', fontsize=6)
ax.set_ylabel('annual domestic\nwater consumption [10$^{14}$ L]', fontsize=6)
# Plot the estimate
ax.hlines(1.1, 1980, 2016, 'k', linestyle='-', lw=0.5, label='total estimated use')
ax.hlines(0.3, 1980, 2016, 'k', linestyle='-.', lw=0.5, label='estimated cooking & drinking')
ax.hlines(0.8, 1980, 2016, 'k', linestyle='--', lw=0.5, label='estimated sanitation use')

# Plot the data
ax.plot(domestic['year'], domestic['scaled_vol'], '-o', color=colors['blue'], ms=1, 
        lw=0.25, label='Qin et al. 2019')
ax.legend(fontsize=5)
ax.set_ylim([0, 1.1])
ax.set_xlim([1980, 2016])
plt.savefig('../../../figures/niagara_number/Qin2019_domestic_use.svg')
# %%
