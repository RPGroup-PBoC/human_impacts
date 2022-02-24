#%%
import pandas as pd 
import altair as alt 
import anthro.io 

# Load the data 
data = pd.read_csv('../processed/FAOSTAT_livestock_population.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
total = data[data['animal']!='beehives'].groupby(['year'])['population_Mhd'].sum().reset_index()

# Restrict it to just cattle, chicken, sheep, and pigs
data = data[data['animal'].isin(['cattle', 'pigs', 'chickens', 'sheep', 'goats'])]

# Format the population to billions insted of millions. 
data['population_Bhd'] = data['population_Mhd'] * 1E-3
data['population'] = anthro.io.numeric_formatter(data['population_Mhd'].values * 1E6, sci=False)
for g, d in data.groupby(['animal']):
  chart = alt.Chart(d).encode(
              x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
              y=alt.Y(field='population_Bhd', type='quantitative', title='population [billions]'),
              tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                       alt.Tooltip(field='population', type='nominal', title='population')]
  ).properties(width="container", height=300)
  l = chart.mark_line(color='dodgerblue')
  p = chart.mark_point(color='dodgerblue', filled=True)

  layer = alt.layer(l, p)
  layer.save(f'{g}_population.json')

# Generate a plot for the total
total['population'] = anthro.io.numeric_formatter(total['population_Mhd'].values *1E6, sci=False)
total['population_Bhd'] = total['population_Mhd'] * 1E-3
chart = alt.Chart(total).encode(
              x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
              y=alt.Y(field='population_Bhd', type='quantitative', title='population [billions]'),
              tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                       alt.Tooltip(field='population', type='nominal', title='population')]
             ).properties(width="container", height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)

layer = alt.layer(l, p)
layer.save(f'livestock_population.json')

# %%
