#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.io 
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load totaled data
data = pd.read_csv('../../../data/agriculture/FAO_fish_production_quantities/processed/FAO_FishStatJ_total_mass_source.csv')

# Set up the figure canvas.
fig, ax = plt.subplots(1, 1, figsize=(3, 1.75))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlabel('year', fontsize=6)
ax.set_ylabel('seafood (animal)\nmass produced [10$^{11}$ kg]', fontsize=6)
ax.set_xlim([1951, 2018])
ax.set_ylim([0, 2.25])
ax.set_yticks([0, 0.5, 1, 1.5, 2])


# Compute produced mass in terms of million kg
data['Bkg_mass'] = data['produced_mass_t'] * 1E3 / 1E11 
capture = data[data['source']=='captured']
culture = data[data['source']=='cultured']
total = data[data['source']=='total']

ax.hlines(2, 1951, 2018, 'k', linestyle='--', label='estimate', lw=0.75)
ax.plot(capture['year'], capture['Bkg_mass'], '-o', color=colors['blue'],
        label='wild-caught', lw=0.5, ms=1)

ax.plot(culture['year'], culture['Bkg_mass'], '-o', color=colors['red'],
        label='aquaculture', lw=0.5, ms=1)

ax.plot(total['year'], total['Bkg_mass'], '-o', color=colors['dark_green'],
        label='total', lw=0.5, ms=1)
ax.legend(fontsize=6)


# Set the yticks. 
ax.set_yticks([0.0, 0.5, 1.0, 1.5, 2.0])
ax.set_yticklabels([0.0, 0.5, 1.0, 1.5, 2.0])
plt.savefig('../../../figures/fishery_source_masses.svg', bbox_inches='tight')

# %%
# Generate the plot of the categorized aquaculture
culture = pd.read_csv('./aquaculture_categorized.csv')
culture = culture[(culture['category']=='carp') |
                  (culture['category']=='shrimp & prawns') |
                  (culture['category']=='oysters, clams, & mussels')]

fig, ax = plt.subplots(1, 1, figsize=(3, 2))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlim([1951, 2017])
ax.set_xlabel('year', fontsize=6)
ax.set_ylabel('estimated standing\npopulation [10$^9$]', fontsize=6)
palette = {'carp':colors['purple'], 'shrimp & prawns':colors['light_red'], 
           'oysters, clams, & mussels':colors['dark_brown']}

for g, d in culture.groupby(['category']):
        label = g
        ax.plot(d['year'], d['population'].values / 1E9, '-o', lw=0.75, 
                ms=1, label=label, color=palette[g])
               
ax.legend(fontsize=6)
plt.savefig('../../../figures/barnyard_number/aquaculture_category_totals.svg')
# # %%




# %%
