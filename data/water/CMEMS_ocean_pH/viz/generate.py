#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Load the production data. 
data = pd.read_csv('../processed/CMEMS_average_ocean_pH.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
data['pH'] = round(data['pH'], 3)
#%%

# Generate a plot for global average surface pH
chart = alt.Chart(data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='pH', type='quantitative', title='ocean pH', scale=alt.Scale(domain=[8.05, 8.12])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='pH', type='nominal', title='pH')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('surface_ocean_pH.json')

# %%

# Load the production data. 
data = pd.read_csv('../processed/CMEMS_trends_ocean_pH.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
agg_data = pd.DataFrame()
agg_data['year'] = data[data['Measure type']=='[H+] percentage trend']['year'][1:]
agg_data['H+ percentage trend'] = data[data['Measure type']=='[H+] percentage trend']['Value'][1:]

pd.set_option("display.max_rows", None, "display.max_columns", None)
print(agg_data)
#%%

# Generate a plot for global average surface pH
chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'H+ percentage trend', type='quantitative', title=r'[H+] percentage change'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'H+ percentage trend', type='nominal', title=r'H+ percentage trend')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('percentage_change_H.json')

# %%