#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the BP oil production data.
data = pd.read_csv('../../processed/BP_global_oil_production_1965-2019.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data['year'], format='%Y')
proc_data['production (m^3)'] = data['production_cubic_meters_per_year']
proc_data['label'] = anthro.io.numeric_formatter(data['production_cubic_meters_per_year'].values * 1E3, unit='m^3')

# Generate a plot for global oil production.
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='production (m^3)', type='quantitative', title='Volume of oil [m^3]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='label', type='nominal', title='production volume')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('./oil_production.json')
# %%
