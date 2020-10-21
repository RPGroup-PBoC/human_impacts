"""
This script concatenates the data files for each month of
sea ice data into a longform tidy version. A separate file is
generated for each hemisphere. The satellite had issues in
Dec 1987 and Jan 1988 and no data were recorded. These lines
can simply be removed by uncommenting lines as below.

"""

import pandas as pd
import glob

#%%
south_fnames = glob.glob('source/south/data/*')
north_fnames = glob.glob('source/north/data/*')
south_dfs = [pd.read_csv(f) for f in south_fnames]
north_dfs = [pd.read_csv(f) for f in north_fnames]

south_df = pd.concat(south_dfs)
south_df.columns = ['year', 'month', 'data-type', 'region', 'extent_million_sq_km', 'area_million_sq_km']
#south_df = south_df[south_df.extent > 0] # uncomment this line to remove Dec 1987 and Jan 1988 when satellite was having problems
south_df = south_df.sort_values(by=['month', 'year'])
south_df = south_df.reset_index(drop = True)
south_df.to_csv('processed/south_processed.csv')

north_df = pd.concat(north_dfs)
north_df.columns = ['year', 'month', 'data-type', 'region', 'extent_million_sq_km', 'area_million_sq_km']
#north_df = north_df[north_df.extent > 0] # uncomment this line to remove Dec 1987 and Jan 1988 when satellite was having problems
north_df = north_df.sort_values(by=['month', 'year'])
north_df = north_df.reset_index(drop = True)
north_df.to_csv('processed/north_processed.csv')
# %%
