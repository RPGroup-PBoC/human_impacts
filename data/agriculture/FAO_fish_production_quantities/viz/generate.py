#%%
import pandas as pd 
import altair as alt 
import anthro.io 

# Load the FishStatJ data for total produced fish mass by source 
data = pd.read_csv('../processed/FAO_FishStatJ_total_mass_source.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')

for g, d in data.groupby(['source']):
  chart = alt.Chart(d).encode(
              x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
              y=alt.Y(field='produced mass (Mt)', type='quantitative', title='Harvested mass [Mt]'),
              tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                       alt.Tooltip(field='produced mass (Mt)', type='nominal', title='Harvested mass [Mt]')]
  ).properties(width="container", height=300)
  l = chart.mark_line(color='dodgerblue')
  p = chart.mark_point(color='dodgerblue', filled=True)

  layer = alt.layer(l, p)
  layer.save(f'{g}_fish_mass.json')

# Compute percentage of fish production from aquaculture
perc_data = data[data['source'] == 'cultured']
total_data = data[data['source'] == 'total']
perc_data['cultured percentage'] = 100*perc_data[['produced mass (Mt)']].div(total_data['produced mass (Mt)'].to_numpy(), axis=0).copy()
chart = alt.Chart(perc_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='cultured percentage', type='quantitative', title='Fraction of fish harvest from aquaculture [%]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='cultured percentage', type='nominal', title='Fish harvest from aquaculture [Mt]')]
).properties(width="container", height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)

layer = alt.layer(l, p)
layer.save(f'aquaculture_mass_percentage.json')
# %%
