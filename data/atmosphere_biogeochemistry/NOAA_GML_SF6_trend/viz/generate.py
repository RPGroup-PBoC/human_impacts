#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot for global atmospheric SF6 concentration from NOAA GML data
data = pd.read_csv('../processed/monthly_global_sf6_data_processed.csv')
data['date'] = pd.to_datetime(data['year'].astype(str)  + data['month'].astype(str), format='%Y%m', errors='coerce')
agg_data = pd.DataFrame()
agg_data['date'] = (data[data['Reported value']=='monthly mean'])['date']
agg_data['concentration'] = (data[data['Reported value']=='monthly mean'])['Concentration (ppt)']
agg_data['total error std'] = ((data[data['Reported value']=='mon. mean 1-sigma unc.'])['Concentration (ppt)']).to_numpy()
agg_data['lower bound'] = agg_data['concentration'] - 1.96*agg_data['total error std'] # 95% confidence interval
agg_data['upper bound'] = agg_data['concentration'] + 1.96*agg_data['total error std'] # 95% confidence interval

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='date', type='temporal', timeUnit='yearmonth', title='date'),
            y=alt.Y(field=r'concentration', type='quantitative', title=r'[SF6] (ppt)',
                scale=alt.Scale(domain=[3, 11])),
            tooltip=[alt.Tooltip(field='date', type='temporal', title='date', format='%Y, %m'),
                     alt.Tooltip(field=r'concentration', type='nominal', title=r'concentration')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='date', type='temporal', timeUnit='yearmonth', title='date'),
            y=alt.Y('lower bound:Q', scale=alt.Scale(zero=False)),
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('atmospheric_SF6.json')

