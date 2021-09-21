# -*- coding: utf-8 -*-
#
#################
# This script takes as input the EPA automotive trends in .csv format,
# and returns a csv file with tidy data
#
# Last updated: Sep 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd

raw_data_ = pd.read_csv('../source/table_export.csv', delim_whitespace=False)
raw_data_ = raw_data_.drop(columns=['Footprint (sq. ft.)'])

data_tidy = raw_data_.melt(id_vars=raw_data_.columns[:3], 
                                var_name="Reported quantity", 
                                value_name="Reported value")

data_tidy = data_tidy.replace('Prelim. 2020', 2020)
data_tidy = data_tidy.replace('Real-World MPG', 'Real-world fuel economy (MPG)')
data_tidy = data_tidy.replace('Real-World MPG_City', 'Real-world city fuel economy (MPG)')
data_tidy = data_tidy.replace('Real-World MPG_Hwy', 'Real-world highway fuel economy (MPG)')
data_tidy = data_tidy.replace('Real-World CO2 (g/mi)', 'Real-world CO2 emissions (g/mi)')
data_tidy = data_tidy.replace('Real-World CO2_City (g/mi)', 'Real-world city CO2 emissions (g/mi)')
data_tidy = data_tidy.replace('Real-World CO2_Hwy (g/mi)', 'Real-world highway CO2 emissions (g/mi)')
data_tidy["Reported value"] = round(data_tidy["Reported value"], 3)

# # Save to file, stripped of index
data_tidy.to_csv(r'../processed/tidy_automotive_trends.csv', index = False)