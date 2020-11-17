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
_colors = [cont_colors[k] for k in regions]
_pos = [cont_positions[k] for k in regions]
# Define the data from Nicholas
regions = ['Africa', 'Northern America', 'Central America', 'South America',
            'Asia', 'Europe', 'Oceania']

prod_total = [7.23E9, 1.58E10, 2.54E8, 1.85E9, 6.96E10, 2.44E10, 5.27E8]
prod_capita = [5.7, 38.7, 1.5, 4.4, 15.3, 32.7, 12.7]
prod_df = pd.DataFrame(np.array([regions, prod_total, prod_capita, _colors]).T,
                    columns=['region', 'total', 'per_capita', 'color'])

ag_total = [4.30E9, 1.46E10, 1.84E9, 8.17E9, 6.31E10, 1.48E10, 1.90E9]
ag_capita = [3.4, 35.8, 10.5, 19.3, 13.8, 19.9, 45.8]
ag_df = pd.DataFrame(np.array([regions, ag_total, ag_capita, _colors]).T,
                    columns=['region', 'total', 'per_capita', 'color'])

# Production
circ = plt.Circle((0, 0), 0.6, color='white')
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
prod_df.sort_values('total', inplace=True)
ax.pie(prod_df['total'], colors=prod_df['color'])
ax.add_artist(circ)
plt.savefig('./nitrogen_production_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 10, 20, 30, 40])
ax.yaxis.set_tick_params(labelsize=6)
for i, p in enumerate(_pos):
    ax.plot(p, prod_capita[i], 'o', ms=3, color=_colors[i])
    ax.vlines(p, 0, prod_capita[i], lw=0.5, color=_colors[i])
ax.set_ylim([0, 40])
plt.savefig('./nitrogen_production_per_capita.svg')

# Agriculture
circ = plt.Circle((0, 0), 0.6, color='white')
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
ag_df.sort_values('total', inplace=True)
ax.pie(ag_df['total'], colors=ag_df['color'])
ax.add_artist(circ)
plt.savefig('./nitrogen_consumption_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 10, 20, 30, 40, 50])
ax.yaxis.set_tick_params(labelsize=6)
for i, p in enumerate(_pos):
    ax.plot(p, ag_capita[i], 'o', ms=3, color=_colors[i])
    ax.vlines(p, 0, ag_capita[i], lw=0.5, color=_colors[i])
ax.set_ylim([0, 55])
plt.savefig('./nitrogen_consumption_per_capita.svg')