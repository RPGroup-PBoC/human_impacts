
# Mapping the world's free-flowing rivers

## Description
An high-resolution (500 m) dataset of global rivers whose upstream catchment areas are greater than 10 km<sup>2</sup> or whose discharge is greater than 0.1 m<sup>3</sup> per second. This dataset thus contains a global river network of 35.9 million kilometers.

## Key Numbers
* Volume in rivers that are not free-flowing: ≈ 6 x 10m<sup>11</sup> m<sup>3</sup>
* Ratio of river volume in disrupted rivers / free-flowing rivers: ≈ 0.9
* Volume in ocean-connected rivers that are not free-flowing: ≈ 4 x 10m<sup>11</sup> m<sup>3</sup>
* Ratio of ocean-connected river volume in disrupted rivers / free-flowing rivers: ≈ 1.2

## Source Information
* **Source Website**: Zenodo: Sarai, Nicholas S. (2020). Mapping the world's free-flowing rivers: CSV Dataset (Version 0.1.0) [Data set]. Zenodo.
* **URL**: CSV dataset used in this analysis: http://doi.org/10.5281/zenodo.3875115, original dataset as published in [Grill _et al._](https://www.nature.com/articles/s41586-019-1111-9): https://figshare.com/articles/Mapping_the_world_s_free-flowing_rivers_data_set_and_technical_documentation/7688801
* **Original License**: CC BY 4.0
* **Bias**: Grill _et al._ present a well-curated and described set of rivers. The data are mostly compiled from international datasets – mostly from the World Wildlife Fund for Nature (WWF) – of rivers that appear reliable. Unconscious biases could be present in determining the cutoff 95 CSI threshold used to divide free-flowing and non-free-flowing rivers.

## Notes
* In the original dataset, rivers were broken up into "reaches", defined as a segment between two river confluences. 8.5 million of these reaches with an average reach length of 4.2 km result. Hydrographic, geometric, and free-flowing status attributes were associated with the river reaches as described in the documentation of the dataset. A comprehensive definition of connectivity, and thus free-flowing status is provided that encompasses longitudinal, lateral, vertical, and temporal connectivity. Using a set of weights guided by the literature, a connectivity status index (CSI) was calculated for each river reach. Free-flowing rivers are defined as those that have a CSI ≥ 95 throughout their length. See the publication, dataset, and documentation for more details.
* The dataset is too large to be practical for standard processing and hosting on Github, so the long form dataset was trimmed by grouping the dataset by free-flowing status, continent, and ocean connectivity. In each resulting grouping category, the total length, volume, and discharge of the river reaches within each category are displayed.
