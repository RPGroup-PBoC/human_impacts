
import itertools
import numpy
from scipy.spatial import ConvexHull

from matplotlib.collections import LineCollection
from matplotlib import pyplot as plot
import shapely.geometry

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
	S_norm = numpy.sum(S ** 2, axis = 1) - R 
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

'''
Compute the segments and half-lines that delimits each Voronoi cell
  * The segments are oriented so that they are in CCW order
  * Each cell is a list of (i, j), (A, U, tmin, tmax) where
     * i, j are the indices of two ends of the segment. Segments end points are
       the circumcenters. If i or j is set to None, then it's an infinite end
     * A is the origin of the segment
     * U is the direction of the segment, as a unit vector
     * tmin is the parameter for the left end of the segment. Can be -1, for minus infinity
     * tmax is the parameter for the right end of the segment. Can be -1, for infinity
     * Therefore, the endpoints are [A + tmin * U, A + tmax * U]
'''
def get_voronoi_cells(S, V, tri_list):
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
				voronoi_cell_map[u].append(((edge_map[edge][0], -1), (D,  W, 0, None)))				
				voronoi_cell_map[v].append(((-1, edge_map[edge][0]), (D, -W, None, 0)))				

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

		# Job done
		return segment_list

	# Job done
	return { i : order_segment_list(segment_list) for i, segment_list in voronoi_cell_map.items() }


def voronoi_to_polygons(vor, border, target_areas):
    # Plot the Voronoi cells
    edge_map = { }
    for segment_list in vor.values():
        for edge, (A, U, tmin, tmax) in segment_list:
            edge = tuple(sorted(edge))
            if edge not in edge_map:
                if tmax is None:
                    tmax = 20
                if tmin is None:
                    tmin = -20
                edge_map[edge] = (A + tmin * U, A + tmax * U)
    lines = [shapely.geometry.LineString(l) for l in edge_map.values()]
    polygons = border.difference(lines)

    # For each polygon in the object, compute props. 
    cx, cy = [], []
    areas = []
    f_adapt = []
    distance = []
    for i, p in enumerate(polygons):
        cx.append(p.centroid.x)
        cy.append(p.centroid.y)
        areas.append(p.area)
        f_adapt.append(target_areas[i] / (p.area / border.area))
        distance.append(p.exterior.distance(p.centroid))
    return dict(centroids=numpy.stack([cx, cy], axis=1), areas=numpy.array(areas), 
                f_adapt=numpy.array(f_adapt), polygon=polygons, distance=numpy.array(distance))


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
					tmax = 20
				if tmin is None:
					tmin = -20

				edge_map[edge] = (A + tmin * U, A + tmax * U)

	line_list = LineCollection(edge_map.values(), lw = 1., colors = 'k')
	line_list.set_zorder(0)
	ax.add_collection(line_list)

	# Job done
	plot.show()

  
def compute_power_diagram(S, W, target, border):
    tri_list, V = get_power_triangulation(S, W)
    vor = get_voronoi_cells(S, V, tri_list)
    props = voronoi_to_polygons(vor, border, target)
    return [V, props, [vor, tri_list]]

def adapt_position_weights(W, props):
    new_weights = []
    for i, w in enumerate(W):
        min_val = numpy.min([numpy.sqrt(w), props['distance'][i]])
        new_weights.append(min_val**2)
    return [props['centroids'], numpy.asarray(new_weights)]

def adapt_weights(props, weights, err):
    sites = props['centroids']
    new_weights = []
    for i, s in enumerate(sites):
        other_sites = [tuple(s) for s_ in sites if tuple(s_) != tuple(s)]

        # Compute the nearest neighbor
        distance = [] 
        for _s in other_sites:
            distance.append(numpy.sqrt((s[0] - _s[0])**2 + (s[1] - _s[1])**2)**2 - weights[i])
        NN_dist = numpy.min(numpy.array(distance))
        w_new = numpy.sqrt(weights[i]) * props['f_adapt'][i]
        w_max = numpy.abs(NN_dist)
        w_update = numpy.min([w_new, w_max])**2
        w_update = numpy.max([w_update, err])
        new_weights.append(w_update)
    return numpy.asarray(new_weights)