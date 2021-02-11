
# NOAA Global Monitoring Laboratory SF<sub>6</sub> Monthly Time Series

## Description
Globally-averaged, monthly mean atmospheric SF<sub>6</sub> concentrations determined from a globally distributed network of air sampling sites from 1998-Present. Retrieved on February 10th 2021.

## Key Numbers
Sulfur hexaflouride atmospheric concentration (2020) : ≈ 10.3 parts per trillion (ppt)

## Source Information
* **Source Website**: Global Monitoring Laboratory, Earth System Research Laboratories, NOAA
* **URL**: [Article](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/94JD01245), [data](https://www.esrl.noaa.gov/gmd/ccgg/trends_sf6/)
* **Original License**:
  - Dlugokencky, E. J., L. P. Steele, P. M. Lang and K. A. Masarie, (1994), The growth rate and distribution of atmospheric methane, Journal of Geophysical Research, 99, D8, 17, doi:10.1029/94JD01245
  - K.A. Masarie and P.P. Tans, (1995), Extension and integration of atmospheric carbon dioxide data into a globally consistent measurement record, J. Geopys. Research, vol. 100, 11593-11610
  - Per the Data Sources and Terms of Use: "These data are made freely available to the public and the scientific community in the belief that their wide dissemination will lead to greater understanding and new scientific insights. The availability of these data does not constitute publication of the data.  NOAA relies on the ethics and integrity of the user to ensure that GML receives fair credit for their work.  If the data are obtained for potential use in a publication or presentation, GML should be informed at the outset of the nature of this work. If the GML data are essential to the work, or if an important result or conclusion depends on the GML data, co-authorship may be appropriate.  This should be discussed at an early stage in the work.  Manuscripts using the GML data should be sent to GML for review before they are submitted for publication so we can ensure that the quality and limitations of the data are accurately represented."

## Files
* `monthly_global_sf6_data.txt`: original data source. 
* `monthly_global_sf6_data_processed.csv`: Processed data.

## Notes
Values for the last year reported are preliminary, pending recalibrations of standard gases and other quality control steps. 

The Global Monitoring Division of NOAA’s Earth System Research Laboratory has measured sulfur hexafluoride since 1997 at a globally distributed network of air sampling sites (Dlugokencky et al., 1994). A global average is constructed by first smoothing the data for each site as a function of time, and then smoothed values for each site are fitted as a function of latitude at 48 equally-spaced time steps per year. Global means are calculated from the latitude fits at each time step (Masarie and Tans, 1995).


