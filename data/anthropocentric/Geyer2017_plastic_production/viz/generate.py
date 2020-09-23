#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Load the produciton data. 
data = pd.read_csv('../processed/Geyer2017_plastic_production.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')

chart = alt.Chart(data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='resin_production_Mt', type='quantitative',
                    title='plastic resin produced [Mt]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', timeUnit='year', title='year'),
                     alt.Tooltip(field='resin_production_Mt', type='quantitative',
                                 title='produced mass [Mt]')]
            ).properties(
            width="container",
            height=300
            )

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)

layer = alt.layer(l, p)
layer.save('platic_production.json')
# %%

# %%
