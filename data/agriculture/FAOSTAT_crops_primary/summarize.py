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
quantities['area_harvested_ha'] = areas['value'].values
quantities['yield_t_per_ha'] = (quantities['harvested_t'].values * 1E6) / quantities['area_harvested_ha'].values

# Sort by harvested_t
quantities.to_csv('./processed/FAOSTAT_crop_primary_yields.csv')
# %%
