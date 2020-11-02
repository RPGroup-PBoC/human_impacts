#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz 
import anthro.io
colors = anthro.viz.plotting_style()

# %%
data = pd.read_csv('../../../data/water/Macknick2012_operational_water_use/processed/Macknick2012_withdrawal_consumption_by_cooling.csv')
thermo = data[data['fuel_type'].isin(['nuclear', 'natural gas', 'coal'])]

# Group by cooling type and compute the min and max
melted = thermo[['fuel_type', 'cooling_type', 'cooling_technology', 'quantity', 
                'median', 'minimum', 'maximum']
                ].melt(['fuel_type', 'cooling_technology', 'cooling_type', 
                        'quantity'])
grouped = melted.groupby(['fuel_type', 'cooling_type', 'quantity'])['value'].agg(('min', 'max')).reset_index()

# Define the positional and coloring details
type_colors = {'coal':'#4b4b4b', 'nuclear':colors['red'], 'natural gas':colors['blue']}
centering = {'coal': -0.25, 'nuclear':0, 'natural gas':0.25}
position = {'once-through':4, 'cooling pond': 3, 'cooling tower': 2, 'dry cooling': 1}
labels = [k.replace(' ','\n').replace('-', '\n') for k in position.keys()]
labels.reverse()
# Instantiate the canvas
fig, ax = plt.subplots(2, 1, figsize=(3, 3.25), sharey=True)

# Format axes and add labels
for a in ax.ravel():
    a.xaxis.set_tick_params(labelsize=6)
    a.yaxis.set_tick_params(labelsize=6)
    a.set_yticks([1, 2, 3, 4])
    a.set_ylim([0.5, 4.5])
    a.set_yticklabels(labels)
ax[0].set_xlabel('withdrawal [L/10$^6$ J]', fontsize=6)
ax[1].set_xlabel('consumption [L/10$^6$ J]', fontsize=6)

# Add the values
for g, d in grouped.groupby(['quantity', 'fuel_type', 'cooling_type']):
    if g[0] == 'withdrawal':
        _ax = ax[0]
    else:
        _ax = ax[1]

    # Convert from L/MWh to L / MJ
    _min = d['min'].values / 3600
    _max = d['max'].values / 3600
    _ax.hlines(position[g[-1]] + centering[g[1]], _min, _max, lw=3.5, color=type_colors[g[1]])

plt.tight_layout()
plt.savefig('../../../figures/niagara_number/operational_use_plots.svg')
# %%
labels
# %%
