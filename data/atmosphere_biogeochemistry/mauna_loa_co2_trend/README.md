
# Mauna Loa CO<sub>2</sub> Time Series

## Description
Atmospheric CO<sub>2</sub> concentrations measured at the Mauna Loa Observatory, Hawaii from 1958-Present. Retrieved on December 9th 2020.

## Source Information
* **Source Website**: Primary Mauna Loa CO<sub>2</sub> Record, Scripps CO<sub>2</sub> Program
* **URL**: [manuscript](http://escholarship.org/uc/item/09v319r9), [data](https://scrippsco2.ucsd.edu/data/atmospheric_co2/primary_mlo_co2_record.html)
* **Original License**:
  - C. D. Keeling, S. C. Piper, R. B. Bacastow, M. Wahlen, T. P. Whorf, M. Heimann, and H. A. Meijer, Exchanges of atmospheric CO<sub>2</sub> and 13CO<sub>2</sub> with the terrestrial biosphere and oceans from 1978 to 2000. I. Global aspects, SIO Reference Series, No. 01-06, Scripps Institution of Oceanography, San Diego, 88 pages, 2001. 

## Files
* `source/monthly_in_situ_co2_mlo.csv`: original data with headers describing columns. 
* `source/monthly_in_situ_co2_mlo_clean.csv`: data reformatted for parsing by pandas by removing header information. Same column order as original.
* `processed/monthly_co2_data_processed.csv`: processed data in tidy format, removing missing values.

## Notes
The original data file below contains 10 columns.  Columns 1-4 give the dates in several redundant
formats. Column 5 below gives monthly Mauna Loa CO<sub>2</sub> concentrations in micro-mol CO<sub>2</sub> per mole (ppm), reported on the 2008A SIO manometric mole fraction scale.  This is the standard version of the data most often sought.  The monthly values have been adjusted to 24:00 hours on the 15th of each month.  Column 6 gives the same data after a seasonal adjustment to remove the quasi-regular seasonal cycle.  The adjustment involves subtracting from the data a 4-harmonic fit with a linear gain factor.  Column 7 is a smoothed version of the data generated from a stiff cubic spline function plus 4-harmonic functions with linear gain.  Column 8 is the same smoothed version with the seasonal cycle removed.  Column 9 is identical to Column 5 except that the missing values from Column 5 have been filled with values from Column 7.  Column 10 is identical to Column 6 except missing values have been filled with values from Column 8.  Missing values are denoted by -99.99.   
