#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load the datasets
totals = pd.read_csv('../../../data/land/Curtis2018_global_forest_loss/processed/Curtis2018_table1_total_forest_loss_region.csv')
drivers = pd.read_csv('../../../data/land/Curtis2018_global_forest_loss/processed/Curtis2018_table1_drivers_forest_loss_regions.csv')

# %% Redefine colors to new regions. 
cont_colors = {'north america':colors['light_red'],
               'oceania': colors['dark_green'],
               'latin america': colors['dark_brown'],
               'europe': '#4b4b4b',
               'southeast asia': colors['light_blue'],
               'russia/china/south asia': colors['blue'],
               'africa': colors['light_green']
               }

# Add the colors to the datasets. 
totals['color'] = [cont_colors[k] for k in totals['region'].values]
drivers['color'] = [cont_colors[k] for k in drivers['region'].values]

# Generate the donut for the total. 
fig, ax = plt.subplots(1,1, figsize=(2.5, 2.5))
circ = plt.Circle((0, 0), 0.6, color='white')
totals.sort_values('area_loss_Mha', inplace=True)
ax.pie(totals['area_loss_Mha'], colors=totals['color'])
ax.add_artist(circ)
plt.savefig('../../../figures/regional_breakdowns/total_tree_cover_loss_donut.svg')

# %% Donut for each driver.
for g, d in drivers.groupby(['driver']):
    print(g)
    # Generate the donut for the total. 
    fig, ax = plt.subplots(1,1, figsize=(2.5, 2.5))
    circ = plt.Circle((0, 0), 0.6, color='white')
    d.sort_values('area_Mha', inplace=True)
    ax.pie(d['area_Mha'], colors=d['color'])
    ax.add_artist(circ)
    _driver = g.replace(' ', '_')
    plt.savefig(f'../../../figures/regional_breakdowns/tree_cover_loss_{_driver}_donut.svg')


# %% Compute the percentages.
percs = []
for g, d in drivers.groupby(['driver']):
    d = d.copy()
    tot = d['area_Mha'].sum()
    d['percent'] = 100 * (d['area_Mha'] / tot)
    percs.append(d)

percs = pd.concat(percs)
percs[percs['driver']=='deforestation']


# %%
