# -*- coding: utf-8 -*-
#
#################
# This script takes as an input the supplementary data 
# from Saunois et al. (2020), imported in csv format from
# the original .xlsx file, and returns a csv file with
# data for the 2008-2017 period for the different regions
# defined in Human Impacts by the Numbers. Data is provided
# for both the Top-Down (TD) and Bottom-Up (BU) estimates.
#
# Last updated: Nov 2020
# Author: Ignacio Lopez-Gomez
# 
#################
import numpy as np
import pandas as pd

def add_agg_col(df, col_inds, type_ = float):
    df_agg_col = df[col_inds[0]].astype(float)
    for i in range(1,len(col_inds)):
        df_agg_col = df_agg_col + df[col_inds[i]].astype(float)
    return df_agg_col

######### Get TD 2008-2017 data #########
data_ = pd.read_csv('../source/TD_2008_2017_clean.csv', header=0)

# Drop spurious row
data_ = data_.drop([0], axis=0)

# Generate standard regional data
data_['North America'] = add_agg_col(data_, ["Canada", "USA", "Central America"])
data_['Africa'] = add_agg_col(data_, ['Northern Africa',
       'Equatorial Africa', 'Southern Africa'])
data_['Europe and Russia'] = add_agg_col(data_, ['Europe', 'Russia'])
data_['Asia'] = add_agg_col(data_, ['South Asia',
        'Southeast Asia', 'Central Asia', 'Middle East',
        'China', 'Korean Japan'])
data_['South America'] = add_agg_col(data_, ['Northern South America',
       'Brazil', 'Southwest South America'])

# Create new DataFrame to store regional data
cols = ['Africa', 'Europe and Russia', 'Asia',
          'South America', 'North America', 'Oceania']
sectors_ = ['Wetlands', 'Other Natural Sources',
            'Agriculture and Waste', 'Fossil Fuels',
            'Biomass and Biofuel Burning',
            'Total Anthropogenic']
source_range = np.linspace(0, 132, 7).astype(int)

# Add sample mean of all available references
td_mean = pd.DataFrame(data_[cols].iloc[
    source_range[0]:source_range[1]].astype(float).mean(),
                     columns=[sectors_[0]])
for j in range(1, len(source_range)-1):
    td_mean[sectors_[j]] = data_[cols].iloc[
        source_range[j]:source_range[j+1]].astype(float).mean()
td_mean["Measure"] = "Sample Mean"

# Add standard deviation of sample mean
td_std = pd.DataFrame(data_[cols].iloc[
    source_range[0]:source_range[1]].astype(float).std()/
                np.sqrt(source_range[1]-source_range[0]),
                     columns=[sectors_[0]])
for j in range(len(source_range)-1):
    td_std[sectors_[j]] = data_[cols].iloc[
        source_range[j]:source_range[j+1]].astype(float).std(
            )/np.sqrt(source_range[j+1]-source_range[j])
td_std["Measure"] = "Std of Sample Mean"

# Concatenate mean and std values
td_total = pd.concat([td_mean, td_std], axis=0, ignore_index=False)
td_total["Region"] = td_total.index
td_total["Estimate type"] = "Top-Down"
td_total["Period"] = "2008-2017"
# Rearrange columns
td_total = td_total[["Region", "Period", "Estimate type", "Measure",
        'Total Anthropogenic', 'Wetlands', 'Other Natural Sources',
            'Agriculture and Waste', 'Fossil Fuels',
            'Biomass and Biofuel Burning']]



######### Get BU 2008-2017 data #########
data_ = pd.read_csv('../source/BU_2008_2017_clean.csv', header=0)

# Drop spurious row
data_ = data_.drop([0], axis=0)

# Generate standard regional data
data_['North America'] = add_agg_col(data_, ["Canada", "USA", "Central America"])
data_['Africa'] = add_agg_col(data_, ['Northern Africa',
        'Equatorial Africa', 'Southern Africa'])
data_['Europe and Russia'] = add_agg_col(data_, ['Europe', 'Russia'])
data_['Asia'] = add_agg_col(data_, ['South Asia',
        'Southeast Asia', 'Central Asia', 'Middle East',
        'China', 'Korean Japan'])
data_['South America'] = add_agg_col(data_, ['Northern South America',
        'Brazil', 'Southwest South America'])

# Create new DataFrame to store regional data
cols = ['Africa', 'Europe and Russia', 'Asia',
          'South America', 'North America', 'Oceania']
sectors_ = ['Biomass Burning', 'Biofuel', 'Fossil Fuels',
            'Agriculture and Waste', 'Wetlands',
            'Total Anthropogenic']
source_range = [0, 6, 10, 14, 18, 31, 35]

# Add sample mean of all available references
bu_mean = pd.DataFrame(data_[cols].iloc[
    source_range[0]:source_range[1]].astype(float).mean(),
                      columns=[sectors_[0]])
for j in range(1, len(source_range)-1):
    bu_mean[sectors_[j]] = data_[cols].iloc[
        source_range[j]:source_range[j+1]].astype(float).mean()
bu_mean['Measure'] = "Sample Mean"

# Add standard deviation of sample mean
bu_std = pd.DataFrame(data_[cols].iloc[
    source_range[0]:source_range[1]].astype(float).std()/
                np.sqrt(source_range[1]-source_range[0]),
                     columns=[sectors_[0]])
for j in range(len(source_range)-1):
    bu_std[sectors_[j]] = data_[cols].iloc[
        source_range[j]:source_range[j+1]].astype(float).std(
            )/np.sqrt(source_range[j+1]-source_range[j])
bu_std["Measure"] = "Std of Sample Mean"

# Concatenate mean and std values
bu_total = pd.concat([bu_mean, bu_std], axis=0, ignore_index=False)
bu_total["Region"] = bu_total.index
bu_total["Estimate type"] = "Bottom-up"
bu_total["Period"] = "2008-2017"
# Rearrange columns
bu_total = bu_total[["Region", "Period", "Estimate type", "Measure",
        'Total Anthropogenic', 'Wetlands',
            'Agriculture and Waste', 'Fossil Fuels',
            'Biomass Burning', 'Biofuel']]

# Concatenate TD and BU data
reg_total = pd.concat([td_total,bu_total], axis=0, ignore_index=True)
# Tidy data
data_tidy = reg_total.melt(id_vars=reg_total.columns[:4], 
                              var_name="Category", 
                              value_name="Emissions (Tg CH4 yr-1)")
data_tidy["Emissions (Tg CH4 yr-1)"] = round(data_tidy["Emissions (Tg CH4 yr-1)"], 2)
# Save to file, stripped of index
data_tidy.to_csv(r'regional_ch4_data_processed.csv', index = False)
