#%%
import numpy as np
import pandas as pd
import altair as alt

# Load the IFASTAT nitrogen data.
data = pd.read_csv('../processed/IFA_ammonia_tidy.csv')
proc_data = pd.DataFrame()
proc_data['year'] = pd.to_datetime(data['year'], format='%Y')
proc_data['production (kg)'] = data['value']*1000000

# Generate a plot for global mean surface temperature
chart = alt.Chart(proc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='production (kg)', type='quantitative', title='Mass of nitrogen in synthesized ammonia [kg]', scale=alt.Scale(domain=[120000000000, 160000000000])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='production (kg)', type='quantitative', title='production mass [kg]', format='.6s')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('nitrogen_production.json')
# %%
