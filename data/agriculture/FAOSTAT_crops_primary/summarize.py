#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load the data 
data = pd.read_csv('processed/FAOSTAT_crop_primary_quantity_harvested_area_tidy.csv')
# Drop nas
data.dropna(inplace=True)

# Restrict to only years 2010-2018
data = data[data['year'] > 2010]

quantities = data[data['variable']=='production_quantity']
areas = data[data['variable']=='area_harvested']

# Convert areas to m^2

# Compute the summaries for individual crops and sort by produced quantity. 
prod_quants = quantities.groupby(['product'])['value'].agg(('mean', 'std')).reset_index()

area_quants = areas.groupby(['product'])['value'].agg(('mean', 'std')).reset_index()
prod_quants.sort_values(by='mean', ascending=False, inplace=True)
area_quants.sort_values(by='mean', ascending=False, inplace=True)
area_quants['frac'] = area_quants['mean'].values / area_quants['mean'].sum()

# %%
areas['value'] *= 1E4 # to m^2
areas.groupby(['year']).sum().reset_index().agg(('mean', 'std'))

# %%
