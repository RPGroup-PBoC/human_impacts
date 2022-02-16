#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the USGS nitrogen data.
data = pd.read_csv('../processed/USGS_ammonia_production_1994-2021.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data['year'], format='%Y')
proc_data['production'] = data['value']

# Generate a plot for global nitrogen production.
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='production', type='quantitative', title='Nitrogen production (Mt)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='production', type='nominal', title='Production (Mt)')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('./nitrogen_production.json')
# %%
