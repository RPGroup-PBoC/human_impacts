
# HadCRUT4 Global Surface Temperature Time Series

## Description
HadCRUT4 is a gridded dataset of global historical surface temperatures. Data are available for each month since January 1850, on a 5 degree grid. Retrieved December 11th 2020.

## Source Information
* **Source Website**: Met Office Hadley Centre observations datasets, HadCRUT4 Data
* **URL**: [Article](https://doi.org/10.1029/2011JD017187), [data](https://www.metoffice.gov.uk/hadobs/hadcrut4/data/current/download.html)
* **Original License**:
  - Morice, C. P., J. J. Kennedy, N. A. Rayner, and P. D. Jones (2012), Quantifying uncertainties in global and regional temperature change using an ensemble of observational estimates: The HadCRUT4 dataset, J. Geophys. Res., 117, D08101, doi:10.1029/2011JD017187.
  - HadCRUT4 is subject to Crown copyright protection. The material may be downloaded to file or printer for the purposes of private study and scientific research. Any other proposed use of the material is subject to a copyright licence available from the Met Office.

## Files
* `HadCRUT.4.6.0.0.annual_ns_avg.txt`: original data source, with anomalies with respect to the 1961-1990 mean.
* `HadCRUT4_global_surf_temperature_trend.csv`: Processed data, with anomalies with respect to the 1850-1900 mean.

## Notes
The HadCRUT4 near surface temperature data set is produced by blending data from the CRUTEM4 surface air temperature dataset and the HadSST3 sea-surface temperature dataset. These *best estimate* series are computed as the medians of regional time series computed for each of the 100 ensemble member realisations. Time series are presented as temperature anomalies (deg C) relative to 1961-1990 in the original file, and as anomalies with respect to the 1850-1900 mean in the processed file. This is the same reference used in the WMO Provisional Report on the State of the Global Climate 2020.


