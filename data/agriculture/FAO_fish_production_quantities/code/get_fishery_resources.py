#%%
#################
# This script takes as input the fish stock trends in Figure 19 
# of the FAO STATE OF WORLD FISHERIES AND AQUACULTURE (2020), in .csv format,
# and returns a csv file with the processed time series in tidy format.
#
# Last updated: Feb 2021
# Author: Ignacio Lopez-Gomez
# 
#################

import pandas as pd
import numpy as np

# load the source data and remove FAO totals for re calculation
undfish_data = pd.read_csv('../source/underfished_stocks_percentage.csv')
undfish_p_msf_data = pd.read_csv('../source/max_sust_percentage_plus_underfished_percentage.csv')

# Need to interpolate to the same years
years_ = np.array([1974, 1978, 1979, 1981, 1983, 1985, 1987, 1989, 1990, 1992, 1995, 1997,
    2000, 2004, 2006, 2008, 2009, 2011, 2013, 2015, 2017])
data = pd.DataFrame()
data["year"] = years_
data["underfished_percentage_i"] = np.interp(years_, undfish_data["year"], undfish_data["underfished_percentage"])
data["underfished_plus_msf_percentage_i"] = np.interp(years_, undfish_p_msf_data["year"], undfish_p_msf_data["underfished_plus_msf_percentage"])

data['maximally sustainably fished'] = round(data["underfished_plus_msf_percentage_i"] - data["underfished_percentage_i"], 1)
data['underfished'] = round(data["underfished_percentage_i"], 1)
data['overfished'] = round(100 - data["underfished_plus_msf_percentage_i"], 1)
data = data.drop(columns=["underfished_plus_msf_percentage_i", "underfished_percentage_i"])

# Tidy data
data_tidy = data.melt(id_vars=data.columns[:1], 
                                var_name="Fishery status", 
                                value_name="Percentage of fish stocks")
data_tidy.to_csv(r'../processed/marine_fish_stock_state.csv', index = False)
# %%