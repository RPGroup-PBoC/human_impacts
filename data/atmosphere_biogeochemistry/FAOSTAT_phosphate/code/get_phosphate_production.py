# -*- coding: utf-8 -*-
#
#################
# This script takes as input the FAOSTAT phosphate production for agriculture and
# agricultural use, with data in .csv format,
# and returns a csv file with the processed time series.
# Original data is provided in tonnes of phosphate (P2O5).
#
# Last updated: May 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd

proc_data_ = pd.read_csv('../source/FAOSTAT_phosphate_5-11-2021.csv',
        delim_whitespace=False,
        usecols=["Year", "Unit", "Value", "Element", "Item"])

# Tidy data
proc_data_["Item"] = "Nutrient phosphate (P2O5)"
proc_data_["Value"] = round(proc_data_["Value"]/1.0e6, 3)
proc_data_["Unit"] = "Mt"

# # # # Save to file, stripped of index
proc_data_.to_csv(r'../processed/FAOSTAT_phosphate_processed.csv', index = False)
