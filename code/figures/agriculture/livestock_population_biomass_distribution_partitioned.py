#%%
import numpy as np
import pandas as pd 
from pywaffle import Waffle
import matplotlib.pyplot as plt 
import seaborn as sns
import anthro.viz
colors = anthro.viz.plotting_style()
# Load the FAOSTAT data 
livestock_pop = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_livestock_population.csv')
livestock_prod = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_product_produced/processed/FAOSTAT_livestock_and_product.csv')
feed_prod = pd.read_csv('../../../data/agriculture/alltech_global_feed_survey/processed/alltech_feed_species_breakdown.csv')

# Assign estimates for animal masses (in kg)
mass = {'ass': 50,
        'beehives': 30,
        'buffalo': 800,
        'camel': 500,
        'camelid': 100,
        'cattle': 800,
        'chicken': 3,
        'duck': 3,
        'geese and guinea fowl': 3,
        'goat': 50,
        'horse': 500,
        'mule': 50,
        'pigeon': 1,
        'swine': 200,
        'rabbit': 3,
        'rodent': 1,
        'sheep': 50,
        'turkey': 5}
cat_colors = {'chicken': colors['green'],
              'cattle': colors['blue'],
              'swine': colors['red'],
              'sheep': colors['purple'],
              'goat': colors['dark_brown'],
              'other': colors['dark_brown']}
for k, v in mass.items():
    livestock_pop.loc[livestock_pop['animal']==k, 'animal_mass_kg'] = v
    # Assign categories
    if k not in ['chicken', 'swine', 'cattle']:
        cat = 'other'
    else:
        cat = k 
    livestock_pop.loc[livestock_pop['animal']==k, 'category'] = cat
    livestock_pop.loc[livestock_pop['animal']==k, 'color'] = cat_colors[cat]

# Compute the total biomass in tonnes
livestock_pop['biomass_Mt'] = livestock_pop['population_Mhd'].values * 1E6 * livestock_pop['animal_mass_kg'] / (1E3 * 1E6)
# livestock_pop['carbon_Gt'] = livestock_pop['biomass_Mt'] * 0.18

# Group years since 2010 and compute agg properties.
agg_pop = livestock_pop[livestock_pop['year'] >= 2010].groupby(['category', 'year', 'color'])[['population_Mhd', 'biomass_Mt']].sum().reset_index()
agg_pop = agg_pop.groupby(['category', 'color'])[['population_Mhd', 'biomass_Mt']].agg(('mean', 'std')).reset_index()
agg_pop['pop_fraction'] =  agg_pop['population_Mhd']['mean'].values / agg_pop['population_Mhd']['mean'].sum()
agg_pop['mass_fraction'] =  agg_pop['biomass_Mt']['mean'].values / agg_pop['biomass_Mt']['mean'].sum()
pop_dict = {g:d['population_Mhd']['mean'].values[0] for g, d in agg_pop.groupby(['category'])}
mass_dict = {g:d['biomass_Mt']['mean'].values[0] for g, d in agg_pop.groupby(['category'])}


#%%
breakdown = {'chicken':'152', 'cattle':'153', 'swine': '154', 'other':'155'}
pop_plots = {}
mass_plots = {}
total_pop = agg_pop['population_Mhd']['mean'].values
total_mass = agg_pop['biomass_Mt']['mean'].values
pop_plots= {'151': {'rows':6, 'columns':6,
                     'values': total_pop,
                     'colors': ['#e3dcd1'] * 4,
                     'block_arranging_style':'snake',
                     'vertical': True}}
mass_plots= {'151': {'rows':6, 'columns':6,
                     'values': total_mass,
                     'colors': ['#e3dcd1'] * 4,
                     'block_arranging_style':'snake',
                     'vertical': True}}

for i, cat in enumerate(agg_pop['category'].values):
    null_colors = ['#e6e7e8'] * 4
    null_colors[i] = cat_colors[cat]
    head_dict = {'rows':6, 'columns':6,
                     'values': total_pop,
                     'colors': null_colors,
                     'block_arranging_style':'snake',
                     'vertical': True}
    mass_dict = {'rows':6, 'columns':6,
                     'values': total_mass,
                     'colors': null_colors,
                     'starting_location': 'SW',
                     'block_arranging_style':'snake',
                     'vertical':True}

    pop_plots[breakdown[cat]] = head_dict
    mass_plots[breakdown[cat]] = mass_dict

fig = plt.figure(FigureClass=Waffle, figsize=(6, 4),
                 plots=pop_plots,
                 tight=True)
plt.savefig('../../../figures/ag_livestock_population_partitioned_waffle.svg', bbox_inches='tight')
fig = plt.figure(FigureClass=Waffle, figsize=(6, 4),
                 plots=mass_plots, tight=True)
plt.savefig('../../../figures/ag_livestock_biomass_partitioned_waffle.svg', bbox_inches='tight')

