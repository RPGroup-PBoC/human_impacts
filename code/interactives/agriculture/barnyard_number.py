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
bokeh.io.output_file('./barnyard_number
.html')

# Load the datasets 
animal_data = pd.read_csv('../../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_livestock_population.csv')
pop_data = pd.read_csv('../../../data/general/FAOSTAT_world_population/processed/FAOSTAT_human_population.csv')

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
    animal_data.loc[animal_data['year']==yr, 'barnyard_number'] = pop / humans

for i, yr in enumerate(cat_data['year'].unique()):
    d = cat_data[cat_data['year']==yr]
    humans = pop_data[pop_data['year']==yr]['population_Mhd'].values[0] * 1E6
    total = d['population_Mhd'].sum()
    pop = d['population_Mhd'].values
    cat_data.loc[cat_data['year']==yr, 'human_population'] = humans
    cat_data.loc[cat_data['year']==yr, 'fraction'] = pop / total
    cat_data.loc[cat_data['year']==yr, 'barnyard_number'] = pop / humans

# Add formatting in to the labels. 
base_powers = np.floor(np.log10(cat_data['pop_total'].values))
base_dict = {2:'o', 3:'k', 6:'m', 9:'b'}
str_vals = []
for i, v in enumerate(cat_data['pop_total']):
    base = base_powers[i]
    if base < 3:
        raise ValueError('value < 3')
    elif (base >= 3) & (base < 6):
        n = 3
        l = 'k'
    elif (base >= 6) & (base < 9):
        n = 6
        l = 'm'
    else:
        n = 9     
        l = 'b'
    val = str(np.round(v*10**-n, decimals=2)) 
    if len(val) <= 3:
        val = val
    else:
        if val[3] == '.':
            end = 4
        else:
            end = 3
        val = val[:end]
    str_vals.append(f'{val}{l}')

cat_data['label'] = str_vals
cat_data['label'] = cat_data['label'].str.pad(28, side = "left")
cat_data['pop_total'] = cat_data['population_Mhd'].values * 1E6
cat_data['angle'] = cat_data['fraction'] * 2 * np.pi


# Compute the year totals. 
tots = cat_data.groupby(['year'])['pop_total'].sum().reset_index()
# ##############################################################################
# COLUMN DATASOURCE DEFINITIONS 
# ##############################################################################


# Define the column data sources. 
animal_source = ColumnDataSource(animal_data)
cat_source = ColumnDataSource(cat_data)
frac_source = ColumnDataSource({'angle':[], 'category':[], 'pop_total':[], 
                                'fraction':[], 'color':[], 'label':[],
                                'year':[]})
barnyard_source = ColumnDataSource({'barnyard_number':[], 'animal':[], 
                                    'color':[], 'year':[]})
animal_filter = IndexFilter([])
animal_view = CDSView(source=animal_source, filters=[animal_filter])

# ##############################################################################
# DEFINING INTERACTIONS
# ##############################################################################
# Define the hover interaction. 
year_hover = HoverTool(
        tooltips=[('year', '@year'),
                  ('selected livestock population', '@pop_total{0.00a}'),
                  ('human population', '@human_population{0.00a}'),
                  ('fraction of livestock population', '@fraction{0.00%}')],
        mode='vline',
        line_policy='nearest',
        names=['points'])

animal_hover = HoverTool(
        tooltips=[('livestock category', '@category'),
                  ('population', '@pop_total{0.00a}'),
                  ('fraction of livestock population', '@fraction{0.00%}'),
                  ('year', '@year')],
        names=['animals'])

barnyard_hover = HoverTool(
            tooltips=[('livestock_category', '@animal'),
                      ('barnyard number', '≈ @barnyard_number{0.0}'),
                      ('year', '@year')],
            mode='vline')

# Set up the selection widgets. 
animal_select = Select(title='Livestock Category', value='', options=list(_top_pop['animal'].values))

# ##############################################################################
# CANVAS FOR TIME SERIEs
# ############################################################################## 
year_canvas = bokeh.plotting.figure(width=500, height=500, x_axis_label='year',
                                    y_axis_label='population (million)',
                                    title='LIVESTOCK ANIMAL POPULATION BY SELECTED YEAR',
                                    tools=[])
year_canvas.add_tools(year_hover)
year_canvas.circle(x='year', y='population_Mhd', color=colors['blue'],
                   line_width=1, size=8, source=animal_source, name='points',
                   view=animal_view,  hover_color=colors['red'])


# ##############################################################################
# CANVAS FOR LIVESTOCK POPULATION BREAKDOWN
# ##############################################################################
breakdown_canvas = bokeh.plotting.figure(width=500, height=300,
                                        x_range=[-0.7, 1.5],
                                        y_range=[0.5, 1.5],
                                        title='POPULATION BREAKDOWN BY YEAR',
                                        tools='hover')
breakdown_canvas.add_tools(animal_hover)
breakdown_canvas.wedge(x=0, y=1, radius=.7,
                       start_angle=bokeh.transform.cumsum('angle', include_zero=True),
                       end_angle=bokeh.transform.cumsum('angle'),
                       line_color='white', fill_color='color',
                       source=frac_source, name='animals',
                       legend_field='category') 
breakdown_canvas.axis.visible = False
breakdown_canvas.axis.axis_label = None
breakdown_canvas.toolbar_location = None
breakdown_canvas.legend.location = 'center_right'

circ = breakdown_canvas.circle(x=0, y=1, radius=0.35, color='white', 
                              name='mask')
breakdown_canvas.background_fill_color = 'white'
breakdown_canvas.legend.label_text_font_size = '8pt'

# Add labels to the wedges
labels = LabelSet(x=0, y=1, text='label',
                  angle=bokeh.transform.cumsum('angle', include_zero=True), 
                  source=frac_source, render_mode='canvas',
                  text_color='white', text_font_size='10pt')
breakdown_canvas.add_layout(labels)


# ##############################################################################
#  CANVAS FOR ANIMAL SPECIFIC BARNYARD NUMBER
# ##############################################################################
barnyard_canvas =  bokeh.plotting.figure(width=500, height=300,
                                        x_range=list(_top_pop['animal'].values),
                                        y_axis_label='barnyard number',
                                        y_axis_type='log',
                                        y_range=[0.001, 4.5],
                                        title='BARNYARD NUMBER BY ANIMAL BY SELECTED YEAR',
                                        tools = [])

barnyard_canvas.ray(x='animal', y='barnyard_number', length=1000, angle=3 * np.pi/2, 
                    color='color', source=barnyard_source, line_width=2.5)
barnyard_canvas.circle(x='animal', y='barnyard_number', color='color', size=10,
                       line_color='black', source=barnyard_source,
                       hover_color=colors['red'])                                        
barnyard_canvas.xaxis.major_label_orientation = np.pi/4
barnyard_canvas.axis.major_tick_line_color = None
barnyard_canvas.add_tools(barnyard_hover)


# ##############################################################################
# CANVAS DEFINITION
# ##############################################################################
animal_selection_cb = anthro.io.load_js(['custom_fns.js', 'livestock_population_select.js'],
                                        args={'animal_source':animal_source,
                                              'animal_select':animal_select,
                                              'animal_filter':animal_filter,
                                              'animal_view':animal_view})
year_selection_cb = anthro.io.load_js(['custom_fns.js', 'livestock_population_hover.js'],
                                       args={'cat_source':cat_source,
                                             'animal_source': animal_source,
                                             'frac_source': frac_source,
                                             'barnyard_source':barnyard_source})
animal_select.js_on_change('value', animal_selection_cb)
year_canvas.hover.callback = year_selection_cb


# ##############################################################################
#  LAYOUT SPECIFICATION AND SAVING
# ##############################################################################
# Define the layout. 
col1 = bokeh.layouts.column(animal_select, year_canvas)
col2 = bokeh.layouts.column(breakdown_canvas, barnyard_canvas)
row = bokeh.layouts.row(col1, col2)
bokeh.io.save(row)
# %%
