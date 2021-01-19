# -*- coding: utf-8 -*-
#
#################
# This script takes as input the JMA global surface temperature dataset
# in .csv format, and returns a csv file with the processed time series.
# Data provided is temperature anomaly with respect to a reference
# in degrees Celsius.
# 
#
# NOTE: anomalies are based on the climatology from 1981 to 2010, and converted to
# anomalies with respect to the 1850-1900 period of the HadCRUT4 dataset.
#
# Last updated: Jan 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd
import numpy as np

raw_data_ = pd.read_csv('../source/year_wld.csv',
    delim_whitespace=False)


# # First remove 1890-1900 mean
raw_data_['Temperature anomaly (K)'] = raw_data_['Global'].astype(float)
jma_data = raw_data_[['Year', 'Temperature anomaly (K)']].copy()
jma_data['Year'] = jma_data['Year'].astype(int)
jma_data_1890_1900 = jma_data[(jma_data['Year']>1890) & (jma_data['Year']<1900)].mean()['Temperature anomaly (K)']
# #Then add the 1890-1900 mean from the HadCRUT4 dataset to center around the same reference
hadcrut_data = pd.read_csv('../../HadCRUT4_global_temperature_trend/processed/HadCRUT4_global_surf_temperature_trend.csv')
hadcrut_data = hadcrut_data[hadcrut_data['Reported value']=='ensemble median']
hadcrut_data_1890_1900 = hadcrut_data[(hadcrut_data['year']>1890) & (hadcrut_data['year']<1900)].mean()['Temperature anomaly (K)']
# # Remove both references
jma_data['Temperature anomaly (K)'] = jma_data['Temperature anomaly (K)'] - jma_data_1890_1900 + hadcrut_data_1890_1900

jma_data['Temperature anomaly (K)'] = round(jma_data['Temperature anomaly (K)'], 3)
# # # # Save to file, stripped of index
jma_data.to_csv(r'../processed/JMA_global_surf_temperature_trend.csv', index = False)
