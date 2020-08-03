#%%
import imp
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import anthro.viz 
import anthro.tessellation as tess
import shapely
import scipy.spatial
from shapely.geometry import LineString, MultiLineString, MultiPoint, Point
from shapely.geometry import Polygon, box, MultiPolygon
from shapely.ops import nearest_points, linemerge, unary_union, polygonize
from shapely import affinity
import tqdm
imp.reload(tess)

# CHoose random starting values
values = np.array([30, 5, 1, 8])
target = values / values.sum()
N = len(target)
S = 5 * tess.disc_uniform_pick(N)
W = .8 * np.random.random(N) + .2
border = box(-10, -10, 10, 10)

tolerance = 1E-5
V, props, _ = tess.compute_power_diagram(S, W, target, border)
for i in tqdm.tqdm(range(100)):
    S, W = tess.adapt_position_weights(W, props)
    V, props, _ = tess.compute_power_diagram(S, W, target, border)
    W = tess.adapt_weights(props, W, 1E-3)
    V, props, _ = tess.compute_power_diagram(S, W, target, border)
    error = np.sum(props['areas'] -  border.area * target) / (2 * border.area)
    if np.abs(error) < tolerance:
        break




# %%


# %%


def voronoi_to_polygons(vor): #, border, target_areas):
    # Plot the Voronoi cells
    edge_map = { }
    for segment_list in vor.values():
        for edge, (A, U, tmin, tmax) in segment_list:
            edge = tuple(sorted(edge))
            if edge not in edge_map:
                if tmax is None:
                    tmax = 100
                if tmin is None:
                    tmin = -100
                edge_map[edge] = (A + tmin * U, A + tmax * U)
    return edge_map
    # lines = [shapely.geometry.LineString(l) for l in edge_map.values()]
    # polygons = border.difference(lines)

values = np.array([30, 5, 1, 20])
target = values / values.sum()
N = len(target)
S =  np.stack([np.random.normal(0, 1, N), np.random.normal(0, 1, N)], axis=1)
W = target
border = box(-10, -10, 10, 10)

tri_list, V = tess.get_power_triangulation(S, W)
vor = tess.get_voronoi_cells(S, V, tri_list)
edges = voronoi_to_polygons(vor)
edges
lines = shapely.geometry.MultiLineString(list(edges.values())).buffer(1E-3)
tess.display(S, W, tri_list, vor)
border.difference(lines)
# %%


# %%
