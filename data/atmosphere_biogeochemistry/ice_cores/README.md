
# Law Dome Ice Core Time Series

## Description
Atmospheric CO<sub>2</sub>, CH<sub>4</sub> and N<sub>2</sub>O concentrations inferred from Law Dome ice cores. Time series are constructed as spline fits to the Law Dome firn and ice core records and the Cape Grim record. Retrieved on September 19th 2020.

## Source Information
* **Source Website**: NOAA
* **URL**: [manuscript](https://doi.org/10.1029/2006GL026152), [data](https://www.ncdc.noaa.gov/paleo-search/study/9959)
* **Original License**:
  - MacFarling Meure, C., D. Etheridge, C. Trudinger, P. Steele, R. Langenfelds, T. van Ommen, A. Smith, and J. Elkins. 2006. The Law Dome CO2, CH4 and N2O Ice Core Records Extended to 2000 years BP. Geophysical Research Letters, Vol. 33, No. 14, L14810 10.1029/2006GL026152. 
* **Original references used to construct data series, Ice Core results**:
  - Etheridge, D.M., L.P. Steele, R.L. Langenfelds, R.J. Francey, J.-M. Barnola, and V.I. Morgan.  1996. Natural and anthropogenic changes in atmospheric CO2 over the last 1000 years from air in Antarctic ice and firn. Journal of Geophysical Research, 101, 4115-4128.
  - Etheridge, D.M., L.P. Steele, R.J. Francey, and R.L. Langenfelds. 1998. Atmospheric methane between 1000 A.D. and present: evidence of anthropogenic emissions and climatic variability. Journal of Geophysical Research, 103, 15979-15996.
  - MacFarling Meure, C. 2004. The natural and anthropogenic variations of carbon dioxide, methane and nitrous oxide during the Holocene from ice core analysis. PhD thesis, University of Melbourne.
  - Ferretti, D.F., J.B. Miller, J.W.C. White, D.M. Etheridge, K.R. Lassey, D.C. Lowe, C.M. MacFarling Meure, M.F. Dreier, C.M. Trudinger, and T.D. van Ommen.  2005. Unexpected Changes to the Global Methane Budget over the Last 2,000 Years. Science, 309 (5741): 1714-1717.
* **Original references used to construct data series, Firn air results**:
  - Etheridge, D.M., L.P. Steele, R.J. Francey, and R.L. Langenfelds. 1998. Atmospheric methane between 1000 A.D. and present: evidence of anthropogenic emissions and climatic variability. Journal of Geophysical Research, 103, 15979-15996.
  - Trudinger, C.M., D.M. Etheridge, P.J. Rayner, I.G. Enting, G.A. Sturrock, R.L. Langenfelds, and A.M. Smith. 2002. Reconstructing atmospheric histories from measurements of air in firn. Journal of Geophysical Research, 107, doi:10.1029/2002JD002545.
  - Sturrock, G.A., D.M. Etheridge, C.M. Trudinger, and P.J. Fraser. 2002. Atmospheric histories of halocarbons from analysis of Antarctic firn air: Major Montreal Protocol species. Journal of Geophysical Research, 107, doi:10.1029/2002JD002548.
* **Original references used to construct data series, Cape Grim Record**:
  - Langenfelds, R.L., P.J. Fraser, R.J. Francey, L.P. Steele, L.W. Porter, and C.E. Allison. 1996. The Cape Grim air archive: The first seventeen years, 1978-1995, In: Baseline Atmospheric Program (Australia) 1994-1995, edited by Francey, R.J., A.L. Dick, and N. Derek, p53-70, Bureau of Meteorology and CSIRO Division of Atmospheric Research, Melbourne, Australia.
  - Langenfelds, R.L., L.P. Steele, M.V. Van der Schoot, L.N. Cooper, D.A. Spencer, and P.B. Krummel. 2004. Atmospheric methane, carbon dioxide, hydrogen, carbon monoxide and nitrous oxide from Cape Grim flask air samples analysed by gas chromatography. In: Baseline Atmospheric Program Australia. 2001-2002 ed. J.M. Cainey, N. Derek, and P.B. Krummel (editors). Melbourne: Bureau of Meteorology and CSIRO Atmospheric Research. p. 46-47.
  - Langenfelds, R.L., P.J. Fraser, L.P. Steele, and L.W. Porter. 2004. Archiving of Cape Grim Air. In: Baseline Atmospheric Program Australia. 2001-2002 ed. J.M. Cainey, N. Derek, and P.B. Krummel (editors). Melbourne: Bureau of Meteorology and CSIRO Atmospheric Research. p. 48.

## Files
* source/law2006.txt: original data, text format.
* source/law2006.xls: original data, Excel format.
* processed/law2006_by_year_clean.csv: data reformatted for parsing by pandas by removing header information and renaming columns with Python-safe names. Same column order as original. 
* processed/ice_core_measurements_co2_ch4_n2o.csv: Tidy data on atmospheric concentrations of CO<sub>2</sub>, CH<sub>4</sub> and N<sub>2</sub>O.

## Notes
Data presented is constructed from Law Dome ice cores (DSS, DE08 and DE08-2), firn air (DSSW20K),
and Cape Grim instrumental (deseasonalised archive, insitu and flask) records of CO<sub>2</sub>, CH<sub>4</sub> and N<sub>2</sub>O concentrations for the past 2000 years. Measurement precision for the ice core air samples is 4.1 ppb CH<sub>4</sub>, 1.1 ppm CO<sub>2</sub>, and 6.5 ppb N<sub>2</sub>O. Measurement precision for the firn air samples is 2 ppb CH<sub>4</sub>, 0.1 ppm CO<sub>2</sub> and 0.3 ppb N<sub>2</sub>O.
