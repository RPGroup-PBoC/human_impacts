#%%
import numpy as np
import pandas as pd

data = pd.read_csv('processed/FAOSTAT_aggregated_livestock_product_categorized.csv')
data = data[~data['product'].str.contains('indigenous')]
grouped = data.groupby(['product']).sum().reset_index()
grouped.drop(columns=['year'])
grouped.to_csv('processed/FAOSTAT_aggregated_livestock_product_cumulative.csv')


# %%
grouped

# %%
