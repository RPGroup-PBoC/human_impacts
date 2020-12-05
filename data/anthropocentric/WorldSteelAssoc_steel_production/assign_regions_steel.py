#%%
import pandas as pd

# Load the region definitions from the FAO and generate the dictionary
regions = pd.read_csv('../../../miscellaneous/FAO_region_definitions.csv')
region_dict = {g[0].lower():g[1].lower() for g, _ in regions.groupby(['Area', 'region'])}
# Load the country level cement production
steel = pd.read_csv('./source/crude_steel_by_region_tidy.csv')

# Add associations to match the FAO region definitions
annotated_regions = []
fao_localities = []
for k in steel['locality'].values:
    if k == 'China':
        k = 'China, mainland'
    elif k == 'Czech Republic':
        k = 'Czechia'
    elif k == 'Former Yugoslavia':
        #to match FAO notation
        k = 'Serbia'
    elif k == "Iran":
        k = 'Iran (Islamic Republic of)'
    elif k == "D.P.R. Korea":
        k = "Democratic People's Republic of Korea"
    elif k == "South Korea":
        k = "Republic of Korea"
    elif k == 'Macedonia':
        # To match FAO notation
        k = 'North Macedonia'
    elif k == 'Moldova':
        k = 'Republic of Moldova'
    elif k == 'Russia':
        k = 'Russian Federation'
    elif k == 'Slovak Republic':
        k = 'Slovakia'
    elif k == 'Syria':
        k = 'Syrian Arab Republic'
    elif k == 'Taiwan, China':
        # To match FAO notation
        k = 'China, Taiwan Province of'
    elif k == 'Tanzania':
        k = 'United Republic of Tanzania'
    elif k == 'United Kingdom':
        k = 'United Kingdom of Great Britain and Northern Ireland'
    elif k == 'United States':
        k = 'United States of America'
    elif k == 'Venezuela':
        k = 'Venezuela (Bolivarian Republic of)'
    elif k == 'Vietnam':
          k = 'Viet Nam'
    try:

        annotated_regions.append(region_dict[str(k).lower()])
    except KeyError:
        print(f"Locality {k} not found in region dictionary.")
    fao_localities.append(k)
steel['region'] = annotated_regions
steel['fao_locality'] = fao_localities
steel.to_csv('./processed/crude_steel_by_region.csv', index=False)

# %%
