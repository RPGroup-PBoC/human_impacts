#%%
import pandas as pd 
import altair as alt 
import anthro.io 

# Load the FishStatJ data for total produced fish mass by source 
data = pd.read_csv('../processed/FAO_FishStatJ_total_mass_source.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')
bounds = [[0, 120], [0, 100], [0, 200]]
i = 0
for g, d in data.groupby(['source']):
  chart = alt.Chart(d).encode(
              x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
              y=alt.Y(field='produced mass (Mt)', type='quantitative', title='Harvested mass [Mt]',
              scale=alt.Scale(domain=bounds[i])),
              tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                       alt.Tooltip(field='produced mass (Mt)', type='nominal', title='Harvested mass [Mt]')]
  ).properties(width="container", height=300)
  l = chart.mark_line(color='dodgerblue')
  p = chart.mark_point(color='dodgerblue', filled=True)
  i += 1
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
                     alt.Tooltip(field='cultured percentage', type='nominal', title='Harvest from aquaculture [%]')]
).properties(width="container", height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)

layer = alt.layer(l, p)
layer.save(f'aquaculture_mass_percentage.json')

# Generate marine fish stock state viz
stock_data = pd.read_csv('../processed/marine_fish_stock_state.csv')
stock_data = stock_data[stock_data['Fishery status'] == 'overfished']
stock_data['year'] = pd.to_datetime(stock_data['year'], format='%Y')

chart = alt.Chart(stock_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='Percentage of fish stocks', type='quantitative', title='Overfished fish stocks [%]',
            scale=alt.Scale(domain=[5, 40])),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='Percentage of fish stocks', type='nominal', title='Overfished fish stocks [%]')]
).properties(width="container", height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save(f'overfished_fish_stocks.json')
# %%

# Load the FishStatJ data for total produced fish mass by species
data = pd.read_csv('../processed/FAO_FishStatJ_total_mass_species.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')

# Select major capture species to plot
main_species = ["Anchoveta(=Peruvian anchovy)", "Alaska pollock(=Walleye poll.)", "Skipjack tuna", 
            "Gazami crab", "Akiami paste shrimp", "Antarctic krill", "Jumbo flying squid",
            "Atlantic herring"]
capture_data = data[data['source'] == 'captured']
capture_data["produced mass (Mt)"] = capture_data["produced mass (tonnes)"] / 1e6

for specie, d in capture_data.groupby(['species']):
  if specie in main_species:
    chart = alt.Chart(d).encode(
              x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
              y=alt.Y(field='produced mass (Mt)', type='quantitative', title='Captured mass [Mt]'),
              tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                       alt.Tooltip(field='produced mass (Mt)', type='nominal', title='Captured mass [Mt]')]
    ).properties(width="container", height=300)
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(color='dodgerblue', filled=True)
    layer = alt.layer(l, p)
    specie_name = specie.replace(" ", "_")
    layer.save(f'{specie_name}_captured_mass.json')

# Select major cultured species to plot
main_species = ["Nile tilapia", "Grass carp(=White amur)", "Silver carp", "Atlantic salmon",
                "Whiteleg shrimp", "Japanese carpet shell"]
culture_data = data[data['source'] == 'cultured']
culture_data["produced mass (Mt)"] = culture_data["produced mass (tonnes)"] / 1e6

for specie, d in culture_data.groupby(['species']):
  if specie in main_species:
    chart = alt.Chart(d).encode(
              x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
              y=alt.Y(field='produced mass (Mt)', type='quantitative', title='Cultured mass [Mt]'),
              tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                       alt.Tooltip(field='produced mass (Mt)', type='nominal', title='Cultured mass [Mt]')]
    ).properties(width="container", height=300)
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(color='dodgerblue', filled=True)
    layer = alt.layer(l, p)
    specie_name = specie.replace(" ", "_")
    layer.save(f'{specie_name}_cultured_mass.json')
# %%

# Percentage of Atlantic salmon harvest coming from aquaculture
num_data = culture_data[culture_data['species'] == "Atlantic salmon"]
den_data = capture_data[capture_data['species'] == "Atlantic salmon"]
num_data['cultured percentage'] = 100*num_data[['produced mass (Mt)']].div(
    den_data['produced mass (Mt)'].to_numpy()[14:] +
    num_data['produced mass (Mt)'].to_numpy(), axis=0).copy()
chart = alt.Chart(num_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='cultured percentage', type='quantitative', title='Atlantic salmon harvest from aquaculture [%]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field='cultured percentage', type='nominal', title='Harvest from aquaculture [%]')]
).properties(width="container", height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)

layer = alt.layer(l, p)
layer.save(f'aquaculture_atlantic_salmon_percentage.json')
