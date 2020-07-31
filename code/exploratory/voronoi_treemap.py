#%%
import imp
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz 
import anthro.geom
import shapely
import scipy.spatial
from shapely.geometry import LineString, MultiLineString, MultiPoint, Point
from shapely.geometry import Polygon, box, MultiPolygon
from shapely.ops import nearest_points, linemerge, unary_union, polygonize
from shapely import affinity

imp.reload(anthro.geom)
colors = anthro.viz.plotting_style()
values = np.array([10, 20, 3, 10, 10, 10, 10, 60]) #, 3, 40, 9, 10])
weights = values / values.sum()
error = 0.01
imax = 100

# Initialize
N = len(weights)
S = 5 * anthro.geom.disc_uniform_pick(N)
W = 0.8 * np.random.random(N) + 0.2
bs = 10 
border = box(-bs, -bs, bs, bs)

tri_list, V = anthro.geom.get_power_triangulation(S, W)
cellmap = anthro.geom.get_voronoi_cells(S, W, tri_list)

# get the lines associated with all the Voronoi cells
edge_map = { }
edge_bounds=bs
for segment_list in cellmap.values():
    for edge, (A, U, tmin, tmax) in segment_list:
        edge = tuple(sorted(edge))
        if edge not in edge_map:
           if tmax is np.inf:
               tmax = edge_bounds
           if tmin is np.inf:
               tmin = -edge_bounds
           edge_map[edge] = (A + tmin * U, A + tmax * U)
_lines = [LineString(e) for e in edge_map.values()]
# _V_map = border.difference(_lines)
V_map = shapely.ops.polygonize(edge_map.values())
areas = []
for p in V_map:
    areas.append(p.area)
    

#%%


v = anthro.geom.optimize_voronoi(weights)
v

# %%
