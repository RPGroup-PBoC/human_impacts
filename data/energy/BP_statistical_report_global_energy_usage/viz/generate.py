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

# Renewable trends
data = pd.read_csv('../processed/bp_renewables_plus_hydro.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
data['consumption_TW'] = data['consumption_EJ_yr'].values*1e6 / (365*24*3600.0)
data['consumption'] = anthro.io.numeric_formatter(data['consumption_TW'] * 1E12, sci=True, unit='W')


chart = alt.Chart(data).encode(
        x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
        y=alt.Y(field='consumption_TW',  type='quantitative', title=f'Renewable power consumption [TW]'),
        tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                alt.Tooltip(field='consumption', type='nominal')]
        ).properties(
            width="container",
            height=300
        )

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('renewables_consumption.json')