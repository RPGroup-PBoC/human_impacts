import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the Southern Hemisphere sea ice area data
southern_area_data = pd.read_csv('../processed/southern_hemisphere_area.csv')
southern_area_data['Year'] = pd.to_datetime(southern_area_data['Year'], format='%Y')
southern_february_area = southern_area_data[southern_area_data['Month']=='February']
southern_september_area = southern_area_data[southern_area_data['Month']=='September']
southern_annual_area = southern_area_data[southern_area_data['Month']=='Annual']

# Generate a plot for February sea ice area
chart = alt.Chart(southern_february_area).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Area', type='quantitative', title='sea ice area (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Area', type='nominal', title='sea ice area in February (sq. km)')]
            ).properties(width='container', height=300)
l1 = chart.mark_line(color='dodgerblue')
p1 = chart.mark_point(color='dodgerblue', filled=True)

# Generate a plot for September sea ice area
chart = alt.Chart(southern_september_area).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Area', type='quantitative', title='sea ice area (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Area', type='nominal', title='sea ice area in September (sq. km)')]
            ).properties(width='container', height=300)
l2 = chart.mark_line(color='dodgerblue')
p2 = chart.mark_point(color='dodgerblue', filled=True)

# Generate a plot for Annual sea ice area
chart = alt.Chart(southern_annual_area).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Area', type='quantitative', title='sea ice area (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Area', type='nominal', title='annually averaged sea ice area (sq. km)')]
            ).properties(width='container', height=300)
l3 = chart.mark_line(color='dodgerblue')
p3 = chart.mark_point(color='dodgerblue', filled=True)

layer = alt.layer(l1,p1,l2,p2,l3,p3)
layer.save('./southern_area.json')

# Load the Southern Hemisphere sea ice extent data
southern_extent_data = pd.read_csv('../processed/southern_hemisphere_extent.csv')
southern_extent_data['Year'] = pd.to_datetime(southern_extent_data['Year'], format='%Y')
southern_february_extent = southern_extent_data[southern_extent_data['Month']=='February']
southern_september_extent = southern_extent_data[southern_extent_data['Month']=='September']
southern_annual_extent = southern_extent_data[southern_extent_data['Month']=='Annual']

# Generate a plot for February sea ice extent
chart = alt.Chart(southern_february_extent).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Extent', type='quantitative', title='sea ice extent (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Extent', type='nominal', title='sea ice extent in February (sq. km)')]
            ).properties(width='container', height=300)

l4 = chart.mark_line(color='dodgerblue')
p4 = chart.mark_point(color='dodgerblue', filled=True)

# Generate a plot for September sea ice extent
chart = alt.Chart(southern_september_extent).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Extent', type='quantitative', title='sea ice extent (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Extent', type='nominal', title='sea ice extent in September (sq. km)')]
            ).properties(width='container', height=300)

l5 = chart.mark_line(color='dodgerblue')
p5 = chart.mark_point(color='dodgerblue', filled=True)

# Generate a plot for Annual sea ice extent
chart = alt.Chart(southern_annual_extent).encode(
            x=alt.X(field='Year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Extent', type='quantitative', title='sea ice extent (sq. km)', scale=alt.Scale(zero=False)),
            tooltip=[alt.Tooltip(field='Year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Extent', type='nominal', title='annually averaged sea ice extent (sq. km)')]
            ).properties(width='container', height=300)

l6 = chart.mark_line(color='dodgerblue')
p6 = chart.mark_point(color='dodgerblue', filled=True)

layer2 = alt.layer(l4,p4,l5,p5,l6,p6)
layer2.save('./southern_extent.json')
