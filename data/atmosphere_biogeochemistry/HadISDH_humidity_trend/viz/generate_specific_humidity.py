#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the HadISDH specific humidity data
data = pd.read_csv('../processed/HadISDH_specific_humidity_trend.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data[data['Reported value']=='anomaly']['year'], format='%Y')
proc_data['global mean'] = data[data['Reported value']=='anomaly']['Specific humidity anomaly (g/kg)']
proc_data['lower bound'] = (data[data['Reported value']=='low. bound combined uncertainty']['Specific humidity anomaly (g/kg)']).to_numpy()
proc_data['upper bound'] = (data[data['Reported value']=='upp. bound combined uncertainty']['Specific humidity anomaly (g/kg)']).to_numpy()
#%%

# Generate a plot for global specific humidity anomaly
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='global mean', type='quantitative', title='Global specific humidity change from the 1981-2010 mean [g/kg]', scale=alt.Scale(domain=[-0.4, 0.4])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='global mean', type='quantitative', title='global mean change [g/kg]', format='0.2f')]
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
layer.save('HadISDH_specific_humidity_trend.json')

# %%
