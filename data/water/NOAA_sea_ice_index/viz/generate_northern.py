#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the Northern Hemisphere sea ice area data
northern_area_data = pd.read_csv('../processed/northern_hemisphere_area.csv')
northern_area_data['Year'] = pd.to_datetime(northern_area_data['Year'], format='%Y')
northern_march_area = northern_area_data[northern_area_data['Month']=='March']
northern_september_area = northern_area_data[northern_area_data['Month']=='September']
northern_annual_area = northern_area_data[northern_area_data['Month']=='Annual']

# Generate a plot for March sea ice area
chart = alt.Chart(northern_march_area).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Area', type='quantitative', title='sea ice area (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Area', type='nominal', title='sea ice area in March (sq. km)')]
            ).properties(width='container', height=300)
l1 = chart.mark_line(color='dodgerblue')
p1 = chart.mark_point(color='dodgerblue', filled=True)

# Generate a plot for September sea ice area
chart = alt.Chart(northern_september_area).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Area', type='quantitative', title='sea ice area (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Area', type='nominal', title='sea ice area in September (sq. km)')]
            ).properties(width='container', height=300)
l2 = chart.mark_line(color='dodgerblue')
p2 = chart.mark_point(color='dodgerblue', filled=True)

# Generate a plot for Annual sea ice area
chart = alt.Chart(northern_annual_area).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Area', type='quantitative', title='sea ice area (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Area', type='nominal', title='annually averaged sea ice area (sq. km)')]
            ).properties(width='container', height=300)
l3 = chart.mark_line(color='dodgerblue')
p3 = chart.mark_point(color='dodgerblue', filled=True)

layer = alt.layer(l1,p1,l2,p2,l3,p3)
layer.save('./northern_area.json')

# Load the Northern Hemisphere sea ice extent data
northern_extent_data = pd.read_csv('../processed/northern_hemisphere_extent.csv')
northern_extent_data['Year'] = pd.to_datetime(northern_extent_data['Year'], format='%Y')
northern_march_extent = northern_extent_data[northern_extent_data['Month']=='March']
northern_september_extent = northern_extent_data[northern_extent_data['Month']=='September']
northern_annual_extent = northern_extent_data[northern_extent_data['Month']=='Annual']

# Generate a plot for March sea ice extent
chart = alt.Chart(northern_march_extent).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Extent', type='quantitative', title='sea ice extent (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Extent', type='nominal', title='sea ice extent in March (sq. km)')]
            ).properties(width='container', height=300)

l4 = chart.mark_line(color='dodgerblue')
p4 = chart.mark_point(color='dodgerblue', filled=True)

# Generate a plot for September sea ice extent
chart = alt.Chart(northern_september_extent).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Extent', type='quantitative', title='sea ice extent (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Extent', type='nominal', title='sea ice extent in September (sq. km)')]
            ).properties(width='container', height=300)

l5 = chart.mark_line(color='dodgerblue')
p5 = chart.mark_point(color='dodgerblue', filled=True)

# Generate a plot for Annual sea ice extent
chart = alt.Chart(northern_annual_extent).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Extent', type='quantitative', title='sea ice extent (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Extent', type='nominal', title='annually averaged sea ice extent (sq. km)')]
            ).properties(width='container', height=300)

l6 = chart.mark_line(color='dodgerblue')
p6 = chart.mark_point(color='dodgerblue', filled=True)

layer2 = alt.layer(l4,p4,l5,p5,l6,p6)
layer2.save('./northern_extent.json')
