#%%
import pandas as pd
import matplotlib.pyplot as plt
import anthro.viz
import holoviews as hv
import bokeh.io 
import bokeh.plotting
hv.extension('bokeh')
bokeh.io.output_notebook()
colors = anthro.viz.bokeh_theme()

# %%
# Load the two data sets. 
global_data = pd.read_csv('./alltech_feed_country_breakdown.csv')

# Restrict to countries with more than 10 mt per year of feed produced. 
global_data = global_data[global_data['mass_Mt'] >= 30]

# set up the chart object
bars = hv.Bars(data=global_data, 
              vdims=['mass_Mt'], 
              kdims=['survey_year', 'country']
              )
bars.opts(stacked=True, width=600, height=400,
          xlabel='Alltech survey year',
          ylabel='feed production [million tonnes]',
          title='Feed Production Above 30 Mt Annually',
          legend_position='left')
hv.save(bars, './country_breakdown.png')
#%%
species_data = pd.read_csv('./alltech_feed_species_breakdown.csv')
bars = hv.Bars(data=species_data,
               vdims=['mass_Mt'])
