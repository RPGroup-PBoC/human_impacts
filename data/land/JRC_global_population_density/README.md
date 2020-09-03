# GSHL - European Commission Joint Research Center — Urban Population and Area  

## Description 
This dataset is a granular representation of the total population, built-up
impervious land surface, and total land area of urban centers across the planet.
Values are collected from a combination of scraping census documents with (most
importantly) their very extensive satellite image database.

## Key Numbers
Total urban land area (2015) ≈ 650 thousand km^2

Average urban center population density (2015) ≈ 5300 people / km^2

## Source Information
* **Source**: Urban Centre Database UCDB R2019A
* **URL**: [GSHL JRC](https://ghsl.jrc.ec.europa.eu/datasets.php)
* **Original License**:[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) 
* **Bias**: The source is a intergovernmental research consortium operated by
  the EU. The source website goes through a great deal of effort in describing
  their data and making it easily accessible. Raw data is also available. 


## Notes
The preferred citation is as follows:

* Florczyk, Aneta; Corbane, Christina; Schiavina, Marcello; Pesaresi, Martino; Maffenini, Luca; Melchiorri, Michele; Politis, Panagiotis; Sabo, Filip; Freire, Sergio; Ehrlich, Daniele; Kemper, Thomas; Tommasi, Pierpaolo; Airaghi, Donato; Zanchetta, Luigi (2019):  GHS Urban Centre Database 2015, multitemporal and multidimensional attributes, R2019A. European Commission, Joint Research Centre (JRC) [Dataset] PID: https://data.jrc.ec.europa.eu/dataset/53473144-b88c-44bc-b4a3-4583ed1f547e


In processing the data, we considered "urban" environments to be settlements
with a population above 5,000 people total. See `processing.py` for further information.

