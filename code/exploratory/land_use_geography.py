#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.io
import anthro.viz
colors = anthro.viz.plotting_style()

# Define the hardcoded data. 
ag_total = 5E13
ag_land_total = {'India':1.7E12/ag_total, 'USA':1.5E12/ag_total, 'China':1.4E12/ag_total, 'Russia':1.2E12/ag_total}

ag_land_capita = {'Niue':2.5, 'Australia':1.9, 'Kazakhstan':1.6, 'Canada':1.3, 'Argentina':0.9}

fig, ax = plt.subplots(1, 2, figsize=(3, 1))
for a in ax:
    a.xaxis.set_tick_params(labelsize=6)
    a.yaxis.set_tick_params(labelsize=6)


iter = 0
for k, v in ag_land_total.items():
    ax[0].plot(iter, v, 'o', color=colors['red'], ms=3)
    ax[0].vlines(iter, 0, v, lw=1, color=colors['red'])

    iter +=1 
ax[0].set_ylim([0, 0.04])
ax[0].set_xticks([0, 1, 2, 3, 4])
ax[0].set_xticklabels(list(ag_land_total.keys()), rotation=90, fontsize=6)
plt.tight_layout()
# %%
