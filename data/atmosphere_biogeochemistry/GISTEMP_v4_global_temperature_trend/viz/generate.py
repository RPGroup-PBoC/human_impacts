#%%
import pandas as pd
import altair as alt
import anthro.io

# Load the data sets
data = pd.read_csv('../processed/Land-OceanTemperatureIndex.csv')
data['year'] = pd.to_datetime(data['Year'], format='%Y')
data = data.groupby(['year']).sum()['°C'].reset_index()

#%%
chart = alt.Chart(data).encode(
        x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
        y=alt.Y(field='°C', type='quantitative', title='°C'),
        tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                 alt.Tooltip(field='°C', type='nominal', title='°C')]
        ).properties(width='container', height=300)
a = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
    x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
    y='°C_lower:Q',
    y2='°C_upper:Q').properties(width='container', height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(a, l, p)

layer.save('./surface_temp.json')
# %%
