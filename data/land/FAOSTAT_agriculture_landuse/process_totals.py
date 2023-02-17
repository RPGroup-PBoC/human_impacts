# %%
import pandas as pd
data = pd.read_csv('source/FAOSTAT_agricultural_cropland_area.csv')

ag_land = data[data['category'] == 'Agriculture']
crop_land = data[data['category'] != 'Agriculture']
ag_land = ag_land[['year', 'area_Mha']]
crop_land = crop_land[['year', 'area_Mha']]
ag_land.to_csv('./processed/FAOSTAT_agricultural_landuse.csv', index=False)
crop_land.to_csv('./processed/FAOSTAT_crop_landuse.csv', index=False)
crop_land['fractional_crop_land'] = crop_land['area_Mha'].values / \
    ag_land['area_Mha'].values
crop_land = crop_land[['year', 'fractional_crop_land']]
crop_land.to_csv('./processed/FAOSTAT_relative_crop_area.csv', index=False)
