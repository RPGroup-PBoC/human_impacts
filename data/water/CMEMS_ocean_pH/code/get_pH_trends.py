# -*- coding: utf-8 -*-
#
#################
# This script takes as an input the csv file
# CMEMS_average_ocean_pH.csv and writes the
# csv file CMEMS_trends_ocean_pH.csv, which
# contains the first order finite difference backwards 
# approximation for the yearly change in pH or [H+].
# Change in [H+] is given as a percentage.
#
#
# Last updated: Jan 2021
# Author: Ignacio Lopez-Gomez
# 
#################

#%%
import pandas as pd

data_ = pd.read_csv('../processed/CMEMS_average_ocean_pH.csv', header=0)

trends_ = pd.DataFrame(data_['year'])
trends_["pH trend"] = round(data_["pH"].diff(), 3)
trends_["[H+] percentage trend"] = round((10**(-trends_["pH trend"])-1.0 )
                                         *100, 2)
# Tidy data
data_tidy = trends_.melt(id_vars=trends_.columns[0], 
                              var_name="Measure type", 
                              value_name="Value")

# Save to file, stripped of index
data_tidy.to_csv(r'../processed/CMEMS_trends_ocean_pH.csv', index = False)

# Compute the mean and standard error of the percent change.
percent = data_tidy[data_tidy['Measure type']=='[H+] percentage trend']
mean_perc = percent['Value'].mean()
sem_perc = percent['Value'].std()
print(f'{mean_perc} ± {sem_perc}')
# %%
