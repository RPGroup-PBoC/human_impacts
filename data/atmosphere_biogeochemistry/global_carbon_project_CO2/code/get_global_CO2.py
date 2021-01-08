# -*- coding: utf-8 -*-
#
#################
# This script takes as an input the supplementary global data 
# from Friedlingstein et al. (2019), imported in csv format from
# the original .xlsx file, and returns a csv file with
# historical global emissions and sinks since 1959.
# Data is provided in Tg C /year and Tg CO2 /year.
#
# Last updated: Jan 2021
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

######### Get global CO2 data #########
data_ = pd.DataFrame(pd.read_csv('../processed/historical_global_budget_clean.csv', header=0))

# # Aggregate data
data_['anthropogenic emissions'] = add_agg_col(data_, ['fossil fuel and industry', 'land-use change emissions'])
data_['natural sink'] = add_agg_col(data_, ['ocean sink','land sink'])
data_['Flux into atmosphere'] = 'source'

# # Tidy data
data_tidy = data_.melt(id_vars=data_[['Year', 'Flux into atmosphere']], 
                                var_name="Sink/source type", 
                                value_name="Pg C yr-1")
data_tidy.index = data_tidy['Sink/source type']
data_tidy.loc[['ocean sink', 'land sink', 'natural sink'],['Flux into atmosphere']] = 'sink'
data_tidy['Reported value'] = 'mean'
data_tidy = data_tidy[['Year', 'Flux into atmosphere', 'Sink/source type', 'Reported value', 'Pg C yr-1']]

# Add uncertainties from Global_Carbon_Budget_2019v1.0
data_unc = data_tidy.copy()
data_unc['Reported value'] = 'standard deviation'
data_unc.loc[['land-use change emissions'],['Pg C yr-1']] = 0.7
data_unc.loc[['fossil fuel and industry'],['Pg C yr-1']] = data_unc.loc[['fossil fuel and industry'],['Pg C yr-1']]*0.05
data_unc.loc[['ocean sink'],['Pg C yr-1']] = 0.5
data_unc.loc[['land sink'],['Pg C yr-1']] = 0.9
# Uncorrelated errors following Friedlingstein, P. et al. (2019)., Table 6
data_unc.loc[['anthropogenic emissions'],['Pg C yr-1']] = np.sqrt(np.add(
                    np.square(0.7), np.square(data_unc.loc[['fossil fuel and industry'],['Pg C yr-1']].to_numpy())))
data_unc.loc[['budget imbalance'],['Pg C yr-1']] = np.nan
data_unc.loc[['atmospheric growth'],['Pg C yr-1']] = 0.2
data_unc.loc[['natural sink'],['Pg C yr-1']] = np.sqrt(0.5*0.5 + 0.9*0.9)
data_tidy=data_tidy.append(data_unc)

# Add CO2 emissions as well
data_tidy["Pg CO2 yr-1"] = data_tidy["Pg C yr-1"]*44.0/12.0
data_tidy = data_tidy.melt(id_vars=data_tidy.columns[:4], 
                                var_name="Units", 
                                value_name="Value")
data_tidy["Value"] = round(data_tidy["Value"], 2)
# Write to file
data_tidy.to_csv(r'global_carbon_budget_processed.csv', index = False)
