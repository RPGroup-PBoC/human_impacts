# -*- coding: utf-8 -*-
#
#################
# This script takes as an input the data 
# from Extended Data Table 1 of Song et al. (2018), imported
# manually from the the manuscript, and returns a csv 
# file with land cover change data for the 1982-2016 period.
#
# Last updated: Aug 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import numpy as np
import pandas as pd

# Concatenate mean and uncertainty values
raw_data = pd.read_csv('../source/global_land_change.csv', delim_whitespace=False)

# Tidy data
data_tidy = raw_data.melt(id_vars=raw_data.columns[:2],
                              var_name="Measure", 
                              value_name="Value (10^3 km2/yr)")

# Save to file, stripped of index
data_tidy.to_csv(r'../processed/global_land_change_processed.csv', index = False)