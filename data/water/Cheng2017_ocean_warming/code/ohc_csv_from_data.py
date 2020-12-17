# -*- coding: utf-8 -*-
#
#################
# This script takes as an input the data 
# from Cheng et al. (2017), imported manually from the
# the manuscript and supplementary information, and returns a csv 
# file with data for the 1960-1991 and 1992-2015 periods.
# Perfect correlation is assumed for the full depth since
# correlations are not reported in the original article.
#
# Last updated: Dec 2020
# Author: Ignacio Lopez-Gomez
# 
#################
import numpy as np
import pandas as pd

#### OHC trend data ####

# Mean values
df_m = pd.DataFrame()
df_m['Time Period'] = ['1960-1991', '1992-2015']
df_m['Measure'] = 'Mean'
df_m['OHC trend 0-700 m'] = [0.15, 0.61] 
df_m['OHC trend 700-2000 m'] = [0.04, 0.37]
df_m['OHC trend 2000- m'] = [0.0, 0.11]
df_m['OHC trend full-depth'] = (df_m['OHC trend 0-700 m'] +
            df_m['OHC trend 700-2000 m'] + 
            df_m['OHC trend 2000- m'])

# Uncertainty values
df_u = pd.DataFrame()
df_u['Time Period'] = ['1960-1991', '1992-2015']
df_u['Measure'] = '95% error bar'
df_u['OHC trend 0-700 m'] = [0.08, 0.04]
df_u['OHC trend 700-2000 m'] = [0.08, 0.02]
df_u['OHC trend 2000- m'] = [0.04, 0.10]
df_u['OHC trend full-depth'] = (df_u['OHC trend 0-700 m'] +
            df_u['OHC trend 700-2000 m'] + 
            df_u['OHC trend 2000- m'])

# Concatenate mean and uncertainty values
df = pd.concat([df_m, df_u], axis=0, ignore_index=True)

# Tidy data
data_tidy = df.melt(id_vars=df.columns[:2],
                              var_name="Location", 
                              value_name="10x22 J / yr")
# Add values in other units
data_tidy["TW"] = round(data_tidy["10x22 J / yr"]*1e10/365/24/3600, 2)
data_tidy = data_tidy.melt(id_vars=data_tidy.columns[:3], 
                              var_name="Units",
                              value_name="Value")

# Save to file, stripped of index
data_tidy.to_csv(r'ohc_trends_cheng2017.csv', index = False)


#### Ocean temperature increase trends ####

# The average global near-surface temperature is ~20 deg C, ~6 deg C at 700 m 
# and ~2.5 deg C at 2000 m. Source: Global Marine Argo Atlas, http://climate4you.com/SeaTemperatures.htm#Global%20ocean%20temperatures%20from%20surface%20to%202000%20m%20depth

# Source of seawater properties: http://web.mit.edu/seawater/2017_MIT_Seawater_Property_Tables_r2b.pdf
d = np.array([700.0, 1300.0]) # Depth of two first layers (m)
rho = np.array([1026.4, 1027.6]) # Seawater density (kg / m3) at 13 (resp., 4) deg celsius and salinity 35 g/kg.
c_p = np.array([3996.1, 3992.0]) # Specific heat of seawater (J / kg K) at 13 (resp., 4) deg celsius and salinity 35 g/kg.
A_s = 3.6184*1e14 # Surface area of the ocean (m2)

heat_over_temp_inc = A_s*np.multiply(np.multiply(rho,c_p),d)

df_temp = pd.DataFrame()
df_temp['Time Period'] = df['Time Period']
df_temp['Measure'] = df['Measure']
df_temp['0-700 m'] = round(df['OHC trend 0-700 m']*1e22/heat_over_temp_inc[0], 5)
df_temp['700-2000 m'] = round(df['OHC trend 700-2000 m']*1e22/heat_over_temp_inc[1], 5)

# Tidy data
data_temp_tidy = df_temp.melt(id_vars=df_temp.columns[:2],
                              var_name="Layer", 
                              value_name="Warming (deg C / yr)")
# Save to file, stripped of index
data_temp_tidy.to_csv(r'temp_trends_cheng2017.csv', index = False)


#### Cumulative ocean temperature change ####

df_temp_cm = data_temp_tidy.copy()
df_temp_cm.loc[df_temp_cm['Time Period']=='1960-1991', ['Warming (deg C / yr)']] *= 32
df_temp_cm.loc[df_temp_cm['Time Period']=='1992-2015', ['Warming (deg C / yr)']] *= 24
df_temp_cm['Temperature increase (K)'] = df_temp_cm['Warming (deg C / yr)']
df_temp_cm = df_temp_cm.drop(columns=['Warming (deg C / yr)'])

full_period_increase = ((df_temp_cm.loc[df_temp_cm['Time Period']=='1960-1991', ['Temperature increase (K)']]).to_numpy() + 
      df_temp_cm.loc[df_temp_cm['Time Period']=='1992-2015', ['Temperature increase (K)']].to_numpy()).flatten()


df2 = pd.DataFrame([['1960-2015', 'Mean', '0-700 m', full_period_increase[0]],
                     ['1960-2015', '95% error bar', '0-700 m', full_period_increase[1]],
                     ['1960-2015', 'Mean', '700-2000 m', full_period_increase[2]],
                     ['1960-2015', '95% error bar', '700-2000 m', full_period_increase[3]]],
      columns=df_temp_cm.columns)
df_temp_cm = df_temp_cm.append(df2).sort_values('Measure', ascending=False)
df_temp_cm = df_temp_cm.sort_values('Layer')
df_temp_cm['Temperature increase (K)'] = round(df_temp_cm['Temperature increase (K)'], 4)
df_temp_cm.to_csv(r'cumulative_temp_increase_cheng2017.csv', index = False)
