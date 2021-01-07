# -*- coding: utf-8 -*-
#
#################
# This script takes as input the NOAA GML CH4 data in .txt format,
# stripped of the explanatory text,
# and returns a csv file with the processed time series.
# Data is provided in ppb (parts per billion).
#
# Last updated: Jan 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd

raw_data_ = pd.read_csv('../source/monthly_global_ch4_data_clean.txt', delim_whitespace=True)
proc_data_ = raw_data_.rename(columns = {'decimal' : 'date (decimal)',
                            'average':'monthly mean',
                            'average_unc': 'mon. mean 1-sigma unc.',
                            'trend':'season-filtered fit',
                            'trend_unc': 'fit 1-sigma unc.'})
proc_data_['date (decimal)'] = round(proc_data_['date (decimal)'], 3)

data_tidy = proc_data_.melt(id_vars=proc_data_.columns[:3], 
                                var_name="Reported value", 
                                value_name="Concentration (ppb)")

# Fix absent value formatting
data_tidy["Concentration (ppb)"] = data_tidy["Concentration (ppb)"].astype(float)
data_tidy["Concentration (ppb)"] = data_tidy["Concentration (ppb)"].where(data_tidy["Concentration (ppb)"] > 0)

# # Save to file, stripped of index
data_tidy.to_csv(r'monthly_global_ch4_data_processed.csv', index = False)