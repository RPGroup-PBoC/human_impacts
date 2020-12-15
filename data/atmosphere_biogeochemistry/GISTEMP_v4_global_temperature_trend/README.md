
# GISTEMP v4 Global Surface Temperature Time Series

## Description
The NASA Goddard Institute for Space Studies (GISS) Surface Temperature Analysis ver. 4 (GISTEMP v4) contains merged land-ocean global surface temperature anomaly data relative to a reference mean. For the original data, the reference is the 1951-1980 mean. Retrieved December 10th, 2020.

## Key Numbers
Global surface temperature change (2019) since 1850-1900 mean: 1.18 °C ± ≈ 0.05 °C

## Source Information
* **Source Website**: NASA Goddard Institute for Space Studies (GISS) Surface Temperature Analysis ver. 4 (GISTEMP v4)
* **URL**: [homepage](https://data.giss.nasa.gov/gistemp/), [dataset](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv), [article](http://dx.doi.org/10.1029/2018JD029522), [uncertainty analysis](https://data.giss.nasa.gov/gistemp/uncertainty/)
* **Original License**: "When referencing the GISTEMP v4 data provided here, please cite both this webpage and also our most recent scholarly publication about the data. In citing the webpage, be sure to include the date of access."

    * GISTEMP Team, 2020: GISS Surface Temperature Analysis (GISTEMP), version 4. NASA Goddard Institute for Space Studies. Dataset accessed 2020-12-10 at https://data.giss.nasa.gov/gistemp/.
    * Lenssen, N., G. Schmidt, J. Hansen, M. Menne, A. Persin, R. Ruedy, and D. Zyss, 2019: Improvements in the GISTEMP uncertainty model. J. Geophys. Res. Atmos., 124, no. 12, 6307-6326, doi:10.1029/2018JD029522.

* **Bias**: These data are collected by NASA, a U.S. Government Agency generally regarded to be an objective science agency.

## Files
* `GLB.Ts+dSST.csv`: original data source, with the most up-to-date anomalies with respect to the 1951-1980 mean.
* `GLB.Ts+dSST.txt`: original data source, with the most up-to-date anomalies with respect to the 1951-1980 mean.
* `totalCI_ERA.csv`: original data source, with previously calculated anomalies and uncertainty data with respect to the 1951-1980 mean.
* `Land-OceanTemperatureIndex.csv`: manually processed data source, with anomalies with respect to the 1951-1980 mean.
* `GISTEMPv4_global_surf_temperature_trend.csv`: Processed data, with anomalies with respect to the 1850-1900 mean from the HadCRUT4 dataset.

## Notes
The GISTEMP v4 surface temperature analysis is produced by blending data from the GHCN v4 surface air temperature dataset and the ERSST v5 sea-surface temperature dataset. The data were manually processed by retaining the J-D annual mean in `GLB.Ts+dSST.csv`, which describes the global annual temperature anomaly in 0.01 °C, and converting it to °C. Temperature anomalies are provided relative to the 1951–1980 mean in the source file. The data in `GISTEMPv4_global_surf_temperature_trend.csv` were processed with script `get_global_surf_temp_trend.py` from `Land-OceanTemperatureIndex.csv`, making the reference temperature the 1850-1900 mean from the HadCRUT4 dataset.

The uncertainty (95% confidence interval) for years 1880-2018 is is derived from `totalCI_ERA.csv` which can be downloaded from the uncertainty analysis webpage (given above) of Lenssen et al. 2019. The uncertainty for 2019 given here is derived from Lenssen et al. 2019 where it is noted that the uncertainty of annual global mean temperatures since 1960 is approximately ± 0.05 °C.
