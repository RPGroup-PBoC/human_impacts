"""
This file reads in the original data set, converts it to long-form tidy format
and saves it in same directory as the original with the suffix `_tidy.csv`
"""
#%%
import pandas as pd

# Read in the raw data. 
raw_data = pd.read_csv('../gapminder_world_population_1800-2100_raw.csv')

# Melt on country to get into longform. 
tidy_data = raw_data.melt('country')

# Rename the columns to make sense.
tidy_data.rename(columns={'variable':'year', 'value':'population'}, inplace=True)

# Save the tidy format to disk. 
tidy_data.to_csv('../gapminder_world_population_1800-2100_tidy.csv', index=False)


# %%
