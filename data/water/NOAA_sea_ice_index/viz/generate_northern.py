#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the Northern Hemisphere sea ice area data
northern_area_data = pd.read_csv('../processed/northern_hemisphere_area.csv')
northern_area_data['Year'] = pd.to_datetime(northern_area_data['Year'], format='%Y')
northern_area_data = northern_area_data.drop(northern_area_data[(northern_area_data.Month != 'Annual') & (northern_area_data.Month != 'March') & (northern_area_data.Month != 'September')].index)

# Generate a plot for sea ice area in March, September, and Annual
base = alt.Chart(northern_area_data).encode(alt.X(field='Year', type='temporal', timeUnit='year', title='year')).properties(width='container', height=300)
columns = sorted(northern_area_data.Month.unique())
selection = alt.selection_single(
    fields=['Year'], nearest=True, on='mouseover', empty='none', clear='mouseout'
)

lines = base.mark_line(point=True).encode(alt.Y(field='Area', type = 'quantitative', title ='sea ice area (sq. km)'), color=alt.Color('Month:N', scale=alt.Scale(range=['rebeccapurple', 'dodgerblue', 'tomato'])))
points = lines.mark_point().transform_filter(selection)

rule = base.transform_pivot(
    'Month', value='Area', groupby=['Year']
).mark_rule().encode(
    opacity=alt.condition(selection, alt.value(0.3), alt.value(0)),
    tooltip=[alt.Tooltip(field = c, type='quantitative') for c in columns]
).add_selection(selection)

northern_area_layer = alt.layer(lines, points, rule)
northern_area_layer.save('./northern_area.json')

# Load the Northern Hemisphere sea ice extent data
northern_extent_data = pd.read_csv('../processed/northern_hemisphere_extent.csv')
northern_extent_data['Year'] = pd.to_datetime(northern_extent_data['Year'], format='%Y')
northern_extent_data = northern_extent_data.drop(northern_extent_data[(northern_extent_data.Month != 'Annual') & (northern_extent_data.Month != 'March') & (northern_extent_data.Month != 'September')].index)

# Generate a plot for sea ice extent in March, September, and Annual
base = alt.Chart(northern_extent_data).encode(alt.X(field='Year', type='temporal', timeUnit='year', title='year')).properties(width='container', height=300)
columns = sorted(northern_extent_data.Month.unique())
selection = alt.selection_single(
    fields=['Year'], nearest=True, on='mouseover', empty='none', clear='mouseout'
)

lines = base.mark_line(point=True).encode(alt.Y(field='Extent', type = 'quantitative', title ='sea ice extent (sq. km)'), color=alt.Color('Month:N', scale=alt.Scale(range=['rebeccapurple', 'dodgerblue', 'tomato'])))
points = lines.mark_point().transform_filter(selection)

rule = base.transform_pivot(
    'Month', value='Extent', groupby=['Year']
).mark_rule().encode(
    opacity=alt.condition(selection, alt.value(0.3), alt.value(0)),
    tooltip=[alt.Tooltip(field = c, type='quantitative') for c in columns]
).add_selection(selection)

northern_extent_layer = alt.layer(lines, points, rule)
northern_extent_layer.save('./northern_extent.json')
