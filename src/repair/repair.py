"""Feasibility repair: duplicate removal + missing-city insertion (TICKET-12).

This is the graded focus of the project. Three insertion variants are supported:
random, position-based, and nearest-neighbour.
"""


def repair(chromosome, n_cities, dist_matrix=None, strategy="random", rng=None):
    """Return a valid permutation derived from a possibly infeasible chromosome."""
    raise NotImplementedError
