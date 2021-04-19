#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Load the ice core data. 
data = pd.read_csv('../processed/law2006_by_year_clean.csv')

# %%
# Generate a plot inferred CO2 concentrations over the last 2k years
agg_data = pd.DataFrame()
agg_data['year'] = data['year_CE']
agg_data['CO2'] = data['CO2_spline_fit']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='quantitative', title='year',
                scale=alt.Scale(domain=(1, 2004))),
            y=alt.Y(field=r'CO2', type='quantitative', title=r'Atmospheric CO2 concentration (ppm)',
                scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='year', type='quantitative', title='year'),
                     alt.Tooltip(field=r'CO2', type='nominal', title=r'[CO2] (ppm)')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('CO2_ice_cores.json')

# %%
# Generate a plot inferred CH4 concentrations over the last 2k years
agg_data = pd.DataFrame()
agg_data['year'] = data['year_CE']
agg_data['CH4'] = data['CH4_spline_fit']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='quantitative', title='year',
                scale=alt.Scale(domain=(1, 2004))),
            y=alt.Y(field=r'CH4', type='quantitative', title=r'Atmospheric CH4 concentration (ppb)',
                scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='year', type='quantitative', title='year'),
                     alt.Tooltip(field=r'CH4', type='nominal', title=r'[CH4] (ppb)')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('CH4_ice_cores.json')

# %%
# Generate a plot inferred N2O concentrations over the last 2k years
agg_data = pd.DataFrame()
agg_data['year'] = data['year_CE']
agg_data['N2O'] = data['N2O_spline_fit']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='quantitative', title='year',
                scale=alt.Scale(domain=(1, 2004))),
            y=alt.Y(field=r'N2O', type='quantitative', title=r'Atmospheric N2O concentration (ppb)',
                scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='year', type='quantitative', title='year'),
                     alt.Tooltip(field=r'N2O', type='nominal', title=r'[N2O] (ppb)')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('N2O_ice_cores.json')
