# -*- coding: utf-8 -*-
#
#################
# This script takes as input the EDGARv5 air pollution data in .csv format,
# stripped of the explanatory text,
# and returns a csv file with the processed time series.
# Data is provided in Gg (10^9 grams).
#
# Last updated: Feb 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd

sources = ['PM2.5', 'PM10', 'NMVOC', 'BC', 'SO2']
for source_ in sources:
    raw_data_ = pd.read_csv('../source/v50_'+str(source_)+'_1970_2015_totals.csv', delim_whitespace=False)
    # Delete empty columns
    raw_data_ = raw_data_[raw_data_.columns[:-2]]
    raw_data_.loc['World']= raw_data_.sum(numeric_only=True, axis=0)
    raw_data_.loc['World', 'IPCC-Annex'] = 'N/A'
    raw_data_.loc['World', 'World Region'] = 'World'
    raw_data_.loc['World', 'ISO_A3'] = 'N/A'
    raw_data_.loc['World', 'Name'] = 'World'

    data_tidy = raw_data_.melt(id_vars=raw_data_.columns[:4], 
                                    var_name="Year", 
                                    value_name="Emissions (Gg)")

    # # Save to file, stripped of index
    data_tidy.to_csv(r'../processed/'+str(source_)+'_emissions_processed.csv', index = False)