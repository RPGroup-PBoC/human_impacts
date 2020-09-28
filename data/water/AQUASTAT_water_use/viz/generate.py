# -*- coding: utf-8 -*-
#%%
import pandas as pd 
import altair as alt

data = pd.read_csv('../processed/AQUASTAT_global_water_use_by_sector.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')

for g, d in data.groupby(['sector']):
    chart = alt.Chart(d).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='volume_km3', type='quantitative', title='withdrawn volume [km³]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                     alt.Tooltip(field='volume_km3', type='quantitative', format='0.1f', title='volume [km³]')]
    ).properties(width=300, height=300)
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(color='dodgerblue', filled=True)
    layer = alt.layer(l, p)
    layer.save(f'{g}.json')
# %%
layer

# %%
g
# %%
