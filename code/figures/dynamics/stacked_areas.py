#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import anthro.viz
colors = anthro.viz.plotting_style() 
# %%

#%% Load the population data 
pop_data = pd.read_csv('../../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_rural_urban_population.csv')
pop_data['pop_bil'] = pop_data['population'] / 1E9
total_pop = pop_data.groupby(['year'])['pop_bil'].sum().reset_index()
min_pop, max_pop = total_pop['pop_bil'].min(), total_pop['pop_bil'].max()
fig, ax =  plt.subplots(1, 1, figsize=(2, 2))

# Format the eaxes
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlim([1960, 2020])
ax.set_xticks([1960, 1980, 2000, 2020])
ax.set_ylim([0, 8])
ax.set_xlabel('year', fontsize=6)
ax.set_ylabel('population [billion]', fontsize=6)

ax.stackplot(pop_data['year'].unique(), pop_data[pop_data['category']=='rural']['pop_bil'].values,
                                pop_data[pop_data['category']=='urban']['pop_bil'].values,
                                labels=['rural', 'urban'], 
                                colors=[colors['green'], colors['blue']],
                                linewidth=0.25)
plt.savefig('../../../figures/database_paper/population_stack.svg', bbox_inches='tight')
#
#%% Load anthropomass data
anthropo = pd.read_csv('../../../data/anthropocentric/Elhacham2020_anthropomass/processed/anthopogenic_mass_2015_processed.csv')
# Tidy
anthropo.rename(columns={'Year':'year'}, inplace=True)
merged = anthropo.merge(total_pop, on='year')
merged.dropna(inplace=True)
merged['bricks_asphalt'] = merged['bricks_Tt'].values + merged['asphalt_Tt'].values
merged['all_others'] = merged['metals_Tt'].values + merged['waste_Tt'].values + merged['other_Tt']

fig, ax =  plt.subplots(1, 1, figsize=(2, 2))

# Format the eaxes
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlim([min_pop, max_pop])


ax.set_xlabel('population [billion]', fontsize=6)
ax.set_ylabel('anthropomass [10$^{15}$ kg]', fontsize=6)

ax.stackplot(merged['pop_bil'].values, merged['concrete_Tt'].values, merged['aggregates_Tt'],
                                merged['bricks_asphalt'], merged['all_others'],
                                colors=['darkgrey', 'grey', colors['green'], 
                                        colors['blue']],
                                linewidth=0.25)
plt.savefig('../../../figures/database_paper/anthropomass_stack.svg', bbox_inches='tight')
#
#%%
# Load livestock data 
livestock = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_livestock_population.csv')
livestock['category'] = 'other'
livestock.loc[livestock['animal']=='cattle', 'category'] = 'cattle'
livestock.loc[livestock['animal']=='chicken', 'category'] = 'chicken'
livestock.loc[livestock['animal']=='swine', 'category'] = 'swine'

livestock = livestock.groupby(['year', 'category'])['population_Mhd'].sum().reset_index()

# Merge on population
merged = livestock.merge(total_pop, on='year')
merged.dropna(inplace=True)

fig, ax =  plt.subplots(1, 1, figsize=(2, 2))

# Format the eaxes
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlim([min_pop, max_pop])
ax.set_xlim([3, max_pop])


ax.set_xlabel('population [billion]', fontsize=6)
ax.set_ylabel('livestock population [million]', fontsize=6)

ax.stackplot(merged['pop_bil'].unique(), 
                                       merged[merged['category']=='other']['population_Mhd']/1E3,
                                       merged[merged['category']=='swine']['population_Mhd']/1E3, 
                                       merged[merged['category']=='cattle']['population_Mhd']/1E3,
                                       merged[merged['category']=='chicken']['population_Mhd']/1E3, 
                                        colors=['grey', colors['light_red'], colors['blue'], 
                                        colors['green']],
                                linewidth=0.25)
plt.savefig('../../../figures/database_paper/livestock_stack.svg', bbox_inches='tight')

# %%
energy = pd.read_csv('../../../data/energy/BP_statistical_report_global_energy_usage/processed/BP_global_energy_usage_by_type.csv')

# Tidy and group
energy.loc[energy['type'].isin(['Geothermal/Biomass/Other', 'Biodiesel/Biogasoline', 'Solar', 'Wind']), 'type'] = 'renew'
energy.loc[energy['type'].isin(['Hydroelectric']), 'type'] = 'hydro'
merged = energy.merge(total_pop, on='year')
merged.fillna(value=0, inplace=True)
merged = merged.groupby(['type', 'year', 'pop_bil'])['consumption_TW'].sum().reset_index()

fig, ax =  plt.subplots(1, 1, figsize=(2, 2))

# Format the axes
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)

ax.set_xlim([3.5, max_pop])


ax.set_xlabel('population [billion]', fontsize=6)
ax.set_ylabel('consumed power [TW]', fontsize=6)

ax.stackplot(merged['pop_bil'].unique(), 
                                       merged[merged['type']=='Nuclear']['consumption_TW'].values,
                                       merged[merged['type']=='renew']['consumption_TW'].values, 
                                       merged[merged['type']=='hydro']['consumption_TW'].values,
                                       merged[merged['type']=='Fossil Fuels']['consumption_TW'].values, 
                                        colors=[colors['red'], colors['green'], colors['blue'], 
                                        'grey'],
                                linewidth=0.25)
plt.savefig('../../../figures/database_paper/energy_stack.svg', bbox_inches='tight')





# %%
