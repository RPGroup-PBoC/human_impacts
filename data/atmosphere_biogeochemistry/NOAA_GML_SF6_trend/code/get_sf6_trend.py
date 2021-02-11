# -*- coding: utf-8 -*-
#
#################
# This script takes as input the NOAA GML SF6 data in .txt format,
# stripped of the explanatory text,
# and returns a csv file with the processed time series.
# Data is provided in ppt (parts per trillion).
#
# Last updated: Feb 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd

raw_data_ = pd.read_csv('../source/monthly_global_sf6_data_clean.txt', delim_whitespace=True)
proc_data_ = raw_data_.rename(columns = {'decimal' : 'date (decimal)',
                            'average':'monthly mean',
                            'average_unc': 'mon. mean 1-sigma unc.',
                            'trend':'season-filtered fit',
                            'trend_unc': 'fit 1-sigma unc.'})
proc_data_['date (decimal)'] = round(proc_data_['date (decimal)'], 3)

data_tidy = proc_data_.melt(id_vars=proc_data_.columns[:3], 
                                var_name="Reported value", 
                                value_name="Concentration (ppt)")

# Fix absent value formatting
data_tidy["Concentration (ppt)"] = data_tidy["Concentration (ppt)"].astype(float)
data_tidy["Concentration (ppt)"] = data_tidy["Concentration (ppt)"].where(data_tidy["Concentration (ppt)"] > 0)

# # Save to file, stripped of index
data_tidy.to_csv(r'../processed/monthly_global_sf6_data_processed.csv', index = False)