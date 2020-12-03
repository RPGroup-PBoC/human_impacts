#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import anthro.viz
colors = anthro.viz.plotting_style()
regions, positions = anthro.viz.region_colors()

# Load the datasets
co2 = pd.read_csv('../../../data/atmosphere_biogeochemistry/global_carbon_project_CO2/processed/regional_co2_data_processed.csv')
ch4 = pd.read_csv('../../../data/atmosphere_biogeochemistry/global_carbon_project_methane/processed/regional_ch4_data_processed.csv')
pop = pd.read_csv('../../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_population_by_region.csv')

# Restrict to the same decadal average (2008 - 2017)
co2 = co2[(co2['Period']=='2008-2017') & (co2['Emission Units']=='Tg CO2 yr-1')]

# For CH4, keep only the sample mean for the anthropogenic total and compute mean of top-down and bototm-up
ch4 = ch4[(ch4['Measure']=='Sample Mean') & (ch4['Category']=='Total Anthropogenic')]
ch4 = ch4.groupby(['Region']).mean().reset_index()

# Compute the decadal average population for 2008 - 2017.
pop = pop[(pop['year'] >= 2008) & (pop['year'] <= 2017)]
pop = pop.groupby(['region']).mean().reset_index()
pop['year'] = '2008-2017'
pop.rename(columns={'region':'Region', 'year':'Period'}, inplace=True)

# Tidy the annotation of the regions
co2.loc[co2['Region']=='Europe and Russia', 'Region'] = 'Europe'
ch4.loc[ch4['Region']=='Europe and Russia', 'Region'] = 'Europe'
co2.loc[co2['Region']=='North America', 'Region'] = 'Northern America'
ch4.loc[ch4['Region']=='North America', 'Region'] = 'Northern America'
ch4.rename(columns={'Emissions (Tg CH4 yr-1)': 'Emissions'}, inplace=True)
# Add color and positional information
co2['color'] = [regions[k] for k in co2['Region'].values]
ch4['color'] = [regions[k] for k in ch4['Region'].values]
co2['position'] = [positions[k] for k in co2['Region'].values]
ch4['position'] = [positions[k] for k in ch4['Region'].values]

# Join the population and CO2 data on the region.
for g, d in pop.groupby(['Region']):
    co2.loc[co2['Region']==g, 'population'] = d['population_Mhd'].values * 1E6
    ch4.loc[ch4['Region']==g, 'population'] = d['population_Mhd'].values * 1E6

# Compute to kg / person / yr
co2['t_co2_per_capita'] = (1E6 * co2['Emissions'].values) / co2['population'].values
ch4['kg_ch4_per_capita'] = (1E9 * ch4['Emissions'].values) / ch4['population'].values

#%% CO2 Figure

# Donut for CO2
fig, ax = plt.subplots(1,1, figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
co2.sort_values('Emissions', inplace=True)
ax.pie(co2['Emissions'], colors=co2['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/co2_regional_donut.svg')

# Per Capita
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 4, 8, 12, 16])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in co2.groupby(['position', 'color']):
    ax.plot(int(g[0]), d['t_co2_per_capita'].values[0], 'o', ms=3, color=g[1])
    ax.vlines(int(g[0]), 0, d['t_co2_per_capita'].values[0], lw=0.5, color=g[1])
ax.set_ylim([0, 17])
plt.savefig('../../../figures/regional_breakdowns/co2_regional_per_capita.svg')
#%% CH4 Figure

# Donut for CH4
fig, ax = plt.subplots(1,1, figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
ch4.sort_values('Emissions', inplace=True)
ax.pie(ch4['Emissions'], colors=ch4['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/ch4_regional_donut.svg')

# Per Capita
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([50, 100, 150, 200])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in ch4.groupby(['position', 'color']):
    ax.plot(int(g[0]), d['kg_ch4_per_capita'].values[0], 'o', ms=3, color=g[1])
    ax.vlines(int(g[0]), 0, d['kg_ch4_per_capita'].values[0], lw=0.5, color=g[1])
ax.set_ylim([35, 200])
plt.savefig('../../../figures/regional_breakdowns/ch4_regional_per_capita.svg')

# %%
# Compute the percentages. 
tot_co2 = co2['Emissions'].sum()
co2['percent'] = 100 * co2['Emissions' ].values / tot_co2
co2[['Region', 'percent']]
tot_ch4 = ch4['Emissions'].sum()
ch4['percent'] = 100 * ch4['Emissions' ].values / tot_ch4
ch4[['Region', 'percent']]

# %%
