"""
This script tidies the data from the source file into individual csv
files containing monthly and yearly sea ice area and extent averages
for both the Northern and Southern Hemispheres. These data are then
used to generate csv files containing annualized trends of the monthly
and yearly sea ice extent and area averages from 1979-present for both
the Northern and Southern Hemispheres.
"""

import pandas as pd
import numpy as np


#load the data from each sheet of the source .xslx document into a dataframe
NH_Extent = pd.read_excel('../source/Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name= "NH-Extent")
NH_Area = pd.read_excel('../source/Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name= "NH-Area")
SH_Extent = pd.read_excel('../source/Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name= "SH-Extent")
SH_Area = pd.read_excel('../source/Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name= "SH-Area")


#drop empty columns, rename columns, drop partial years (1978 and the latest year)
dfs = [NH_Extent, NH_Area, SH_Extent, SH_Area]
for df in dfs:
    df.drop(columns='Unnamed: 13', inplace = True)
    df.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)
    df.drop(df[(df['Year'] == 1978) | (df['Year'] == 2022)].index, inplace = True)


#get a list of columns, for use later
time_periods = list(NH_Extent.columns.values)
time_periods.remove("Year")


#tidy the dataframes by melting them, export csv files that contain data for monthly sea ice extent/area
NH_Extent = pd.melt(NH_Extent,
                    ["Year"],
                    var_name="Month",
                    value_name="Extent")
NH_Extent.dropna(inplace = True)
NH_Extent['Extent'] = NH_Extent['Extent']*1000000
NH_Extent['Extent'] = round(NH_Extent['Extent'],3)
NH_Extent['Units'] = "km^2"
NH_Extent.to_csv('../processed/northern_hemisphere_extent.csv', index = False)

NH_Area = pd.melt(NH_Area,
                    ["Year"],
                    var_name="Month",
                    value_name="Area")
NH_Area.dropna(inplace = True)
NH_Area['Area'] = NH_Area['Area']*1000000
NH_Area['Area'] = round(NH_Area['Area'],3)
NH_Area['Units'] = "km^2"
NH_Area.to_csv('../processed/northern_hemisphere_area.csv', index = False)

SH_Extent = pd.melt(SH_Extent,
                    ["Year"],
                    var_name="Month",
                    value_name="Extent")
SH_Extent.dropna(inplace = True)
SH_Extent['Extent'] = SH_Extent['Extent']*1000000
SH_Extent['Extent'] = round(SH_Extent['Extent'],3)
SH_Extent['Units'] = "km^2"
SH_Extent.to_csv('../processed/southern_hemisphere_extent.csv', index = False)

SH_Area = pd.melt(SH_Area,
                    ["Year"],
                    var_name="Month",
                    value_name="Area")
SH_Area.dropna(inplace = True)
SH_Area['Area'] = SH_Area['Area']*1000000
SH_Area['Area'] = round(SH_Area['Area'],3)
SH_Area['Units'] = "km^2"
SH_Area.to_csv('../processed/southern_hemisphere_area.csv', index = False)


#calculate the annualized sea ice extent/area change for each month and for the yearly average over the period 1979-present
NH_extent_change = pd.DataFrame(columns=["Month", "Annualized Extent Change", "Units"])
for month in time_periods:
    temp_df = NH_Extent[NH_Extent['Month'] == month]
    x = temp_df['Year']
    y = temp_df['Extent']
    linear_fit = np.polyfit(x,y,1)
    extent_loss = round(linear_fit[0],-2)
    NH_extent_change.loc[NH_extent_change.shape[0]] = [month, extent_loss, "km^2 / yr"]
NH_extent_change.to_csv('../processed/northern_hemisphere_extent_change.csv', index = False)

NH_area_change = pd.DataFrame(columns=["Month", "Annualized Area Change", "Units"])
for month in time_periods:
    temp_df = NH_Area[NH_Area['Month'] == month]
    x = temp_df['Year']
    y = temp_df['Area']
    linear_fit = np.polyfit(x,y,1)
    area_loss = round(linear_fit[0],-2)
    NH_area_change.loc[NH_area_change.shape[0]] = [month, area_loss, "km^2 / yr"]
NH_area_change.to_csv('../processed/northern_hemisphere_area_change.csv', index = False)

"""
The changes in Southern Hemisphere sea ice are not robust and are not currently
displayed in the Human Impacts Database. They can be calculated with the code below.
"""
"""
SH_extent_change = pd.DataFrame(columns=["Month", "Annualized Extent Change", "Units"])
for month in time_periods:
    temp_df = SH_Extent[SH_Area['Month'] == month]
    x = temp_df['Year']
    y = temp_df['Extent']
    linear_fit = np.polyfit(x,y,1)
    extent_loss = round(linear_fit[0],-3)
    SH_extent_change.loc[SH_extent_change.shape[0]] = [month, extent_loss, "km^2 / yr"]
SH_extent_change.to_csv('../processed/southern_hemisphere_extent_change.csv', index = False)

SH_area_change = pd.DataFrame(columns=["Month", "Annualized Area Change", "Units"])
for month in time_periods:
    temp_df = SH_Area[SH_Area['Month'] == month]
    x = temp_df['Year']
    y = temp_df['Area']
    linear_fit = np.polyfit(x,y,1)
    area_loss = round(linear_fit[0],-3)
    SH_area_change.loc[SH_area_change.shape[0]] = [month, area_loss, "km^2 / yr"]
SH_area_change.to_csv('../processed/southern_hemisphere_area_change.csv', index = False)
"""
