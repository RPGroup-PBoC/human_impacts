#%%
import numpy as np
import pandas as pd

data = pd.read_csv('processed/FAOSTAT_livestock_and_product.csv')
grouped = data.groupby(['subcategory']).sum().reset_index()
grouped.drop(columns=['year', 'Unnamed: 0', 'yield_kg_per_head'], inplace=True)
grouped.to_csv('./processed/FAOSTAT_aggregated_livestock_product_cumulative.csv')


# %%
