#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load the data. 
data = pd.read_csv('../../../data/land/FAOSTAT_agriculture_landuse/processed/FAOSTAT_global_crop_pasture_land_use.csv')

# Set up the figure canvas. 
fig, ax = plt.subplots(1, 1, figsize=(3, 2.25))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlabel('year', fontsize=6)
ax.set_ylabel('land area [million km$^2$]', fontsize=6)
ax.set_ylim([10, 60])
ax.set_xlim([1960, 2018])

crops = data[data['usage_type']=='crops']
pasture = data[data['usage_type']=='pasture']
total = data.groupby(['year']).sum().reset_index()

ax.plot(crops['year'], crops['area_km2'].values / 10**6, '-o', color='#eac264',
        ms=2, label='crops', lw=1)
ax.plot(pasture['year'], pasture['area_km2'].values / 10**6, '-o', 
        color=colors['dark_brown'], ms=2, label='pasture', lw=1)
ax.plot(total['year'], total['area_km2'].values / 10**6, '-o', 
        color=colors['dark_green'], ms=2, label='total', lw=1)
ax.legend(fontsize=6, ncol=3)       
plt.tight_layout()
plt.savefig('../../../figures/terra_number/agricultural_land.svg')


# %%
