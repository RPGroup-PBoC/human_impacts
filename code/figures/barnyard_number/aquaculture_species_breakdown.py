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
culture = data[data['source']=='cultured']

# Do manual categorization
dfs = []
for g, d in culture.groupby(['year']):
    _carp = d[d['species'].str.contains(' carp') & 
                   ~d['species'].str.contains('carpet')]
    carp_species = _carp['species'].values
    carp = pd.DataFrame([_carp['produced_mass_t'].sum() * 1E3], columns=['produced_mass_kg'])
    carp['category'] = 'carp'
    carp['approx_indiv_mass_kg'] = 3
    carp['approx_res_time_yr'] = 0.7 
    carp['approx_standing_population'] = carp['approx_res_time_yr'].values * carp['produced_mass_kg'].values\
                                / carp['approx_indiv_mass_kg'].values
    carp['approx_standing_biomass_kg'] = carp['approx_standing_population'].values * carp['approx_indiv_mass_kg']
    
    
    # Tilapia
    _tilapia = d[d['species'].str.contains('tilapia')]
    tilapia_species = _tilapia['species'].values
    tilapia = pd.DataFrame([_tilapia['produced_mass_t'].sum() * 1E3], columns=['produced_mass_kg'])
    tilapia['category'] = 'tilapia'
    tilapia['approx_indiv_mass_kg'] = 2
    tilapia['approx_res_time_yr'] = 0.7 
    tilapia['approx_standing_population'] = tilapia['approx_res_time_yr'].values * tilapia['produced_mass_kg'].values\
                                / tilapia['approx_indiv_mass_kg'].values
    tilapia['approx_standing_biomass_kg'] = tilapia['approx_standing_population'].values * tilapia['approx_indiv_mass_kg']
    
    
    
    # Shrimp and prawns
    _shrimp = d[d['species'].str.contains('shrimp') | 
                     d['species'].str.contains('prawn')]
    shrimp_species = _shrimp['species'].values
    shrimp = pd.DataFrame([_shrimp['produced_mass_t'].sum() * 1E3], columns=['produced_mass_kg'])
    shrimp['category'] = 'shrimp & prawns'
    shrimp['approx_indiv_mass_kg'] = 0.05 
    shrimp['approx_res_time_yr'] = 0.5
    shrimp['approx_standing_population'] = shrimp['approx_res_time_yr'].values * shrimp['produced_mass_kg'].values\
                                / shrimp['approx_indiv_mass_kg'].values
    shrimp['approx_standing_biomass_kg'] = shrimp['approx_standing_population'].values * shrimp['approx_indiv_mass_kg']
    
    shrimp
    
    _shells = d[d['species'].str.contains('clam') | 
                     d['species'].str.contains('carpet') | 
                     d['species'].str.contains('mussel') |
                     d['species'].str.contains('cupped') | 
                     d['species'].str.contains('abalone') |
                     d['species'].str.contains('scallop') |
                     d['species'].str.contains('oyster')]
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
    _others = d[~d['species'].isin(cat_species)]
    other = pd.DataFrame([_others['produced_mass_t'].sum() * 1E3], columns=['produced_mass_kg'])
    other['category'] = 'other'
    other['approx_indiv_mass_kg'] = 3 
    other['approx_res_time_yr'] = 1
    other['approx_standing_population'] = other['approx_res_time_yr'].values * other['produced_mass_kg'].values\
                                        / other['approx_indiv_mass_kg'].values
    other['approx_standing_biomass_kg'] = other['approx_standing_population'].values * other['approx_indiv_mass_kg'].values
    
    # Merge everything. 
    categorized = pd.concat([categorized, other], sort=False)
    categorized['year'] = g
    dfs.append(categorized)
categorized = pd.concat(dfs, sort=False)
categorized.to_csv('./aquaculture_categorized.csv', index=False)



# %%
