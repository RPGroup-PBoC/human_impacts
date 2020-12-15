# -*- coding: utf-8 -*-
#
#################
# This script takes as input the supplementary national-level data 
# from Friedlingstein et al. (2019), imported in csv format from
# the original .xlsx file, and returns a csv file with
# data for the 2008-2017 period, for 2017, and for 2018
# for the different regions defined in Human Impacts by the Numbers. 
# Data is provided in Tg C /year and Tg CO2 /year.
#
# Last updated: Dec 2020
# Author: Ignacio Lopez-Gomez
# 
#################
import numpy as np
import pandas as pd

def add_agg_col(df, col_inds, type_ = float):
    df_agg_col = df[col_inds[0]].astype(float)
    for i in range(1,len(col_inds)):
        corrected_col = correct_col(col_inds[i])
        df_agg_col = df_agg_col + df[corrected_col].astype(float)
    return df_agg_col

def correct_col(column_name):
    """
    Takes HuID country names and returns the corresponding
    country name from the Friedlingstein et al (2019)
    national data.
    """
    corr_col_name = column_name
    # Corrected South America
    if 'Bolivia' in column_name:
        corr_col_name = 'Bolivia'
    elif 'Venezuela' in column_name:
        corr_col_name = 'Venezuela'
    # Corrected Asia
    elif 'Hong Kong' in column_name:
        corr_col_name = 'Hong Kong'
    elif 'Macao' in column_name:
        corr_col_name = 'Macao'
    elif 'China, mainland' in column_name:
        corr_col_name = 'China'
    elif 'Taiwan' in column_name:
        corr_col_name = 'Taiwan'
    elif 'Democratic People' in column_name:
        corr_col_name = 'North Korea'
    elif 'Republic of Korea' in column_name:
        corr_col_name = 'South Korea'
    elif 'Iran' in column_name:
        corr_col_name = 'Iran'
    elif 'Lao' in column_name:
        corr_col_name = 'Laos'
    elif 'Palestine' in column_name:
        corr_col_name = 'Occupied Palestinian Territory'
    elif 'Syrian Arab Republic' in column_name:
        corr_col_name = 'Syria'
    # Corrected Europe
    elif 'Czech' in column_name:
        corr_col_name = 'Czech Republic'
    elif 'Macedonia' in column_name:
        corr_col_name = 'Macedonia (Republic of)'
    elif 'Moldova' in column_name:
        corr_col_name = 'Moldova'
    elif 'United Kingdom' in column_name:
        corr_col_name = 'United Kingdom'
    # Corrected Africa
    elif 'Cabo Verde' in column_name:
        corr_col_name = 'Cape Verde'
    elif 'Eswatini' in column_name:
        corr_col_name = 'Swaziland'
    elif 'Saint Helena' in column_name:
        corr_col_name = 'Saint Helena'
    elif 'Tanzania' in column_name:
        corr_col_name = 'Tanzania'
    # Corrected North America
    elif 'United States of America' in column_name:
        corr_col_name = 'USA'
    elif 'Bonaire, Sint Eustatius and Saba' in column_name:
        corr_col_name  = 'Bonaire, Saint Eustatius and Saba'
        
    return corr_col_name

######### Get national CO2 data #########
data_ = pd.DataFrame(pd.read_csv('../source/National_Carbon_Emissions_2019v1.0.csv', header=0))
# Get region definitions used in Human Impacts by the Numbers
regions_ = pd.read_csv('../../../../miscellaneous/region_definitions.csv', header=0)

# Get HuID regions
africa_ = np.array(regions_.loc[regions_['region'] == 'Africa', 'area'])
# Remove unspecified
africa_  = africa_[africa_ != "Mayotte"]
africa_  = africa_[africa_ != "Réunion"]
africa_  = africa_[africa_ != "Western Sahara"]

north_am_ = np.array(regions_.loc[regions_['region'] == 'North America', 'area'])
# Remove unspecified
north_am_  = north_am_[north_am_ != "Cayman Islands"]
north_am_  = north_am_[north_am_ != "Guadeloupe"]
north_am_  = north_am_[north_am_ != "Martinique"]
north_am_  = north_am_[north_am_ != "Netherlands Antilles (former)"]
north_am_  = north_am_[north_am_ != "Puerto Rico"]
north_am_  = north_am_[north_am_ != "United States Virgin Islands"]
north_am_  = north_am_[north_am_ != "Saint-Martin (French part)"]
north_am_  = north_am_[north_am_ != "Sint Maarten  (Dutch part)"]


south_am_ = np.array(regions_.loc[regions_['region'] == 'South America', 'area'])
# Remove unspecified
south_am_ = south_am_[south_am_ != "Falkland Islands (Malvinas)"]
south_am_  = south_am_[south_am_ != "French Guyana"]

asia_ = np.array(regions_.loc[regions_['region'] == 'Asia', 'area'])

europe_russia_ = np.array(regions_.loc[regions_['region'] == 'Europe', 'area'])
# Remove unspecified
europe_russia_  = europe_russia_[europe_russia_ != "Channel Islands"]
europe_russia_  = europe_russia_[europe_russia_ != "Faroe Islands"]
europe_russia_  = europe_russia_[europe_russia_ != "Isle of Man"]
europe_russia_  = europe_russia_[europe_russia_ != "San Marino"]
europe_russia_  = europe_russia_[europe_russia_ != "Gibraltar"]
europe_russia_  = europe_russia_[europe_russia_ != "Holy See"]
europe_russia_  = europe_russia_[europe_russia_ != "Monaco"]

oceania_ = np.array(regions_.loc[regions_['region'] == 'Oceania', 'area'])
# Remove unspecified
oceania_  = oceania_[oceania_ != "American Samoa"]
oceania_  = oceania_[oceania_ != "Guam"]
oceania_  = oceania_[oceania_ != "Northern Mariana Islands"]
oceania_  = oceania_[oceania_ != "Tokelau"]


# # Generate standard regional data
data_['North America'] = add_agg_col(data_, north_am_)
data_['South America'] = add_agg_col(data_, south_am_)
data_['Africa'] = add_agg_col(data_, africa_)
data_['Europe and Russia'] = add_agg_col(data_, europe_russia_)
data_['Asia'] = add_agg_col(data_, asia_)
data_['Oceania'] = add_agg_col(data_, oceania_)


# Create new DataFrame to store regional data
cols = ['Africa', 'Europe and Russia', 'Asia',
            'South America', 'North America', 'Oceania']
# # Add 10 year mean 2008-2017
reg_data = pd.DataFrame(data_[cols].iloc[
    -11:-1].astype(float).mean(),
                      columns=["2008-2017"])
# Add yearly data for last two recorded years
reg_data["2017"] = data_[cols].iloc[-2].astype(float)
reg_data["2018"] = data_[cols].iloc[-1].astype(float)

reg_data["Region"] = reg_data.index
# # Rearrange columns
reg_data = reg_data[["Region", "2008-2017", "2017", "2018"]]

# # Tidy data
data_tidy = reg_data.melt(id_vars=reg_data.columns[0], 
                                var_name="Period", 
                                value_name="Tg C yr-1")
# Add CO2 emissions as well
data_tidy["Tg CO2 yr-1"] = data_tidy["Tg C yr-1"]*44.0/12.0
data_tidy = data_tidy.melt(id_vars=data_tidy.columns[:2], 
                                var_name="Emission Units", 
                                value_name="Emissions")
data_tidy["Emissions"] = round(data_tidy["Emissions"], 2)
# # Save to file, stripped of index
data_tidy.to_csv(r'regional_co2_data_processed.csv', index = False)
