
# NOAAGlobalTemp v5 Global Surface Temperature Time Series

## Description
The NOAA Merged Land Ocean Global Surface Temperature Analysis Dataset
(NOAAGlobalTemp) is a merged land–ocean surface temperature analysis. It is a spatially gridded (5° × 5°) global surface temperature dataset, with monthly resolution from January 1880 to present. Retrieved January 5th 2021.

## Key Numbers
Global surface temperature change (2020) since 1850-1900 mean: ≈ 1.20 °C ± 0.16 °C

## Source Information
* **Source Website**: NOAA Merged Land Ocean Global Surface Temperature Analysis (NOAAGlobalTemp) v5
* **URL**: [Article](https://doi.org/10.1029/2019EO128229), [data](https://www.ncdc.noaa.gov/noaa-merged-land-ocean-global-surface-temperature-analysis-noaaglobaltemp-v5)
* **Original License**:
  - Huang, B., M. J. Menne, T. Boyer, E. Freeman, B. E. Gleason, J. H. Lawrimore, C. Liu, J. J. Rennie, C. Schreck, F. Sun, R. Vose, C. N. Williams, X. Yin, H.-M. Zhang, 2020: Uncertainty estimates for sea surface temperature and land surface air temperature in NOAAGlobalTemp version 5. , J. Climate, 33, 1351-1379, doi: 10.1175/JCLI-D-19-0395.1.
  - Zhang, Huai-Min, Jay H. Lawrimore, Boyin Huang, Matthew J. Menne, Xungang Yin, Ahira Sánchez-Lugo, Byron E. Gleason, Russell Vose, Derek Arndt, J. Jared Rennie, Claude N. Williams, 2019:  Updated temperature data give a sharper view of climate trends, Eos, 100, doi.org/10.1029/2019EO128229.
  - Smith, T.M., R.W. Reynolds, T.C. Peterson, and J. Lawrimore, 2008: Improvements to NOAA's historical merged land–ocean surface temperatures analysis (1880–2006); Journal of Climate, 21, 2283–2296, doi:10.1175/2007JCLI2100.1.
  - Cite dataset when used as a source. See the dataset's DOI landing page for citation details at doi:10.7289/V5FN144H.

## Files
* `aravg.ann.land_ocean.90S.90N.v5.0.0.202112.asc.txt`: original data source, with anomalies with respect to the 1971–2000 mean. 
* `NOAAGlobalTempv5_global_surf_temperature_trend.csv`: Processed data, with anomalies with respect to the 1850-1900 mean of the HadCRUT4 dataset. 

## Notes
Temperature anomalies are provided relative to a 1971–2000 monthly climatology in the source file, following the World Meteorological Organization convention. In the processed file, anomalies are presented with respect to the 1850-1900 mean of the HadCRUT4 dataset for ease of comparison. This is the same reference used in the WMO Provisional Report on the State of the Global Climate 2020. Obtained by combining a global sea surface (water) temperature (SST) dataset with a global land surface air temperature dataset into a merged dataset of both the Earth’s land and ocean surface temperatures. The Extended Reconstructed Sea Surface Temperature (ERSST) version 5 provides the foundational SST observations. The land surface air temperature observations come from the Global Historical Climatology Network Monthly (GHCN-Monthly) database, version 4.


