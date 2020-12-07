#%%
import numpy as np
import pandas as pd 
import altair as alt

# First generate plot of observed values
observed = pd.read_csv('../processed/Frederikse2020_observed_GMSL_from_1900.csv')
observed['year'] = pd.to_datetime(observed['year'], format='%Y')

#%%
# Plot only the mean values
chart = alt.Chart(observed).encode(
        x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
        y=alt.Y(field='observed_GMSL_mean', type='quantitative', title='observed change from average sea-level in 1900 [mm]'),
        tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                 alt.Tooltip(field='observed_GMSL_mean', type='quantitative', title='mean [mm]', format='0.1f')]
    ).properties(width='container', height=300)
a = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
    x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
    y='observed_GMSL_lower:Q',
    y2='observed_GMSL_upper:Q')
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)

layer = alt.layer(a, l, p)
layer.save('observed_GMSL.json')

# %%

# Do the same for estimated contributors
contrib = pd.read_csv('../processed/Frederikse2020_contributor_GMSL_from_1900.csv')
contrib['year'] = pd.to_datetime(contrib['year'], format='%Y')

for g, d in contrib.groupby('source'):
    # Plot only the mean values
    chart = alt.Chart(d).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='mean', type='quantitative', title='estimated change from average sea-level in 1900 [mm]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                     alt.Tooltip(field='mean', type='quantitative', title='mean [mm]', format='0.1f')]
        ).properties(width='container', height=300)
    a = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
        x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
        y='observed_GMSL_lower:Q',
        y2='observed_GMSL_upper:Q')
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(color='dodgerblue', filled=True)

    layer = alt.layer(a, l, p)
    layer.save(f"{'_'.join(g.lower().split(' '))}_GMSL.json")