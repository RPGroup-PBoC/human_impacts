# -*- coding: utf-8 -*-
#
#################
# This script takes as input the manually processed GISTEMP v4 dataset in .csv format,
# and returns a csv file with the tidy time series with respect to the 
# 1850-1900 HadCRUT4 mean.
#
# Data originally provided is temperature anomaly with respect to 
# the 1951-1980 climatology in degrees Celsius.
#
# Last updated: Dec 2020
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd
import numpy as np

proc_data_ = pd.read_csv('../processed/Land-OceanTemperatureIndex.csv')

# First remove 1880-1900 mean
giss_data_1880_1900 = (proc_data_[proc_data_['Year']>1880])[proc_data_['Year']<1900].mean()['°C']
# Then add the 1880-1900 mean from the HadCRUT4 dataset to center around the same reference
hadcrut_data = pd.read_csv('../../HadCRUT4_global_temperature_trend/processed/HadCRUT4_global_surf_temperature_trend.csv')
hadcrut_data = hadcrut_data[hadcrut_data['Reported value']=='ensemble median']
hadcrut_data_1880_1900 = (hadcrut_data[hadcrut_data['year']>1880])[hadcrut_data['year']<1900].mean()['Temperature anomaly (K)']
# Remove both references
proc_data_ ['°C'] = proc_data_ ['°C'] - giss_data_1880_1900 + hadcrut_data_1880_1900

# Convert variances to standard deviations
proc_data_['global mean'] = proc_data_['°C']
proc_data_['low. bound, 95% CI bias unc.'] = proc_data_['°C_lower']
proc_data_['upp. bound, 95% CI bias unc.'] = proc_data_['°C_upper']
proc_data_['95% CI'] = proc_data_['ci95']

proc_data_ = proc_data_.drop(['°C', '°C_lower','°C_upper', 'ci95'], axis=1)

data_tidy = proc_data_.melt(id_vars=proc_data_.columns[0], 
                                var_name="Reported value", 
                                value_name="Temperature anomaly (K)")
data_tidy['Temperature anomaly (K)'] = round(data_tidy['Temperature anomaly (K)'], 3)
# # # Save to file, stripped of index
data_tidy.to_csv(r'GISTEMPv4_global_surf_temperature_trend.csv', index = False)
