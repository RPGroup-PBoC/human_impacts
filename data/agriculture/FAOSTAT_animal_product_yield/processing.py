# %%
import pandas as pd
src = pd.read_csv('source/FAOSTAT_animal_production_yield.csv')

# Remove units that aren't mass
src = src[src['Unit'].str.contains('g')]

# Convert yield to standard units
src.loc[src['Unit'] == '100mg/An',
        'yield_kg_per_head'] = src.loc[src['Unit'] == '100mg/An', 'Value'] / 1E4
src.loc[src['Unit'] == '0.1g/An',
        'yield_kg_per_head'] = src.loc[src['Unit'] == '0.1g/An', 'Value'] / 1E4
src.loc[src['Unit'] == 'hg/An',
        'yield_kg_per_head'] = src.loc[src['Unit'] == 'hg/An', 'Value'] / 10
# %%
src = src[['Item', 'Year', 'yield_kg_per_head']]

# Assign products
src.loc[src['Item'].str.contains('eggs'), 'product'] = 'eggs'
src.loc[src['Item'].str.contains('Meat'), 'product'] = 'meat'
src.loc[src['Item'].str.contains('milk'), 'product'] = 'milk'

# Assign animals
src.loc[src['Item'].str.contains('Hen') | src['Item'].str.contains(
    'chickens'), 'animal'] = 'chicken'
src.loc[src['Item'].str.contains('pig'), 'animal'] = 'pig'
src.loc[src['Item'].str.contains('camels'), 'animal'] = 'camel'
src.loc[src['Item'].str.contains('goat'), 'animal'] = 'goat'
src.loc[src['Item'].str.contains('turkeys'), 'animal'] = 'turkey'
src.loc[src['Item'].str.contains('sheep'), 'animal'] = 'sheep'
src.loc[src['Item'].str.contains('cattle'), 'animal'] = 'cow'

src.drop(columns=['Item'], inplace=True)
src.to_csv('./processed/FAOSTAT_animal_product_yield.csv', index=False)
