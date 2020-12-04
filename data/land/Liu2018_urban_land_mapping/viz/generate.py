#%%
import pandas as pd 
import altair as alt
import anthro.io

# Load the data sets 
data = pd.read_csv('../processed/Liu2018_table_3.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
total = data[data['region']=='Total']

#%%
chart = alt.Chart(total).encode(
        x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
        y=alt.Y(field='area_km2', type='quantitative', title='land area [sq. km]',
                 scale=alt.Scale(domain=[4, 5.25])),
        tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                 alt.Tooltip(field='area_km2', type='nominal', title='land area [sq. km]')]
        ).properties(width='container', height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)

layer.save('./urban_land_area.json')



# %%