#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.io 
import anthro.viz
import pycountry
colors = anthro.viz.plotting_style()
cont_colors = {'Africa':colors['light_green'], 'Northern America':colors['light_red'],                
               'Europe':'#4b4b4b', 'Central America':colors['purple'],
               'South America':colors['dark_brown'],
               'Asia':colors['blue'], 'Oceania':colors['dark_green']}
cont_positions = {k:i for i, k in enumerate(cont_colors.keys())}

# Define the data from @rbanks

# %%
regions = ['Africa', 'Asia', 'Europe', 'Oceania', 
           'South America,', 'Central America', 'Northern America']

totals = [1.3E11, 1.1E12, 3.4E11, 1.6E10, 81E10, 9.2E10, 4.9E11]
per_capita = [300, 550, 490, 680, 340, 670, 1300]


# Set up the pie chart. 