#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the NOAA NCEI data.
data = pd.read_csv('../processed/NOAA_NCEI_global_ocean_temperature.csv')
data = data[data['Layer']=='0-700 m']
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data[data['Reported value']=='global mean']['Year'], format='%Y')
proc_data['global mean'] = data[data['Reported value']=='global mean']['Temperature anomaly (K)']
proc_data['lower bound'] = (data[data['Reported value']=='global mean']['Temperature anomaly (K)'] - 
                            data[data['Reported value']=='95% CI']['Temperature anomaly (K)'].to_numpy())
proc_data['upper bound'] = (data[data['Reported value']=='global mean']['Temperature anomaly (K)'] + 
                            data[data['Reported value']=='95% CI']['Temperature anomaly (K)'].to_numpy())
#%%

# Generate a plot for global mean surface temperature
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='global mean', type='quantitative', title='0-700 m temperature change from 1958-1962 mean [°C]', scale=alt.Scale(domain=[-0.05, 0.25])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='global mean', type='quantitative', title='global mean change [°C]', format='0.2f')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='darkorange', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y='lower bound:Q',
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='darkorange')
p = chart.mark_point(color='darkorange', filled=True)
layer = alt.layer(bands, l, p)
layer.save('NOAA_NCEI_global_700m_temp.json')
# %%
