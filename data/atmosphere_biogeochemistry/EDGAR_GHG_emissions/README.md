
# EDGAR v6.0 Greenhouse Gas Emissions

## Description
The Emissions Database for Global Atmospheric Research (EDGAR) provides independent estimates of the global anthropogenic emissions and emission trends, based on publicly available statistics. This scientific independent emission inventory is characterized by a coherent world historical trend from 1970 to year x-3, including emissions of all greenhouse gases, air pollutants and aerosols. Data are presented for all countries, with emissions provided per main source category, and spatially allocated on a 0.1x0.1 grid over the globe.

## Source Information
* **Source Website**: EDGAR v6.0 Greenhouse Gas Emissions, European Commission, Joint Research Centre
* **URL**: [data](https://edgar.jrc.ec.europa.eu/dataset_ghg60 )
* **Original License**:
  - Crippa, Monica; Guizzardi, Diego; Muntean, Marilena; Schaaf, Edwin; Lo Vullo, Eleonora; Solazzo, Efisio; Monforti-Ferrario, Fabio; Olivier, Jos; Vignati, Elisabetta (2021): EDGAR v6.0 Greenhouse Gas Emissions. European Commission, Joint Research Centre (JRC) [Dataset](http://data.europa.eu/89h/97a67d67-c62e-4826-b873-9d972c4f670b)

  - Janssens-Maenhout, G., Crippa, M., Guizzardi, D., Muntean, M., Schaaf, E., Dentener, F., Bergamaschi, P., Pagliari, V., Olivier, J. G. J., Peters, J. A. H. W., van Aardenne, J. A., Monni, S., Doering, U., Petrescu, A. M. R., Solazzo, E., and Oreggioni, G. D. (2019): EDGAR v4.3.2 Global Atlas of the three major greenhouse gas emissions for the period 1970–2012, Earth Syst. Sci. Data, 11, 959–1002 [DOI](https://doi.org/10.5194/essd-11-959-2019)

  - Crippa, M., Oreggioni, G., Guizzardi, D., Muntean, M., Schaaf, E., Lo Vullo, E., Solazzo, E., Monforti-Ferrario, F., Olivier, J.G.J., Vignati, E., Fossil CO2 and GHG emissions of all world countries - 2019 Report, EUR 29849 EN, Publications Office of the European Union, Luxembourg, 2019, ISBN 978-92-76-11100-9, doi:10.2760/687800, JRC117610.

  - Users of the data are obliged to acknowledge the source of the data with a reference to the JRC EDGAR website (https://edgar.jrc.ec.europa.eu/dataset_ghg60).

## Copyright notice

(c) European Union, 1995-2021

The Commission's reuse policy is implemented by the Commission Decision of 12 December 2011 
on the reuse of Commission documents [1]. Any copyright and/or sui generis right on the dataset 
is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) licence [2]. 
Reuse is allowed provided appropriate credit is given and any changes are indicated.

[1] https://eur-lex.europa.eu/eli/dec/2011/833/oj
[2] https://creativecommons.org/licenses/by/4.0

## Files
* `v60_CH4_1970_2018.xls`: original data source for CH4 emissions.

* `CH4_emissions_processed.csv`: Processed data at regional level for CH4 emissions.
* ` uncertainty_emissions_Janssens_Maenhout.csv`: Relative uncertainty bands for GHG emissions.

## Notes

EDGARv6.0 provides emissions of the three main greenhouse gases (CO<sub>2</sub>, CH<sub>4</sub>, N<sub>2</sub>O) and fluorinated gases per sector and country.
CO<sub>2</sub> emissions are provided separately for CO2_excl_short-cycle_org_C and CO2_short-cycle_org_C. Emissions of CO2_excl_short-cycle_org_C include all fossil CO2 sources, such as fossil fuel combustion, non-metallic mineral processes (e.g. cement production), metal (ferrous and non-ferrous) production processes, urea production, agricultural liming and solvents use. Large scale biomass burning with Savannah burning, forest fires, and sources and sinks from land-use, land-use change and forestry (LULUCF) are excluded.

For the energy related sectors the activity data are primarily based on IEA data from IEA (2019) World Energy Balances, (Internet: link), All rights reserved, as modified by Joint Research Centre, European Commission, whereas the activity data for the agricultural sectors originate primarily from FAO (2020) (Internet: link). United States Geological Survey (USGS), International Fertiliser Association (IFA), Gas Flaring Reduction Partnership (GGFR)/U.S. National Oceanic and Atmospheric Administration (NOAA), UNFCCC and World Steel Association (worldsteel) recent statistics are also used for activity data. Additional information can be found in Crippa et al. (2021).
Compared to EDGARv5.0 the following updates have been included: - updates of all activity data up to 2018 - inclusion of CO2 emissions from coal mining based on the IPCC 2019 refinements - new international shipping proxies and monthly profiles (Jalkanen et al. (2012), Johansson et al. (2017))

Emissions from large scale biomass burning with Savannah burning, forest fires, and sources and sinks from land-use, land-use change and forestry (LULUCF) are excluded.

Uncertainties are not provided for the latest iteration of EDGAR (v6.0), but they are reported for EDGAR v4.3.2 in Table 2 of Janssens-Maenhout et al (2019) at the national/regional level. Since information about the error in certain regions is not consistently with the data from EDGARv6, we assume the average error of those regions to be that of non-Annex I national entities. This is likely an upper bound of the uncertainty. Uncertainties reported represent relative 2 standard deviations.
