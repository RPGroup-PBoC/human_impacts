#%%
import pandas as pd 

# Load the region definitions from the FAO and generate the dictionary
regions = pd.read_csv('../../../miscellaneous/FAO_region_definitions.csv')
region_dict = {g[0].lower():g[1].lower() for g, _ in regions.groupby(['Area', 'region'])}

# Load the country level cement production
cement = pd.read_csv('./source/USGS_cement_by_country_tidy.csv')

# Add associations to match the FAO region definitions  
annotated_regions = []
fao_localities = []
for k in cement['locality'].values:
    if k == 'Bolivia':
        k = 'Bolivia (Plurinational State of)'
    elif k == 'Brunei':
        k = 'Brunei Darussalam'
    elif k == 'Burma': 
        # To agree with FAO notation
        k = 'Myanmar'
    elif k == 'China':
        k = 'China, mainland'
    elif (k == 'Congo (Brazzaville)') | (k == 'Congo (Kinshasa)'):
        k = 'Democratic Republic of the Congo'
    elif k == "Côte d’Ivoire":
        k = "Côte d'Ivoire"
    elif k == "French Guiana":
        k = 'French Guyana'
    elif k == "Hong Kong":
        k = 'China, Hong Kong SAR'
    elif k == "Iran":
        k = 'Iran (Islamic Republic of)'
    elif k == "North Korea":
        k = "Democratic People's Republic of Korea"
    elif k == "South Korea":
        k = "Republic of Korea"
    elif k == "Kosovo":
        # To match FAO notation
        k = 'Serbia'
    elif k == 'Laos':
        k = "Lao People's Democratic Republic"
    elif k == 'Macau':
        # TO match FAO notation
        k = 'China, mainland'
    elif k == 'Macedonia': 
        # To match FAO notation
        k = 'North Macedonia'
    elif k == 'Moldova':
        k = 'Republic of Moldova'
    elif k == 'Papua New Guineae':
        k = 'Papua New Guinea'
    elif k == 'Reunion':
        k = "Réunion"
    elif k == 'Russia':
        k = 'Russian Federation'
    elif k == 'Syria':
        k = 'Syrian Arab Republic'
    elif k == 'Taiwan':
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

        annotated_regions.append(region_dict[k.lower()]) 
    except KeyError:
        print(f"Locality {k} not found in region dictionary.")
    fao_localities.append(k)
cement['region'] = annotated_regions
cement['fao_locality'] = fao_localities
cement.to_csv('./processed/USGS_cement_by_region.csv', index=False)

# %%
