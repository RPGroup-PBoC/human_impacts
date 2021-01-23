# -*- coding: utf-8 -*-
#
#################
# This script takes as input the NASA Ozone Watch dataset in .txt format,
# and returns a csv file with the processed time series of the ozone hole area
# for the period 07 September -- 13 October and daily minimum ozone levels for
# the period 21 September -- 16 October.
# Data provided in millions of km2 (area) and Dobson Units (ozone levels). Data
# for 1995 is missing.
#
# Last updated: Jan 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd

########## Get maximum ozone hole area
proc_data_ = pd.read_csv('../source/to3area_0907-1013_toms+omi+omps.txt',
    delim_whitespace=True, skiprows=5)
# Remove year with missing data
proc_data_ = proc_data_[proc_data_["Year"] != 1995]

# Correct typo in source and change names
proc_data_["Minimum"] = proc_data_["Minumum"]
proc_data_["Mean"] = proc_data_["Data"]
proc_data_ = proc_data_.drop(columns=["Minumum", "Data"])
area_data_tidy = proc_data_.melt(id_vars=proc_data_.columns[0], 
                                var_name="Reported value", 
                                value_name="Value")
area_data_tidy["Units"] = "Millions of km2 (10^12 m2)"
area_data_tidy["Variable"] = "Ozone hole area"

########## Get minimum ozone amount
proc_data_ = pd.read_csv('../source/to3min_0921-1016_toms+omi+omps.txt',
    delim_whitespace=True, skiprows=5)
# Remove year with missing data
proc_data_ = proc_data_[proc_data_["Year"] != 1995]

# Correct typo in source and change names
proc_data_["Minimum"] = proc_data_["Minumum"]
proc_data_["Mean"] = proc_data_["Data"]
proc_data_ = proc_data_.drop(columns=["Minumum", "Data"])
du_data_tidy = proc_data_.melt(id_vars=proc_data_.columns[0], 
                                var_name="Reported value", 
                                value_name="Value")
du_data_tidy["Units"] = "Dobson Units"
du_data_tidy["Variable"] = "Ozone minimum"

# # Concatenate area and ozone levels data, order
data_tidy = pd.concat([area_data_tidy,du_data_tidy], axis=0, ignore_index=True)
data_tidy = data_tidy[['Year', 'Variable', 'Reported value', 'Units', 'Value']]

# # # # Save to file, stripped of index
data_tidy.to_csv(r'../processed/NASA_ozone_hole_evolution_SH_spring.csv', index = False)
