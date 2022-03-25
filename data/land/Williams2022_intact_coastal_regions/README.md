
# Global assessment of anthropogenic pressure on coastal regions

## Description

Quantification of anthropogenic pressure levels on coastal regions as of 2013, including terrestrial and maritime human footprints. This quantification excludes global stressors due to climate change, and focuses on local anthropogenic stressors from land and sea.

## Key Numbers

Fraction of coastal regions under low anthropogenic pressure (2013): ≈ 15.5 %

Fraction of coastal regions under very high anthropogenic pressure (2013): ≈ 47.9 %

Fraction of coastal regions under formal protection (2013): ≈ 16.4 %

## Source Information
* **URL**: [Article](https://doi.org/10.1111/cobi.13874)
* **Original License**:
  - Williams, B. A., Watson, J. E.M., Beyer, H. L., Klein, C. J., Montgomery, J., Runting, R. K., Roberson, L. A., Halpern, B. S., Grantham, H. S., Kuempel, C. D., Frazier, M., Venter, O., & Wenger, A. (2022). Global rarity of intact coastal regions. Conservation Biology, e138374. https://doi.org/10.1111/cobi.13874

## Files
* `coastal_region_intactness.csv`: Processed data from Appendix S7 of the Article Supplement.

## Notes

Definition of coastal region (Appendix S1 of source): The definition is taken from an ecological connectivity perspective. The authors used a buffer size of 50 km, which roughly corresponds to a local scale capturing the land–sea ecological connectivity aspects of tidal migration of neritic animals (or fish), foraging migration of neritic animals (or fish), breeding migration of neritic animals (or fish), stranded dead marine products on the shore, bird moving foraging, and bird seasonal migration. The authors carried out sensitivity analyses using buffer radii of 10 and 30 km, yielding similar results as the 50 km radius buffer.

Method to generate intactness measure (Appendix S2 of source): The authors took the human footprint (Williams et al. 2020) for the terrestrial realm, and the cumulative human impact map (Halpern et al. 2019) for the marine realm and allocated a point along every 1 km of Earth’s coastline. They then calculated the summed proportion of intact pixels within each 50 km buffer for each point with terrestrial and marine pixels contributing equally to the final intactness value, to create the final coastal region intactness map representing the proportion of each point along the coast that is intact (0-100% intact, divided into five equal bins or “categories” for reporting purposes). For the terrestrial realm they defined intactness as any pixel under a threshold of <4 from their human pressure scale, representing a reasonable approximation of when anthropogenic land conversion has occurred to an extent that the land can be considered human-dominated and no longer “natural” (Williams et al. 2020), and for the marine realm they used any pixel under a threshold of the 40% quantile – and excluding climate change pressures (Jones et al. 2018).


