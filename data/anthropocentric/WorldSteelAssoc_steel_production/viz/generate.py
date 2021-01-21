#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the USGS steel data.
data = pd.read_csv('../processed/WorldSteelAssoc_steel_production_1950-2019.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data['year'], format='%Y')
proc_data['production (kg)'] = data['value']
proc_data['label'] = anthro.io.numeric_formatter(data['value'].values * 1E3, unit='kg')

# Generate a plot for global steel production.
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='production (kg)', type='quantitative', title='Mass of steel [kg]', scale=alt.Scale(domain=[100000000000, 2000000000000])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='label', type='nominal', title='production mass')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('./steel_production.json')
# %%
