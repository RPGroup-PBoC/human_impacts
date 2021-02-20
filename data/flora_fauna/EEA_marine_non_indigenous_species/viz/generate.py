#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot for EEA non-indigenous marine species
data = pd.read_csv('../processed/non_ind_marine_species_europe.csv')
data['year'] = pd.to_datetime(data['year'].astype(str), format='%Y', errors='coerce')
agg_data = pd.DataFrame()
agg_data['year'] = (data[ data['Reported group'].str.contains("All species") ])['year']
agg_data['Number'] = (data[ data['Reported group'].str.contains("All species") ])['Number']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'Number', type='quantitative', title=r'Number of non-indigenous species',
                scale=alt.Scale(domain=[0, 1200])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'Number', type='nominal', title=r'Non-indigenous species')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('EEA_non_ind_marine_species.json')