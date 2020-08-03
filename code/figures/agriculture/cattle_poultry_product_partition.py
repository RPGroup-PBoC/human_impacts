#%%
import numpy as np
import pandas as pd 
from pywaffle import Waffle

# Load in the product data. 
produced = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_product_produced/processed/FAOSTAT_livestock_and_product.csv')
produced = produced[produced['year'] >= 2010]
produced = produced.groupby(['category', 'subcategory']).agg(('mean', 'std')).reset_index()


cattle_produced = produced[produced['category']=='cattle']

fig = plt.figure(FigureClass=Waffle,
            plots={'121': {
                        'values': cattle_produced['mass_produced_Mt']['mean'].values,
                        'colors': [colors['blue'], colors['light_blue']],
                        'columns':6, 
                        'rows':6
            },
                '122': {
                        'values': cattle_produced['producing_population_Mhd']['mean'].values,
                        'colors': [colors['blue'], colors['light_blue']],
                        'columns':6,
                        'rows': 6

                }}, tight=True)

plt.savefig('../../../figures/agriculture/cattle_product_distribution.svg')
# %%
