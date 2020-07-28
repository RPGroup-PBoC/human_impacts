#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load the livestock production data
production = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_product_produced/processed/FAOSTAT_livestock_and_product.csv')
population = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_livestock_population.csv')

# Find the past eight years
production = production[(production['year'] >= 2010) & ((production['category']=='cattle') | (production['category']=='poultry'))] 
prod_total = production.groupby(['category', 'year']).sum().reset_index()
prod_total = prod_total.groupby(['category']).agg(('mean', 'sem')).reset_index()
prod_agg = production.groupby(['category', 'subcategory']).agg(('mean', 'std')).reset_index()

fig, ax = plt.subplots(1, 2)
mass_values = prod_agg[prod_agg['category']=='cattle']['mass_produced_Mt']
head_values = prod_agg[prod_agg['category']=='cattle']['producing_population_Mhd']
ax[0].pie(mass_values['mean'].values,
               colors=[colors['blue'], colors['light_blue']])
mask = plt.Circle((0, 0), 0.7, color='white')
ax[0].add_artist(mask)

ax[1].pie(head_values['mean'].values,
            colors=[colors['blue'], colors['light_blue']])

mask = plt.Circle((0, 0), 0.7, color='white')
ax[1].add_artist(mask)
plt.savefig('../../../figures/cattle_product_breakdown.svg', bbox_inches='tight')


# %%

fig, ax = plt.subplots(1, 2)
mass_values = prod_agg[prod_agg['category']=='poultry']['mass_produced_Mt']
head_values = prod_agg[prod_agg['category']=='poultry']['producing_population_Mhd']
ax[0].pie(mass_values['mean'].values,
               colors=[colors['green'], colors['light_green']])
mask = plt.Circle((0, 0), 0.7, color='white')
ax[0].add_artist(mask)
ax[1].pie(head_values['mean'].values, colors=[colors['green'], colors['light_green']])
mask = plt.Circle((0, 0), 0.7, color='white')
ax[1].add_artist(mask)
plt.savefig('../../../figures/chicken_product_breakdown.svg', bbox_inches='tight')



# %%
