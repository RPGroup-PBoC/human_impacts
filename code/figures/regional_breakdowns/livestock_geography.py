#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz
colors = anthro.viz.plotting_style()
regions, positions = anthro.viz.region_colors()

# Load the livestock data
data = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_livestock_population_continent.csv')
data = data[data['year']==2018]

# Load the population data
pop = pd.read_csv('../../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_population_by_region.csv')
pop = pop[pop['year']==2018]
pop.loc[pop['region']=='Central America', 'region'] = 'North America'
pop.loc[pop['region']=='Northern America', 'region'] = 'North America'
pop_dict = {k:v for k, v in zip(pop['region'].values, pop['population_Mhd'].values)}
for k, v in pop_dict.items():
    data.loc[data['region']==k, 'region_pop'] = v
data.loc[data['region']=='Central America', 'region'] = 'North America'
data.loc[data['region']=='Northern America', 'region'] = 'North America'
data = data.groupby(['region', 'animal']).sum().reset_index()
data['per_capita'] = data['population_Mhd'].values / data['region_pop'].values
data['color'] = [regions[k] for k in data['region'].values]


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
    plt.savefig(f'../../../figures/regional_breakdowns/{ls}_donut.svg')

    # Plot the per capita
    d.sort_values(['per_capita'], inplace=True, ascending=False)
    position = np.arange(len(d)) 
    fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
    ax.xaxis.set_tick_params(labelsize=6)
    ax.yaxis.set_tick_params(labelsize=6)
    ax.set_ylabel('per capita', fontsize=6)    
    iter = 0
    for _, _d in d.groupby(['region']):
        ax.plot(positions[_], _d['per_capita'], 'o', ms=3, color=_d['color'].values[0])
        ax.vlines(positions[_], 0, _d['per_capita'], lw=0.5, color=_d['color'].values[0])
        iter += 1
    ylim = [0, ax.get_ylim()[1] * 1.1]
    ax.set_ylim(ylim)
    plt.savefig(f'../../../figures/regional_breakdowns/{ls}_per_capita.svg')

# %%
df = []
for g, d in data.groupby(['animal']):
    d = d.copy()
    d['percent'] = 100 * d['population_Mhd'].values / d['population_Mhd'].sum() 

    df.append(d)


percs = pd.concat(df, sort=False)
percs = percs[percs['animal'].isin(['cattle', 'pigs', 'chickens'])]
percs
# %%

# %%
