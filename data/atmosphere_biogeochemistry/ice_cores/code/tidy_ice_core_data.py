# -*- coding: utf-8 -*-
#
#################
# This script takes as an input the ice core data 
# from MacFarling Meure et al. (2006), imported in csv format from
# the original .xlsx file, and returns a csv file with
# tidy inferred atmospheric concentrations since year 1 of the current era.
#
# Last updated: Apr 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import numpy as np
import pandas as pd

######### Get clean ice core data #########
data_ = pd.DataFrame(pd.read_csv('../processed/law2006_by_year_clean.csv', header=0))

# # Aggregate data
proc_data = pd.DataFrame()
proc_data['Year'] = data_['year_CE']
proc_data['CH4 concentration (ppb)'] = data_['CH4_spline_fit'].to_numpy()
proc_data['CO2 concentration (ppm)'] = data_['CO2_spline_fit'].to_numpy()
proc_data['N2O concentration (ppb)'] = data_['N2O_spline_fit'].to_numpy()

# # Tidy data
data_tidy = proc_data.melt(id_vars=proc_data.columns[:1], 
                                var_name="Measurement type", 
                                value_name="Value (Spline fit)")

data_tidy.to_csv(r'../processed/ice_core_measurements_co2_ch4_n2o.csv', index = False)
