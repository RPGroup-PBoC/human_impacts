#%%
import numpy as np
import pandas as pd
import altair as alt
import anthro.io

# Load the IFASTAT nitrogen data.
data = pd.read_csv('../processed/IFA_ammonia_tidy.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data['year'], format='%Y')
proc_data['production (kt)'] = data['value']
proc_data['label'] = anthro.io.numeric_formatter(data['value'].values * 1E3, unit='t')

# Generate a plot for global nitrogen production.
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='production (kt)', type='quantitative', title='Mass of nitrogen in synthesized ammonia [kt]', scale=alt.Scale(domain=[120000, 160000])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='label', type='nominal', title='production mass')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('./nitrogen_production.json')
# %%
