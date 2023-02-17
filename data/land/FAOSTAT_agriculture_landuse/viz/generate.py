# %%
import pandas as pd
import altair as alt
import anthro.io

# Load the data sets
data = pd.read_csv('../processed/FAOSTAT_global_agricultural_landuse.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
data['land_area'] = anthro.io.numeric_formatter(data['area_Mha'].values * 1E6,
                                                sci=False, unit='Ha')
data['land_area_Bha'] = data['area_Mha'].values / 1E3
chart = alt.Chart(data).encode(
    x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
    y=alt.Y(field='land_area_Bha', type='quantitative', title='land area [billion hectares]',
            scale=alt.Scale(domain=[4, 5.25])),
    tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
             alt.Tooltip(field='land_area', type='nominal', title='land area')]
).properties(width='container', height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)

layer.save('./agricultural_area.json')

# %%
# Load the data sets
data = pd.read_csv('../processed/FAOSTAT_global_crop_landuse.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
data['land_area'] = anthro.io.numeric_formatter(data['area_Mha'].values * 1E6,
                                                sci=False, unit='Ha')
data['land_area_Bha'] = data['area_Mha'].values / 1E3
chart = alt.Chart(data).encode(
    x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
    y=alt.Y(field='land_area_Bha', type='quantitative', title='land area [billion hectares]',
            scale=alt.Scale(domain=[4, 5.25])),
    tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
             alt.Tooltip(field='land_area', type='nominal', title='land area')]
).properties(width='container', height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)

layer.save('./crop_area.json')
# %%
# Generate a plot of the fraction of agricultural land that is used for pasture
data = pd.read_csv('../processed/FAOSTAT_relative_crop_area.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
data.columns = ['year', 'fractional_crop_land']
data['fractional_crop_land'] *= 100

chart = alt.Chart(data).encode(
    x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
    y=alt.Y(field='fractional_crop_land', type='quantitative',
            title='crop area [% of total agricultural land]',
            scale=alt.Scale(domain=[0, 50])),
    tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
             alt.Tooltip(field='fractional_crop_land', type='quantitative',
                         format='0.0f', title='fraction [%]')]
).properties(width='container', height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)

layer = alt.layer(l, p)
layer.save('crop_fraction.json')
# %%

# %%
# Generate a plot of the fraction of agricultural land that is used for pasture
data = pd.read_csv('../processed/FAOSTAT_global_crop_pasture_land_use.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
area_ha = data[data['usage_type'] == 'pasture']['area_km2'] * 100

data = data.groupby('year').apply(
    lambda x: x[x['usage_type'] == 'pasture']['area_km2'].values[0] / x['area_km2'].sum()).reset_index()
data.columns = ['year', 'fraction_pct']
data['fraction_pct'] *= 100
data['area_ha'] = anthro.io.numeric_formatter(
    area_ha.values, unit='Ha', sci=False)

chart = alt.Chart(data).encode(
    x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
    y=alt.Y(field='fraction_pct', type='quantitative',
            title='pasture area [% of total agricultural land]',
            scale=alt.Scale(domain=[60, 80])),
    tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
             alt.Tooltip(field='fraction_pct', type='quantitative',
                         format='0.0f', title='fraction [%]'),
             alt.Tooltip(field='area_ha', type='nominal', title='area')]
).properties(width='container', height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)

layer = alt.layer(l, p)
layer.save('pasture_fraction.json')
# %%
