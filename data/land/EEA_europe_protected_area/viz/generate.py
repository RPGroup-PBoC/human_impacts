#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot for terrestrial designated protected area in the EEA countries (EEA-38+UK)
data = pd.read_csv('../processed/protected_land_area_europe.csv')
data['year'] = pd.to_datetime(data['year'].astype(str), format='%Y', errors='coerce')
agg_data = pd.DataFrame()
agg_data['year'] = (data[ ( data['Reported value']=='Area' ) & (data['Region']=='EEA-38+UK' ) ])['year']
agg_data['Area'] = (data[ ( data['Reported value']=='Area' ) & (data['Region']=='EEA-38+UK' ) ])['Value']/1.0e6

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'Area', type='quantitative', title=r'Terrestrial protected area in Europe [Millions of km2]',
                scale=alt.Scale(domain=[0, 2])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'Area', type='nominal', title=r'Area [Millions of km2]')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('EEA38_protected_area.json')

