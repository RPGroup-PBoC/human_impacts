#%%
import numpy as np
import pandas as pd
import altair as alt

# Load the NOAAGlobalTempv5 data.
data = pd.read_csv('../processed/GISTEMPv4_global_surf_temperature_trend.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data[data['Reported value']=='global mean']['Year'], format='%Y')
proc_data['global mean'] = data[data['Reported value']=='global mean']['Temperature anomaly (K)']
proc_data['lower bound'] = data[data['Reported value']=='low. bound, 95% CI bias unc.']['Temperature anomaly (K)'].to_numpy()
proc_data['upper bound'] = data[data['Reported value']=='upp. bound, 95% CI bias unc.']['Temperature anomaly (K)'].to_numpy()

# Generate a plot for global mean surface temperature
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='global mean', type='quantitative', title='Global surface temperature change (°C)', scale=alt.Scale(domain=[-0.5, 1.4])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='global mean', type='nominal', title='global mean')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = alt.Chart(proc_data).mark_area(color='darkorange', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y='lower bound:Q',
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='darkorange')
p = chart.mark_point(color='darkorange', filled=True)
layer = alt.layer(l, p, bands) #.resolve_scale(y='shared')
layer.save('surface_temp.json')
# %%
