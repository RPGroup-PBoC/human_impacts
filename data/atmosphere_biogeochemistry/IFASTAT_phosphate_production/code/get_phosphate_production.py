# -*- coding: utf-8 -*-
#
#################
# This script takes as input the IFA phosphate rock production data in .csv format,
# and returns a csv file with the processed time series.
# Original data is provided in 1,000 tonnes of phosphate rock.
#
# Last updated: May 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd

raw_data_ = pd.read_csv('../source/IFA_phosphate_rock_public_2008_2019_clean.csv', delim_whitespace=False)
# Melt on year
proc_data_ = raw_data_.melt(id_vars=raw_data_.columns[0],
                            var_name="Year",
                            value_name="Phosphate rock production mass (Mt)")

# Remove whitespaces, transform units from kt to Mt
proc_data_["Phosphate rock production mass (Mt)"] = proc_data_["Phosphate rock production mass (Mt)"].apply(
    lambda x: float(x.replace(" ", ""))/1000.0)

# # # Save to file, stripped of index
proc_data_.to_csv(r'../processed/IFA_phosphate_rock_public_2008_2019_processed.csv', index = False)