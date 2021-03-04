
# HadISDH Global Surface Humidity Time Series

## Description
HadISDH is a gridded dataset of global historical humidity data. Data are available for each month since January 1973 on a 5° grid. The version of HadISDH.blend used here is 1.0.0.2019f; retrieved March 3, 2021.

## Key Numbers
* Global specific humidity change (2019) since 1981-2010 mean: ≈ 0.20 ± 0.10 g/kg
* Global relative humidity change (2019) since 1981-2010 mean: ≈ -0.62 ± 0.29 %rh

## Source Information
* **Source Website**: Met Office Hadley Centre observations datasets, HadISDH - gridded global surface humidity dataset
* **URL**: [Article](https://doi.org/10.5194/cp-10-1983-2014), [Article](https://doi.org/10.1175/2011BAMS3015.1), [Article](https://doi.org/10.5194/cp-9-657-2013), [Article](https://doi.org/10.1002/joc.4775), [data](https://www.metoffice.gov.uk/hadobs/hadisdh/onlinematerialBLEND1002020.html)
* **Original License**:
  - Willett, K. M., Dunn, R. J. H., Thorne, P. W., Bell, S., de Podesta, M., Parker, D. E., Jones, P. D., and Williams Jr., C. N.: HadISDH land surface multi-variable humidity and temperature record for climate monitoring, Clim. Past, 10, 1983-2006, doi:10.5194/cp-10-1983-2014, 2014.
  - Smith, A., N. Lott, and R. Vose, 2011: The Integrated Surface Database: Recent Developments and Partnerships. Bulletin of the American Meteorological Society, 92, 704\u2013708, doi:10.1175/2011BAMS3015.1.
  - Willett, K. M., Williams Jr., C. N., Dunn, R. J. H., Thorne, P. W., Bell, S., de Podesta, M., Jones, P. D., and Parker D. E., 2013: HadISDH: An updated land surface specific humidity product for climate monitoring. Climate of the Past, 9, 657-677, doi:10.5194/cp-9-657-2013.
  - Freeman, E., S.D. Woodruff, S.J. Worley, S.J. Lubker, E.C. Kent, W.E. Angel, D.I . Berry, P. Brohan, R. Eastman, L. Gates, W. Gloeden, Z. Ji, J. Lawrimore, N.A. Rayner, G. Rosenhagen, and S.R. Smith, 2016: ICOADS Release 3.0: A major update to the historical marine climate record. Int. J. Climatol. (doi:10.1002/joc.4775).
  - HadISDH is subject to Crown copyright protection. The material may be downloaded to file or printer for the purposes of private study and scientific research. Any other proposed use of the material is subject to a copyright licence available from the Met Office.

## Files
* `HadISDH.blendq.1.0.0.2019fSHIP_global_annual_full_anoms8110_JAN2020.dat`: original data source with specific humidity anomalies with respect to the 1981-2010 mean.
* `HadISDH_specific_humidity_1973-2019.csv`: processed data with specific humidity anomalies with respect to the 1981-2010 mean.
* `HadISDH.blendRH.1.0.0.2019fSHIP_global_annual_full_anoms8110_JAN2020.dat`: original data source with relative humidity anomalies with respect to the 1981-2010 mean.
* `HadISDH_relative_humidity_1973-2019.csv`: processed data with relative humidity anomalies with respect to the 1981-2010 mean.

## Notes
HadISDH provides globally gridded data for land surface humidity, marine surface humidity, and blend surface humidity. These estimates are computed from temperature measurements and dew point data taken at over >8000 HadISD stations over land and ICOADS observations from marine stations on ships, buoys, and ocean platforms. Measurements are taken at hourly resolution, from which monthly means are created. HadISDH blend is produced by weighting and combining the land and marine data. The data here are anomalies averaged over 5° gridboxes and relative to the 1981-2010 climatological average. 

In addition to the specific humidity and relative humidity data given here, gridded products are also available for dew point temperature, wet bulb temperature, vapour pressure, dew point depression, and temperature.
