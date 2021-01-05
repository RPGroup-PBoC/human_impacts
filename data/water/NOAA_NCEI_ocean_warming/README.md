
# Time Series of Global Ocean Mean Temperature

## Description
The time series of yearly global mean temperature anomaly for the 0-100 m, 0-700 m, and 0-2000 m layers. 

## Key Numbers

### Ocean temperature increase since 1958-1962
| Year |  Layer 0-100 m (&#8451;) | Layer 0-700 m (&#8451;) | Layer 0-2000 m (&#8451;) |
|:--:|:--:|:--:|:--:|
|2019| 0.51 &plusmn; 0.05 | 0.20 &plusmn; 0.02 | 0.11 &plusmn; 0.01 |

## Source Information

* **Source**: Basin time series of vertical mean temperature anomaly, National Centers for Environmental Information, NOAA
* **URL**: [Article](https://doi.org/10.1029/2012GL051106), [data](https://www.ncei.noaa.gov/access/global-ocean-heat-content/basin_avt_data.html)
* **Original License**: Levitus, S., et al. (2012), World ocean heat content and thermosteric sea level change (0–2000 m), 1955–2010, Geophys. Res. Lett., 39, L10603, doi:10.1029/2012GL051106.
* **Bias**: The views, opinions, and findings contained in the original  article are those of the authors and should not be construed as an official NOAA or U.S. Government position, policy, or decision.

## Files
* `T-dC-w0-100m.dat.txt`: original data source for 0-100 m layer, with anomalies with respect to the 1955-2006 mean temperature.
* `T-dC-w0-700m.dat.txt`: original data source for 0-700 m layer, with anomalies with respect to the 1955-2006 mean temperature.
* `T-dC-w0-2000m.dat.txt`: original data source for 0-2000 m layer, with anomalies with respect to the 1955-2006 mean temperature.
* `NOAA_NCEI_global_ocean_temperature.csv`: Processed data, with anomalies with respect to the 1958-1962 mean temperature. 

## Notes
Temperature anomalies in the original data are reported with respect to the 1955-2006 mean temperature. In the processed file, temperature anomalies are reported with respect to the 1958-1962 mean, following Cheng et al, 2017. All uncertainties reported in the processed file are the 95% confidence interval.

The uncertainties reported in the Key Numbers are the 95% confidence interval of the temperature change with respect to the reference temperature (average temperature during pentadal period 1958-1962) rounded to one significant figure. Uncertainty is obtained from the summary statistics provided in the original source, assuming worst-case scenario for correlation among variables. In this case, perfect positive correlation is assumed for years 1958-1962, and perfect negative correlation is assumed between the 1958-1962 average and the 2019 value.
