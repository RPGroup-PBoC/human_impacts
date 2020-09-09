#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load the various datasets 
aquatic = pd.read_csv('./aquaculture_categorized.csv')
terra = pd.read_csv('./livestock_categorized.csv')

# For each dataset, consider only most recent year
aquatic = aquatic[aquatic['year']==2018]
terra = terra[terra['year']==2018]

# Assign colors for each category of aquatic animal
aquatic.loc[aquatic['category']=='carp', 'color'] = colors['green'] 
aquatic.loc[aquatic['category']=='tilapia', 'color'] = colors['purple'] 
aquatic.loc[aquatic['category']=='shrimp & prawns', 'color'] = colors['light_red']
aquatic.loc[aquatic['category']=='molluscs', 'color'] = '#a97c50'
aquatic.loc[aquatic['category']=='other', 'color'] = '#3c3c3c'

# Color terrestrial animals
terra.loc[terra['category']=='cattle', 'color'] = colors['red']
terra.loc[terra['category']=='chicken', 'color'] = colors['dark_green']
terra.loc[terra['category']=='swine', 'color'] = colors['blue']
terra.loc[terra['category']=='other poultry', 'color'] = colors['light_green']
terra.loc[terra['category']=='other ruminants', 'color'] = colors['light_purple']
terra.loc[terra['category']=='rodents', 'color'] = colors['pale_blue']
terra.loc[terra['category']=='equines & camelids', 'color'] = colors['dark_brown'] 

# Make the combined dataset
aq_tot = aquatic.groupby(['year']).sum().reset_index()
te_tot = terra.groupby(['year']).sum().reset_index()
aq_tot['category'] = 'aquatic'
te_tot['category'] = 'terrestrial'
aq_tot['color'] = colors['blue']
te_tot['color'] = colors['dark_brown']
tot = pd.concat([aq_tot, te_tot], sort=False)


# Save them as TSV files for voronoi maps
aq_pop = aquatic[['category', 'population']]
aq_pop.to_csv('./aquaculture_population.tsv', sep='\t', index=False)

# # Compute the fraction for each cat
# aquatic['pop_fraction'] = aquatic['population'].values / aquatic['population'].sum()
# terra['pop_fraction'] = terra['population'].values / terra['population'].sum()
# tot['pop_fraction'] = tot['population'].values / tot['population'].sum()
# aquatic['mass_fraction'] = aquatic['biomass_kg'].values / aquatic['biomass_kg'].sum()
# terra['mass_fraction'] = terra['biomass_kg'].values / terra['biomass_kg'].sum()
# tot['mass_fraction'] = tot['biomass_kg'].values / tot['biomass_kg'].sum()

# # Generate the population figures
# fig, ax = plt.subplots(1, 1, figsize=(3, 1.5))
# terra.sort_values(by=['pop_fraction'], ascending=False, inplace=True)
# aquatic.sort_values(by=['pop_fraction'], ascending=False, inplace=True)

# ax.set_yticks([0, 1, 2])
# ax.set_yticklabels(['terrestrial\nlivestock', 'aquatic\nlivestock', 'all\nlivestock'])
# ax.yaxis.set_tick_params(labelsize=6)
# ax.xaxis.set_tick_params(labelsize=6)
# ax.set_xlim([0, 1])
# ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
# ax.set_xlabel('fraction of total', fontsize=6)
# for y, ds in zip([2, 1, 0], [tot, terra, aquatic]):
#     left = 0
#     for i in range(len(ds)):
#         d = ds.iloc[i]
#         ax.barh(y, d['pop_fraction'], left=left, color=d['color'],
#                 lw=0.5, edgecolor='k')
#         left += d['pop_fraction']
# plt.savefig('../../../figures/barnyard_number/all_population_composition.svg')
# # %%
# # Generate the population figures
# fig, ax = plt.subplots(1, 1, figsize=(3, 1.5))
# terra.sort_values(by=['mass_fraction'], ascending=False, inplace=True)
# aquatic.sort_values(by=['mass_fraction'], ascending=False, inplace=True)

# ax.set_yticks([0, 1, 2])
# ax.set_yticklabels(['terrestrial\nlivestock', 'aquatic\nlivestock', 'all\nlivestock'])
# ax.yaxis.set_tick_params(labelsize=6)
# ax.xaxis.set_tick_params(labelsize=6)
# ax.set_xlim([0, 1])
# ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
# ax.set_xlabel('fraction of total', fontsize=6)
# for y, ds in zip([2, 1, 0], [tot, terra, aquatic]):
#     left = 0
#     for i in range(len(ds)):
#         d = ds.iloc[i]
#         ax.barh(y, d['mass_fraction'], left=left, color=d['color'],
#                 lw=0.5, edgecolor='k')
#         left += d['mass_fraction']
# plt.savefig('../../../figures/barnyard_number/all_biomass_composition.svg')

# # %%

# %%
