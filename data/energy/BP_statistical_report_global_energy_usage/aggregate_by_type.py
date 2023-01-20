# %%
import pandas as pd
import glob
files = glob.glob('processed/consumption_by_type/*.csv')

# Compile all types into a single datafile
compiled = pd.concat([pd.read_csv(f) for f in files])

# Load total
total = pd.read_csv('processed/bp_total_energy_consumption.csv')
total['type'] = 'total'

# compile to renewables (+ hydro) and fossil fuels
renew = compiled[compiled['type'].isin(
    ['solar', 'wind', 'hydroelectric', 'geothermal/biomass/other'])]
fossil = compiled[compiled['type'].isin(['natural gas', 'oil', 'coal'])]
renew = renew.groupby(['year'])['consumption_EJ_yr'].sum().reset_index()
fossil = fossil.groupby(['year'])['consumption_EJ_yr'].sum().reset_index()
fossil['type'] = 'fossil fuels'
renew['type'] = 'renewables + hydro'

# Recompile for a single table
compiled = pd.concat([compiled, total, renew, fossil], sort=False)
compiled['consumption_TW'] = (
    compiled['consumption_EJ_yr'].values * 1E6) / 3.154E7
compiled.to_csv('processed/bp_consumption_by_type.csv', index=False)
