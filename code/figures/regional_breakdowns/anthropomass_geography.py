#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz
colors = anthro.viz.plotting_style()
regions, positions = anthro.viz.region_colors()


# Define the data for steel production as reported by Nicholas.
_conts = ['Asia', 'Africa', 'Northern America', 'Central America',
          'South America', 'Europe', 'Oceania']
_pos = [positions[k] for k in _conts]
_colors = [regions[k] for k in _conts]
totals = [1.36E12, 1.74E10, 1.00E11, 2.06E10, 4.49E10, 2.69E11, 6.34E9]
per_capita = [298, 14, 246, 117, 106, 360, 152]

# Set up the dataframe
steel = pd.DataFrame(np.array([_conts, _pos, _colors, totals, per_capita]).T,
            columns=['region', 'position', 'color', 'total', 'per_capita'])


# %%
# Donut for steel 
fig, ax = plt.subplots(1,1, figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
steel.sort_values('total', inplace=True)
ax.pie(steel['total'], colors=steel['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/steel_regional_donut.svg')

# Per Capita
fig, ax = plt.subplots(1, 1, figsize=(1.5, 0.75))
ax.set_xticks([])
ax.set_yticks([0, 100, 200, 300, 400])
ax.yaxis.set_tick_params(labelsize=6)
for g, d in steel.groupby(['position', 'color']):
    ax.plot(int(g[0]), float(d['per_capita'].values[0]), 'o', ms=3, color=g[1])
    ax.vlines(int(g[0]), 0, float(d['per_capita'].values[0]), lw=0.5, color=g[1])
ax.set_ylim([0, 400])
plt.savefig('../../../figures/regional_breakdowns/steel_regional_per_capita.svg')
# %%
