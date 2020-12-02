#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz
colors = anthro.viz.plotting_style()
cont_colors = {'Africa':colors['light_green'], 'Northern America':colors['light_red'],                
               'Europe':'#4b4b4b', 'Central America':colors['purple'],
               'South America':colors['dark_brown'],
               'Asia':colors['blue'], 'Oceania':colors['dark_green']}
cont_positions = {k:i for i, k in enumerate(cont_colors.keys())}

# Load the livestock data
data = pd.read_csv('../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_livestock_population_continent.csv')
data = data[data['year']==2018]
data['color'] = np.array([cont_colors[k] for k in data['region'].values])

# Load the population data
pop = pd.read_csv('../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_population_by_region.csv')
pop = pop[pop['year']==2018]
pop_dict = {k:v for k, v in zip(pop['region'].values, pop['population_Mhd'].values)}
for k, v in pop_dict.items():
    data.loc[data['region']==k, 'region_pop'] = v
data['per_capita'] = data['population_Mhd'].values / data['region_pop'].values

# %%
for ls in ['cattle', 'chickens', 'pigs']:
    d = data[data['animal']==ls]
    d.sort_values(['population_Mhd'], inplace=True)

    # Plot the composition
    fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
    ax.pie(d['population_Mhd'], colors=d['color'])
    circ = plt.Circle((0, 0), 0.6, color='white')
    ax.add_artist(circ)
    if ls == 'chickens':
        ls = 'chicken'
    elif ls == 'pigs':
        ls = 'swine'
    plt.savefig(f'./{ls}_donut.svg')

    # Plot the per capita
    d.sort_values(['per_capita'], inplace=True, ascending=False)
    position = np.arange(len(d)) 
    fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
    ax.xaxis.set_tick_params(labelsize=6)
    ax.yaxis.set_tick_params(labelsize=6)
    ax.set_ylabel('per capita', fontsize=6)    
    iter = 0
    for _, _d in d.groupby(['region']):
        ax.plot(cont_positions[_], _d['per_capita'], 'o', ms=3, color=_d['color'].values[0])
        ax.vlines(cont_positions[_], 0, _d['per_capita'], lw=0.5, color=_d['color'].values[0])
        iter += 1
    plt.savefig(f'./{ls}_per_capita.svg')

# %%
data['animal'].unique()
# %%
df = []
for g, d in data.groupby(['animal']):
    d = d.copy()
    d['percent'] = 100 * d['population_Mhd'].values / d['population_Mhd'].sum() 

    df.append(d)


percs = pd.concat(df, sort=False)
percs = percs[percs['animal'].isin(['cattle', 'pigs', 'chickens'])]

# %%

# %%