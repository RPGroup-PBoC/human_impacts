#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the NOAAGlobalTempv5 data.
data = pd.read_csv('../processed/NOAAGlobalTempv5_global_surf_temperature_trend.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data[data['Reported value']=='global mean']['year'], format='%Y')
proc_data['global mean'] = data[data['Reported value']=='global mean']['Temperature anomaly (K)']
proc_data['total error std'] = data[data['Reported value']=='total error std']['Temperature anomaly (K)'].to_numpy()
proc_data['lower bound'] = proc_data['global mean'] - 2.0*proc_data['total error std'] # 95% confidence interval
proc_data['upper bound'] = proc_data['global mean'] + 2.0*proc_data['total error std'] # 95% confidence interval
#%%

# Generate a plot for global mean surface temperature
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='global mean', type='quantitative', title='Global surface temperature change from the 1850-1900 mean [°C]', scale=alt.Scale(domain=[-0.5, 1.4])),
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
layer = alt.layer(bands, l, p) #.resolve_scale(y='shared')
layer.save('NOAAGlobalTempv5_global_surface_temp.json')

# %%
