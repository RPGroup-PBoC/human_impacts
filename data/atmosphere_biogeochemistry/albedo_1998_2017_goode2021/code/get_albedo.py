#################
# This script takes as input the Earthshine albedo data from
# Goode et al (GRL, 2021) in .txt format, as well as the
# uncertainty bands of their figure 3,
# and returns a csv file with the processed time series.
# Data is provided in W/m2.
#
# Last updated: Oct 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import copy
import numpy as np
import pandas as pd

raw_data_ = pd.read_csv('../source/Earthshine.txt',
    delim_whitespace=True, skipinitialspace=True)
upper_unc_band = pd.read_csv('../source/Earthshine_upper_uncertainty_band.csv',
    delim_whitespace=False, skipinitialspace=True)
lower_unc_band = pd.read_csv('../source/Earthshine_lower_uncertainty_band.csv',
    delim_whitespace=False, skipinitialspace=True)

proc_data = copy.deepcopy(raw_data_.round(3))

proc_data["Upper error margin"] = np.round(np.interp(proc_data["Date"],
    upper_unc_band["Date"], upper_unc_band["Albedo_anomaly_upper"]), 3)
proc_data["Lower error margin"] = np.round(np.interp(proc_data["Date"],
    lower_unc_band["Date"], lower_unc_band["Albedo_anomaly_lower"]), 3)

proc_data = proc_data.rename(columns = {'Date': 'year',
                                        'Albedo_anomaly': 'Measured value'})
# Tidy data
data_tidy = proc_data.melt(id_vars=proc_data.columns[0], 
                                var_name="Reported quantity", 
                                value_name="Albedo anomaly (W/m2)")
# # # Save to file, stripped of index
data_tidy.to_csv(r'../processed/earthshine_data.csv', index = False)