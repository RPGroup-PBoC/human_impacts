import itertools
import numpy
from scipy.spatial import ConvexHull
import tqdm
from matplotlib.collections import LineCollection
from matplotlib import pyplot as plot
from shapely.geometry import LineString, MultiLineString, MultiPoint, Point
from shapely.geometry import Polygon, box, MultiPolygon
from shapely.ops import nearest_points, linemerge, unary_union, polygonize
from shapely import affinity

# --- Misc. geometry code -----------------------------------------------------

'''
Pick N points uniformly from the unit disc
This sampling algorithm does not use rejection sampling.
'''
def disc_uniform_pick(N):
	angle = (2 * numpy.pi) * numpy.random.random(N)
	out = numpy.stack([numpy.cos(angle), numpy.sin(angle)], axis = 1)
	out *= numpy.sqrt(numpy.random.random(N))[:,None]
	return out



def norm2(X):
	return numpy.sqrt(numpy.sum(X ** 2))



def normalized(X):
	return X / norm2(X)



# --- Delaunay triangulation --------------------------------------------------

def get_triangle_normal(A, B, C):
	return normalized(numpy.cross(A, B) + numpy.cross(B, C) + numpy.cross(C, A))



def get_power_circumcenter(A, B, C):
	N = get_triangle_normal(A, B, C)
	return (-.5 / N[2]) * N[:2]



def is_ccw_triangle(A, B, C):
	M = numpy.concatenate([numpy.stack([A, B, C]), numpy.ones((3, 1))], axis = 1)
	return numpy.linalg.det(M) > 0



def get_power_triangulation(S, R):
    # Compute the lifted weighted points
    S_norm = numpy.sum(S**2, axis = 1) - numpy.array(R)** 2
    S_lifted = numpy.concatenate([S, S_norm[:,None]], axis = 1)

    # Special case for 3 points
    if S.shape[0] == 3:
        if is_ccw_triangle(S[0], S[1], S[2]):
            return [[0, 1, 2]], numpy.array([get_power_circumcenter(*S_lifted)])
        else:
            return [[0, 2, 1]], numpy.array([get_power_circumcenter(*S_lifted)])

    # Compute the convex hull of the lifted weighted points
    hull = ConvexHull(S_lifted)

    # Extract the Delaunay triangulation from the lower hull
    tri_list = tuple([a, b, c] if is_ccw_triangle(S[a], S[b], S[c]) else [a, c, b]  for (a, b, c), eq in zip(hull.simplices, hull.equations) if eq[2] <= 0)

    # Compute the Voronoi points
    V = numpy.array([get_power_circumcenter(*S_lifted[tri]) for tri in tri_list])

    # Job done
    return tri_list, V



# --- Compute Voronoi cells ---------------------------------------------------

def get_voronoi_cells(S, W, tri_list):

    '''
    Compute the segments and half-lines that delimits each Voronoi cell
      * The segments are oriented so that they are in CCW order
      * Each cell is a list of (i, j), (A, U, tmin, tmax) where
         * i, j are the indices of two ends of the segment. Segments end points are
           the circumcenters. If i or j is set to None, then it's an infinite end
         * A is the origin of the segment
         * U is the direction of the segment, as a unit vector
         * tmin is the parameter for the left end of the segment. Can be None, for minus infinity
         * tmax is the parameter for the right end of the segment. Can be None, for infinity
         * Therefore, the endpoints are [A + tmin * U, A + tmax * U]
    '''
    S_norm = numpy.sum(S ** 2, axis = 1) - numpy.array(W)
    S_lifted = numpy.concatenate([S, S_norm[:,None]], axis = 1)
    # Compute the Voronoi points
    V = numpy.array([get_power_circumcenter(*S_lifted[tri]) for tri in tri_list])
    # Keep track of which circles are included in the triangulation
    vertices_set = frozenset(itertools.chain(*tri_list))

    # Keep track of which edge separate which triangles
    edge_map = { }
    for i, tri in enumerate(tri_list):
        for edge in itertools.combinations(tri, 2):
            edge = tuple(sorted(edge))
            if edge in edge_map:
                edge_map[edge].append(i)
            else:
                edge_map[edge] = [i]

    # For each triangle
    voronoi_cell_map = { i : [] for i in vertices_set }

    for i, (a, b, c) in enumerate(tri_list):
        # For each edge of the triangle
        for u, v, w in ((a, b, c), (b, c, a), (c, a, b)):
        # Finite Voronoi edge
            edge = tuple(sorted((u, v)))
            if len(edge_map[edge]) == 2:
                j, k = edge_map[edge]
                if k == i:
                    j, k = k, j

                # Compute the segment parameters
                U = V[k] - V[j]
                U_norm = norm2(U)

                # Add the segment
                voronoi_cell_map[u].append(((j, k), (V[j], U / U_norm, 0, U_norm)))
            else:
            # Infinite Voronoi edge
                # Compute the segment parameters
                A, B, C, D = S[u], S[v], S[w], V[i]
                U = normalized(B - A)
                I = A + numpy.dot(D - A, U) * U
                W = normalized(I - D)
                if numpy.dot(W, I - C) < 0:
                    W = -W

                # Add the segment
                voronoi_cell_map[u].append(((edge_map[edge][0], numpy.inf), (D,  W, 0, numpy.inf)))
                voronoi_cell_map[v].append(((numpy.inf, edge_map[edge][0]), (D, -W, numpy.inf, 0)))



    # Order the segments
    def order_segment_list(segment_list):
        # Pick the first element
        first = min((seg[0][0], i) for i, seg in enumerate(segment_list))[1]

        # In-place ordering
        segment_list[0], segment_list[first] = segment_list[first], segment_list[0]
        for i in range(len(segment_list) - 1):
            for j in range(i + 1, len(segment_list)):
                if segment_list[i][0][1] == segment_list[j][0][0]:
                    segment_list[i+1], segment_list[j] = segment_list[j], segment_list[i+1]
                    break

        return segment_list

    return { i : order_segment_list(segment_list) for i, segment_list in voronoi_cell_map.items() }

def compute_power_voronoi_map(S, W, border, eps):
    '''
    input:
    S - Voronoi points/sites
    W - positive real weights associated with Voronoi points
    eps - for shapely conversion of lines to polygon - needed?
    border - bounds of desired map

    output:
    tri_list: Delaunay triangulation from the lower hull
    V_cell: Set of polygons forming all Voronoi cells

    '''

    # Compute the power triangulation of the circles
    if S.shape[0] > 3:
        tri_list, tri_list_ = get_power_triangulation(S, W)

        # Compute the Voronoi cells
        voronoi_cell_map = get_voronoi_cells(S, W, tri_list)

        # get the lines associated with all the Voronoi cells
        edge_map = { }
        for segment_list in voronoi_cell_map.values():
            for edge, (A, U, tmin, tmax) in segment_list:
                edge = tuple(sorted(edge))
                if edge not in edge_map:
                    if tmax is numpy.inf:
                        tmax = 20
                    if tmin is numpy.inf:
                        tmin = -20

                    edge_map[edge] = (A + tmin * U, A + tmax * U)

        V_map = MultiLineString(list(edge_map.values())).buffer(eps)

        V_cell = border.difference(V_map)

        while len(S) != len(V_cell):
            V_cell = VoronoiMap_fix(S, V_cell)



    elif S.shape[0] <= 3:
        S_points = MultiPoint(S[:2])
        bisect = affinity.rotate(LineString(S_points), 90, 'center')
        bisect = affinity.scale(bisect, xfact=100, yfact=100)

        borders = unary_union(linemerge([border.boundary, bisect]))
        V_cell = MultiPolygon(polygonize(borders))

        while len(S) != len(V_cell):
            V_cell = VoronoiMap_fix(S, V_cell)

    return V_cell


def VoronoiMap_fix(S, V_cell):
    '''
    Use to shift Voronoi sites and adapt weights W
    input:
    V_cell - Set of polygons forming all Voronoi cells
    S: Voronoi points

    output:
    V_cell_corr - Corrected Voronoi polygons
    '''

    S_points = MultiPoint(S)

    V_cell_ = MultiPolygon([cell for cell in V_cell if ((cell.intersection(S_points)).type  != 'MultiPoint')])
    V_ = MultiPolygon([cell for cell in V_cell if ((cell.intersection(S_points)).type  == 'MultiPoint')])

    while (len(V_) >=1):
        for cell in V_:
            V_ = MultiPolygon([P for P in V_ if P != cell])
            # identify the multipe voronoi points in cell
            P = cell.intersection(S_points)
            P_coords = [((p_.xy[0][0], p_.xy[1][0])) for p_ in P]
            for s in P:
                # find point closest to s and split cell using line orthogonal to
                # their center line
                s_coords = ((s.xy[0][0], s.xy[1][0]))
                s_other = [tuple(s_) for s_ in P_coords if tuple(s_) != tuple(s_coords)]
                NN = nearest_points((s),MultiPoint(s_other))
                bisect = affinity.rotate(LineString(NN), 90, 'center')
                bisect = affinity.scale(bisect, xfact=100, yfact=100)

                borders = unary_union(linemerge([cell.boundary, bisect]))
                cell_split = polygonize(borders)

                for cell_ in cell_split:
                    if ((cell_.intersection(S_points)).type  == 'MultiPoint'):
                        poly=[]
                        for pol in V_:
                            poly.append(pol)
                        poly.append(cell_)
                        V_ = MultiPolygon(poly)
                    else:
                        poly=[]
                        for pol in V_cell_:
                            poly.append(pol)
                        poly.append(cell_)
                        V_cell_ = MultiPolygon(poly)
                break
    return V_cell_


def adapt_positions_weights(S, V_cell, W):
    '''
    Use to shift Voronoi sites and adapt weights W
    Parameters
    ----------
    S: nd-array
        Array of sites
    V_cell: shapley polygon object
        Set of polygons forming all Voronoi cells
    W: nd-array
        Weights for sites.

    Returns
    -------
        S_new: updated Voronoi points
        W_new: updated weights
    '''

    S_ = []
    dist_border = []
    for s in S:
        # identify Voronoi cell associated with s
        for cell_ in V_cell:
            if (Point(s).within(cell_)):
                cell =  cell_
        # Move s to centroid of cell
        for pp in cell.centroid.coords:
            S_.append(pp)
            dist_border.append(abs(cell.exterior.distance(Point(pp))))
    # S_new = numpy.array(S_)
    S_new = numpy.array(list(map(list, S_)))
    W_new = [numpy.min([numpy.sqrt(W[i]),dist_border[i]])**2 for i in numpy.arange(len(W))]

    return S_new, W_new

def adapt_weights(V_cell, S, bound, W, w_desired, err=0.001):
    '''
    Use to adapt weights W
    input:
    V_cell - Set of polygons forming all Voronoi cells
    S - Voronoi points
    W - positive real weights associated with Voronoi points
    w_desired - desired weighting of each cell
    err - error threshold for values in W; need to understand better.

    output:
    W_new: updates weights
    '''
    W_new = []

    for i, s in enumerate(S):
        s_other = [tuple(s_) for s_ in S if tuple(s_) != tuple(s)]
        NN = nearest_points(Point(s),MultiPoint(s_other))

        for cell_ in V_cell:
            if (Point(s).within(cell_)):
                cell = cell_

        A_current = cell.area
        A_desired = bound.area * w_desired[i]

        f_adapt = A_desired / A_current

        w_new_ = numpy.sqrt(W[i]) * f_adapt

        w_max = abs(LineString(NN).length)

        W_ = numpy.min([w_new_, w_max])**2

        W_new.append(numpy.max([W_, err]))
    return W_new


def optimize_voronoi(weights, imax=100, err=0.001):
    # Random initialization of positions and weights
    N = len(weights)
    S = 5 * disc_uniform_pick(N)
    W = 0.8 * numpy.random.random(N) + 0.2

    # Define the bounding boox
    b_s = 10
    border = box(-b_s, -b_s, b_s, b_s)

    # Compute the initial power diagram. 
    V_s = compute_power_voronoi_map(S, W, border, 1E-9)

    # Instantiate the iterator and error calculation.
    err_calc = numpy.inf
    for _ in range(imax):
        # Update the weights
        print('Updating positions weights')
        S, W = adapt_positions_weights(S, V_s, W)

        # Recompute the power diagram
        print('computing the power diagram')
        V_s = compute_power_voronoi_map(S, W, border, 1E-9)

        # Adapt the weights
        print('Adapting the weights')
        W = adapt_weights(V_s, S, border, W, weights, err)

        # Recompute the power diagram with updated weights. 
        print('Recomputing the power diagram')
        V_s = compute_power_voronoi_map(S, W, border, 1E-9)

        # Perform the error calculation
        print('Evaluating error function')
        area_difference = 0
        for i, s in enumerate(S):
            # identify Voronoi cell associated with s
            for cell_ in V_s:
                if (Point(s).within(cell_)):
                    cell =  cell_

            area_difference += abs(cell.area - border.area * weights[i])

        # update the error calculation and the iteration number
        err_calc = area_difference / (2 * border.area)**-1
        if err_calc <= err:
           return V_s
           

    # Return the voronoi cells
    print(f'Maximum number of iterations exceeded. Error calculation is {err_calc}, greater than threshold of {err}')
    return V_s 

# --- Plot all the things -----------------------------------------------------

def display(S, R, tri_list, voronoi_cell_map):
	# Setup
	fig, ax = plot.subplots()
	plot.axis('equal')
	plot.axis('off')	

	# Set min/max display size, as Matplotlib does it wrong
	min_corner = numpy.amin(S, axis = 0) - numpy.max(R)
	max_corner = numpy.amax(S, axis = 0) + numpy.max(R)
	plot.xlim((min_corner[0], max_corner[0]))
	plot.ylim((min_corner[1], max_corner[1]))

	# Plot the samples
	for Si, Ri in zip(S, R):
		ax.add_artist(plot.Circle(Si, Ri, fill = True, alpha = .4, lw = 0., color = '#8080f0', zorder = 1))

	# Plot the power triangulation
	edge_set = frozenset(tuple(sorted(edge)) for tri in tri_list for edge in itertools.combinations(tri, 2))
	line_list = LineCollection([(S[i], S[j]) for i, j in edge_set], lw = 1., colors = '.9')
	line_list.set_zorder(0)
	ax.add_collection(line_list)

	# Plot the Voronoi cells
	edge_map = { }
	for segment_list in voronoi_cell_map.values():
		for edge, (A, U, tmin, tmax) in segment_list:
			edge = tuple(sorted(edge))
			if edge not in edge_map:
				if tmax is None:
					tmax = 10
				if tmin is None:
					tmin = -10

				edge_map[edge] = (A + tmin * U, A + tmax * U)

	line_list = LineCollection(edge_map.values(), lw = 1., colors = 'k')
	line_list.set_zorder(0)
	ax.add_collection(line_list)

	# Job done
	plot.show()

  