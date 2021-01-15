# -*- coding: utf-8 -*-
#
#################
# This script takes as input the HadCRUT4 dataset in .txt format,
# and returns a csv file with the processed time series.
# Data provided is temperature anomaly with respect to a reference
# in degrees Celsius.
# 
# The original data file contains 12 columns:
# Column 1 is the date.
# Column 2 is the median of the 100 ensemble member time series.
# Columns 3 and 4 are the lower and upper bounds of the 95% confidence interval of
#   bias uncertainty computed from the 100 member ensemble.
# Columns 5 and 6 are the lower and upper bounds of the 95% confidence interval of
#   measurement and sampling uncertainties around the ensemble median. These are the
#  combination of fully uncorrelated measurement and sampling uncertainties and 
#   partially correlated uncertainties described by the HadCRUT4 error covariance matrices.
# Columns 7 and 8 are the lower and upper bounds of the 95% confidence interval of
#   coverage uncertainties around the ensemble median.
# Columns 9 and 10 are the lower and upper bounds of the 95% confidence interval of
#   the combination of measurement and sampling and bias uncertainties.
# Columns 11 and 12 are the lower and upper bounds of the 95% confidence interval of
#   the combined effects of all the uncertainties described in the HadCRUT4 error model (measurement and sampling, bias and coverage uncertainties).
#
# Last updated: Jan 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd

proc_data_ = pd.read_csv('../source/HadCRUT.4.6.0.0.annual_ns_avg.txt',
    delim_whitespace=True, names=['year', 'ensemble median',
                                  'low. bound, 95% CI bias unc.', 'upp. bound, 95% CI bias unc.',
                                  'low. bound, 95% CI sampling unc.', 'upp. bound, 95% CI sampling unc.',
                                  'low. bound, 95% CI coverage unc.', 'upp. bound, 95% CI coverage unc.',
                                  'low. bound, 95% CI bias + sampling unc.', 'upp. bound, 95% CI bias + sampling unc.',
                                  'low. bound, 95% CI total uncertainty', 'upp. bound, 95% CI total uncertainty',
                                  ])

# Remove 1850-1900 mean to ensure consistency with other datasets
hadcrut_data_ref = proc_data_[['year', 'ensemble median']]
hadcrut_data_1850_1900 = hadcrut_data_ref[hadcrut_data_ref['year']<1900].mean()['ensemble median']
proc_data_['ensemble median'] = proc_data_['ensemble median'] - hadcrut_data_1850_1900
proc_data_['low. bound, 95% CI bias unc.'] = proc_data_['low. bound, 95% CI bias unc.'] - hadcrut_data_1850_1900
proc_data_['upp. bound, 95% CI bias unc.'] = proc_data_['upp. bound, 95% CI bias unc.'] - hadcrut_data_1850_1900
proc_data_['low. bound, 95% CI sampling unc.'] = proc_data_['low. bound, 95% CI sampling unc.'] - hadcrut_data_1850_1900
proc_data_['upp. bound, 95% CI sampling unc.'] = proc_data_['upp. bound, 95% CI sampling unc.'] - hadcrut_data_1850_1900
proc_data_['low. bound, 95% CI coverage unc.'] = proc_data_['low. bound, 95% CI coverage unc.'] - hadcrut_data_1850_1900
proc_data_['low. bound, 95% CI bias + sampling unc.'] = proc_data_['low. bound, 95% CI bias + sampling unc.'] - hadcrut_data_1850_1900
proc_data_['upp. bound, 95% CI bias + sampling unc.'] = proc_data_['upp. bound, 95% CI bias + sampling unc.'] - hadcrut_data_1850_1900
proc_data_['low. bound, 95% CI total uncertainty'] = proc_data_['low. bound, 95% CI total uncertainty'] - hadcrut_data_1850_1900
proc_data_['upp. bound, 95% CI total uncertainty'] = proc_data_['upp. bound, 95% CI total uncertainty'] - hadcrut_data_1850_1900

data_tidy = proc_data_.melt(id_vars=proc_data_.columns[0], 
                                var_name="Reported value", 
                                value_name="Temperature anomaly (K)")
data_tidy['Temperature anomaly (K)'] = round(data_tidy['Temperature anomaly (K)'], 3)
# # # Save to file, stripped of index
data_tidy.to_csv(r'../processed/HadCRUT4_global_surf_temperature_trend.csv', index = False)
