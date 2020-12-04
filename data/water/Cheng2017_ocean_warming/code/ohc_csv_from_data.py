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

rho = 1025.0 # Seawater density (kg / m3)
c_p = 3998.9 # Specific heat of seawater (J / kg K)
A_s = 3.6184*1e14 # Surface area of the ocean (m2)
d = np.array([700.0, 1300.0]) # Depth of two first layers (m)

heat_over_temp_inc = rho*c_p*A_s*d

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
