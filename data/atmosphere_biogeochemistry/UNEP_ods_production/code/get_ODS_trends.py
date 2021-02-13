# -*- coding: utf-8 -*-
#
#################
# This script takes as input the UNEP ODS data in .csv format,
# and returns a csv file with the processed time series.
# Data is provided in ODP-equivalent tonnes.
#
# Last updated: Feb 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd
import numpy as np
substance_categories = ['A_I_CFC', 'A_II_Halons', 'B_I_HalCFC', 'B_II_CTC',
        'B_III_TCA', 'C_I_HCFC', 'C_II_HBFC', 'C_III_BCM', 'E_I_MB']
all_subs = pd.DataFrame()
for subs_ in substance_categories:
    raw_data_ = pd.read_csv('../source/'+subs_+'.csv',
        skiprows=1, delim_whitespace=False)
    raw_data_.insert(loc=0, column='Substance category', value=subs_)

    subs_tidy = raw_data_.melt(id_vars=raw_data_.columns[:2], 
                                    var_name="Year", 
                                    value_name="Consumption (10^6 ODP kg)")
    # Fold negative values to zero
    subs_tidy.loc[subs_tidy["Consumption (10^6 ODP kg)"] < 0.0, "Consumption (10^6 ODP kg)"] = 0.0
    # From tonnes to millions of kg
    subs_tidy["Consumption (10^6 ODP kg)"] = subs_tidy["Consumption (10^6 ODP kg)"]/1000.0
    # Clean up
    subs_tidy = subs_tidy[subs_tidy["Year"] != "Baseline"]

    all_subs = pd.concat([all_subs, subs_tidy], axis=0, ignore_index=True)

# Go through years and create totals
years = (np.linspace(1989, 2019, 31).astype(int)).astype(str)
years = np.insert(years, 0, "1986", axis=0)
total = pd.DataFrame()
total["Year"] = years
total["Substance category"] = "All substances"
total["Region"] = "World"
total["Consumption (10^6 ODP kg)"] = np.array([round(np.nansum( 
    (all_subs[ all_subs["Year"] == year_])["Consumption (10^6 ODP kg)"] )) for year_ in years])

all_subs = pd.concat([all_subs, total], axis=0, ignore_index=True)
# # # Save to file, stripped of index
all_subs.to_csv(r'../processed/annual_ods_consumption.csv', index = False)
