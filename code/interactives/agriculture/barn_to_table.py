#%%
import numpy as np
import pandas as pd
import bokeh.io 
import bokeh.plotting
import bokeh.palettes
from bokeh.models import * 
import bokeh.transform
import bokeh.layouts
import anthro.viz
import anthro.io
colors, palette = anthro.viz.bokeh_theme()
bokeh.io.output_file('barn_to_table.html')

# ##############################################################################
# DATA LOADING AND CLEANING
# ##############################################################################
data = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_product_produced/processed/FAOSTAT_granular_categorized_product_and_population.csv')

# Compute population and production totals with nice formatting
data['pop_total'] = data['producing_population_Mhd'] * 1E6
data['prod_total'] = data['produced_Mt'] * 1E6

# Create nice formatting for each
data['pop_format'] = anthro.io.numeric_formatter(data['pop_total'].values, sci=False)
data['prod_format'] = anthro.io.numeric_formatter(data['prod_total'].values, sci=True, unit='t')

# Assign some colors
data.loc[(data['primary']=='cattle') & (data['secondary']=='beef'), 'color'] = colors['blue']
data.loc[(data['primary']=='cattle') & (data['secondary']=='milk'), 'color'] = colors['light_blue']
data.loc[(data['primary']=='chicken') & (data['secondary']=='poultry'), 'color'] = colors['green']
data.loc[(data['primary']=='chicken') & (data['secondary']=='eggs'), 'color'] = colors['light_green']
data.loc[(data['primary']=='duck') & (data['secondary']=='poultry'), 'color'] = colors['dark_brown']
data.loc[(data['primary']=='goat') & (data['secondary']=='meat'), 'color'] = colors['purple']
data.loc[(data['primary']=='goat') & (data['secondary']=='milk'), 'color'] = colors['light_purple']
data.loc[(data['primary']=='sheep') & (data['secondary']=='milk'), 'color'] = '#8a8d8e'
data.loc[(data['primary']=='sheep') & (data['secondary']=='meat'), 'color'] = '#4b4b4b'
data.loc[(data['primary']=='swine') & (data['secondary']=='meat'), 'color'] = colors['light_red']
data.loc[(data['primary']=='total') & (data['secondary']=='meat'), 'color'] = colors['light_red']
data.loc[(data['primary']=='total') & (data['secondary']=='milk'), 'color'] = colors['blue']
data.loc[(data['primary']=='total') & (data['secondary']=='eggs'), 'color'] = colors['green']


# ##############################################################################
# COLUMN DATA SOURCE DEFINITION
# ##############################################################################
cat_source = ColumnDataSource(data)
pop_display_source = ColumnDataSource({'year':[], 'producing_population_Mhd':[], 'pop_total':[],
                                        'color':[], 'secondary':[], 'primary':[]})
prod_display_source = ColumnDataSource({'year':[], 'produced_Mt':[], 'prod_total':[],
                                        'color':[], 'secondary':[], 'primary':[]})
# ##############################################################################
#  INTERACTION DEFINITION
# ##############################################################################
cat_select = Select(title='Product category', options=list(data['primary'].unique()),
                    value='Cattle')


pop_hover = HoverTool(tooltips=[('product', '@primary, @secondary'),
                                 ('producing animals', '@pop_total'),
                                 ('year', '@year')],
                      mode='vline')

prod_hover = HoverTool(tooltips=[('product', '@primary, @secondary'),
                                 ('amount produced', '@prod_total'),
                                 ('year', '@year')],
                      mode='vline')

# ##############################################################################
#  POPULATION TIME SERIES CANVAS DEFINITION
# ##############################################################################
pop_canvas = bokeh.plotting.figure(width=500, height=350, 
                                    x_axis_label='year',
                                    y_axis_label='producing population [millions]')
pop_canvas.circle(x='year', y='producing_population_Mhd', color='color', source=pop_display_source,
                line_width=1, size=8,
                legend_field='secondary', hover_color=colors['red'])
pop_canvas.add_tools(pop_hover)
pop_canvas.legend.location = 'top_left'

# ##############################################################################
#  MASS PRODUCED TIME SERIES CANVAS DEFINITION
# ##############################################################################
prod_canvas = bokeh.plotting.figure(width=500, height=350, 
                                    x_axis_label='year',
                                    y_axis_label='amount produced [million tonnes]')

prod_canvas.circle(x='year', y='produced_Mt', source=prod_display_source, color='color',
                  line_width=1, size=8,
                  legend_field='secondary',
                  hover_color=colors['red'])
prod_canvas.add_tools(prod_hover)
prod_canvas.legend.location = 'top_left'

# ##############################################################################
# PRODUCTION DONUT CANVAS DEFINITION
# ##############################################################################

# ##############################################################################
# POPULATION DONUT CANVAS DEFINITION
# ##############################################################################

# ##############################################################################
# LOLLIPOP BARN-TO-TABLE CANVAS DEFINITION
# ##############################################################################

# ##############################################################################
# CALLBACK DEFINITION AND ASSIGNMENT
# ##############################################################################
select_cb = anthro.io.load_js(['custom_fns.js', 'barn_to_table_select.js'],
                              args={'cat_select': cat_select,
                                    'cat_source': cat_source,
                                    'pop_display_source':pop_display_source,
                                    'prod_display_source':prod_display_source})

cat_select.js_on_change('value', select_cb)
# ##############################################################################
# LAYOUT AND SAVING
# ##############################################################################
col1 = bokeh.layouts.column(cat_select, pop_canvas, prod_canvas)
bokeh.io.save(col1)
# %%


# %%
