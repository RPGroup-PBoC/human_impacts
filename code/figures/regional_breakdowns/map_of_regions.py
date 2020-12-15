#%%
#################
# This script takes as input the FAO country definitions
# and corresponding HuID regions, and returns different 
# Earth projections containing the defined regions.
#
# Last updated: Dec 2020
# Author: Ignacio Lopez-Gomez
# 
#################

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import pandas as pd
import anthro.viz

def plot_huid_countries(df,projection,colors,edgecolor):
    """
    Returns a world map using a projection. Continents
    are colored based on the Human Impacts regional
    definitions and the anthro.viz colors.
    """
    colors_huid = anthro.viz.plotting_style()
    ocean = colors_huid['light_blue']
    ax = plt.axes(projection=projection)
    ax.outline_patch.set_edgecolor(edgecolor)
    ax.add_feature(cfeature.OCEAN,
                   facecolor=ocean,
                   edgecolor='black',
                   linewidth=1.5)
    # Get countries
    shpfilename = shpreader.natural_earth(resolution='110m',
                                          category='cultural',
                                          name='admin_0_countries')
    reader = shpreader.Reader(shpfilename)
    countries = reader.records()
    
    # Get provinces and subnational territories
    shpfilename_2 = shpreader.natural_earth(resolution='10m',
                                      category='cultural',
                                      name='admin_1_states_provinces')
    reader2 = shpreader.Reader(shpfilename_2)
    subcountries = reader2.records()

    linewidth_cont_ = .4
    # Iterate through countries in HuID definition and natural earth dataset
    for country in countries:
        for huid_country_index in range(len(df["area"])):
            # Resolve country name conflicts
            if "Viet Nam" in df["area"][huid_country_index]:
                df["area"][huid_country_index] = 'Vietnam'
            elif "Eswatini" in df["area"][huid_country_index]:
                df["area"][huid_country_index] = 'Swaziland'
                
            # If HuID and natural earth definitions coincide, change color
            if (df["area"][huid_country_index] in country.attributes.values() or
                    country.attributes['NAME'] in df["area"][huid_country_index] or
                    country.attributes['NAME_EN'] in df["area"][huid_country_index]):
                
                # color country
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor=(colors[df["region"][huid_country_index]]),
                                  label=country.attributes["NAME"],
                                  edgecolor=(colors[df["region"][huid_country_index]]),
                                  linewidth=linewidth_cont_)
                
            # Color "disputed countries" not present in the HuID definitions
            elif "Somaliland" in country.attributes['NAME']:
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor=(colors["Africa"]),
                                  label="Somaliland",
                                  edgecolor=(colors["Africa"]),
                                  linewidth=linewidth_cont_)
            elif "Kosovo" in country.attributes['NAME']:
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor=(colors["Europe"]),
                                  label="Kosovo",
                                  edgecolor=(colors["Europe"]),
                                  linewidth=linewidth_cont_)
            elif "N. Cyprus" in country.attributes['NAME']:
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor=(colors["Asia"]),
                                  label="N. Cyprus",
                                  edgecolor=(colors["Asia"]),
                                  linewidth=linewidth_cont_)
                
        # Resolve name conficts and recolor
        if country.attributes["NAME"] in "Guinea":
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor=(colors["Africa"]),
                                  label="Guinea",
                                  edgecolor=(colors["Africa"]),
                                  linewidth=linewidth_cont_)
        if country.attributes["NAME"] in "Antarctica":
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor='white',
                                  label="Antarctica",
                                  edgecolor='white',
                                  linewidth=linewidth_cont_)
            
    # Correct provinces and subnational territories
    for subcountry in subcountries:
        # Fix French Guyana
        if "French" in subcountry.attributes["name_en"]:
            ax.add_geometries(subcountry.geometry, ccrs.PlateCarree(),
                              facecolor=(colors["South America"]),
                              label="French Guyana",
                              edgecolor=(colors["South America"]),
                              linewidth=linewidth_cont_)
        # Fix Greenland
        elif "Greenland" in subcountry.attributes["name_en"]:
            ax.add_geometries(subcountry.geometry, ccrs.PlateCarree(),
                              facecolor=(colors["North America"]),
                              label=subcountry.attributes["name_en"],
                              edgecolor=(colors["North America"]),
                              linewidth=linewidth_cont_)
        elif "Pituffik" in subcountry.attributes["name_en"]:
            ax.add_geometries(subcountry.geometry, ccrs.PlateCarree(),
                              facecolor=(colors["North America"]),
                              label=subcountry.attributes["name_en"],
                              edgecolor=(colors["North America"]),
                              linewidth=linewidth_cont_)
        elif "Qeqqata" in subcountry.attributes["name_en"]:
            ax.add_geometries(subcountry.geometry, ccrs.PlateCarree(),
                              facecolor=(colors["North America"]),
                              label=subcountry.attributes["name_en"],
                              edgecolor=(colors["North America"]),
                              linewidth=linewidth_cont_)
        elif "Kujalleq" in subcountry.attributes["name_en"]:
            ax.add_geometries(subcountry.geometry, ccrs.PlateCarree(),
                              facecolor=(colors["North America"]),
                              label=subcountry.attributes["name_en"],
                              edgecolor=(colors["North America"]),
                              linewidth=linewidth_cont_)
        elif "Qaasuitsup" in subcountry.attributes["name_en"]:
            ax.add_geometries(subcountry.geometry, ccrs.PlateCarree(),
                              facecolor=(colors["North America"]),
                              label=subcountry.attributes["name_en"],
                              edgecolor=(colors["North America"]),
                              linewidth=linewidth_cont_)
        elif "Sermersooq" in subcountry.attributes["name_en"]:
            ax.add_geometries(subcountry.geometry, ccrs.PlateCarree(),
                              facecolor=(colors["North America"]),
                              label=subcountry.attributes["name_en"],
                              edgecolor=(colors["North America"]),
                              linewidth=linewidth_cont_)
        # Fix missing islands
        elif "Santa Cruz de Tenerife" in subcountry.attributes["name_en"]:
            ax.add_geometries(subcountry.geometry, ccrs.PlateCarree(),
                              facecolor=(colors["Europe"]),
                              label=subcountry.attributes["name_en"],
                              edgecolor=(colors["Europe"]),
                              linewidth=linewidth_cont_)
        elif "Las Palmas" in subcountry.attributes["name_en"]:
            ax.add_geometries(subcountry.geometry, ccrs.PlateCarree(),
                              facecolor=(colors["Europe"]),
                              label=subcountry.attributes["name_en"],
                              edgecolor=(colors["Europe"]),
                              linewidth=linewidth_cont_)
        elif "Balearic Islands" in subcountry.attributes["name_en"]:
            ax.add_geometries(subcountry.geometry, ccrs.PlateCarree(),
                              facecolor=(colors["Europe"]),
                              label=subcountry.attributes["name_en"],
                              edgecolor=(colors["Europe"]),
                              linewidth=linewidth_cont_)
    return

# Other projections:
# ccrs.InterruptedGoodeHomolosine() #ccrs.PlateCarree() #ccrs.Mollweide() #ccrs.Robinson()
plt.figure()
projection = ccrs.PlateCarree() 
huid_colors = anthro.viz.region_colors()[0]
df2 = pd.read_csv('../../../miscellaneous/region_definitions.csv')
plot_huid_countries(df2,projection,huid_colors,edgecolor='white')

plt.figure()
projection = ccrs.Robinson() 
huid_colors = anthro.viz.region_colors()[0]
df2 = pd.read_csv('../../../miscellaneous/region_definitions.csv')
plot_huid_countries(df2,projection,huid_colors,edgecolor='white')




# %%
