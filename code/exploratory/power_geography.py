#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.io
import anthro.viz
colors = anthro.viz.plotting_style()

cont_colors = {'Africa':colors['light_green'], 'Northern America':colors['light_red'],                
               'Europe':'#4b4b4b', 'Central America':colors['purple'],
               'South America':colors['dark_brown'],
               'Asia':colors['blue'], 'Oceania':colors['dark_green']}
cont_positions = {k:i for i, k in enumerate(cont_colors.keys())}


# Define the data provided by @mason
regions = ['Asia', 'Africa', 'Northern America', 'South America', 
            'Central America', 'Europe', 'Oceania']
_pos = [cont_positions[k] for k in regions]
_colors = [cont_colors[k] for k in regions]

# Total consumption
totals = np.array([9753, 662, 3763, 836, 311, 3809, 244])
per_capita = np.array([2155, 532, 10410, 1990, 1792, 5133, 6053])
tot_df = pd.DataFrame(np.array([regions, _pos, _colors, totals, per_capita]).T,
                        columns=['region', 'position', 'color', 'total', 'per_capita'])

# Nuclear power generation
nuke_total = np.array([157, 5, 318, 7, 4, 376, 0])
nuke_capita = np.array([35, 4, 879, 506, 21, 506, 0])
nuke_df = pd.DataFrame(np.array([regions, _pos, _colors, nuke_total, nuke_capita]).T,
                        columns=['region', 'position', 'color', 'total', 'per_capita'])

# Renewable power generation
renew_total = np.array([799, 45, 365, 244, 28, 423, 24])
renew_capita = np.array([176, 36, 1009, 580, 161, 569, 593])
renew_df = pd.DataFrame(np.array([regions, _pos, _colors, renew_total, renew_capita]).T,
                        columns=['region', 'position', 'color', 'total', 'per_capita'])


# Fossil fuel consumption
fossil_total = np.array([8794, 609, 2993, 589, 279, 3002, 221])
fossil_capita = np.array([1942, 489, 8279, 1405, 1605, 4045, 5467])
fossil_df = pd.DataFrame(np.array([regions, _pos, _colors, fossil_total, fossil_capita]).T,
                        columns=['region', 'position', 'color', 'total', 'per_capita'])
#%% Fossil Fuel Consumption 
fossil_df.sort_values('total', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(fossil_df['total'], colors=fossil_df['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('./fossil_fuel_consumption_donut.svg')
# Make the percapita plot
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_ylim([400, 8800])
ax.set_ylabel('W per capita', fontsize=6)
for g, d in fossil_df.groupby(['region']):
    ax.plot(cont_positions[g], int(d['per_capita']), 'o', ms=3, color=cont_colors[g])
    ax.vlines(cont_positions[g], 0, int(d['per_capita']), lw=0.5, color=cont_colors[g])

ax.set_yticks([1500, 3000, 4500, 6000, 7500, 9000])
plt.savefig('./fossil_fuel_consumption_per_capita.svg')
#
#%% Total Consumption Figure
tot_df.sort_values('total', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(tot_df['total'], colors=tot_df['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('./total_power_donut.svg')
# Make the percapita plot
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_ylim([500, 12000])
ax.set_ylabel('W per capita', fontsize=6)
for g, d in tot_df.groupby(['region']):
    ax.plot(cont_positions[g], int(d['per_capita']), 'o', ms=3, color=cont_colors[g])
    ax.vlines(cont_positions[g], 0, int(d['per_capita']), lw=0.5, color=cont_colors[g])

ax.set_yticks([0, 2000, 4000, 6000, 8000, 10000])
plt.savefig('./total_power_per_capita.svg')
#
#%% Nuclear Power Figure
nuke_df.sort_values('total', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(nuke_df['total'], colors=nuke_df['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('./nuclear_power_donut_donut.svg')
#%%
# Make the percapita plot
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_ylim([0, 1000])
ax.set_ylabel('W per capita', fontsize=6)
for g, d in nuke_df.groupby(['region']):
    ax.plot(cont_positions[g], int(d['per_capita']), 'o', ms=3, color=cont_colors[g])
    ax.vlines(cont_positions[g], 0, int(d['per_capita']), lw=0.5, color=cont_colors[g])

ax.set_yticks([0, 200, 400, 600, 800, 1000])
plt.savefig('./nuclear_power_per_capita.svg')
#%% Renewable Power Figure
renew_df.sort_values('total', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5))
ax.pie(renew_df['total'], colors=renew_df['color'])
circ = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circ)
plt.savefig('./renewable_power_donut.svg')

# Make the percapita plot
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_ylim([0, 1100])
# ax.set_ylabel('W per capita', fontsize=6)
ax.set_xticks([])
for g, d in renew_df.groupby(['region']):
    ax.plot(cont_positions[g], int(d['per_capita']), 'o', ms=3, color=cont_colors[g])
    ax.vlines(cont_positions[g], 0, int(d['per_capita']), lw=0.5, color=cont_colors[g])

ax.set_yticks([0, 200, 400, 600, 800, 1000])
plt.savefig('./renewable_power_per_capita.svg')

# %%
