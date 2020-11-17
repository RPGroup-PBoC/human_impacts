#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.io 
import anthro.viz
import pycountry
colors = anthro.viz.plotting_style()
cont_colors = {'Africa':colors['light_green'], 'Northern America':colors['light_red'],                
               'Europe':'#4b4b4b', 'Central America':colors['purple'],
               'South America':colors['dark_brown'],
               'Asia':colors['blue'], 'Oceania':colors['dark_green']}
cont_positions = {k:i for i, k in enumerate(cont_colors.keys())}

# Define the data from @rbanks
regions = ['Africa', 'Asia', 'Europe', 'Oceania',
           'Northern America', 'South America', 'Central America']
_colors = [cont_colors[k] for k in regions]
_pos = [cont_positions[k] for k in regions]
ag_total = [103E9, 841E9, 80E9, 10E9, 190E9, 52E9, 70E9]
ag_capita = [210, 420, 110, 416, 487, 185, 318]
ag_df = pd.DataFrame(np.array([regions, ag_total, ag_capita, _colors]).T,
                    columns=['region', 'total', 'per_capita', 'color'])
ind_total = [11E9, 178E9, 133E9, 2.7E9, 240E9, 13.4E9, 7E9]
ind_capita = [22, 90, 180, 110, 610, 61, 30]
ind_df = pd.DataFrame(np.array([regions, ind_total, ind_capita, _colors]).T,
                    columns=['region', 'total', 'per_capita', 'color'])

domestic_total = [21E9, 137E9, 68E9, 3.4e9, 65E9, 23E9, 15E9]
domestic_capita = [42, 70, 93, 140, 170, 82, 68]
domestic_df = pd.DataFrame(np.array([regions, domestic_total, domestic_capita, _colors]).T,
                    columns=['region', 'total', 'per_capita', 'color'])

# Set up the central circle to make it a donut
circ = plt.Circle((0, 0), 0.6, color='white')

# Agriculture
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
ag_df.sort_values('total', inplace=True)
ax.pie(ag_df['total'], colors=ag_df['color'])
ax.add_artist(circ)
plt.savefig('./agricultural_water_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([100, 200, 300, 400, 500])
ax.yaxis.set_tick_params(labelsize=6)
for i, p in enumerate(_pos):
    ax.plot(p, ag_capita[i], 'o', ms=3, color=_colors[i])
    ax.vlines(p, 50, ag_capita[i], lw=0.5, color=_colors[i])
ax.set_ylim([50, 550])
plt.savefig('./agricultural_water_per_capita.svg')
# Set up the pie chart. 
# %%
# Industrial
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
ind_df.sort_values('total', inplace=True)
ax.pie(ind_df['total'], colors=ind_df['color'])
ax.add_artist(circ)
plt.savefig('./industrial_water_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([150, 300, 450, 600])
ax.yaxis.set_tick_params(labelsize=6)
for i, p in enumerate(_pos):
    ax.plot(p, ind_capita[i], 'o', ms=3, color=_colors[i])
    ax.vlines(p, 0, ind_capita[i], lw=0.5, color=_colors[i])
ax.set_ylim([0, 650])
plt.savefig('./industrial_water_per_capita.svg')

# %% Domestic
fig, ax = plt.subplots(1,1,  figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
domestic_df.sort_values(by='total', inplace=True)
ax.pie(domestic_df['total'], colors=domestic_df['color'])
ax.add_artist(circ)
plt.savefig('./domestic_water_donut.svg')

fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 50, 100, 150])
ax.yaxis.set_tick_params(labelsize=6)
for i, p in enumerate(_pos):
    ax.plot(p, domestic_capita[i], 'o', ms=3, color=_colors[i])
    ax.vlines(p, 0, domestic_capita[i], lw=0.5, color=_colors[i])
ax.set_ylim([0, 200])
plt.savefig('./domestic_water_per_capita.svg')




# %%
