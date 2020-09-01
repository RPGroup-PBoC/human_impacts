# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:13:33 2020

@author: tinev

This data set uses the accumulated cyclone energy (ACE) of North Atlantic
hurricane seasons 1851-2019. Source for 1851-2016 data:
    http://psl.noaa.gov/data/timeseries/monthly/ACE/
Source for 2017-2019 data:
    http://climatlas.com/tropical/
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import data from tab-separated file made from combining NOAA and Climatlas
# data sets. Convert columns to np arrays.
ace_data = pd.read_table('ace_data.tsv')
year = np.array(ace_data['year'])
ace = np.array(ace_data['ace'])

# Let's get some idea of trends in total ACE - compute 10-yr rolling avg.
ace_10yravg = np.zeros(np.size(ace)-9)
for i in range(np.size(ace_10yravg)):
    ace_10yravg[i] = np.average(ace[i:i+10])

# Plot 10-yr rolling avg.
plt.figure()
plt.plot(year[9:], ace_10yravg)
plt.ylabel('ACE (10^4 kt^2)')
plt.title('accumulated cyclone energy, 10-year rolling avgs, 1851-2019')
plt.show()

# Obviously there's a sinusoidal pattern here, most likely driven by the 
# Atlantic Multidecadal Oscillation.