#%%
import imp
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz 
import anthro.geom
imp.reload(anthro.geom)
colors = anthro.viz.plotting_style()
values = np.array([10, 20, 3, 60]) #, 3, 40, 9, 10])
weights = values / values.sum()
error = 0.01
imax = 100
vcell = anthro.geom.optimize_voronoi(weights, imax=10)
vcell

# %%
