
# Evolution of Earth's albedo as measured from earthshine

## Description
Evolution of Earth's albedo obtained from observations of the earthshine for the period 1998-2017. Observations are from the Big Bear Solar Observatory.

## Key Numbers
Decline in the global albedo (2017, with respect to 1998) : ≈ 0.5 W / m<sup>2</sup>

## Source Information
* **URL**: [manuscript](https://doi.org/10.1029/2021GL094888), [data](http://www.bbso.njit.edu/Data/Earthshine.txt)
* **Original License**:
  - Goode, P. R., Pallé, E., Shoumko, A., Shoumko, S., Montañes-Rodriguez,
P., & Koonin, S. E. (2021). Earth's albedo 1998–2017 as measured from earthshine. Geophysical Research Letters, 48, e2021GL094888.

## Files
* `source/Earthshine.txt`: original data from the authors. 
* `source/Earthshine_lower_uncertainty_band.csv`: Lower limit of error bar taken from Figure 3 of the original publication.
* `source/Earthshine_upper_uncertainty_band.csv`: Upper limit of error bar taken from Figure 3 of the original publication.
* `processed/earthshine_data.csv`: processed data in tidy format, rounded to 3 decimals.

## Notes

The reflectance of the Earth was measured from Big Bear Solar Observatory between 1998 and 2017 by observing the earthshine using modern photometric techniques to precisely determine changes in terrestrial albedo from earthshine. The data show a climatologically significant ≈ 0.5 W / m<sup>2</sup> decline in the global albedo over the two decades of data.

The upper and lower uncertainty margins are taken from Figure 3 of the original article, and interpolated to the dates of measured albedo anomaly values using linear interpolation.

