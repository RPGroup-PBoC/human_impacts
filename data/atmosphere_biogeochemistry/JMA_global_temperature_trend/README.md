
# Japan Meteorological Agency Global Surface Temperature Time Series

## Description
JMA estimates global temperature anomalies using data combined not only over land but also over ocean areas. The land part of the combined data for the period before 2000 consists of GHCN (Global Historical Climatology Network) information provided by NCDC (the U.S.A.'s National Climatic Data Center), while that for the period after 2001 consists of CLIMAT messages archived at JMA. The oceanic part of the combined data consists of JMA's own long-term sea surface temperature analysis data, known as COBE-SST. Retrieved January 15th 2021.

## Key Numbers
Global surface temperature change (2020) since 1850-1900 mean: ≈ 1.06 °C

## Source Information
* **Source Website**: JMA Global Average Surface Temperature Anomalies
* **URL**: [Article about ocean SST analysis](https://doi.org/10.1002/joc.1169), [data](https://ds.data.jma.go.jp/tcc/tcc/products/gwp/temp/ann_wld.html)
* **Original License**:
  - Ishii, M., Shouji, A., Sugimoto, S. and Matsumoto, T. (2005), Objective analyses of sea‐surface temperature and marine meteorological variables for the 20th century using ICOADS and the Kobe Collection. Int. J. Climatol., 25: 865-879. https://doi.org/10.1002/joc.1169

## Files
* `year_wld.csv`: original data source, with anomalies with respect to the 1981–2010 mean. 
* `JMA_global_surf_temperature_trend.csv`: Processed data, with anomalies with respect to the 1850-1900 mean of the HadCRUT4 dataset. 

## Notes
Temperature anomalies are provided relative to a 1981–2010 monthly climatology in the source file. In the processed file, anomalies are presented with respect to the 1850-1900 mean of the HadCRUT4 dataset for ease of comparison. This is the same reference used in the WMO Provisional Report on the State of the Global Climate 2020. No measure of uncertainty is provided in the original source.


