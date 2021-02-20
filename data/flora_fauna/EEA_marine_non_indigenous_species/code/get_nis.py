# -*- coding: utf-8 -*-
#
#################
# This script takes as input the EEA non-indigenous marine species data in csv format,
# and returns a tidy csv file of the data. Data reported for each period in the original
# source is reported here for the last year of the period. Thus, new NIS should be 
# interpreted as introduced between the year reported and the previous year in the 
# time series, starting in 1949.
#
# Last updated: Feb 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd
import numpy as np
raw_data_ = pd.read_csv('../source/cumulative-number-of-non-indigenous-2.csv', delim_whitespace=False)
proc_data_ = raw_data_.rename(columns = {'Time range:text':'Period',
                            'Year:text' : 'year',
                            'Vertebrates:number':'Vertebrates',
                            'Invertebrates:number':'Invertebrates',
                            'Primary producers:number': 'Primary producers',
                            'Vertebrates (cumulative):number':'Vertebrates (cumulative)',
                            'Invertebrates (cumulative):number':'Invertebrates (cumulative)',
                            'Primary producers (cumulative):number': 'Primary producers (cumulative)'})

# Change period to last year of period, to ensure correct time shift for cumulative numbers
proc_data_['year'] = proc_data_['Period'].str.split('-').str[-1]
proc_data_ = proc_data_[['year', 'Vertebrates', 'Invertebrates', 'Primary producers']]

proc_data_['All species'] = proc_data_['Vertebrates'] + proc_data_['Invertebrates'] + proc_data_['Primary producers']
data_tidy = proc_data_.melt(id_vars=proc_data_.columns[0],
                                var_name="Reported group",
                                value_name="Number")
# Save to file, stripped of index
data_tidy.to_csv(r'../processed/non_ind_marine_species_europe.csv', index = False)