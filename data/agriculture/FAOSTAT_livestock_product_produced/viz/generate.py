#%%
import numpy as np 
import pandas as pd 
import altair as alt 


# Load the production data. 
data = pd.read_csv('../processed/FAOSTAT_livestock_and_product.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')

# Generate JSON vis for subcategories
for g, d in data.groupby('subcategory'):
    chart= alt.Chart(d).encode(
                        x=alt.X(field="year", type="temporal", timeUnit='year',
                                title="year"),
                        y=alt.Y(field="mass_produced_Mt", 
                                type="quantitative",
                                title="produced mass [Mt]"),
                       tooltip=[alt.Tooltip("year:T", timeUnit="year", title="year"),
                                alt.Tooltip("mass_produced_Mt:Q", format="0.0f", title="produced mass [Mt]")]
                      ).properties(width="container", 
                                    height=300
                      ).mark_line(color='dodgerblue')
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(filled=True, color='dodgerblue')
    figure = alt.layer(l, p)
    figure.save(f'{g}.json')


# %%
# Generate JSON vis for categories
for g, d in data.groupby('category'):
    d = d.groupby(['year']).sum().reset_index() 
    chart= alt.Chart(d).encode(
                        x=alt.X(field="year", type="temporal", timeUnit='year',
                                title="year"),
                        y=alt.Y(field="mass_produced_Mt", 
                                type="quantitative",
                                title="produced mass [Mt]"),
                       tooltip=[alt.Tooltip("year:T", timeUnit="year", title="year"),
                                alt.Tooltip("mass_produced_Mt:Q", format="0.0f", title="produced mass [Mt]")]
                      ).properties(width="container", 
                                    height=300
                      ).mark_line(color='dodgerblue')
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(filled=True, color='dodgerblue')
    figure = alt.layer(l, p)
    figure.save(f'{g}.json')


# %%

# Generate JSON vis for subcategories
for g, d in data.groupby('subcategory'):
    chart= alt.Chart(d).encode(
                        x=alt.X(field="year", type="temporal", timeUnit='year',
                                title="year"),
                        y=alt.Y(field="yield_kg_per_head", 
                                type="quantitative",
                                title="production yield [kg / animal]"),
                       tooltip=[alt.Tooltip("year", type='temporal', timeUnit="year", title="year", format='%Y'),
                                alt.Tooltip("yield_kg_per_head", type='quantitative', format="0.1f", title="yield [kg / animal]")]
                      ).properties(width="container", 
                                    height=300
                      ).mark_line(color='dodgerblue')
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(filled=True, color='dodgerblue')
    figure = alt.layer(l, p)
    figure.save(f"{'_'.join(g.lower().split(' '))}_yield.json")

# %%
