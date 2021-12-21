#%%
import pandas as pd 
data = pd.read_csv('../processed/Tuholske2021_TableS5_N_input_by_country.csv')
# %%
# Compute the totals
tot = data.groupby(['wastewater_type']).sum().reset_index()
tot.to_csv('../processed/Tuholske2021_TableS5_N_input_global.csv', index=False)

# %%
