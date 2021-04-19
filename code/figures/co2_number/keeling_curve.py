#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import anthro.viz
colors = anthro.viz.plotting_style()

# Extend default matplotlib fonts
font_files = font_manager.findSystemFonts()
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)

# Load the ice core data (0CE - 1960)
ice_data = pd.read_csv('../../../data/atmosphere_biogeochemistry/ice_cores/processed/law2006_by_year_clean.csv')
ice_data = ice_data[ice_data['year_CE'] < 1958]

# Load the mauna loa data (since 1958)
ml_data = pd.read_csv('../../../data/atmosphere_biogeochemistry/mauna_loa_co2_trend/processed/monthly_co2_data_processed.csv')
# Seasonally filtered data for Panels A and B
ml_data_season_filt = ml_data[ml_data['Reported value'] == 'season-filtered fit' ].copy()
ml_data_season_filt['dt'] = [int(y) + m/12 for y, m in zip(ml_data_season_filt['year'].values, ml_data_season_filt['month'].values)]
# Monthly averaged data for Panel C
ml_data = ml_data[ml_data['Reported value'] == 'monthly mean' ]
ml_data['dt'] = [int(y) + m/12 for y, m in zip(ml_data['year'].values, ml_data['month'].values)]

# Format the axes
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
ax[0].plot(ml_data_season_filt['dt'], ml_data_season_filt['Concentration (ppm)'], '-', color=colors['red'],
            lw=0.5)
ax[1].plot(ice_data['year_CE'], ice_data['CO2_spline_fit'], '-', color=colors['red'],
            lw=0.5)
ax[1].plot(ml_data_season_filt['dt'], ml_data_season_filt['Concentration (ppm)'], '-', lw=0.5, color=colors['red'])
ax[2].plot(ml_data['dt'], ml_data['Concentration (ppm)'], '-', marker='.', color=colors['red'], lw=0.5, ms=3)

plt.tight_layout()
plt.savefig('../../../figures/co2_number/keeling_curve.svg')

# %%
