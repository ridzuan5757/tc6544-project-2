"""TSPLIB loader and Euclidean distance-matrix builder (TICKET-04)."""

import numpy as np
import tsplib95


def load_tsp(path):
    """Parse a TSPLIB file and return (coords, dist_matrix).

    coords: ndarray of shape (n, 2) — city coordinates in node order.
    dist_matrix: ndarray of shape (n, n) — full Euclidean distance matrix (float64).
    """
    problem = tsplib95.load(str(path))
    nodes = list(problem.get_nodes())
    n = len(nodes)

    coords = np.array([problem.node_coords[node] for node in nodes], dtype=np.float64)

    diff = coords[:, np.newaxis, :] - coords[np.newaxis, :, :]
    dist_matrix = np.sqrt((diff**2).sum(axis=-1))

    return coords, dist_matrix
