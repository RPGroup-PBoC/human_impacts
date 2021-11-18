# -*- coding: utf-8 -*-
#
#################
# This script takes as input the EDGARv6 GHG data in .xls format,
# stripped of the explanatory text,
# and returns a csv file with the processed time series.
# Original data is provided in Gg of substance.
#
# Last updated: Nov 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import pandas as pd
import numpy as np


sources = ['CH4', 'N2O']
unc_df = pd.DataFrame()
unc_df['years'] = np.linspace(1970, 2018, 49).astype(int)
years_table2 = np.array([1990, 1995, 2000, 2001, 2002, 2003, 2004,
    2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012])

for source_ in sources:
    raw_data_ = pd.read_csv('../source/v60_'+str(source_)+'_1970_2018_totals.csv', delim_whitespace=False)
    # Delete empty columns
    raw_data_.loc['World']= np.round(raw_data_.sum(numeric_only=True, axis=0), 1)
    raw_data_.loc['World', 'IPCC_annex'] = 'N/A'
    raw_data_.loc['World', 'C_group_IM24_sh'] = 'World'
    raw_data_.loc['World', 'Country_code_A3'] = 'N/A'
    raw_data_.loc['World', 'Name'] = 'World'
    raw_data_.loc['World', 'fossil_bio'] = 'All'

    data_tidy = raw_data_.melt(id_vars=raw_data_.columns[:5],
                                    var_name="Year", 
                                    value_name="Emissions (Gg)")
    # Change years to numeric
    data_tidy["Year"] = data_tidy["Year"].apply(lambda x: x.split('_')[1])
    # # Save to file, stripped of index
    data_tidy.to_csv(r'../processed/'+str(source_)+'_emissions_processed.csv', index = False)

    #######
    # Save uncertainty data from EDGARv4.32 to csv, Table 2 from Janssens-Maenhout et al (2019).
    #
    # Uncertainty corresponds to 2-sigma for countries and country types.
    #
    # Relative uncertainties for 1990, 1995, 2000 and yearly from 2000 to 2012 are given.
    # No data available yet for 2013-2018, so uncertainty for those years is
    # extrapolated as equal to the uncertainty for 2012. Since the uncertainty is relative,
    # the 95% uncertainty bands are given by [base*(1-2_sigma), base*(1+2_sigma)].
    #######
    if source_ == 'CH4':
        unc_list_non_annex1 = np.repeat(0.6, len(years_table2))
        unc_list_usa = np.array([0.6, 0.57, 0.57, 0.57, 0.57, 0.57, 0.57,
                                    0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32])
        unc_list_eu15_oecd = np.array([0.6, 0.57, 0.57, 0.57, 0.57, 0.57, 0.57,
                                    0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32])
        unc_list_china = np.array([0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6,
                                    0.57, 0.57, 0.57, 0.57, 0.57, 0.57, 0.57, 0.57])
        unc_list_india = np.array([0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.57,
                                    0.57, 0.57, 0.57, 0.57, 0.57, 0.57, 0.57, 0.57])
    elif source_ == 'N2O':
        unc_list_non_annex1 = np.repeat(1.0, len(years_table2))
        unc_list_usa = np.array([1.0, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93,
                                    0.42, 0.42, 0.42, 0.42, 0.42, 0.42, 0.42, 0.42])
        unc_list_eu15_oecd = np.array([1.0, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93,
                                    0.42, 0.42, 0.42, 0.42, 0.42, 0.42, 0.42, 0.42])
        unc_list_china = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                    0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93])
        unc_list_india = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                    0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93])

    # Weighted average of uncertainties from fossil category
    usa_annex1_data = (data_tidy[data_tidy['IPCC_annex'] == 'Annex_I']
            [data_tidy['C_group_IM24_sh'] == 'USA'][data_tidy['fossil_bio'] == 'fossil'])
    # For EU, also add all countries (group by year)
    eu_annex1_data = (data_tidy[data_tidy['IPCC_annex'] == 'Annex_I']
            [data_tidy['C_group_IM24_sh'] == 'OECD_Europe'][data_tidy['fossil_bio'] == 'fossil'].groupby('Year').sum())
    # For EU, also add all countries (group by year)
    india_data = (data_tidy[data_tidy['C_group_IM24_sh'] == 'India +'][data_tidy['fossil_bio'] == 'fossil'].groupby('Year').sum())
    china_data = (data_tidy[data_tidy['C_group_IM24_sh'] == 'China +'][data_tidy['fossil_bio'] == 'fossil'].groupby('Year').sum())
    world_data = data_tidy[data_tidy['C_group_IM24_sh'] == 'World']

    usa_weight = np.divide(np.array(usa_annex1_data["Emissions (Gg)"]),
            np.array(world_data["Emissions (Gg)"]))
    eu_weight = np.divide(np.array(eu_annex1_data["Emissions (Gg)"]),
            np.array(world_data["Emissions (Gg)"]))
    india_weight = np.divide(np.array(india_data["Emissions (Gg)"]),
            np.array(world_data["Emissions (Gg)"]))
    china_weight = np.divide(np.array(china_data["Emissions (Gg)"]),
            np.array(world_data["Emissions (Gg)"]))
    rest_weight = np.subtract(1.0, np.add(
        np.add(usa_weight, eu_weight), np.add(china_weight, india_weight)
        ))

    # # Non Annex I + USA
    unc_df[source_] = np.add(
            np.multiply(
                    np.interp(unc_df['years'], years_table2, unc_list_non_annex1),rest_weight),
            np.multiply(
                    np.interp(unc_df['years'], years_table2, unc_list_usa),usa_weight),)
    # # Add China data
    unc_df[source_] = np.add(unc_df[source_], np.add(
        np.multiply(
                    np.interp(unc_df['years'], years_table2, unc_list_china),china_weight),
        np.multiply(
                    np.interp(unc_df['years'], years_table2, unc_list_india),india_weight),
        ))
    # Add EU and round
    unc_df[source_] = np.round(
            np.add(unc_df[source_],
            np.multiply(
                    np.interp(unc_df['years'], years_table2, unc_list_eu15_oecd), eu_weight),), 3)

unc_tidy = unc_df.melt(id_vars=unc_df.columns[0], 
                                    var_name="Greenhouse Gas", 
                                    value_name='Relative uncertainty, 2 std')
unc_tidy.to_csv(r'../processed/uncertainty_emissions_Janssens_Maenhout.csv', index = False)
