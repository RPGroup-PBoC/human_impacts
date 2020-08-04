#%% 
import numpy as np
import pandas as pd 
from pywaffle import Waffle
import matplotlib.pyplot as plt 
import anthro.viz
colors = anthro.viz.plotting_style()

# Define the data from Eshel 2014 (percent of total)
dairy = 0.12
beef = 0.07 
poultry = 0.06  
pork = 0.04
eggs = 0.01
other = 0.04
plant = 1.00 - dairy - beef - poultry - pork - eggs - other

# Assemble a value list. 
values = np.array([plant, dairy, beef, poultry, pork, eggs, other]) * daily

# Define the daily kcal intake. 
breakdown = np.array(values) * daily
cat_colors = ['#e3dcd0', colors['light_blue'], colors['blue'], colors['green'],
             colors['red'], colors['light_green'], colors['pale_yellow']] 


fig = plt.figure(figsize=(2.5, 2.5), FigureClass=Waffle,
                 values=values,
                 colors=cat_colors,
                 rows=10,
                 columns=10,
                 vertical=True)  
plt.savefig('../../../figures/agriculture/eshel_2014_calorie_breakdown.svg')
# %%
