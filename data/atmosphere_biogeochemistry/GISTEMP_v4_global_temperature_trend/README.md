
# GISTEMP v4 GLOBAL Land-Ocean Temperature Index

## Description
The GISS Surface Temperature Analysis (GISTEMP v4) dataset contains global surface temperature change data relative to a reference mean. For the original data, the reference is the 1951-1980 mean.

## Key Numbers
Global surface temperature change (2019) since 1850-1900 mean: 1.18 °C ± ≈ 0.05 °C

## Source Information
* **Source Website**: NASA Goddard Institute for Space Studies
* **URL**: https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv
* **Original License**: Per the GISTEMP v4 webpage: "When referencing the GISTEMP v4 data provided here, please cite both this webpage and also our most recent scholarly publication about the data. In citing the webpage, be sure to include the date of access."

    * GISTEMP Team, 2020: GISS Surface Temperature Analysis (GISTEMP), version 4. NASA Goddard Institute for Space Studies. Dataset accessed 2020-12-10 at https://data.giss.nasa.gov/gistemp/.
    * Lenssen, N., G. Schmidt, J. Hansen, M. Menne, A. Persin, R. Ruedy, and D. Zyss, 2019: Improvements in the GISTEMP uncertainty model. J. Geophys. Res. Atmos., 124, no. 12, 6307-6326, doi:10.1029/2018JD029522.

* **Bias**: These data are collected by NASA, a U.S. Government Agency generally regarded to be an objective science agency.

## Files
* `Land-OceanTemperatureIndex.csv`: manually processed data source, with anomalies with respect to the 1951-1980 mean.
* `GISTEMPv4_global_surf_temperature_trend.csv`: Processed data, with anomalies with respect to the 1850-1900 mean from the HadCRUT4 dataset.

## Notes
The data were manually processed by retaining the J-D annual mean, which describes the global annual temperature change, and converting it to °C. The uncertainty is derived from Lenssen et al. 2019, where it is noted that the uncertainty of annual global mean temperatures since 1960 is approximately ± 0.05 °C. The data in `GISTEMPv4_global_surf_temperature_trend.csv` were processed with script `get_global_surf_temp_trend.py` from `Land-OceanTemperatureIndex.csv`, making the reference temperature the 1850-1900 mean from the HadCRUT4 dataset.
