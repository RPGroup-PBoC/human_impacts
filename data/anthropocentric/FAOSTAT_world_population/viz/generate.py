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
# # Generate JSON vis for subcategories
# for g, d in data.groupby('subcategory'):
#     chart= alt.Chart(d).encode(
#                         x=alt.X(field="year", type="temporal", timeUnit='year',
#                                 title="year"),
#                         y=alt.Y(field="mass_produced_Mt", 
#                                 type="quantitative",
#                                 title="produced mass [Mt]"),
#                        tooltip=[alt.Tooltip("year:T", timeUnit="year", title="year"),
#                                 alt.Tooltip("mass_produced_Mt:Q", format="0.0f", title="produced mass [Mt]")]
#                       ).properties(width="container", 
#                                     height=300
#                       ).mark_line(color='dodgerblue')
#     l = chart.mark_line(color='dodgerblue')
#     p = chart.mark_point(filled=True, color='dodgerblue')
#     figure = alt.layer(l, p)
#     figure.save(f'{g}.json')

# %%
