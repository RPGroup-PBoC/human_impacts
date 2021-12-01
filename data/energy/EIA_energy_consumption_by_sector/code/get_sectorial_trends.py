# -*- coding: utf-8 -*-
#
#################
# This script takes as input the EIA sectorial energy consumption data
# in .csv format, stripped of the explanatory text,
# and returns a csv file with the processed time series.
# Original Data are provided in BTU per year, and are converted here to TW.
#
# Last updated: Nov 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd
import numpy as np

raw_data_ = pd.read_csv('../source/Passenger_transportation_energy_use_clean.csv', delim_whitespace=False)
proc_data_ = raw_data_.rename(columns = {
    'World: Light-duty vehicles quad Btu' : 'Passenger light-duty vehicles',
    'World: Air quad Btu':'Passenger air transport',
    'Total World quad Btu': 'Total passenger transport',
    })

# quadrillion BTU/year -> TW, where 1 BTU/year = 3.343e-5 W,
# quadrillion = Peta = 1e15, Tera = 1e12
quad_btu_yr_tw = 3.343e-5*1.0e3
proc_data_['Passenger light-duty vehicles'] = round(
    np.multiply(proc_data_['Passenger light-duty vehicles'], quad_btu_yr_tw),
    3)
proc_data_['Passenger air transport'] = round(
    np.multiply(proc_data_['Passenger air transport'], quad_btu_yr_tw),
    3)
proc_data_['Total passenger transport'] = round(
    np.multiply(proc_data_['Total passenger transport'], quad_btu_yr_tw),
    3)

data_tidy = proc_data_.melt(id_vars=proc_data_.columns[0], 
                                var_name="Reported sector", 
                                value_name="Energy consumption (TW)")

# # Save to file, stripped of index
data_tidy.to_csv(r'../processed/Passenger_transportation_energy_use.csv', index = False)
