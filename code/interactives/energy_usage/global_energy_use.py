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
colors, palette = anthro.viz.bokeh_theme()
bokeh.io.output_file('./global_energy_use.html')


# ##############################################################################
# DATA MUNGING
# ##############################################################################
# Load the datasets
power_data = pd.read_csv('../../../data/energy/BP_statistical_report_global_energy_usage/processed/BP_global_energy_usage_by_type.csv')
pop_data = pd.read_csv('../../../data/anthropocene/FAOSTAT_world_population/processed/FAOSTAT_human_population.csv')
pop_data = pop_data.append({'year':2019, 'population_Mhd': 7713468000 / 1E6}, 
                            ignore_index=True)
# By year, compute the per capita power. 
for g, d in pop_data.groupby(['year']):
    power_data.loc[power_data['year']==g, 'population_Bhd'] = d['population_Mhd'].values[0] * 1E6

# Manually add information for 2019
power_data['W_per_capita'] = power_data['consumption_TW'].values * 1E12 / power_data['population_Bhd'].values

# By year, compute the fractional occupancy. 
dfs = []
for g, d in power_data.groupby(['year']):
    tot_power = d['consumption_TW'].sum()
    tot_per_capita = d['W_per_capita'].sum()
    for _g, _d in d.groupby('type'):
        _d = _d.copy()
        _d['total_frac'] = _d['consumption_TW'].values / tot_power
        _d['capita_frac'] = _d['W_per_capita'].values / tot_per_capita
        dfs.append(_d)
power_source_df = pd.concat(dfs, sort=False)

# Compute the angles for the donut charts. 
power_source_df['total_angle'] = 2 * np.pi * power_source_df['total_frac'].values
power_source_df['capita_angle'] = 2 * np.pi * power_source_df['capita_frac'].values

# Add nicely formatted names to each.
power_source_df['total_label'] = anthro.io.numeric_formatter(power_source_df['consumption_TW'].values * 1E12, unit='W', sci=True)
power_source_df['capita_label'] = anthro.io.numeric_formatter(power_source_df['W_per_capita'].values, unit='W / person', sci=True)

# To each power type, assign a unique color. 
power_source_df.loc[power_source_df['type']=='Hydroelectric', 'color'] = colors['blue']
power_source_df.loc[power_source_df['type']=='Coal', 'color'] = '#6a6a6a' 
power_source_df.loc[power_source_df['type']=='Oil', 'color'] = '#000000' 
power_source_df.loc[power_source_df['type']=='Wind', 'color'] = '#FFFFFF' 
power_source_df.loc[power_source_df['type']=='Natural Gas', 'color'] = colors['red']
power_source_df.loc[power_source_df['type']=='Solar', 'color'] = '#eac264'
power_source_df.loc[power_source_df['type']=='Biodiesel/Biogasoline', 'color'] = colors['dark_green']
power_source_df.loc[power_source_df['type']=='Geothermal/Biomass/Other', 'color'] = colors['dark_brown']

# Assemble the data to multilines for simplicity in plotting
multiline_df = pd.DataFrame([])
for g, d in power_source_df.groupby(['type', 'color']):
    multiline_df = multiline_df.append({'years': list(d['year'].values),
                                         'total': list(d['consumption_TW'].values),
                                         'capita': list(d['W_per_capita'].values),
                                         'total_label':list(d['total_label'].values),
                                         'capita_label':list(d['total_label'].values),
                                         'type':g[0],
                                         'color':g[1]}, ignore_index=True)
# ##############################################################################
# DATA SOURCE DEFINITION
# ##############################################################################
multiline_source = ColumnDataSource(multiline_df)
power_source = ColumnDataSource(power_source_df)
donut_display = ColumnDataSource({'type':[], 'total_frac':[], 'capita_frac':[], 
                                  'total_angle':[], 'capita_angle':[],
                                  'color':[]})
# ##############################################################################
# DEFINE YEAR SLIDER INTERACTION
# ##############################################################################
year_slider = Slider(start=power_source_df['year'].min(),
                     end=power_source_df['year'].max(),
                     value=power_source_df['year'].min(),
                     step=1, title='Select Year')

# ##############################################################################
# DEFINE HOVER INTERACTION
# ##############################################################################
TOOLTIPS = [('year', '@year'),
            ('power type', '@type'),
            ('global consumption', '@total_label'),
            ('consumption per capita', '@capita_label')]

# ##############################################################################
# BLANK NARROW LEGEND CANVAS
# ##############################################################################
legend_canvas = bokeh.plotting.figure(height=700, width=220)
legend_canvas.circle(x='year', y='consumption_TW', color='color', size=0,
                    legend_field='type', source=power_source, line_color='black',
                    line_width=0.5)
legend_canvas.background_fill_color = 'white'
legend_canvas.toolbar.logo = None
legend_canvas.toolbar_location = None
legend_canvas.xaxis.major_tick_line_color = None
legend_canvas.yaxis.major_tick_line_color = None
legend_canvas.xaxis.major_label_text_font_size = '0px'
legend_canvas.yaxis.major_label_text_font_size = '0px'
legend_canvas.legend.location='center'

# ##############################################################################
# TOTAL CONSUMPTION CANVAS DEFINITION
# ##############################################################################
total_canvas = bokeh.plotting.figure(width=600, height=350,
                                     x_axis_label='year',
                                     y_axis_label='total consumption [TW]',
                                     title='global power consumption by type')
total_canvas.multi_line(xs='years', ys='total', line_width=1, color='color',
                         name='total_lines', source=multiline_source)
total_points = total_canvas.circle(x='year', y='consumption_TW', color='color', 
                                      size=6, source=power_source, line_color='black',
                                      line_width=0.1, hover_color='dodgerblue')
total_hover = HoverTool(tooltips=TOOLTIPS, renderers=[total_points])
total_canvas.add_tools(total_hover)
# # ##############################################################################
# # TOTAL CONSUMPTION DONUT
# # ##############################################################################
# total_donut = bokeh.plotting.figure(width=, height=425,
#                                     title='breakdown of global power consumption')

# total_donut.wedge(x=0, y=1, radius=0.7,
#                   start_angle=bokeh.transform.cumsum('total_angle', include_zero=True),
#                   end_angle = bokeh.transform.cumsum('total_angle'),
#                   fill_color='color', source=donut_display)
# total_donut.axis.visible = False
# total_donut.axis.axis_label = None
# total_donut.toolbar_location = None
# circ = total_donut.circle(x=0, y=1, radius=0.35, color='red', 
#                               name='mask')
# total_donut.background_fill_color = 'white'

# # Add labels to the wedges
# labels = LabelSet(x=0, y=1, text='total_frac',
#                   angle=bokeh.transform.cumsum('total_angle', include_zero=True), 
#                   source=donut_display, render_mode='canvas',
#                   text_color='white', text_font_size='10pt')
# total_donut.add_layout(labels)

# ##############################################################################
# CAPITA CONSUMPTION CANVAS DEFINITION
# ##############################################################################
capita_canvas = bokeh.plotting.figure(width=600, height=350,
                                     x_axis_label='year',
                                     y_axis_label='consumption per capita [W]',
                                     title='global per capita power consumption by type')
capita_canvas.multi_line(xs='years', ys='capita', line_width=1, color='color',
                         name='capita_lines', source=multiline_source)
capita_points = capita_canvas.circle(x='year', y='W_per_capita', color='color', size=6, 
                     name='capita_points', source=power_source,
                     line_color='black', line_width=0.1, alpha=0.8,
                     hover_color='dodgerblue')
capita_hover = HoverTool(tooltips=TOOLTIPS, renderers=[capita_points],
                  point_policy='snap_to_data', names=['capita_points'])
capita_canvas.add_tools(capita_hover)

# # ##############################################################################
# # CAPITA CONSUMPTION DONUT
# # ##############################################################################
# capita_donut = bokeh.plotting.figure(width=425, height=425,
#                                     title='PER CAPITA POWER CONSUMPTION BY TYPE')
# capita_donut.wedge(x=0, y=1, radius=0.7,
#                   start_angle=bokeh.transform.cumsum('capita_angle', include_zero=True),
#                   end_angle = bokeh.transform.cumsum('capita_angle'),
#                   line_color='white', fill_color='color',
#                   source=donut_display)
# capita_donut.axis.visible = False
# capita_donut.axis.axis_label = None
# capita_donut.toolbar_location = None
# circ = capita_donut.circle(x=0, y=1, radius=0.35, color='white', 
#                               name='mask')
# capita_donut.background_fill_color = 'white'

# # Add labels to the wedges
# labels = LabelSet(x=0, y=1, text='capita_frac',
#                   angle=bokeh.transform.cumsum('capita_angle', include_zero=True), 
#                   source=donut_display, render_mode='canvas',
#                   text_color='white', text_font_size='10pt')
# capita_donut.add_layout(labels)

# # ##############################################################################
# # CALLBACK DEFINITION
# # ##############################################################################
# cb = anthro.io.load_js('global_energy_use.js', 
#                        args={'year_slider':year_slider,
#                              'power_source':power_source,
#                              'donut_display':donut_display})
#  year_slider.js_on_change('value', cb)

# ##############################################################################
# LAYOUT DEFINITION
# ##############################################################################
# total_row = bokeh.layouts.row(total_canvas, total_donut)
# capita_row = bokeh.layouts.row(capita_canvas, capita_donut)
# interaction = bokeh.layouts.column(legend_canvas, year_slider)
# lay = bokeh.layouts.column(interaction, total_row, capita_row)
plots = bokeh.layouts.column(total_canvas, capita_canvas)
lay = bokeh.layouts.row(legend_canvas, plots)
bokeh.io.save(lay)
# %%
