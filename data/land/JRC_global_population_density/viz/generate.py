#%%
import pandas as pd 
import altair as alt
import anthro.io

# Load the data sets 
data = pd.read_csv('../processed/JRC_urban_geq5k_density_tidy.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
data = data.groupby(['year']).sum()['total_area_km2'].reset_index()


#%%
chart = alt.Chart(data).encode(
        x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
        y=alt.Y(field='total_area_km2', type='quantitative', title='land area [sq. km]',
                 scale=alt.Scale(domain=[200000, 675000 ])),
        tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                 alt.Tooltip(field='total_area_km2', type='nominal', title='land area [sq. km]')]
        ).properties(width=300, height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)

layer.save('./urban_land_area.json')
# %%
