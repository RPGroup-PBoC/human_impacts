# -*- coding: utf-8 -*-
#
#################
# This script takes as input the NOAAGlobalTempv5 dataset in .txt format,
# and returns a csv file with the processed time series.
# Data provided is temperature anomaly with respect to a reference
# in degrees Celsius.
# 
# File name convention for areal average (aravg) time series:
# ann=annual average
# mon=monthly average
# land_ocean=merged land-ocean surface temperature
# land=land surface temperature
# ocean=ocean surface temperature
# latitudes=southern and northern limits of areal average
# v=version number
# yyyymm=date for the latest data

# Annual data (aravg.ann.*) :
# 1st column = year
# 2nd column = anomaly of temperature (K)
# 3rd column = total error variance (K**2)
# 4th column = high-frequency error variance (K**2)
# 5th column = low-frequency error variance (K**2)
# 6th column = bias error variance (K**2)
#
# NOTE: anomalies are based on the climatology from 1971 to 2000
#
# Last updated: Dec 2020
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd
import numpy as np

raw_data_ = pd.read_csv('../source/aravg.ann.land_ocean.90S.90N.v5.0.0.202010.asc.txt',
    delim_whitespace=True, names=['year', 'global mean',
                                  'total error variance',
                                  'high-frequency error variance',
                                  'low-frequency error variance',
                                  'bias error variance',
                                  ])

# First remove 1880-1900 mean
noaa_data = raw_data_[['year', 'global mean']]
noaa_data_1880_1900 = (noaa_data[noaa_data['year']>1880])[noaa_data['year']<1900].mean()['global mean']
#Then add the 1880-1900 mean from the HadCRUT4 dataset to center around the same reference
hadcrut_data = pd.read_csv('../../HadCRUT4_global_temperature_trend/processed/HadCRUT4_global_surf_temperature_trend.csv')
hadcrut_data = hadcrut_data[hadcrut_data['Reported value']=='ensemble median']
hadcrut_data_1880_1900 = (hadcrut_data[hadcrut_data['year']>1880])[hadcrut_data['year']<1900].mean()['Temperature anomaly (K)']
# Remove both references
raw_data_['global mean'] = raw_data_['global mean'] - noaa_data_1880_1900 + hadcrut_data_1880_1900

# Convert variances to standard deviations
raw_data_['total error std'] = np.sqrt(raw_data_['total error variance'])
raw_data_['high-frequency error std'] = np.sqrt(raw_data_['high-frequency error variance'])
raw_data_['low-frequency error std'] = np.sqrt(raw_data_['low-frequency error variance'])
raw_data_['bias error std'] = np.sqrt(raw_data_['bias error variance'])

proc_data_ = raw_data_.drop(['total error variance', 'high-frequency error variance',
                                'low-frequency error variance', 'bias error variance',],
                                axis=1)


data_tidy = proc_data_.melt(id_vars=proc_data_.columns[0], 
                                var_name="Reported value", 
                                value_name="Temperature anomaly (K)")
data_tidy['Temperature anomaly (K)'] = round(data_tidy['Temperature anomaly (K)'], 3)
# # # Save to file, stripped of index
data_tidy.to_csv(r'NOAAGlobalTempv5_global_surf_temperature_trend.csv', index = False)
