#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Load the produciton data. 
data = pd.read_csv('../processed/FAOSTAT_rural_urban_population.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
agg_data = data.groupby(['year']).apply(lambda x: x[x['category']=='urban']['population'].values[0] / x['population'].sum()).reset_index()
agg_data.columns = ['year', 'urban_fraction_pct']
agg_data['urban_fraction_pct'] *= 100
agg_data['urban_population'] = anthro.io.numeric_formatter(data[data['category']=='urban']['population'].values, sci=False)
agg_data['total_population'] = anthro.io.numeric_formatter(data.groupby(['year'])['population'].sum().values,sci=False)
agg_data
#%%
# Generate the plot.
chart = alt.Chart(agg_data).encode(
                x=alt.X(field='year',  type='temporal', 
                        timeUnit='year', title='year'),
                y=alt.Y(field='urban_fraction_pct', type='quantitative', 
                        title='urban population [% of total]',
                        scale=alt.Scale(domain=[25, 60])),
                tooltip=[alt.Tooltip(field='year', type='temporal', timeUnit='year', title='year'),
                         alt.Tooltip(field='urban_population', type='nominal', title='urban population'),
                         alt.Tooltip(field='total_population', type='nominal', title='total population')]
                ).properties(
                width="container",
                height=300
                )
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)

chart = alt.layer(l, p)
chart.save('urban_pop.json')

#%%
# Generate a plot for the total population
data = pd.read_csv('../processed/FAOSTAT_total_population.csv')
data['year'] = pd.to_datetime(data['Year'].values, format='%Y')
data['population_Bhd'] = data['population'] * 1E-9
data['population'] = anthro.io.numeric_formatter(data['population'].values, sci=False)

chart = alt.Chart(data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='population_Bhd', type='quantitative', title='population [billions]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='population', type='nominal', title='population')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('total_population.json')

# %%
