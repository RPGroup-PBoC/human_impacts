# -*- coding: utf-8 -*-
#
#################
# This script takes as input the manually processed Table 2 from the corrigendum of
# Fry et al (2018) in .csv format, and returns a csv file with the tidy data.
#
# Last updated: Mar 2021
# Author: Ignacio Lopez-Gomez
#
#################
import pandas as pd
import numpy as np

orig_data_ = pd.read_csv('../source/aquaculture_efficiencies_table2_corr.csv')
mean_data_ = orig_data_.copy(deep=True)
mean_data_['Measure type'] = 'mean'
groups = ['Beef','Poultry','Pork','Tilapia','Whiteleg shrimp','Atlantic salmon',
            'Common carp','Grass carp']
for g_ in groups:
    mean_data_[g_] = orig_data_[g_]

proc_data_ = mean_data_
proc_data_ = proc_data_[['Parameter', 'Units', 'Measure type',
                'Beef','Poultry','Pork','Tilapia','Whiteleg shrimp','Atlantic salmon',
            'Common carp','Grass carp']]
data_tidy = proc_data_.melt(id_vars=proc_data_.columns[0:3],
                                var_name="Product", 
                                value_name="Value")
# # # Save to file, stripped of index
data_tidy = data_tidy.sort_values(by=['Parameter', 'Measure type', 'Product'])
data_tidy.to_csv(r'../processed/aquaculture_efficiencies.csv', index = False)
