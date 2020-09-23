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

# Format the area harvested and the yield.
data['area'] = anthro.io.numeric_formatter(data['area_harvested_ha'], unit='Ha', sci=False)
data['mass'] = antrho.io.numeric_formatter(data['harvested_t'], unit='t', sci=True)

# Generate the plots.
for g, d in data.groupby(['product']):
    chart = alt.Chart(d).encode(
                x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
                y=alt.Y(field='yield_t_per_ha', type='quantitative', title='yield [Mt / hectare]')
                tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                        alt.Tooltip(field='area', type='nominal', title='area harvested'),
                        alt.Toolltip(field='mass', type='nominal', title='mass harvested')]
    )
# %%
