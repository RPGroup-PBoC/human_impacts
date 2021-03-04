#################
# This script converts the HadISDH data in .dat format to a CSV file in tidy format
# with the processed time series. The data provided are relative humidity anomalies
# with respect to a 1981-2010 reference in %rh. Uncertainty estimates are 2 sigma.

# The original data file contains 10 columns:
# Column 1 is the date in year.decimal format.
# Column 2 is the relative humidity anomaly.
# Columns 3 and 4 are the lower and upper bounds of the within gridbox
#    sampling uncertainty.
# Columns 5 and 6 are the lower and upper bounds of the regional gridbox coverage
#   uncertainty.
# Columns 7 and 8 are the lower and upper bounds of the station uncertainty
#     (climatology, measurement and homogeneity adjustment).
# Columns 9 and 10 are the lower and upper bounds of the combined uncertainty.
#
# Last updated: March 2021
# Author: Nicholas S. Sarai
#
#################

import pandas as pd
from PyAstronomy import pyasl

proc_data = pd.read_csv('../source/HadISDH.blendRH.1.0.0.2019fSHIP_global_annual_full_anoms8110_JAN2020.dat',
                        header=None, delim_whitespace=True, engine = 'python',
                        names=['year', 'anomaly', 'low. bound within gridbox sampling uncertainty', 'upp.bound within gridbox sampling uncertainty',
                              'low. bound regional gridbox coverage uncertainty', 'upp. bound regional gridbox coverage uncertainty', 'low. bound station uncertainty (climatology, measurement and homogeneity adjustment)',
                              'upp. bound station uncertainty (climatology, measurement and homogeneity adjustment)', 'low. bound combined uncertainty', 'upp. bound combined uncertainty']
                       )

proc_data_clean = proc_data.drop([47,48,49])

proc_data_clean['year'] = pd.to_numeric(proc_data_clean['year']).astype(int)

data_tidy = proc_data_clean.melt(id_vars=proc_data_clean.columns[0],
                                var_name="Reported value",
                                value_name="Relative humidity anomaly (%rh)")

data_tidy.to_csv(r'../processed/HadISDH_relative_humidity_1973-2019.csv', index = False)
