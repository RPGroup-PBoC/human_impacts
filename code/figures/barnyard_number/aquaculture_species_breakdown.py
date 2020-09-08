#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz 
import anthro.io
from pywaffle import Waffle
colors = anthro.viz.plotting_style()
data = pd.read_csv('../../../data/agriculture/FAO_fish_production_quantities/processed/FAO_FishStatJ_total_mass_species.csv')

# Restrict to most recent year and seaprate by catch type
data = data[data['year']==2018] 
culture = data[data['source']=='cultured']
culture.sort_values(by='produced_mass_t', ascending=False, inplace=True)

# Do manual categorization

# Carps
_carp = culture[culture['species'].str.contains(' carp') & 
               ~culture['species'].str.contains('carpet')]
carp_species = _carp['species'].values
carp = pd.DataFrame([_carp['produced_mass_t'].sum() * 1E3], columns=['produced_mass_kg'])
carp['category'] = 'carp'
carp['approx_indiv_mass_kg'] = 3
carp['approx_res_time_yr'] = 0.7 
carp['approx_standing_population'] = carp['approx_res_time_yr'].values * carp['produced_mass_kg'].values\
                            / carp['approx_indiv_mass_kg'].values
carp['approx_standing_biomass_kg'] = carp['approx_standing_population'].values * carp['approx_indiv_mass_kg']


# Tilapia
_tilapia = culture[culture['species'].str.contains('tilapia')]
tilapia_species = _tilapia['species'].values
tilapia = pd.DataFrame([_tilapia['produced_mass_t'].sum() * 1E3], columns=['produced_mass_kg'])
tilapia['category'] = 'tilapia'
tilapia['approx_indiv_mass_kg'] = 2
tilapia['approx_res_time_yr'] = 0.7 
tilapia['approx_standing_population'] = tilapia['approx_res_time_yr'].values * tilapia['produced_mass_kg'].values\
                            / tilapia['approx_indiv_mass_kg'].values
tilapia['approx_standing_biomass_kg'] = tilapia['approx_standing_population'].values * tilapia['approx_indiv_mass_kg']



# Shrimp and prawns
_shrimp = culture[culture['species'].str.contains('shrimp') | 
                 culture['species'].str.contains('prawn')]
shrimp_species = _shrimp['species'].values
shrimp = pd.DataFrame([_shrimp['produced_mass_t'].sum() * 1E3], columns=['produced_mass_kg'])
shrimp['category'] = 'shrimp & prawns'
shrimp['approx_indiv_mass_kg'] = 0.05 
shrimp['approx_res_time_yr'] = 0.5
shrimp['approx_standing_population'] = shrimp['approx_res_time_yr'].values * shrimp['produced_mass_kg'].values\
                            / shrimp['approx_indiv_mass_kg'].values
shrimp['approx_standing_biomass_kg'] = shrimp['approx_standing_population'].values * shrimp['approx_indiv_mass_kg']

shrimp

_shells = culture[culture['species'].str.contains('clam') | 
                 culture['species'].str.contains('carpet') | 
                 culture['species'].str.contains('mussel') |
                 culture['species'].str.contains('cupped') | 
                 culture['species'].str.contains('abalone') |
                 culture['species'].str.contains('scallop') |
                 culture['species'].str.contains('oyster')]
shell_species = _shells['species'].values
shells = pd.DataFrame([_shells['produced_mass_t'].sum() * 1E3], columns=['produced_mass_kg'])
shells['category'] = 'shells'
shells['approx_indiv_mass_kg'] = 0.1
shells['approx_res_time_yr'] = 2 
shells['approx_standing_population'] = shells['approx_res_time_yr'].values * shells['produced_mass_kg'].values\
                            / shells['approx_indiv_mass_kg'].values
shells['approx_standing_biomass_kg'] = shells['approx_standing_population'].values * shells['approx_indiv_mass_kg']

# Concatenate these 
categorized = pd.concat([carp, tilapia, shrimp, shells], sort=False)
cat_species =  list(np.concatenate([carp_species, tilapia_species, shrimp_species, shell_species]))
_others = culture[~culture['species'].isin(cat_species)]
other = pd.DataFrame([_others['produced_mass_t'].sum() * 1E3], columns=['produced_mass_kg'])
other['category'] = 'other'
other['approx_indiv_mass_kg'] = 3 
other['approx_res_time_yr'] = 1
other['approx_standing_population'] = other['approx_res_time_yr'].values * other['produced_mass_kg'].values\
                                    / other['approx_indiv_mass_kg'].values
other['approx_standing_biomass_kg'] = other['approx_standing_population'].values * other['approx_indiv_mass_kg'].values

# Merge everything. 
categorized = pd.concat([categorized, other], sort=False)
categorized
# #%%
# # Assign approximate masses to the top 5 types of farmed seafood
# mass_maturation = {'Grass carp(=White amur)': (3, 0.8),
#             'Cupped Oysters nei': (0.1, 2),
#             'Whiteleg shrimp': (0.05, 0.5),
#             'Silver carp': (10, 0.8),
#             'Nile tilapia': (2, 1),
#             'Common carp': (5, 1),
#             'Japanese carpet shell': (0.1, 3),
#             'Bighead carp': (20,  1)}

# for k, v in mass_maturation.items():
#     culture.loc[culture['species']==k, 'mass'] = v[0]
#     culture.loc[culture['species']==k, 'lifecycle_yr'] = v[1] 

# names = {'Grass carp(=White amur)': 'Grass Carp',
#           'Cupped Oysters nei': 'Cuppedn Oysters',
#           'Whiteleg shrimp': 'Whiteleg Shrimp',
#           'Silver carp': 'Silver Carp',
#           'Nile tilapia': 'Nile Tilapia',
#           'Common carp':  'Common Carp',
#           'Japanese carpet shell': 'Manila Clam',
#           'Bighead carp': 'Bighead Carp'}
 
# for k, v in names.items():
#     culture.loc[culture['species']==k, 'name'] = v
# others = culture[culture['name'].isnull()].copy()
# others = others.groupby(['year']).sum().reset_index()
# others['name'] = 'other'
# others['mass'] = 3
# others['lifecycle_yr'] = 1
# culture.dropna(inplace=True)
# culture.drop(columns=['source', 'species'], inplace=True)
# culture.sort_values(by='produced_mass_t')
# merged = pd.concat([culture, others], sort=False)
# merged['population'] = (merged['produced_mass_t'].values * 1E3 / merged['mass'].values) * merged['lifecycle_yr'].values
# merged['mass_bkg'] = merged['produced_mass_t'].values * 1E-6
# merged['pop_bhd'] = merged['population'].values / 1E9
# merged.sort_values(by='pop_bhd', inplace=True, ascending=False)
# merged['position'] = np.array([0, 1, 7, 2, 3, 4, 5, 6])
# merged.sort_values(by=['position'], inplace=True)

# #%%
# # Set up the lollipop plot
# fig, ax = plt.subplots(1,1, figsize=(3, 1.5))
# # ax.set_yscale('log')
# ax.xaxis.set_tick_params(labelsize=6)
# ax.yaxis.set_tick_params(labelsize=6)
# ax.plot(merged['position'], merged['pop_bhd'], 'o', ms=3, color=colors['blue'])
# ax.vlines(merged['position'], 0, merged['pop_bhd'], lw=1, color=colors['blue'])
# ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7])
# ax.set_xticklabels(merged['name'].values, fontsize=6, rotation=90)
# ax.set_ylabel('estimated processed\npopulation [billions]', fontsize=6)
# plt.savefig('../../../figures/estimated_population.svg')
# #%%
# # %%

# %%
