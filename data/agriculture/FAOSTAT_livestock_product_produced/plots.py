#%%
import pandas as pd
import holoviews as hv
import anthro.viz
hv.extension('bokeh')

# Load the data
data = pd.read_csv('processed/FAOSTAT_livestock_and_product.csv')


# Define the charts
quantity_curves = hv.Curve(data=data,
                      vdims=['mass_produced_Mt'], 
                      kdims=['year', 'subcategory']).groupby(['subcategory']).overlay()
quantity_curves.opts(width=600, height=400,
                    xlabel='year',
                    ylabel='mass of produced product [Mt]',
                    legend_position='left',
                    title='Production Quantity [million tonnes]')
hv.save(quantity_curves, 'output/production_quantity.png')

population_curves = hv.Curve(data=data,
                      vdims=['producing_population_Mhd'], 
                      kdims=['year', 'subcategory']).groupby(['subcategory']).overlay()
population_curves.opts(width=600, height=400,
                    xlabel='year',
                    ylabel='number of animals harvested [Mhd]',
                    legend_position='left',
                    title='Production Population [million head]')
hv.save(population_curves, 'output/production_population.png')
# %%
