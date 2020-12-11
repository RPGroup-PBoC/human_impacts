#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot for global atmospheric CH4 concentration from NOAA GML data
data = pd.read_csv('../processed/monthly_global_ch4_data_processed.csv')
data['date'] = pd.to_datetime(data['year'].astype(str)  + data['month'].astype(str), format='%Y%m', errors='coerce')
agg_data = pd.DataFrame()
agg_data['date'] = (data[data['Reported value']=='monthly mean'])['date']
agg_data['concentration'] = (data[data['Reported value']=='monthly mean'])['Concentration (ppb)']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='date', type='temporal', timeUnit='yearmonth', title='date'),
            y=alt.Y(field=r'concentration', type='quantitative', title=r'[CH4] (ppb)',
                scale=alt.Scale(domain=[1600, 1900])),
            tooltip=[alt.Tooltip(field='date', type='temporal', title='date', format='%Y, %m'),
                     alt.Tooltip(field=r'concentration', type='nominal', title=r'concentration')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('atmospheric_CH4.json')

