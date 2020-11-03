#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz 
import anthro.io
colors = anthro.viz.plotting_style()

# Load data and restrict to just once-through
data = pd.read_csv('../../../data/water/Macknick2012_operational_water_use/processed/Macknick2012_withdrawal_consumption_by_cooling.csv')
thermo = data[(data['fuel_type'].isin(['nuclear', 'natural gas', 'coal'])) & 
              (data['quantity']=='withdrawal')]
tech = thermo[thermo['cooling_type']=='once-through']

# Define position and colors based on fuel and technology
centers = {'coal':0, 'nuclear':-0.25, 'natural gas':0.25}
fuel_colors = {'coal': 'grey', 'nuclear':colors['red'], 'natural gas':colors['blue']}
positions = {k:i for i, k in enumerate(tech['cooling_technology'].unique())}
labels = [k.replace(' ', '\n') for k in positions.keys()]

# Instantiate the canvas and format the axis
fig, ax = plt.subplots(1, 1, figsize=(2, 1))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlabel('water volume [L / 10$^6$ J]', fontsize=6)
ax.set_xlim([-0.5, 0.5 ])
ax.set_xlim([0, 80])
ax.set_ylim([-0.5, 0.5])
ax.set_yticks([])
# ax.set_yscale('log')

# Group by fuel type and plot the minimum, maximum, and median
for g, d in tech.groupby(['fuel_type']):
    _min = d['minimum'].min() / 3600
    _max = d['maximum'].max() / 3600
    ax.hlines(centers[g], _min, _max, lw=8, color=fuel_colors[g])

# Over the bars, plot the estimated value
ax.vlines(30, -0.5, 0.5, 'k', linestyle='--', linewidth=0.5)
plt.savefig('../../../figures/niagara_number/once_through_withdrawal.svg')
# %%
