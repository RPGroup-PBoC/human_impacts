#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import anthro.viz 
colors = anthro.viz.plotting_style()

# Load the ice core data (0CE - 1960)
ice_data = pd.read_csv('../../../data/atmosphere_biogeochemistry/ice_cores/law2006_by_year_formatted.csv')
ice_data = ice_data[ice_data['year_CE'] < 1958]

# Load the mauna loa data (since 1958)
ml_data = pd.read_csv('../../../data/atmosphere_biogeochemistry/mauna_loa/monthly_in_situ_co2_mlo_formatted.csv')
ml_data = ml_data[ml_data['CO2_fit_ppm'] > 0 ]
ml_data['dt'] = [int(y) + m/12 for y, m in zip(ml_data['year'].values, ml_data['month'].values)]


# FOrmat the axes
fig, ax = plt.subplots(1, 3, figsize=(6, 2))
for a in ax:
    a.xaxis.set_tick_params(labelsize=6)
    a.yaxis.set_tick_params(labelsize=6)
    a.set_xlabel('year [C.E.]', fontsize=6)
    a.set_ylabel('CO$_2$ concentration [ppm]', fontsize=6)

anthro.viz.titlebox(ax[0], 'historical trend', size=6, color='black', 
                    bgcolor=colors['pale_yellow'], boxsize=0.08)
anthro.viz.titlebox(ax[1], 'modern trend', size=6, color='black', 
                    bgcolor=colors['pale_yellow'], boxsize=0.08)
anthro.viz.titlebox(ax[2], 'seasonal trend', size=6, color='black', 
                    bgcolor=colors['pale_yellow'], boxsize=0.08)

ax[1].set_xlim([1800, 2020])
ax[2].set_xlim([2016.58, 2020.58])
ax[2].set_ylim([400, 420])
ax[0].plot(ice_data['year_CE'], ice_data['CO2_spline_fit'], '-', color=colors['red'],
            lw=0.5)
ax[0].plot(ml_data['dt'], ml_data['CO2_fit_ppm'], '-', color=colors['red'],
            lw=0.5)
ax[1].plot(ice_data['year_CE'], ice_data['CO2_spline_fit'], '-', color=colors['red'],
            lw=0.5)
ax[1].plot(ml_data['dt'], ml_data['CO2_fit_ppm'], '-', lw=0.5, color=colors['red'])
ax[2].plot(ml_data['dt'], ml_data['CO2_fit_ppm'], '-', marker='.', color=colors['red'], lw=0.5, ms=3)

plt.tight_layout()
plt.savefig('../../../figures/co2_number/keeling_curve.svg')

# %%
