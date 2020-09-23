#%%
import numpy as np
import pandas as pd 
import anthro.io 
import altair as alt

# Load thea data
data = pd.read_csv('../processed/FAOSTAT_crop_primary_yields.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')

# Limit the products to those ultimately entered in the database
products = ['Wheat', 'Maize', 'Cereals, Total', 'Potatoes', 'Rice']
data = data[data['product'].isin(products)]

# Generate the plots.
for g, d in data.groupby(['product']):
    chart = alt.Chart(d).encode(
                x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
                y=alt.Y(field='yield_t_per_ha', type='quantitative', title='yield [tonnes / hectare]'),
                tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                        alt.Tooltip(field='yield_t_per_ha', type='quantitative', format='0.1f', title='yield [t/ha]')]
                   ).properties(
                        width="container",
                        height=300
                    )
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(color='dodgerblue', filled=True)
    layer = alt.layer(l, p)

    if g == 'Cereals, Total':
        g = 'cereals'
    else:
        g = g
    layer.save(f'{g.lower()}_yield.json')
# %%
