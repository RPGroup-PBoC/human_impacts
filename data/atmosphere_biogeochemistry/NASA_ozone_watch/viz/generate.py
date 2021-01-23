#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the Ozone hole data.
full_data = pd.read_csv('../processed/NASA_ozone_hole_evolution_SH_spring.csv')
data = full_data[full_data['Variable'] == 'Ozone hole area'].copy()
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data[data['Reported value']=='Mean']['Year'], format='%Y')
proc_data['mean'] = data[data['Reported value']=='Mean']['Value']
proc_data['minimum'] = (data[data['Reported value']=='Minimum']['Value']).to_numpy()
proc_data['maximum'] = (data[data['Reported value']=='Maximum']['Value']).to_numpy()
#%%

# Generate a plot for ozone hole area
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='mean', type='quantitative', title='Ozone hole area, Southern Hemisphere spring [Millions of km2]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='mean', type='quantitative', title='ozone hole area', format='0.2f')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y='minimum:Q',
            y2='maximum:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('ozone_hole_area.json')

# %%
data = full_data[full_data['Variable'] == 'Ozone minimum'].copy()
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data[data['Reported value']=='Mean']['Year'], format='%Y')
proc_data['mean'] = data[data['Reported value']=='Mean']['Value']
proc_data['minimum'] = (data[data['Reported value']=='Minimum']['Value']).to_numpy()
proc_data['maximum'] = (data[data['Reported value']=='Maximum']['Value']).to_numpy()
#%%

# Generate a plot for ozone minimum of ozone hole
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='mean', type='quantitative', title='Ozone minimum, Southern Hemisphere spring [DU]',
                scale=alt.Scale(domain=[60, 250])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='mean', type='quantitative', title='ozone minimum', format='0.2f')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y('minimum:Q', scale=alt.Scale(zero=False)),
            y2='maximum:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('ozone_hole_minimum.json')
