# -*- coding: utf-8 -*-
#
#################
# This script takes as input the Mauna Loa CO2 data in .csv format,
# stripped of the explanatory text,
# and returns a csv file with the processed time series.
# Data is provided in ppm (parts per million).
#
# Last updated: Jan 2022
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd

raw_data_ = pd.read_csv('../source/monthly_in_situ_co2_mlo_clean.csv', delim_whitespace=False,
                        skipinitialspace=True)
# Change columns names to standard format
proc_data_ = raw_data_.rename(columns = {'Yr' : 'year',
                            'Mn':'month',
                            'Date.1': 'date (decimal)',
                            'CO2':'monthly mean',
                            'seasonally': 'season-filtered fit',
                            'fit': 'spline fit, monthly mean',
                            'seasonally.1': 'spline fit, season-filtered',
                            'CO2.1': 'monthly mean, filled',
                            'seasonally.2': 'season-filtered fit, filled'
                            })
# Drop unnecessary columns and rows
proc_data_ = proc_data_.drop(["Date"], axis=1)
proc_data_ = proc_data_.drop([0, 1, 2, 3])

# Fix numerical format
proc_data_[["year", "month"]] = proc_data_[["year", "month"]].astype(int)
proc_data_[["monthly mean", "season-filtered fit", 
            "spline fit, monthly mean",
            "spline fit, season-filtered",
            "monthly mean, filled",
            "season-filtered fit, filled"]
   ] = proc_data_[["monthly mean", "season-filtered fit", 
            "spline fit, monthly mean",
            "spline fit, season-filtered",
            "monthly mean, filled",
            "season-filtered fit, filled"]].astype(float)
proc_data_['date (decimal)'] = round(proc_data_['date (decimal)'], 3)
             
# Fix absent value formatting
proc_data_ = proc_data_.replace(-99.99, '')

# Tidy data
data_tidy = proc_data_.melt(id_vars=proc_data_.columns[:3], 
                                var_name="Reported value", 
                                value_name="Concentration (ppm)")
# # # Save to file, stripped of index
data_tidy.to_csv(r'../processed/monthly_co2_data_processed.csv', index = False)