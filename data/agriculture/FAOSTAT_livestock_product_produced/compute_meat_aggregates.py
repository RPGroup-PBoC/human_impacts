#%%
import numpy as np
import pandas as pd

data = pd.read_csv('processed/FAOSTAT_aggregated_livestock_product_categorized.csv')

data = data[~data['product'].str.contains('indigenous')]
data = data[data['category']=='meat']
data = data.groupby(['year', 'category'])['producing_population_Mhd']


# %%
