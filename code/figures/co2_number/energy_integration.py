#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import anthro.viz 
colors = anthro.viz.plotting_style()

# Compute the estimated exponential growth in energy consumption
dT = 2020-1800
time = np.arange(1800, 2020, 1) 
E_0 = 2E16
C_0 = 2E16
C_contemp = 1E18
k = dT**-1 * np.log2(C_contemp / C_0)
energy = E_0 * 2**((time - 1800) * k)


# Set the bounds for the rects
bins = np.arange(1810, 2020, 20)
bar_energy = E_0 * 2**((bins - 1800) * k)

# Generate the textual labels for the area
labels = [f'{int(np.round((bar_energy[i] * 20)/1E16, decimals=-1))}' + r'$\times 10^{16}$ kJ' for i in range(len(bar_energy))]

# Instantiate canvas and format axes
fig, ax = plt.subplots(1, 1, figsize=(4.5, 2))
ax.xaxis.set_tick_params(labelsize=6)
ax.yaxis.set_tick_params(labelsize=6)
ax.set_xlabel('year [C.E.]', fontsize=6)
ax.set_ylabel('estimated energy usage [10$^{16}$ kJ]', fontsize=6)
ax.set_xlim([1800, 2020])

# Plot the curve
ax.fill_between(time, 0, energy/1E16, color=colors['light_red'], label='__nolegend__')
ax.plot(time, energy/1E16, '-', color=colors['red'], lw=0.75, label='exponential growth')

# Plot the bars in a somewhat stupidway
ax.plot(bins, bar_energy/1E16, 'o', color=colors['blue'], ms=3)
ax.plot([], [], '-o', ms=3, color=colors['blue'], label='approximate integration')
ax.vlines(bins-10, 0, bar_energy/1E16, lw=0.75, color=colors['blue'], zorder=1000,
          label='__nolegend__')
ax.vlines(bins+10, 0, bar_energy/1E16, lw=0.75, color=colors['blue'], zorder=1000,
          label='__nolegend__')
ax.hlines(bar_energy/1E16, bins-10, bins+10, lw=0.75, color=colors['blue'],
         zorder=1000, label='__nolegend__')

# Add textual labels
for i  in range(len(bar_energy)):
    ax.annotate(labels[i], xy=(bins[i], bar_energy[i]/1E16 + 5), rotation=90, 
                color=colors['blue'], fontsize=6, transform=ax.transAxes)
# Add a legend 
ax.legend(fontsize=6)
plt.savefig('../../../figures/co2_number/energy_integration_plot.svg')



# %%
labels

# %%
