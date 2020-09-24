#%%
import pandas as pd 
import altair as alt 
import anthro.io 

# Load the data 
data = pd.read_csv('../processed/FAOSTAT_livestock_population.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')

# Restrict it to just cattle, chicken, sheep, and pigs
# data = data[data['animal'].isin([])]
# %%
