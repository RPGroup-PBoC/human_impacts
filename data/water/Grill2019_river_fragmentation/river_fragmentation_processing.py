"""
This script reads the the long form dataset and trims it. It
does this by grouping the dataset by free-flowing status, continent, and
ocean connectivity. The script then individually sums the length,
volume, and discharge of the river reaches within each category.
"""

import pandas as pd

#%%

# Set to the directory that your csv file is in
# data_dir = curr_dir + "RiverReaches.csv"
data_dir = ""
RiverReaches = pd.read_csv(data_dir + "RiverReaches.csv", low_memory=False)
river_df = pd.DataFrame(RiverReaches)

# group by the three most important variables and sum the values of the other variables
river_df_summary = river_df.groupby(["CSI_FF1", "CONTINENT", 'BB_OCEAN']).sum().reset_index()

# keep desired variables
river_df_summary = river_df_summary[['CONTINENT','CSI_FF1', 'BB_OCEAN','LENGTH_KM', 'VOLUME_TCM', 'DIS_AV_CMS']]

# convert thousant cubic meters to cubic meters
river_df_summary['VOLUME_TCM'] = river_df_summary['VOLUME_TCM'].apply(lambda x: x * 1000)

# convert numeric representations of free flowing status and ocean connectivity to strings
river_df_summary['BB_OCEAN'] = river_df_summary['BB_OCEAN'].replace(1,"directly connected to ocean")
river_df_summary['BB_OCEAN'] = river_df_summary['BB_OCEAN'].replace(0,"non directly connected to ocean")
river_df_summary['CSI_FF1'] = river_df_summary['CSI_FF1'].replace(3,"non-free-flowing")
river_df_summary['CSI_FF1'] = river_df_summary['CSI_FF1'].replace(1,"free-flowing")
river_df_summary

# rename columns
river_df_summary.columns = ['region','free_flowing_status','ocean_connectivity','length_km','volume_m^3','discharge_m^3_s-1']

# group by free flowing status and ocean connectivity at the global scale
river_df_global = river_df_summary.groupby(["free_flowing_status", 'ocean_connectivity']).sum().reset_index()
river_df_global['region'] = ["Global", "Global", "Global", "Global"]

# group by free flowing status at the global scale
river_df_global_all = river_df_summary.groupby(["free_flowing_status"]).sum().reset_index()
river_df_global_all['region'] = ["Global", "Global"]
river_df_global_all['ocean_connectivity'] = ["all rivers", "all rivers"]

# concatenate dataframes and reorder columns
river_df_final = pd.concat([river_df_summary, river_df_global, river_df_global_all])
river_df_final = river_df_final[['region', 'free_flowing_status', 'ocean_connectivity', 'length_km', 'volume_m^3', 'discharge_m^3_s-1']]

river_df_final.to_csv('processed/Grill_et_al_river_fragmentation_summary.csv')
# %%
