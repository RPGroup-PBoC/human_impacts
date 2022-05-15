#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot of worldwide installed AC units
data = pd.read_csv('../processed/processed_global-air-conditioner-stock-1990-2016.csv')
data['date'] = pd.to_datetime(data['year'], format='%Y')
agg_data = pd.DataFrame()
agg_data['date'] = (data[data['Region']=='World'])['date']
# In billion units
agg_data['units'] = round((data[data['Region']=='World'])['A/C units (million)']/1000.0, 3)
#%%

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='date', type='temporal', timeUnit='year', title='Year'),
            y=alt.Y(field=r'units', type='quantitative', title=r'Installed AC units (billion)'),
            tooltip=[alt.Tooltip(field='date', type='temporal', title='date', format='%Y'),
                     alt.Tooltip(field=r'units', type='nominal', title=r'AC units (billion)')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('installed_ac_units.json')

