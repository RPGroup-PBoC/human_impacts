#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot for the albedo anomaly for the 1998-2017 period
data = pd.read_csv('../processed/earthshine_data.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
agg_data = pd.DataFrame()
agg_data['year'] = (data[data['Reported quantity']=='Measured value'])['year']
agg_data['Albedo anomaly'] = (data[data['Reported quantity']=='Measured value'])['Albedo anomaly (W/m2)']

agg_data['lower bound'] = data[data['Reported quantity']=='Lower error margin']['Albedo anomaly (W/m2)'].to_numpy()
agg_data['upper bound'] = data[data['Reported quantity']=='Upper error margin']['Albedo anomaly (W/m2)'].to_numpy()

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'Albedo anomaly', type='quantitative', title=r'Albedo anomaly (W/m2)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'Albedo anomaly', type='nominal', title=r'Albedo anomaly')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y='lower bound:Q',
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('albedo_anomaly.json')

