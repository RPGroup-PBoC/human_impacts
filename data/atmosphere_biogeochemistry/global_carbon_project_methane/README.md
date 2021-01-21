
# Global Methane Budget

## Description
The Global Methane Budget contains data on CH<sub>4</sub> emissions from anthropogenic and natural sources.

## Key Numbers
* CH<sub>4</sub> emissions from anthropogenic sources (2017): ≈ 0.4 Gt CH<sub>4</sub> / yr
* CH<sub>4</sub> emissions from natural sources (2017): ≈ 0.3 Gt CH<sub>4</sub> / yr
* Atmospheric CH<sub>4</sub> growth rate (2017): ≈ 17 Mt CH<sub>4</sub> / yr

## Source Information
* **Source Website**: Global Methane Budget 2000-2017
* **URL**: https://doi.org/10.5194/essd-12-1561-2020
* **Original License**: Saunois, M. et al. (2020). The global methane budget 2000–2017. Earth system science data, 12(3), 1561-1623.
* **Bias**: These data are mostly from original publications but collected and curated by the Global Carbon Project, a Global Research Project of Future Earth and a research partner of the World Climate Research Programme. No inherent bias seems to be present.

## Notes
The data were processed by 1) tidying Table 3 of the publication and retaining the categories needed for this analysis and 2) processing the source dataset for regional and more granular information. "Atmospheric growth is given in the same unit (Tg CH<sub>4</sub> / yr), based on the conversion factor of 2.75 Tg CH<sub>4</sub> / ppb given by Prather et al. 2012 DOI: 10.1029/2012gl051440 and the atmospheric growth rates provided in the text in parts per billion per year." Using top-down and bottom-up estimates arrived at different final emissions values for the year 2017:
* Total anthropogenic sources (top-down):0.364 Gt CH<sub>4</sub> / yr,
* Total anthropogenic sources (bottom-up): 0.38 Gt CH<sub>4</sub> / yr,
* Total natural sources (top-down): 0.232 Gt CH<sub>4</sub> / yr,
* Total natural sources (bottom-up): 0.367 Gt CH<sub>4</sub> / yr.

All data used in the original publication (Saunois et al., 2020) are available at https://doi.org/10.18160/GCP-CH4-2019 in `.xlsx` format, for both bottom-up and top-down estimates. Estimates are provided for 18 geographical regions, as well as three latitudinal bands (<30 N, 30 N - 60 N, 60 N - 90 N) and the whole globe. The processed regional values reported here were obtained using the original data in `source/Global_Methane_Budget_2000_2017_v2.0_full.xlsx`. The data in the 2008-2017 TD and BU budget tabs were converted into `.csv` files, named `TD_2008_2017_clean.csv` and `BU_2008_2017_clean.csv`. These csv files were processed using the script `code/regional_CH4_stats.py`. Data on the global methane inventory were processed using `code/global_CH4_fluxes.py`.
