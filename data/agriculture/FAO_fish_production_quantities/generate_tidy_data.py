#%%
import pandas as pd

# load the source data and remove FAO totals for re calculation
data = pd.read_csv('./source/FAO_FishStatJ_production_quantities.csv')
data = data[~data['Country (Name)'].str.contains('Totals')]
data = data[~data['Country (Name)'].str.contains('FAO.')]

# Rename id vars
data.rename(columns={'Country (Name)': 'country', 
                     'ASFIS species (Name)':'species', 
                     'FAO major fishing area (Name)': 'fishing_area', 
                     'Detailed production source (Name)':'source',
                     'Unit (Name)':'unit'}, inplace=True)
# Melt on the year
longform = data.melt(id_vars=['country', 'species', 'fishing_area', 'source', 'unit'])
longform = longform[~longform['variable'].str.contains('S')]

# Rename the year values. 
longform['year'] = [int(f'{s[1:-1]}') for s in longform['variable'].values]
# Fix odd naming in some species
species = [s.replace('[', '') for s in longform['species'].values]
longform['species'] = [s.replace(']', '') for s in species]

# Rename the sources 
longform.loc[longform['source'].str.contains('Aquaculture'), 'source'] = 'cultured'
longform.loc[longform['source'].str.contains('Capture'), 'source'] = 'captured'

# Drop unnecessary columns, nans, and zeros
longform.drop(columns=['variable', 'unit'], inplace=True)
longform.dropna(inplace=True)
longform.rename(columns={'value':'produced_mass_t'}, inplace=True)
longform = longform[longform['produced_mass_t'] != 0]

# save the longform output
longform.to_csv('./processed/FAO_FishStatJ_production_quantities_species_country.csv', index=False)

# %%
# Compute the aggregate totals by species
species_totals = longform.groupby(['species', 'source', 'year']
                                 )['produced_mass_t'].sum().reset_index()
species_totals.sort_values(['produced_mass_t'], ascending=False, inplace=True)
species_totals.to_csv('./processed/FAO_FishStatJ_total_mass_species.csv', index=False)

# %%
# Compute the aggregate totals by source
source_totals = species_totals.groupby(['source', 'year']   
                                      )['produced_mass_t'].sum().reset_index()
total = species_totals.groupby(['year']
                             )['produced_mass_t'].sum().reset_index()
total['source'] = 'total'
merged = pd.concat([source_totals, total], sort=False)
merged.to_csv('./processed/FAO_FishStatJ_total_mass_source.csv', index=False)
merged
# %%
