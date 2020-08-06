"""
This script transforms the short-form data file
'FAOSTAT_crop_primary_quantity_harvested_area.csv
to a longform tidy version.
"""
#%%
import pandas as pd 
data = pd.read_csv('processed/FAOSTAT_crop_primary_quantity_harvested_area.csv')
data.rename(columns={'production_quantity_Mt':'production_quantity', 'area_harvested_ha':'area_harvested'},
            inplace=True)
melted = pd.melt(data, id_vars=['product', 'year'])
melted.loc[melted['variable']=='production_quantity', 'units'] = 'megatonnes'
melted.loc[melted['variable']=='area_harvested', 'units'] = 'hectares'
melted.to_csv('processed/FAOSTAT_crop_primary_quantity_harvested_area_tidy.csv', index=False)

# %%
