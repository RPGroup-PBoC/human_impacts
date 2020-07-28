import pandas as pd
import squarify as sq
import numpy as np
from bokeh.themes import Theme
from bokeh.models import *
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.path import Path
from matplotlib.patches import BoxStyle
from matplotlib.offsetbox import AnchoredText
import geopandas as gpd
import seaborn as sns
import altair as alt
import bokeh.io
from . import geom

# Style and useful function definitions.
def titlebox(
    ax, text, color, bgcolor=None, size=8, boxsize=0.1, pad=0.05, loc=10, **kwargs
):
    """Sets a colored box about the title with the width of the plot"""
    boxsize=str(boxsize * 100)  + '%'
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("top", size=boxsize, pad=pad)
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.spines["top"].set_visible(False)
    cax.spines["right"].set_visible(False)
    cax.spines["bottom"].set_visible(False)
    cax.spines["left"].set_visible(False)

    plt.setp(cax.spines.values(), color=color)
    if bgcolor != None:
        cax.set_facecolor(bgcolor)
    else:
        cax.set_facecolor("white")
    at = AnchoredText(text, loc=loc, frameon=False, prop=dict(size=size, color=color))
    cax.add_artist(at)


def ylabelbox(ax, text, color, bgcolor=None, size=6, boxsize=0.1, pad=0.05, **kwargs):
    """Sets a colored box about the title with the width of the plot"""
    boxsize=str(boxsize * 100)  + '%'
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("left", size=boxsize, pad=pad)
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.spines["top"].set_visible(True)
    cax.spines["right"].set_visible(True)
    plt.setp(cax.spines.values(), color=color)
    if bgcolor != None:
        cax.set_facecolor(bgcolor)
    else:
        cax.set_facecolor("white")

    at = AnchoredText(
        text,
        loc=10,
        frameon=False,
        prop=dict(rotation="vertical", size=size, color=color),
    )
    cax.add_artist(at)

def assign_rect_bounds(df, key, width=500, height=500, text_pad=0,
                       copy_df=False):
    """
    Uses squarify to assign the bounds for a tree map. 
    """
    # Make a copy of the dataframe
    if copy_df:
        df = df.copy()

    # Compute the values and rects. 

    # Drop the quantities that are equal to zero in hte key dimension
    df = df[df[key] > 0]
    values = sq.normalize_sizes(df[key], width, height)
    rects = sq.squarify(values, 0, 0, width, height)

    # Assign the information to the data frame and return
    df['left'] = [r['x'] for r in rects] 
    df['right'] = [r['x'] + r['dx'] for r in rects]
    df['bottom'] = [r['y'] for r in rects]
    df['top'] = [r['y'] + r['dy'] for r in rects]

    # Determine if text padding should be applied
    df['text_left'] = df['left'] + text_pad
    df['text_bottom'] = df['bottom'] + text_pad
    df['text_right'] = df['right'] - text_pad
    df['text_top'] = df['top'] - text_pad

    return df

def altair_theme():
    colors = {'green': '#7AA974', 'light_green': '#BFD598',
              'pale_green': '#DCECCB', 'yellow': '#EAC264',
              'light_yellow': '#F3DAA9', 'pale_yellow': '#FFEDCE',
              'blue': '#738FC1', 'light_blue': '#A9BFE3',
              'pale_blue': '#C9D7EE', 'red': '#D56C55', 'light_red': '#E8B19D',
              'pale_red': '#F1D4C9', 'purple': '#AB85AC',
              'light_purple': '#D4C2D9', 'dark_green':'#7E9D90', 'dark_brown':'#905426'}
    palette = [colors['red'], colors['blue'], colors['green'], 
               colors['purple'], colors['dark_green'], colors['dark_brown'],
               colors['yellow'], colors['light_red'], colors['light_blue'], 
               colors['light_green'], colors['light_purple']]
    
    def _theme():
        return {
            'config': {
                'background': 'white',
                    'group': { 
                    'fill': '#E3DCD0'
                    },
                'view': {
                    'strokeWidth': 0,
                    'height': 300,
                    'width': 400,
                    'fill': '#E3DCD0'
                    },
                'mark': {
                    'strokeWidth': 0.5,
                    'stroke': 'black'
                },
                'axis': {
                    'domainColor': None,
                    'labelFont': 'Lucida Sans Unicode',
                    'titleFont': 'Lucida Sans Unicode',
                    'titleFontWeight': 400,
                    'grid': False,
                    'ticks': True,
                    'tickColor': 'white',
                    'tickOffset': 8,
                    'tickWidth': 1.5
                },
                'range': {
                    'category': palette
                },
                'legend': {
                    'labelFont': 'Lucida Sans Unicode',
                    'titleFont': 'Lucida Sans Unicode',
                    'titleFontWeight': 400
                },
                'title' : { 
                    'font': 'Lucida Sans Unicode',
                    'fontWeight': 400,
                    'anchor': 'middle'

                }
                  }
                }

    alt.themes.register('pboc', _theme)# enable the newly registered theme
    alt.themes.enable('pboc')

def color_palette():
    """
    Returns a dictionary of the PBOC color palette
    """
    return {'green': '#7AA974', 'light_green': '#BFD598',
              'pale_green': '#DCECCB', 'yellow': '#EAC264',
              'light_yellow': '#F3DAA9', 'pale_yellow': '#FFEDCE',
              'blue': '#738FC1', 'light_blue': '#A9BFE3',
              'pale_blue': '#C9D7EE', 'red': '#D56C55', 'light_red': '#E8B19D',
              'pale_red': '#F1D4C9', 'purple': '#AB85AC',
              'light_purple': '#D4C2D9', 'dark_green':'#7E9D90', 'dark_brown':'#905426'}

def bokeh_theme():
    """A custom bokeh theme to match PBoC 2e colors"""
    theme_json = {'attrs':
            {'Figure': {
                'background_fill_color': '#E3DCD0',
                'outline_line_color': '#FFFFFF',
            },
            'Axis': {
            'axis_line_color': "white",
            'major_tick_in': 7,
            'major_tick_line_width': 2.5,
            'major_tick_line_color': "white",
            'minor_tick_line_color': "white",
            'axis_label_text_font': 'Helvetica',
            'axis_label_text_font_style': 'normal'
            },
            'Grid': {
                'grid_line_color': None,
            },
            'Legend': {
                'background_fill_color': '#E3DCD0',
                'border_line_color': '#FFFFFF',
                'border_line_width': 1.5,
                'background_fill_alpha': 0.5
            },
            'Text': {
                'text_font_style': 'normal',
               'text_font': 'Helvetica'
            },
            'Title': {
                'background_fill_color': '#FFEDC0',
                'text_font_style': 'normal',
                'align': 'center',
                'text_font': 'Helvetica',
                'offset': 2,
            }}}

    theme = Theme(json=theme_json)
    bokeh.io.curdoc().theme = theme

    # Define the colors
    colors = color_palette()
    palette = [v for k, v in colors.items() if 'pale' not in k]
    return [colors, palette]

def load_js(fname, args):
    """
    Given external javascript file names and arguments, load a bokeh CustomJS
    object
    
    Parameters
    ----------
    fname: str or list of str
        The file name of the external javascript file. If the desired javascript
        exists in multiple external files, they can be provided as a list of
        strings.
    args: dict
        The arguments to supply to the custom JS callback. 
    
    Returns
    -------
    cb : bokeh CustomJS model object
        Returns a bokeh CustomJS model object with the supplied code and
        arguments. This can be directly assigned as callback functions.
    """
    if type(fname) == str:
        with open(fname) as f:
            js = f.read() 
    elif type(fname) == list:
        js = ''
        for _fname in fname:
            with open(_fname) as f:
                js += f.read()

    cb = CustomJS(code=js, args=args)
    return cb

def plotting_style(grid=False):
    """
    Sets the style to the publication style
    """
    rc = {'axes.facecolor': '#E3DCD0',
          'font.family': 'Lucida Sans Unicode',
          'grid.linestyle': '-',
          'grid.linewidth': 0.5,
          'grid.alpha': 0.75,
          'grid.color': '#ffffff',
          'axes.grid': grid,
          'ytick.direction': 'in',
          'xtick.direction': 'in',
          'xtick.gridOn': grid,
          'ytick.gridOn': grid,
          'ytick.major.width':5,
          'xtick.major.width':5,
          'ytick.major.size': 5,
          'xtick.major.size': 5,
          'mathtext.fontset': 'stixsans',
          'mathtext.sf': 'sans',
          'legend.frameon': True,
          'legend.facecolor': '#FFEDCE',
          'figure.dpi': 150,
           'xtick.color': 'k',
           'ytick.color': 'k'}
    plt.rc('text.latex', preamble=r'\usepackage{sfmath}')
    plt.rc('mathtext', fontset='stixsans', sf='sans')
    sns.set_style('darkgrid', rc=rc)
    return color_palette()

def compute_voronoi_treemap(cell_names, cell_weights, imax=1000, error=0.001):
    """
    Computes a Voronoi treemap with a *single* layer.
    """
    vcell = geom.optimize_voronoi(cell_weights, imax=imax, error=0.001)
    gdf = pd.concat([gpd.GeoSeries(cell) for cell in vcell]).pipe(gpd.GeoDataFrame)
    gdf = gdf.rename(columns={0:'geometry'})
    gdf['cell'] = np.arange(len(cell_names))
    _df = pd.DataFrame([])
    _df['name'] = cell_names
    _df['weights'] = cell_weights
    _df['cell'] = np.arange(len(cell_names))
    result = gdf.merge(_df, on=['cell'])
    return [result, vcell]
