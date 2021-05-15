#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot for phosphate rock production
data = pd.read_csv('../processed/FAOSTAT_phosphate_processed.csv')
data['year'] = pd.to_datetime(data['Year'].astype(str), format='%Y', errors='coerce')
agg_data = pd.DataFrame()
agg_data['year'] = (data[data['Element']=='Agricultural Use'])['year']
agg_data['value'] = (data[data['Element']=='Agricultural Use'])['Value']

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'value', type='quantitative', title=r'Phosphate agriculturar use (Mt)',
                scale=alt.Scale(domain=[5, 50])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'value', type='nominal', title=r'Phosphate use (Mt)')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('phosphate_agricultural_use_FAO.json')

