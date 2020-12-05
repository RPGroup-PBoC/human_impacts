#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Load the production data. 
# Generate a plot for net natural sinks
data = pd.read_csv('../processed/global_carbon_budget_processed.csv')
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

agg_data = pd.DataFrame()
agg_data['year'] = (data[data['Sink/source type']=='natural sink'])[data['Units']=='Pg CO2 yr-1']['Year']
agg_data['net sink'] = (data[data['Sink/source type']=='natural sink'])[data['Units']=='Pg CO2 yr-1']['Value']
agg_data['land-use change emissions'] = (data[data['Sink/source type']==
    'land-use change emissions'])[data['Units']=='Pg CO2 yr-1']['Value']
#%%

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'net sink', type='quantitative', title=r'Net sink (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'net sink', type='nominal', title=r'net sink')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('natural_CO2_sink.json')


# %%
# Generate a plot for land-use change emissions
agg_data = pd.DataFrame()
agg_data['year'] = (data[data['Sink/source type']=='land-use change emissions'])[data['Units']=='Pg CO2 yr-1']['Year']
agg_data['land-use change emissions'] = (data[data['Sink/source type']==
    'land-use change emissions'])[data['Units']=='Pg CO2 yr-1']['Value']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'land-use change emissions', type='quantitative', title=r'Land-use change emissions (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'land-use change emissions', type='nominal', title=r'land-use change emissions')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('land_use_CO2_source.json')

# %%
# Generate a plot for fossil fuel emissions
agg_data = pd.DataFrame()
agg_data['year'] = (data[data['Sink/source type']=='fossil fuel and industry'])[data['Units']=='Pg CO2 yr-1']['Year']
agg_data['fossil fuels'] = (data[data['Sink/source type']==
    'fossil fuel and industry'])[data['Units']=='Pg CO2 yr-1']['Value']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'fossil fuels', type='quantitative', title=r'Fossil fuel emissions (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'fossil fuels', type='nominal', title=r'fossil fuels')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('fossil_fuels_CO2_source.json')

# %%
# Generate a plot for atmospheric CO2 growth rate
agg_data = pd.DataFrame()
agg_data['year'] = (data[data['Sink/source type']=='atmospheric growth'])[data['Units']=='Pg CO2 yr-1']['Year']
agg_data['atmospheric growth'] = (data[data['Sink/source type']==
    'atmospheric growth'])[data['Units']=='Pg CO2 yr-1']['Value']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'atmospheric growth', type='quantitative', title=r'Atmospheric [CO2] growth (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'atmospheric growth', type='nominal', title=r'atmospheric growth')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('atmos_growth_CO2_source.json')

# %%