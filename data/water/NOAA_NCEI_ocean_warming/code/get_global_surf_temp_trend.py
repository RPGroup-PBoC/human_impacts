# -*- coding: utf-8 -*-
#
#################
# This script takes as input the NOAA NCEI global ocean temperature
# dataset in .txt format, and returns a csv file with the processed
# time series. Data provided is temperature anomaly with respect to
# a reference in degrees Celsius.
# 
# The original data file contains 7 columns:
#
# 1st column - year+0.5 (for the yearly vertical mean temperature anomaly);
# 2nd column - time series of vertical mean temperature anomaly of full ocean;
# 3rd column - time series of the standard error of vertical mean temperature anomaly of full ocean;
# 4th column - time series of vertical mean temperature anomaly of northern hemisphere part of the ocean;
# 5th column - time series of the standard error of vertical mean temperature anomaly of northern hemisphere part of the ocean;
# 6th column - time series of vertical mean temperature anomaly of southern hemisphere part of the ocean;
# 7th column - time series of the standard error of vertical mean temperature anomaly of southern hemisphere part of the ocean.
#
# Last updated: Dec 2020
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd

##### 0-100 m layer
proc_data_ = pd.read_csv('../source/T-dC-w0-100m.dat.txt',
    delim_whitespace=True, skipinitialspace=True)
proc_data_['Year'] = (proc_data_['YEAR'] - 0.5).astype(int)
proc_data_['global mean'] = proc_data_['WO']
proc_data_['95% CI'] = proc_data_['WOse']*2.0 # 95% CI is 2 times the standard error (assuming gaussian noise)
proc_data_ = proc_data_.drop(columns=['YEAR', 'WO', 'WOse', 'NH', 'NHse', 'SH', 'SHse'])

# Get mean temperature over 1958-1962 period, following Cheng et al, 2017
mean_ = (proc_data_[(proc_data_['Year']<1963) & (proc_data_['Year']>1957)])['global mean'].mean(axis=0)
# Subtract 1958-1962 mean to data, setting this period as the reference temperature
proc_data_['global mean'] -= mean_

data_tidy_100 = proc_data_.melt(id_vars=proc_data_.columns[0], 
                                var_name="Reported value", 
                                value_name="Temperature anomaly (K)")
data_tidy_100['Layer'] = '0-100 m'

# Get uncertainty of 2019 with respect to 1958-1962 mean, assuming perfect correlation of years 1958-1962,
# and correlation of -1 between 2019 and 1958-1962 mean.
# This correlation leads to the highest possible uncertainty given the summary statistics.
ref_two_std = (proc_data_[(proc_data_['Year']<1963) & (proc_data_['Year']>1957)])['95% CI'].mean(axis=0)
unc_95_2019_wrt_ref = ref_two_std + proc_data_[proc_data_['Year']==2019]['95% CI']
print('95% confidence interval of 0-100 m layer temperature change in 2019 with respect to 1958-1962 reference is',
    unc_95_2019_wrt_ref.values, 'degrees Celsius')

##### 0-700 m layer
proc_data_ = pd.read_csv('../source/T-dC-w0-700m.dat.txt',
    delim_whitespace=True, skipinitialspace=True)
proc_data_['Year'] = (proc_data_['YEAR'] - 0.5).astype(int)
proc_data_['global mean'] = proc_data_['WO']
proc_data_['95% CI'] = proc_data_['WOse']*2.0 # 95% CI is 2 times the standard error (assuming gaussian noise)
proc_data_ = proc_data_.drop(columns=['YEAR', 'WO', 'WOse', 'NH', 'NHse', 'SH', 'SHse'])

# Get mean temperature over 1958-1962 period, following Cheng et al, 2017
mean_ = (proc_data_[(proc_data_['Year']<1963) & (proc_data_['Year']>1957)])['global mean'].mean(axis=0)
# Subtract 1958-1962 mean to data, setting this period as the reference temperature
proc_data_['global mean'] -= mean_

data_tidy_700 = proc_data_.melt(id_vars=proc_data_.columns[0], 
                                var_name="Reported value", 
                                value_name="Temperature anomaly (K)")
data_tidy_700['Layer'] = '0-700 m'
data_tidy = data_tidy_100.append(data_tidy_700)

# Get uncertainty of 2019 with respect to 1958-1962 mean, assuming perfect correlation of years 1958-1962,
# and correlation of -1 between 2019 and 1958-1962 mean.
# This correlation leads to the highest possible uncertainty given the summary statistics.
ref_two_std = (proc_data_[(proc_data_['Year']<1963) & (proc_data_['Year']>1957)])['95% CI'].mean(axis=0)
unc_95_2019_wrt_ref = ref_two_std + proc_data_[proc_data_['Year']==2019]['95% CI']
print('95% confidence interval of 0-700 m layer temperature in 2019 with respect to 1958-1962 reference is',
    unc_95_2019_wrt_ref.values, 'degrees Celsius')

##### 0-2000 m layer
proc_data_ = pd.read_csv('../source/T-dC-w0-2000m.dat.txt',
    delim_whitespace=True, skipinitialspace=True)
proc_data_['Year'] = (proc_data_['YEAR'] - 0.5).astype(int)
proc_data_['global mean'] = proc_data_['WO']
proc_data_['95% CI'] = proc_data_['WOse']*2.0 # 95% CI is 2 times the standard error (assuming gaussian noise)
proc_data_ = proc_data_.drop(columns=['YEAR', 'WO', 'WOse', 'NH', 'NHse', 'SH', 'SHse'])

# Get mean temperature over 1958-1962 period, following Cheng et al, 2017
mean_ = (proc_data_[(proc_data_['Year']<1963) & (proc_data_['Year']>1957)])['global mean'].mean(axis=0)
# Subtract 1958-1962 mean to data, setting this period as the reference temperature
proc_data_['global mean'] -= mean_

data_tidy_2000 = proc_data_.melt(id_vars=proc_data_.columns[0], 
                                var_name="Reported value", 
                                value_name="Temperature anomaly (K)")
data_tidy_2000['Layer'] = '0-2000 m'
data_tidy = data_tidy.append(data_tidy_2000)

# Get uncertainty of 2019 with respect to 1958-1962 mean, assuming perfect correlation of years 1958-1962,
# and correlation of -1 between 2019 and 1958-1962 mean.
# This correlation leads to the highest possible uncertainty given the summary statistics.
ref_two_std = (proc_data_[(proc_data_['Year']<1963) & (proc_data_['Year']>1957)])['95% CI'].mean(axis=0)
unc_95_2019_wrt_ref = ref_two_std + proc_data_[proc_data_['Year']==2019]['95% CI']
print('95% confidence interval of 0-2000 m layer temperature change in 2019 with respect to 1958-1962 reference is',
    unc_95_2019_wrt_ref.values, 'degrees Celsius')

data_tidy = data_tidy[['Year', 'Reported value', 'Layer', 'Temperature anomaly (K)']]
data_tidy['Temperature anomaly (K)'] = round(data_tidy['Temperature anomaly (K)'], 4)
# # # # Save to file, stripped of index
data_tidy.to_csv(r'NOAA_NCEI_global_ocean_temperature.csv', index = False)
