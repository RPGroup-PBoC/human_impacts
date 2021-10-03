# -*- coding: utf-8 -*-
#
#################
# This script takes as input the FAO fish capture/culture
# data by country and species specified in
# `FAO_FishStatJ_production_quantities_species_country.csv`,
# and generates a csv file with data aggregated by regions
# as defined in the Human Impacts Database.
#
# Last updated: Oct 2021
# Author: Ignacio Lopez-Gomez
# 
#################
import copy
from typing import List

import numpy as np
import pandas as pd


def aggregate_country_data(df: pd.DataFrame, regions: np.ndarray,
        agg_region_name: str,
    ) -> pd.DataFrame:
    sources = ['captured', 'cultured']
    years = np.arange(1950, 2019)

    df_years = []
    proc_mass = []
    df_sources = []
    for year in years:
        for source in sources:
            # for country in regions:
            df_years.append(year)
            df_sources.append(source)
            proc_mass.append(sum(
                [df.loc[(df['country'] == country) & (df['source'] == source)
                    & (df['year'] == year), 'produced mass (tonnes)'].sum() for country in regions]
                ))
    proc_df = pd.DataFrame()
    proc_df['source'] = df_sources
    proc_df['year'] = df_years
    proc_df['produced mass (tonnes)'] = proc_mass
    proc_df['Region'] = agg_region_name
    return proc_df

def add_missing_countries(regions: List[np.ndarray], region_names: List[str]
    ) -> List[np.ndarray]:
    """Add missing FishStatJ countries to corresponding world regions."""
    filled_regions = copy.deepcopy(regions)
    for (i, (region, region_name)) in enumerate(zip(regions, region_names)):
        if region_name == 'Asia':
            asian_countries = np.array(
                ['China',
                 'Taiwan Province of China',
                 "Lao People's Dem. Rep.",
                 'Korea, Republic of',
                 "Korea, Dem. People's Rep",
                 'Iran (Islamic Rep. of)',
                 ])
            filled_regions[i] = np.concatenate([region,
                asian_countries])
        elif region_name == 'Europe':
            euro_countries = np.array(
                ['Un. Sov. Soc. Rep.',
                 'United Kingdom',
                 'Moldova, Republic of',
                 ])
            filled_regions[i] = np.concatenate([region,
                euro_countries])
        elif region_name == 'Africa':
            afr_countries = np.array(
                ['Tanzania, United Rep. of',
                 'Zanzibar'
                 ])
            filled_regions[i] = np.concatenate([region,
                afr_countries])
        elif region_name == 'Oceania':
            oc_countries = np.array(
                ['Wallis and Futuna Is.',
                 'Northern Mariana Is.',
                 'Micronesia, Fed.States of',
                 ])
            filled_regions[i] = np.concatenate([region,
                oc_countries])
        elif region_name == 'South America':
            southam_countries = np.array(
                ['Venezuela, Boliv Rep of',
                 'Falkland Is.(Malvinas)',
                 'Bolivia (Plurinat.State)',
                 ])
            filled_regions[i] = np.concatenate([region,
                southam_countries])
        elif region_name == 'North America':
            northam_countries = np.array(
                ['US Virgin Islands',
                 'Turks and Caicos Is',
                 'St. Pierre and Miquelon',
                 'Saint Vincent/Grenadines',
                 ])
            filled_regions[i] = np.concatenate([region,
                northam_countries])
    return filled_regions

######### Get seafood capture/culture data by country #########
data_ = pd.DataFrame(pd.read_csv('../processed/FAO_FishStatJ_production_quantities_species_country.csv', header=0))
# Get region definitions used in Human Impacts by the Numbers
regions_ = pd.read_csv('../../../../miscellaneous/region_definitions.csv', header=0)

# Get HuID regions
region_names = ['Africa', 'North America', 'South America',
                'Asia', 'Europe', 'Oceania']
regions_list = [np.array(regions_.loc[regions_['region'] == region_name, 'area'])
                    for region_name in region_names]
regions_list = add_missing_countries(regions_list, region_names)

# Construct new regional dataset. Results for 2018 have been manually verified against the
# values reported in Table 17 of the SOFIA 2018 Fisheries Report, page 166,
# URL: http://www.fao.org/3/ca9229en/ca9229en.pdf
# Regional definitions in that report coincide with our methodology for Asia, Europe and
# Oceania. North Am and South Am and Lat Am / North Am in the report differ in their definitions,
# but their combined value is the same.
proc_df = pd.concat([aggregate_country_data(data_, region, region_name)
    for (region, region_name) in zip(regions_list, region_names)])
# # Rearrange columns
proc_df = proc_df[["Region", "year", "source", "produced mass (tonnes)"]]
proc_df.to_csv(r'../processed/FAO_FishStatJ_regional_production_quantities.csv', index = False)
