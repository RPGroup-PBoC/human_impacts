
# BP Statistical Review Global Energy Use

## Description 
This dataset contains data of the primary energy used per country (or
continental region) in units of Exajoules from years 1965 - 2019. Units of
Exajoules were converted to units of TW.

## Key Numbers

* Global power usage (2019) ≈ 19 TW


Top 10 (2019)
| Country | Power Usage (TW) |
|:--:|:--:|
| China | ≈ 4.5 | 
| USA | ≈ 3 | 
| India | ≈ 1| 
| Russian Federation | ≈1 | 
| Japan | ≈ 0.6 |
| Canada | ≈ 0.5 | 
| Germany | ≈0.4 |
| Brazil | ≈ 0.4 |
| South Korea | ≈0.4 |
| Iran | ≈0.4 |

## Source Information

* **Source**: BP Statistical Review
* **URL**: [website](https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html)
* **Original License**: As per the 2020 PDF: "Publishers are welcome to quote
    from this review provided that they attribute the source
    to bp Statistical Review of World Energy 2020. However, where extensive
    reproduction of tables and/or charts is planned, permission must first be
    obtained from: The editor Statistical Review of World Energy BP p.l.c. 1 St
    James’s Square London SW1Y 4PD UK sr@bp.com"
* **Bias**: BP is a major energy company specializing in many forms of energy
  resource management and mining. They are most well known for their major
  player status in the petroleum industry. This data set, despite this obvious
  conflict of interest, appears to be robust and the numbers make sense with
  intuition. This data set is also used extensively by Our World in Data, which
  itself has high standards for what data is used.

## Notes 
Processed data file was manipulated manually into a long-form tidy format where
each row corresponds to a single measurement of energy use for a given country
and year. Data was reported in units of Exajoules. This was converted to TW by
using ≈3.154x10^7 seconds per year. 

![](media/figure_file_name.png) 