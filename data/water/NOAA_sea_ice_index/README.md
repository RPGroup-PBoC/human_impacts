
# NOAA Sea Ice Index, Version 3

## Description
The Sea Ice Index provides satellite data for sea ice cover described as sea ice extent (the area containing > 15% ice) and area (calculated by multiplying the percentage of sea ice in each pixel by pixel area) in the northern and southern hemispheres from 1979-present. NOAA recommends using monthly data to look at long-term trends in sea ice cover.

## Key Numbers
Annualized rate of change of Northern Hemisphere sea ice cover in March (March corresponds to the maximum yearly extent, 1979-2022): extent: -3.98 x 10<sup>10</sup> m<sup>2</sup> / yr, area: -4.2 x 10<sup>9</sup> m<sup>2</sup> / yr

Annualized rate of change of Northern Hemisphere sea ice cover in September (September corresponds to the minimum yearly extent, 1979-2022): extent: -8.13 x 10<sup>10</sup> m<sup>2</sup> / yr, area: -4.82 x 10<sup>10</sup> m<sup>2</sup> / yr

Annualized rate of change of annual Northern Hemisphere sea ice cover (1979-2022): extent: -5.41 x 10<sup>10</sup> m<sup>2</sup> / yr, area: -2.45 x 10<sup>10</sup> m<sup>2</sup> / yr

Annualized rate of change of Southern Hemisphere sea ice cover in March (March corresponds to the maximum yearly extent, 1979-2022): extent:  x 10<sup>10</sup> m<sup>2</sup> / yr, area:  x 10<sup>9</sup> m<sup>2</sup> / yr

Annualized rate of change of Southern Hemisphere sea ice cover in September (September corresponds to the minimum yearly extent, 1979-2022): extent:  x 10<sup>10</sup> m<sup>2</sup> / yr, area:  x 10<sup>10</sup> m<sup>2</sup> / yr

Annualized rate of change of Southern Hemisphere sea ice cover (1979-2022): extent:  x 10<sup>10</sup> m<sup>2</sup> / yr, area:  x 10<sup>10</sup> m<sup>2</sup> / yr

## Source Information
* **Source Website**: National Snow & Ice Data Center (NSIDC)
* **URL**: https://nsidc.org/data/g02135
* **Original License**: The Use and Copyright page of the website states: "You may download and use photographs, imagery, or text from our Web site, unless limitations for its use are specifically stated. Please credit the National Snow and Ice Data Center as described below." The citation section states: "As a condition of use, you must cite the use of our data in your work with a formal citation. A citation acknowledges our data contributors, and allows us to track the use and impact of our data. It also helps us report data distribution activity to funding agencies, and to assist others who may contact us about data that are referenced in publications."
Fetterer, F., K. Knowles, W. N. Meier, M. Savoie, and A. K. Windnagel. 2017, updated daily. Sea Ice Index, Version 3. [Indicate subset used]. Boulder, Colorado USA. NSIDC: National Snow and Ice Data Center. doi: https://doi.org/10.7265/N5K072F8. [2022-Feb-16].
* **Bias**: The data is available at NSIDC, a CoreTrustSeal Repository that maintains and distributes data on the cryosphere. These data were collected by the National Oceanic and Atmospheric Administration (NOAA) a U.S. Government Agency.

## Notes
The monthly extent and area data were processed from the source file Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx by converting the data to tidy format and removing partial years 1978 and the current year. This results in individual csv files containing monthly and yearly sea ice area and extent averages for both the Northern and Southern Hemispheres. Annualized rates of change were derived from these data via linear regression for the monthly and yearly ice extent/area averages. This results in individual csv files containing annualized rates of change for Northern and Southern Hemisphere sea ice area and extent.

The trend in Antarctic sea ice is not included in the key numbers as the long term trend is not clear per the IPCC Special Report on the Ocean and Cryosphere in a Changing Climate, Chapter 3: "It is very likely that Antarctic sea ice cover exhibits no significant trend over the period of satellite observations
(1979–2018). While the drivers of historical decadal variability are known with medium confidence, there is currently limited evidence and low agreement concerning causes of the strong recent decrease (2016–2018), and low confidence in the ability of current-generation climate models to reproduce and explain the observations."

More information about the dataset: https://nsidc.org/data/seaice_index/faq
