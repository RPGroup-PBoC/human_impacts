"""
This script calculates the annual trend of the average
sea ice extent from 1979-2019. A file is generated that contains
this trend.

"""

import numpy as np
import pandas as pd

#%%
annual_average_extents = pd.read_csv("processed/NOAA_sea_ice_index_annual_average.csv")

x = annual_average_extents.year
y = annual_average_extents.average_extent_sq_meter

linear_fit = np.polyfit(x,y,1)
annual_loss = linear_fit[0]
df_list = [["annual", annual_loss]]
df = pd.DataFrame(df_list, columns = ["period", "trend_sq_meter_per_yr"])

df.to_csv('processed/NOAA_sea_ice_index_annual_trend.csv')
#%%
