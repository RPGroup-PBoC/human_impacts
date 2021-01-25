#%%
import numpy as np
from PyAstronomy import pyasl
import pandas as pd
import altair as alt
import anthro.io

# Load the ice sheet data.
data = pd.read_csv('../processed/NASA_greenland_anomaly_042002-102020.csv')
proc_data = pd.DataFrame()
# Convert year.decimal format to Gregorian format
for index, row in data.iterrows():
    proc_data.loc[index,'yyyy-mm-dd'] = pd.to_datetime(str(pyasl.decimalYearGregorianDate((row['year.decimal']))))
proc_data['Greenland mass (Gt)'] = data['Greenland Mass Gt']
proc_data['lower bound'] = proc_data['Greenland mass (Gt)']-data['Greenland Mass Gt (1-sigma uncertainty)']
proc_data['upper bound'] = proc_data['Greenland mass (Gt)']+data['Greenland Mass Gt (1-sigma uncertainty)']

# Generate a plot for ice sheet mass change
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='yyyy-mm-dd', type='temporal', timeUnit='yearmonthdate', title='year', axis = alt.Axis(format='%Y')),
            y=alt.Y(field='Greenland mass (Gt)', type='quantitative', title='Greenland mass [Gt]', scale=alt.Scale(domain=[-6000, 0])),
            tooltip=[alt.Tooltip(field='yyyy-mm-dd', type='temporal', title='date', format='%Y-%b-%d'),
                     alt.Tooltip(field='label', type='nominal', title='mass change (Gt)')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='yyyy-mm-dd', type='temporal', timeUnit='yearmonthdate', title='year'),
            y='lower bound:Q',
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('./Greenland_mass_loss.json')
# %%
