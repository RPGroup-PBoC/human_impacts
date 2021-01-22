#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the ice sheet data.
data = pd.read_csv('../processed/NASA_greenland_anomaly_042002-102020.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data['year.decimal'], format='%Y')
proc_data['Greenland mass (Gt)'] = data['Greenland Mass Gt']
#proc_data['label'] = anthro.io.numeric_formatter(data['Greenland Mass Gt'].values, unit='Gt')

# Generate a plot for ice sheet mass loss production.
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Greenland mass (Gt)', type='quantitative', title='Greenland mass [Gt]', scale=alt.Scale(domain=[0, -5000])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='label', type='nominal', title='Mass loss')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('./Greenland_mass_loss.json')
# %%
