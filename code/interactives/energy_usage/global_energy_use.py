#%%
import numpy as np
import pandas as pd
import bokeh.io 
import bokeh.plotting
import bokeh.palettes
from bokeh.models import * 
import bokeh.transform
import bokeh.layouts
import anthro.viz
colors, palette = anthro.viz.bokeh_theme()
bokeh.io.output_file('./global_energy_use.html')

# Load the datasets
power_data = pd.read_csv('../../../data/energy/BP_statistical_report_global_energy_usage/processed/BP_global_energy_usage_by_type.csv')
pop_data = pd.read_csv('../../../data/anthropocene/FAOSTAT_world_population/processed/FAOSTAT_human_population.csv')

# By year, compute the per capita power. 
for g, d in pop_data.groupby(['year']):
    power_data.loc[power_data['year']==g, 'population_Bhd'] = d['population_Mhd'].values[0] * 1E6
power_data['W_per_captia'] = power_data['consumption_TW'].values * 1E12 / power_data['population_Bhd'].values

# By year, compute the fractional occupancy. 
dfs = []
for g, d in power_data.groupby(['year']):
    tot_power = d['consumption_TW'].sum()
    tot_per_capita = d['W_per_captia'].sum()
    for _g, _d in d.groupby('type'):
        _d = d.copy()
        _d['frac_of_total'] = d['consumption_TW'].values / tot_power
        _d['frac_of_capita'] = d['W_per_captia'].values / tot_per_capita
        dfs.append(_d)
pop_source_df = pd.concat(dfs, sort=False)


# Compute the angles for the donut charts. 
pop_source_df['total_angle'] = 2 * np.pi * pop_source_df['frac_of_total'].values
pop_source_df['capita_angle'] = 2 * np.pi * pop_source_df['frac_of_capita'].values
pop_source_df.head()




# %%

# %%
