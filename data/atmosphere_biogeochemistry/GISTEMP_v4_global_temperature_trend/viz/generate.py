#%%
import numpy as np
import pandas as pd
import altair as alt

# Load the NOAAGlobalTempv5 data.
data = pd.read_csv('../processed/GISTEMPv4_global_surf_temperature_trend_1880-2020.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data[data['Reported value']=='global mean']['Year'], format='%Y')
proc_data['global mean'] = data[data['Reported value']=='global mean']['Temperature anomaly (K)']
proc_data['lower bound'] = data[data['Reported value']=='low. bound, 95% CI bias unc.']['Temperature anomaly (K)'].to_numpy()
proc_data['upper bound'] = data[data['Reported value']=='upp. bound, 95% CI bias unc.']['Temperature anomaly (K)'].to_numpy()

# Generate a plot for global mean surface temperature
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='global mean', type='quantitative', title='Global surface temperature change from the 1850-1900 mean [°C]', scale=alt.Scale(domain=[-0.5, 1.4])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='global mean', type='quantitative', title='global mean change [°C]', format='0.2f')]
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
layer.save('surface_temp.json')
# %%
