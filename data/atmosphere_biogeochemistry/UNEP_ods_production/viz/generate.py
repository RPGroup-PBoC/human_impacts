#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot for ozone depleting substances consumption from the UN Environmental Programme
data = pd.read_csv('../processed/annual_ods_consumption.csv')
data['year'] = pd.to_datetime(data['Year'].astype(str), format='%Y', errors='coerce')
agg_data = pd.DataFrame()
agg_data['year'] = (data[data['Substance category']=='All substances'])['year']
agg_data['consumption'] = (data[data['Substance category']=='All substances'])['Consumption (10^6 ODP kg)']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'consumption', type='quantitative', title=r'Consumption of controlled substances (10^6 ODP kg)',
                ),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'consumption', type='nominal', title=r'Consumption (10^6 ODP kg)')]
            ).properties(width='container', height=300)


l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('ods_consumption.json')

