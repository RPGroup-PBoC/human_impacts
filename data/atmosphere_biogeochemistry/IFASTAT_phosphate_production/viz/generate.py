#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot for phosphate rock production
data = pd.read_csv('../processed/IFA_phosphate_rock_public_2008_2019_processed.csv')
data['year'] = pd.to_datetime(data['Year'].astype(str), format='%Y', errors='coerce')
agg_data = pd.DataFrame()
agg_data['date'] = (data[data['Region']=='Total World'])['year']
agg_data['production'] = (data[data['Region']=='Total World'])['Phosphate rock production mass (Mt)']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='date', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'production', type='quantitative', title=r'Phosphate rock production (Mt)',
                scale=alt.Scale(domain=[150, 220])),
            tooltip=[alt.Tooltip(field='date', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'production', type='nominal', title=r'Production (Mt)')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('phosphate_rock_IFA.json')

