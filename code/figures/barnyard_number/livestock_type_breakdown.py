#%% 
import numpy as np
import pandas as pd 

# Load the livestock dataset
data = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_livestock_population.csv')



# Do the categorization by hand
cattle = data[data['animal']=='cattle']
cattle['indiv_mass_kg'] = 1000
chicken = data[data['animal']=='chicken']
chicken['indiv_mass_kg'] = 3
swine = data[data['animal']=='swine']
swine['indiv_mass_kg'] = 100

#  Non-chicken poultry
poultry = data[(data['animal']=='duck') | 
               (data['animal']=='geese and guinea fowl') |
               (data['animal']=='pigeon') |
               (data['animal']=='turkey')]
poultry = poultry.groupby(['year']).sum().reset_index()
poultry['animal'] = 'other poultry'
poultry['indiv_mass_kg'] = 3

# Non-cattle ruminants
ruminants = data[(data['animal']=='sheep') | 
                 (data['animal']=='buffalo') |
                 (data['animal']=='goat')]
ruminants = ruminants.groupby(['year']).sum().reset_index()
ruminants['animal'] = 'other ruminants'
ruminants['indiv_mass_kg'] = 100

# All rodents
rodents = data[(data['animal']=='rodent') |
               (data['animal']=='rabbit')]
rodents = rodents.groupby(['year']).sum().reset_index()
rodents['animal'] = 'rodents'
rodents['indiv_mass_kg'] = 3

# horses & camel
horses  = data[(data['animal']=='horse') | 
               (data['animal']=='mule') |
               (data['animal']=='camelid') |
               (data['animal']=='ass') |
               (data['animal']=='camel') ]
horses = horses.groupby(['year']).sum().reset_index()
horses['animal'] = 'equines & camelids'
horses['indiv_mass_kg'] = 300

# Concatenate and compute the biomass
livestock_cat = pd.concat([cattle, chicken, swine, poultry, ruminants, 
                           rodents, horses], sort=False)
livestock_cat.rename(columns={'animal':'category', 
                              'population_Mhd':'population'}, 
                    inplace=True)
livestock_cat['population'] *= 1E6
livestock_cat['biomass_kg']= livestock_cat['population'].values * livestock_cat['indiv_mass_kg'].values

# Save
livestock_cat.to_csv('./livestock_categorized.csv', index=False)
# %%
