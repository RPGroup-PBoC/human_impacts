#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Load the production data. 
data = pd.read_csv('../processed/CMEMS_average_ocean_pH.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
data['pH'] = round(data['pH'], 2)
#%%

# Generate a plot for global average surface pH
chart = alt.Chart(data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='pH', type='quantitative', title='ocean pH', scale=alt.Scale(domain=[8.05, 8.15])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='pH', type='nominal', title='pH')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('surface_ocean_pH.json')

# %%
