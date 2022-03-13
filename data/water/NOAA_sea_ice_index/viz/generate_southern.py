import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the Southern Hemisphere sea ice area data
southern_area_data = pd.read_csv('../processed/southern_hemisphere_area.csv')
southern_area_data['Year'] = pd.to_datetime(southern_area_data['Year'], format='%Y')
southern_area_data = southern_area_data.drop(southern_area_data[(southern_area_data.Month != 'Annual') & (southern_area_data.Month != 'February') & (southern_area_data.Month != 'September')].index)

# Generate a plot for sea ice area in February, September, and Annual
base = alt.Chart(southern_area_data).encode(alt.X(field='Year', type='temporal', timeUnit='year', title='year')).properties(width='container', height=300)
columns = sorted(southern_area_data.Month.unique())
selection = alt.selection_single(
    fields=['Year'], nearest=True, on='mouseover', empty='none', clear='mouseout'
)

lines = base.mark_line(point=True).encode(alt.Y(field='Area', type = 'quantitative', title ='sea ice area (sq. km)'), color=alt.Color('Month:N', scale=alt.Scale(range=['rebeccapurple', 'tomato', 'dodgerblue'])))
points = lines.mark_point().transform_filter(selection)

rule = base.transform_pivot(
    'Month', value='Area', groupby=['Year']
).mark_rule().encode(
    opacity=alt.condition(selection, alt.value(0.3), alt.value(0)),
    tooltip=[alt.Tooltip(field = c, type='quantitative') for c in columns]
).add_selection(selection)

southern_area_layer = alt.layer(lines, points, rule)
southern_area_layer.save('./southern_area.json')

# Load the Southern Hemisphere sea ice extent data
southern_extent_data = pd.read_csv('../processed/southern_hemisphere_extent.csv')
southern_extent_data['Year'] = pd.to_datetime(southern_extent_data['Year'], format='%Y')
southern_extent_data = southern_extent_data.drop(southern_extent_data[(southern_extent_data.Month != 'Annual') & (southern_extent_data.Month != 'February') & (southern_extent_data.Month != 'September')].index)

# Generate a plot for sea ice extent in February, September, and Annual
base = alt.Chart(southern_extent_data).encode(alt.X(field='Year', type='temporal', timeUnit='year', title='year')).properties(width='container', height=300)
columns = sorted(southern_extent_data.Month.unique())
selection = alt.selection_single(
    fields=['Year'], nearest=True, on='mouseover', empty='none', clear='mouseout'
)

lines = base.mark_line(point=True).encode(alt.Y(field='Extent', type = 'quantitative', title ='sea ice extent (sq. km)'), color=alt.Color('Month:N', scale=alt.Scale(range=['rebeccapurple', 'tomato', 'dodgerblue'])))
points = lines.mark_point().transform_filter(selection)

rule = base.transform_pivot(
    'Month', value='Extent', groupby=['Year']
).mark_rule().encode(
    opacity=alt.condition(selection, alt.value(0.3), alt.value(0)),
    tooltip=[alt.Tooltip(field = c, type='quantitative') for c in columns]
).add_selection(selection)

southern_extent_layer = alt.layer(lines, points, rule)
southern_extent_layer.save('./southern_extent.json')
