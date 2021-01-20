#%%
import pandas as pd 
import altair as alt 
import anthro.io 
data = pd.read_csv('../processed/FAOSTAT_nitrogen_production_consumption.csv')

# Separate by production and consumption 
data['year'] = pd.to_datetime(data['year'].values, format='%Y')

# compute value in SI units. 
data['mass_nitrogen_grams'] = data['mass_nitrogen'].values * 1E6

# Apply useful numeric formatting
data['label'] = anthro.io.numeric_formatter(data['mass_nitrogen_grams'].values, 
                                            unit='g', sci=True)
data
# %%
data


# %%
