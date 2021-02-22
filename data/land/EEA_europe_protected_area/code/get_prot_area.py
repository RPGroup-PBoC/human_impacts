# -*- coding: utf-8 -*-
#
#################
# This script takes as input the EEA protected area data in csv format,
# and returns a tidy csv file of the data in units of millions of km2.
#
# Last updated: Feb 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd
import numpy as np
raw_data_ = pd.read_csv('../source/growth-of-the-nationally-designated-5.csv', delim_whitespace=False)
proc_data_ = raw_data_.rename(columns = {'Region:text':'Region',
                            'Year:text' : 'year',
                            'Cumulative area (km2):number':'Area',
                            'cumulative number of sites:number': 'Number of sites'})
proc_data_['Units'] = 'km2'
proc_data_ = proc_data_[['Region', 'year', 'Units', 'Area', 'Number of sites']]

data_tidy = proc_data_.melt(id_vars=proc_data_.columns[:3],
                                var_name="Reported value",
                                value_name="Value")
data_tidy['Value'] = round(data_tidy['Value'], 1)
data_tidy['Units'] = np.where( data_tidy['Reported value'].str.contains("Number of sites"), 'N/A', 'km2')
# # # Save to file, stripped of index
data_tidy.to_csv(r'../processed/protected_land_area_europe.csv', index = False)