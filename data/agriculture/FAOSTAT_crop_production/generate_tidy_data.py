#%%
import numpy as np
import pandas as pd

# Load the source data
crop_source = pd.read_csv('source/FAOSTAT_crop_totals_production.csv')
crop_source.head()

# %%
crop_source['crop'].unique()


# %%
