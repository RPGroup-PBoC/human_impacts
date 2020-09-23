#%%
import numpy as np
import pandas as pd 
import altair as alt
import anthro.io

# Load the data 
data = pd.read_csv('../processed/BP_global_energy_usage_by_type.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
data['consumption_GW'] = data['consumption_TW'].values * 1E3
data['consumption'] = anthro.io.numeric_formatter(data['consumption_TW'] * 1E12, sci=True, unit='W')
for g, d in data.groupby(['type']):
    if (g == 'Natural Gas') | (g=='Oil') | (g=='Coal') | (g=='Hydroelectric'):
        d['consumption_GW'] *= 1E-3
        title = 'TW'
    else:
        title = 'GW'

    chart = alt.Chart(d).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='consumption_GW',  type='quantitative', title=f'power consumption [{title}]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                    alt.Tooltip(field='consumption', type='nominal')]
            ).properties(
                width="container",
                height=300
            )

    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(color='dodgerblue', filled=True)
    layer = alt.layer(l, p)
    if g.lower()=='biodiesel/biogasoline':
        g = 'biogas'
    if g.lower()=='geothermal/biomass/other':
        g = 'other'
    layer.save(f'./{g.lower()}.json')
# %%
