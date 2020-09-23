#%%
import numpy as np 
import pandas as pd 
import altair as alt 


# Load the produciton data. 
data = pd.read_csv('../processed/FAOSTAT_livestock_and_product.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
for g, d in data.groupby('subcategory'):
    chart= alt.Chart(d).encode(
                        x=alt.X(field="year", type="temporal", timeUnit='year'),
                        y=alt.Y(field="mass_produced_Mt", 
                                type="quantitative",
                                title="produced mass [Mt]"),
                       tooltip=[alt.Tooltip("year:T", timeUnit="year", title="year"),
                                alt.Tooltip("mass_produced_Mt:Q", format="0.0f", title="mass [Mt]")]
                      ).properties(width=300, 
                                    height=300
                      ).mark_line(color='dodgerblue')
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(filled=True, color='dodgerblue')
    figure = alt.Layer(l, p)
    figure.save(f'../vis/{g}.json')
# %%

chart
# %%