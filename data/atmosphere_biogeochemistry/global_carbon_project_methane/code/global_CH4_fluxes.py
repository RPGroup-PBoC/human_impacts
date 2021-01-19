# -*- coding: utf-8 -*-
#
#################
# This script takes as an input the data from Saunois et al. (2020),
# imported in csv format from the original Global_Methane_Budget_2000_2017_v2.0_full.xlsx
# file, and returns a csv file with CH4 flux data for 2017 and 2008-2017.
# Data is provided for both the Top-Down (TD) and Bottom-Up (BU) estimates.
#
# Last updated: Jan 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import numpy as np
import pandas as pd

periods = ['2017', '2008_2017']

for period in periods:
  ######### Get Bottom Up global data #########
  data_BU = pd.read_csv('../source/global_BU_'+period+'_clean.csv', header=0)

  # Drop spurious row
  data_BU = data_BU.drop([0], axis=0)

  # Rename columns
  data_BU['Sink/source type'] = data_BU['Emission totals']
  data_BU.loc[data_BU['Sink/source type'] == 'Wetland','Sink/source type'] = 'Wetlands'

  data_BU['Original data source'] = data_BU['Regions']
  data_BU['Value (Tg CH4 yr-1)'] = round(data_BU['GLOBAL'], 0).astype(int)
  #data_BU['Units'] = 'Tg CH4 yr-1'
  data_BU['Estimate type'] = 'Bottom-up'
  data_BU = data_BU[['Sink/source type', 'Estimate type','Original data source', 'Value (Tg CH4 yr-1)']].copy()

  # Report maximum and minimum values
  for flux_type in data_BU['Sink/source type'].unique():
      # Get flux type
      data_BU_chunk = data_BU[ data_BU['Sink/source type'] == flux_type].copy()
      # Get max
      data_BU = data_BU.append(
        data_BU_chunk[
        data_BU_chunk['Value (Tg CH4 yr-1)'] ==
        data_BU_chunk['Value (Tg CH4 yr-1)'].max()].drop_duplicates(
          subset=['Value (Tg CH4 yr-1)']), ignore_index=True
          )
      data_BU.loc[len(data_BU.index)-1, 'Original data source'] = 'Ensemble max'

      # Get min
      data_BU = data_BU.append(
        data_BU_chunk[
        data_BU_chunk['Value (Tg CH4 yr-1)'] ==
        data_BU_chunk['Value (Tg CH4 yr-1)'].min()].drop_duplicates(
          subset=['Value (Tg CH4 yr-1)']), ignore_index=True
          )
      data_BU.loc[len(data_BU.index)-1, 'Original data source'] = 'Ensemble min'


  ######### Get Top Down global data #########
  data_TD = pd.read_csv('../source/global_TD_'+period+'_clean.csv', header=0)

  # # Drop spurious row
  data_TD = data_TD.drop([0], axis=0)

  # Rename columns
  data_TD['Sink/source type'] = data_TD['Emission totals']

  data_TD['Original data source'] = data_TD['Regions']
  data_TD['Value (Tg CH4 yr-1)'] = round(data_TD['GLOBAL'], 0).astype(int)
  #data_TD['Units'] = 'Tg CH4 yr-1'
  data_TD['Estimate type'] = 'Top-down'
  data_TD = data_TD[['Sink/source type', 'Estimate type','Original data source', 'Value (Tg CH4 yr-1)']].copy()

  # Report maximum and minimum values
  for flux_type in data_TD['Sink/source type'].unique():
      # Get flux type
      data_TD_chunk = data_TD[ data_TD['Sink/source type'] == flux_type].copy()
      # Get max
      data_TD = data_TD.append(
        data_TD_chunk[
        data_TD_chunk['Value (Tg CH4 yr-1)'] ==
        data_TD_chunk['Value (Tg CH4 yr-1)'].max()].drop_duplicates(
          subset=['Value (Tg CH4 yr-1)']), ignore_index=True
          )
      data_TD.loc[len(data_TD.index)-1, 'Original data source'] = 'Ensemble max'

      # Get min
      data_TD = data_TD.append(
        data_TD_chunk[
        data_TD_chunk['Value (Tg CH4 yr-1)'] ==
        data_TD_chunk['Value (Tg CH4 yr-1)'].min()].drop_duplicates(
          subset=['Value (Tg CH4 yr-1)']), ignore_index=True
          )
      data_TD.loc[len(data_TD.index)-1, 'Original data source'] = 'Ensemble min'

  # # Concatenate TD and BU data, order
  total = pd.concat([data_TD,data_BU], axis=0, ignore_index=True)
  total = total.sort_values(by=['Sink/source type', 'Estimate type', 'Value (Tg CH4 yr-1)'])
  # Save to file, stripped of index
  total.to_csv(r'../processed/global_ch4_data_'+period+'_processed.csv', index = False)
