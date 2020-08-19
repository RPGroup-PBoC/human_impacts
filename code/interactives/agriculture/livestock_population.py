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
bokeh.io.output_file('./livestock_population.html')

# Load the datasets 
animal_data = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_livestock_population.csv')
pop_data = pd.read_csv('../../../data/anthropocene/FAOSTAT_world_population/processed/FAOSTAT_human_population.csv')

# Update the animal names. 
names = [f'{s[0].upper()}{s[1:]}' for s in animal_data['animal'].values]
animal_data['animal'] = names
animal_data['pop_total'] = animal_data['population_Mhd'] * 1E6
pop_data['pop_total'] = pop_data['population_Mhd'] * 1E6

# Assign broader categories 
_top_pop = animal_data.groupby(['animal'])['population_Mhd'].max().reset_index().sort_values(
                by='population_Mhd', ascending=False)
top_pop = _top_pop['animal'].values[:6]

# Define the color palettes
category_dict = {'chicken':colors['green'], 'cattle':colors['blue'],
                 'swine':colors['light_red'], 'sheep':colors['purple'],
                 'duck':colors['dark_brown'], 'goat':colors['light_blue'],
                 'all other livestock': '#4b4b4b'}

for i, anml in enumerate(animal_data['animal'].unique()):
    if anml in top_pop:
        cat = anml
    else:
        cat = 'All other livestock'
    animal_data.loc[animal_data['animal']==anml, 'color'] = category_dict[cat.lower()]
    animal_data.loc[animal_data['animal']==anml, 'category'] = cat
    
# Make a ne data  source for breakdown by category.
cat_data = animal_data.groupby(['year', 'category', 'color'])[['population_Mhd', 'pop_total']].sum().reset_index()

# compute the yearly breakdown of all animals.
for i, yr in enumerate(animal_data['year'].unique()):
    d = animal_data[animal_data['year']==yr]
    humans = pop_data[pop_data['year']==yr]['population_Mhd'].values[0]
    total = d['population_Mhd'].sum()
    pop = d['population_Mhd'].values
    animal_data.loc[animal_data['year']==yr, 'human_population'] = humans * 1E6
    animal_data.loc[animal_data['year']==yr, 'fraction'] = pop / total
    animal_data.loc[animal_data['year']==yr, 'capita'] = pop*1E6 / humans

for i, yr in enumerate(cat_data['year'].unique()):
    d = cat_data[cat_data['year']==yr]
    humans = pop_data[pop_data['year']==yr]['population_Mhd'].values[0] * 1E6
    total = d['population_Mhd'].sum()
    pop = d['population_Mhd'].values
    cat_data.loc[cat_data['year']==yr, 'human_population'] = humans
    cat_data.loc[cat_data['year']==yr, 'fraction'] = pop / total
    cat_data.loc[cat_data['year']==yr, 'angle'] = 2 * np.pi * (pop / total)
    cat_data.loc[cat_data['year']==yr, 'capita'] = pop*1E6 / humans

# Add labels with nice formatting.
cat_data['human_population_label'] = anthro.io.numeric_formatter(cat_data['human_population'], unit='') 
animal_data['human_population_label'] = anthro.io.numeric_formatter(animal_data['human_population'], unit='') 
cat_data['population_label'] = anthro.io.numeric_formatter(cat_data['population_Mhd'].values*1E6, unit='') 
cat_data['frac_label'] = [f'{np.round(100 * v, decimals=1)}%' for v in cat_data['fraction'].values]
cat_data['frac_label'] = cat_data['frac_label'].str.pad(28, side='left')
animal_data['population_label'] = anthro.io.numeric_formatter(animal_data['population_Mhd'].values*1E6, unit='') 
cat_data.head()

# Make a multiline df and animal and category
cat_multiline_df = pd.DataFrame([])
for g, d in cat_data.groupby(['category', 'color']):
    cat_multiline_df = cat_multiline_df.append({'years': list(d['year'].values),
                                                'pop': list(d['pop_total']),
                                                'category':g[0],
                                                'color':g[1]}, ignore_index=True)
animal_multiline_df = pd.DataFrame([])
for g, d in animal_data.groupby(['category', 'color']):
    animal_multiline_df = animal_multiline_df.append({'years': list(d['year'].values),
                                                      'pop': list(d['pop_total']),
                                                      'category':g[0],
                                                      'color':g[1]}, ignore_index=True)

# ##############################################################################
# DATA SOURCE DEFINITION
# ##############################################################################
animal_source = ColumnDataSource(animal_data)
animal_multiline = ColumnDataSource(animal_multiline_df)
cat_source = ColumnDataSource(cat_data)
cat_multiline = ColumnDataSource(cat_multiline_df)
cat_display = ColumnDataSource({'year':[], 'angle':[], 'color':[],
                              'human_pop':[], 'cat_pop':[], 
                              'capita':[], 'frac_label':[], 'frac':[],
                              'category':[]})
animal_display = ColumnDataSource({'year':[], 'color':[], 
                                  'human_pop':[], 'animal_pop':[],
                                  'capita':[], 'frac':[],
                                  'animal':[]})

# ##############################################################################
# INTERACTIONS
# ##############################################################################
year_slider = Slider(start=cat_data['year'].min(), end=cat_data['year'].max(),
                    value=cat_data['year'].min(), title='select year', step=1)
TOOLTIPS = [('year', '@year'),
            ('animal', '@category'),
            ('animal population', '@population_label'),
            ('human population', '@human_population_label'),
            ('fraction of livestock population', '@frac{0.0%}'),
            ('animals per capita', '@capita{0.0}')]


# ##############################################################################
# CAT LEGEND CANVAS 
# ##############################################################################
cat_legend = bokeh.plotting.figure(width=200, height=300)
cat_legend.circle(x='year', y='pop_total', color='color', size=0, source=cat_source,
                  line_color='black', line_width=0.5, legend_field='category')
cat_legend.background_fill_color = None
cat_legend.axis.visible = False
cat_legend.axis.axis_label = None
cat_legend.toolbar_location = None

# ##############################################################################
# ANIMAL LEGEND CANVAS 
# ##############################################################################
animal_legend = bokeh.plotting.figure(width=200, height=300)
animal_legend.circle(x='year', y='pop_total', color='color', size=0, source=animal_source,
                  line_color='black', line_width=0.5, legend_field='animal')

animal_legend.background_fill_color = None
animal_legend.axis.visible = False
animal_legend.axis.axis_label = None
animal_legend.toolbar_location = None

# ##############################################################################
# CATEGORY TIME SERIES PLOT
# ##############################################################################
cat_time = bokeh.plotting.figure(width=300, height=300, x_axis_label='year',
                                y_axis_label='population', y_axis_type='log')
cat_time.multi_line(xs='years', ys='pop', color='color', source=cat_multiline)
cat_time.circle(x='year', y='pop_total', color='color', size=4, source=cat_source,
                name='cat_time_points', line_width=0.5, line_color='black',)
cat_time_hover = HoverTool(tooltips=TOOLTIPS, names=['cat_time_points'])
cat_time.add_tools(cat_time_hover)

# ##############################################################################
# CATEGORY DONUT PLOT
# ##############################################################################
cat_donut = bokeh.plotting.figure(width=400, height=400,
                                    title='breakdown of global livestock population',
                                    tooltips=TOOLTIPS) 
cat_donut.wedge(x=0, y=1, radius=0.7,
                  start_angle=bokeh.transform.cumsum('angle', include_zero=True),
                  end_angle = bokeh.transform.cumsum('angle'),
                 fill_color='color', name='wedges',
                 source=cat_display)
cat_donut.axis.visible = False
cat_donut.axis.axis_label = None
cat_donut.toolbar_location = None
cat_donut.circle(x=0, y=1, radius=0.35, color='white', 
                              name='mask')
cat_donut.background_fill_color = 'white'

# Add labels to the wedges
labels = LabelSet(x=0, y=1, text='frac_label',
                  angle=bokeh.transform.cumsum('total_angle', include_zero=True), 
                  source=cat_display, render_mode='canvas',
                 text_color='white', text_font_size='10pt')
cat_donut.add_layout(labels)

# Add the hover
cat_hover = HoverTool(tooltips=TOOLTIPS, mode='mouse', names=['wedges']) 
cat_donut.add_tools(cat_hover)

# ##############################################################################
# ANIMAL TIME SERIES
# ##############################################################################
animal_time = bokeh.plotting.figure(width=300, height=300, x_axis_label='year',
                                y_axis_label='livestock population', y_axis_type='log')
animal_time.multi_line(xs='years', ys='pop', color='color', source=animal_multiline)
animal_time.circle(x='year', y='pop_total', color='color', size=4, source=animal_source,
                name='animal_time_points', line_width=0.5, line_color='black',)
animal_time_hover = HoverTool(tooltips=TOOLTIPS, names=['animal_time_points'])
animal_time.add_tools(animal_time_hover)

# ##############################################################################
# ANIMAL STICK PLOT
# ##############################################################################
x_range = list(animal_data[animal_data['year']==2018].sort_values(by='population_Mhd',
              ascending=False)['animal'].unique())
animal_stick = bokeh.plotting.figure(width=300, height=300, x_range=x_range,
                                    y_axis_label='fraction of livestoc pop.',
                                    y_axis_type='log')

animal_stick.ray(x='animal', y='frac', length=1000, angle=3 * np.pi/2,
                color='color', source=animal_display, line_width=2.5)
animal_stick.circle(x='animal', y='frac', size=4, line_color='black', line_width=0.5,
                color='color', source=animal_display, hover_color='dodgerblue',
                name='animal_points')
animal_stick.xaxis.major_label_orientation = np.pi/4
animal_stick.axis.major_tick_line_color = None
stick_hover = HoverTool(tooltips=TOOLTIPS, mode='vline', names=['animal_points'])
animal_stick.add_tools(stick_hover)

# ##############################################################################
# CALLBACK DEFINITION
# ##############################################################################
cb = anthro.io.load_js('livestock_population.js', 
                        args={'year_slider':year_slider,
                              'cat_display':cat_display,
                              'animal_display':animal_display,
                              'cat_source':cat_source, 'animal_source':animal_source})
year_slider.js_on_change('value', cb)
# ##############################################################################
# LAYOUT DEFINITION
# ##############################################################################
cat_col = bokeh.layouts.column(year_slider, cat_legend)
cat_row = bokeh.layouts.row(cat_col, cat_time, cat_donut)
animal_col = bokeh.layouts.column(year_slider, animal_legend)
animal_row = bokeh.layouts.row(animal_col, animal_time, animal_stick)
cat_panel = Panel(child=cat_row, title='(A) Population of major livestock')
animal_panel = Panel(child=animal_row, title='(B) Population of all livestock')
tabs = Tabs(tabs=[cat_panel, animal_panel])
bokeh.io.save(cat_panel)
# %%
