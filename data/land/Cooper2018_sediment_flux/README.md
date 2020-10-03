
# Sediment Mass and Flux From Earthmoving Operations

## Description 
This dataset is composed of both direct measurements, estimated values, and 
interpolated estimates of the mass of sediment moved via earthmoving processes —
such as mining, dredging, and construction — from 1921 through 2015.

## Key Numbers
Total Sediment Flux in 2015 ≈ 150 cubic km (316 Gt)

## Source Information
* **Source**: Cooper, A.H., Brown, T.J., Price, S.J., Ford, J.R., and Waters, C.N. (2018). Humans are the most significant global geomorphological driving force of the 21st century. The Anthropocene Review 5, 222–229.
 
* **URL**: [DOI: 10.1177/2053019618800234](https://doi.org/10.1177/2053019618800234). 
* **Original License**: The manuscript is not open access and authors hold creative copyright. The data comes from a variety of public sources and is available in the supplementary information. 
* **Bias**: The authors declare no conflict of interest. The data comes from a  
        variety of sources ranging from academic, governmental, and industry 
        data sets. The methods by which they calculate, report, or infer values 
        is relatively clearly presented and explained.
 

## Notes 

* Data was manually transformed from a Table PDF (see source folder) to a tidy CSV. The units were exchanged from Mt to Gt to conform to standard units for these types
of measurements. 

* The total sediment flux was calculated as follows (as described by the authors)
   + World coal production (reported value) with associated overburden and waste (calculated), adjusted for changes over time for stripping ratio and underground/surface working. 
   + World production of metals and minerals other than coal (reported in key years, interpolated for the remainder) with associated overburden and waste (calculated)
   + World cement production (reported)
   + World aggregates production (Estimated from a cement/aggregates ratio)
   + Minimum quantity of material moved during the course of civil engineering earthworks related to construction (estimated based on cement and aggregates production)
   + Material moved by world dredging operations (limited reported data with significant estimates to fill in data gaps)

* Measurements for metal and mineral production (other than coal) were only reported for the years1925, 1950, 1975, 2000, 2010, 2015. Values between these reported values are interpolated, but the interpolating procedure is not explained. 