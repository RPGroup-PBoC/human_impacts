#%%
"""
This script accesses yearly GMSL observations and estimates as reported in
Frederikse et al. 2020 and generates a dataset of the GMSL since 1900. Original 
data are reported as difference from the mean of 2003 - 2018.
"""
import numpy as np 
import pandas as pd 

# First process the globlal observed
data = pd.read_csv('processed/Frederikse2020_observed_GMSL_timeseries.csv')

yr1900 = data[data['year']==1900]['observed_GMSL_mean'].values[0]
data['observed_GMSL_mean'] -= yr1900
data['observed_GMSL_lower'] -= yr1900
data['observed_GMSL_upper'] -= yr1900

data['units'] = 'mm difference from 1900 average'
data.to_csv('./processed/Frederikse2020_observed_GMSL_from_1900.csv', index=False)

# Process the categorization
data = pd.read_csv('./processed/Frederikse2020_contributor_GMSL_timeseries.csv')
dfs = []
for g, d in data.groupby(['source']):
    d = d.copy()
    yr1900 = d[d['year']==1900]['mean'].values[0]
    d['mean'] -= yr1900
    d['lower'] -= yr1900
    d['upper'] -= yr1900
    d['units'] = 'mm difference from 1900 average'
    dfs.append(d)

contributor_df = pd.concat(dfs, sort=False)
contributor_df.to_csv('./processed/Frederikse_contributor_GMSL_from_1900.csv', index=False)

# %%
