#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

colors = anthro.viz.plotting_style()

# Load the data 
data = pd.read_csv('./processed/AQUASTAT_water_use_by_country.csv')

# First consider just the total. 
totals = data[data['sector']=='total']
totals.country.unique()
usa = totals[totals['country']=='United States of America']
len(usa)

# %%
plt.plot(usa['year'], usa['cubic_m_yr'], '-o')

# %%
