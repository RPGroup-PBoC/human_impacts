#%%
"""
This script computes the total global water use by sector by summing over 
country-level data reported by AQUASTAT
"""
# %%
import pandas as pd
data = pd.read_csv('./processed/AQUASTAT_water_use_by_country.csv')
grouped = data.groupby(['sector', 'year']).sum().reset_index()
grouped
# Truncate data from 1970 onward
# grouped = grouped[grouped['year'] >= 1970]

# Rename to cubic kilometers 
# grouped.rename(columns={'withdrawal_billion_m3':'volume_km3'}, inplace=True)
# grouped.to_csv('./processed/AQUASTAT_global_water_use_by_sector.csv', index=False)

# %%
data.head()
# %%
