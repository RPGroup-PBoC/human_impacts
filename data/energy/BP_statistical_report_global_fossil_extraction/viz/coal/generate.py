#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the BP coal production data.
data = pd.read_csv('../../processed/BP_global_coal_production_1981-2019.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data['year'], format='%Y')
proc_data['production (kg)'] = data['production_kg']
proc_data['label'] = data['production_kg'].values

# Generate a plot for global coal production.
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='production (kg)', type='quantitative', title='Mass of coal [kg]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='label', type='nominal', title='production mass')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('./coal_production.json')
# %%
