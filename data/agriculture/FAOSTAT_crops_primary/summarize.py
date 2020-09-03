#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load data 
data = pd.read_csv('./processed/FAOSTAT_crop_primary_quantity_harvested_area_tidy.csv')

# Compute the yields in a less elegant way
quantities = data[data['variable']=='production_quantity']
areas = data[data['variable']=='area_harvested']
quantities.rename(columns={'value':'harvested_t'}, inplace=True)
quantities.drop(column='units', inplace=True)
quantities['area_harvested_ha'] = areas['value'].values
quantities['yield_t_per_ha'] = (quantities['harvested_t'].values * 1E6) / quantities['area_harvested_ha'].values

# Sort by harvested_t
quantities.sort_values(by='harvested_t', ascending=False, inplace=True)
quantities.to_csv('./processed/FAOSTAT_crop_primary_yields.csv', index=False)
quantities.head()
# %%
# Compute average yields over 2010 - 2018 time period
recent = quantities[quantities['year'] >= 2010]
recent = recent.groupby(['product']).mean().reset_index()
recent.drop(column=['year'], inplace=True)
recent.sort_values(by='harvested_t', ascending=False, inplace=True)
recent.to_csv('./processed/2010-2018_avg_crop_yields.csv', index=False)
recent.head()

# %%
