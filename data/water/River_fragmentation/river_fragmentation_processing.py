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

# convert non-free-flowing entries to 0
river_df_summary['CSI_FF1'] = river_df_summary['CSI_FF1'].replace(3,0)

#rename columns
river_df_summary.columns = ['continent','free_flowing_status','ocean_connectivity','length_km','volume_m^3','discharge_m^3_s-1']
del river_df_summary['']

river_df_summary.to_csv('processed/river_fragmentation_summary.csv')
# %%
