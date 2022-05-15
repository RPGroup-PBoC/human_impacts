# -*- coding: utf-8 -*-
#
#################
# This script takes as an input the csv file
# global-air-conditioner-stock-1990-2016.csv from IEA,
# which contains regional information about number of
# A/C units, and computes the worldwide number of A/C units,
# returning a tidy csv file.
#
#
# Last updated: May 2022
# Author: Ignacio Lopez-Gomez
# 
#################

#%%
import pandas as pd

data_ = pd.read_csv('../source/global-air-conditioner-stock-1990-2016.csv', header=0)
cols = ["United States","China","Japan and Korea","European Union","India","Indonesia","Mexico","Brazil","Middle East","Rest of world"]

data_proc = pd.DataFrame(data_)
data_proc["World"] = round(data_[cols].sum(axis=1), 3)

# Tidy data
data_tidy = data_proc.melt(id_vars=data_proc.columns[0], 
                              var_name="Region", 
                              value_name="A/C units (million)")

# Save to file, stripped of index
data_tidy.to_csv(r'../processed/processed_global-air-conditioner-stock-1990-2016.csv', index = False)

