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
import numpy as np

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

#######
# Save uncertainty data from EDGARv4.32 to csv, Table S4 from Crippa et al (2018)
# Uncertainty corresponds to 1-sigma for countries in the non-Annex I group,
# which is a high bound for developed countries (conservative estimate).
# FRACTIONAL uncertainties for 1970, 1980, 1990 and yearly from 2000 to 2012.
# No data available yet for 2013-2015, so uncertainty for those years is 
# extrapolated as equal to the uncertainty for 2012.
#######
years_appendix = np.array([1970, 1980, 1990, 2000, 2001, 2002, 2003, 2004,
    2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012])
unc_list_so2 = np.array([0.561, 0.547, 0.532, 0.511, 0.513, 0.514, 0.508, 0.502, 
        0.497, 0.494, 0.491, 0.487, 0.486, 0.483, 0.479, 0.477])
unc_list_nmvoc = np.array([1.292, 1.265, 1.265, 1.275, 1.278, 1.278, 1.288, 131, 132,
        132.6, 133.6, 133.8, 133, 133.8, 134.1, 133.9])
unc_list_pm10 = np.array([1.418, 1.345, 1.262, 1.198, 1.219, 1.222, 1.200, 1.169,
        1.152, 1.135, 1.111, 1.102, 1.098, 1.081, 1.061, 1.043])
unc_list_pm25 = np.array([1.275, 0.937, 0.675, 0.62, 0.624, 0.639, 0.637, 0.626,
        0.629, 0.624, 0.603, 0.596, 0.607, 0.58, 0.567, 0.565])
unc_list_bc = np.array([1.287, 1.212, 1.103, 1.044, 1.057, 1.067, 1.05, 1.016, 1.009,
        1, 0.978, 0.974, 0.971, 0.953, 0.937, 0.92])

unc_df = pd.DataFrame()
unc_df['years'] = np.linspace(1970, 2015, 46).astype(int)
unc_df['SO2'] = np.round(np.interp(unc_df['years'], years_appendix, unc_list_so2), 3)
unc_df['NMVOC'] = np.round(np.interp(unc_df['years'], years_appendix, unc_list_nmvoc), 3)
unc_df['PM10'] = np.round(np.interp(unc_df['years'], years_appendix, unc_list_pm10), 3)
unc_df['PM2.5'] = np.round(np.interp(unc_df['years'], years_appendix, unc_list_pm25), 3)
unc_df['BC'] = np.round(np.interp(unc_df['years'], years_appendix, unc_list_bc), 3)

unc_tidy = unc_df.melt(id_vars=unc_df.columns[0], 
                                    var_name="Pollutant", 
                                    value_name="Fractional uncertainty, 1 std")
unc_tidy.to_csv(r'../processed/uncertainty_emissions_crippa2018.csv', index = False)
