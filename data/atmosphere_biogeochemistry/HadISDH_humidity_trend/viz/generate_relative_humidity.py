#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the HadISDH relative humidity data
data = pd.read_csv('../processed/HadISDH_relative_humidity_trend.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data[data['Reported value']=='anomaly']['year'], format='%Y')
proc_data['global mean'] = data[data['Reported value']=='anomaly']['Relative humidity anomaly (%)']
proc_data['lower bound'] = (data[data['Reported value']=='low. bound combined uncertainty']['Relative humidity anomaly (%)']).to_numpy()
proc_data['upper bound'] = (data[data['Reported value']=='upp. bound combined uncertainty']['Relative humidity anomaly (%)']).to_numpy()
#%%

# Generate a plot for global relative humidity anomaly
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='global mean', type='quantitative', title='Global relative humidity change from the 1981-2010 mean [%]', scale=alt.Scale(domain=[-1.0, 0.6])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='global mean', type='quantitative', title='global mean change [%]', format='0.2f')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y='lower bound:Q',
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p) #.resolve_scale(y='shared')
layer.save('HadISDH_relative_humidity_trend.json')

# %%
