#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz
import anthro.io
colors = anthro.viz.plotting_style()

# Load the urban dataset from the JRC and from liu et al
JRC_urban_data = pd.read_csv('../../../data/land/JRC_global_population_density/processed/JRC_urban_geq5k_density_tidy.csv')
liu_table3 = pd.read_csv('../../../data/land/Liu_2018_urban_land_mapping/processed/Liu2018_table_3.csv')

# Add nice units for population
JRC_urban_data['pop_label'] = anthro.io.numeric_formatter(JRC_urban_data['population'].values, 
                                                          digits=2)

# ############################################################################### 
# URBAN POPULATION DENSITY
# ############################################################################### 
fig, ax = plt.subplots(1, 1, figsize=(3.5, 1.75), dpi=300)
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)

# Set up the axes. 
ax.set_ylabel('thousand people / km$^2$', fontsize=6)
ax.set_xlim([-1, 25])
ax.set_ylim([0, 25])

# ############################################################################### 
# POPULATION DENSITY
# ############################################################################### 

# Restrict to 2015 data and plot the top 25 cities
recent = JRC_urban_data[JRC_urban_data['year']==2015].copy()
recent.sort_values(by='population', ascending=False, inplace=True)
city_data = recent[:25]

# Substitute some names. 
city_data.loc[city_data['urban_center']=='Delhi [New Delhi]', 'urban_center'] = 'New Delhi'
city_data.loc[city_data['urban_center']=='Quezon City [Manila]', 'urban_center'] = 'Manila'
city_data.loc[city_data['urban_center']=='Osaka [Kyoto]', 'urban_center'] = 'Osaka'

# Plot the data average
avg_density = recent['population'].mean() / recent['total_area_km2'].mean() / 10**3
ax.hlines(avg_density, -1, len(city_data) + 1, lw=6, color=colors['dark_brown'], 
            alpha=0.25, label=f'{int(avg_density / 10**3)}' + r' $\times$ 10$^3$ people / km$^2$')

# plot the individual cities
ax.vlines(np.arange(len(city_data)), 0, city_data['people_per_km2'].values / 10**3,  
          color=colors['blue'], lw=1, label='__nolegend__')
ax.plot(np.arange(len(city_data)), city_data['people_per_km2'].values / 10**3, 'o', 
          color=colors['blue'], ms=4, label='__nolegend__')

# Plot the population counts
for i in range(len(city_data)):
    ax.text(i - 0.25, (city_data['people_per_km2'].values[i] /1000) + 2.8, 
               city_data['pop_label'].values[i],
               fontsize=4, rotation=90, color='k', label='__nolegend__')


# Set the tick labels. 
ax.xaxis.set_ticks(np.arange(len(city_data)))
ax.xaxis.set_ticklabels(city_data['urban_center'].values, size=4.5, rotation=45)
plt.savefig('../../../figures/terra_number/urban_pop_density.svg')

#%%
# ############################################################################### 
# URBAN LAND AREA
# ############################################################################### 
fig, ax = plt.subplots(1, 1, figsize=(3, 2))
ax.set_xlim([1973, 2017])
ax.set_ylim([0,1.15])
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_ylabel('urban land area [10$^6$ km$^2$]', fontsize=6)
ax.set_xlabel('year', fontsize=6)

JRC_total = JRC_urban_data.groupby('year')['total_area_km2'].sum().reset_index()
liu_total = liu_table3[liu_table3['region']=='Total']
ax.hlines(1, 1975, 2017, 'k', linestyle='--', lw=0.75, label='estimate')
ax.plot(JRC_total['year'], JRC_total['total_area_km2'] / 10**6, '-o', 
        color=colors['blue'], lw=1, ms=4, label='Florczyk et al. 2019')
ax.plot(liu_total['year'], liu_total['area_km2'] / 10**6, '-o', lw=1, 
        color=colors['red'], ms=4,  label='Liu et al. 2018')

ax.set_xticks([1975, 1985, 1995, 2005, 2015])
ax.set_xlim([1975, 2015])
ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
ax.legend(fontsize=6, loc='upper left')

plt.tight_layout()
plt.savefig('../../../figures/terra_number/urban_land_data.svg')

# %%
