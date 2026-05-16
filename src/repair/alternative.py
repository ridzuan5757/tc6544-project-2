"""Alternative constraint handling for comparative analysis (TICKET-13).

Provides one or both of:
- penalty(): penalty-function constraint handling
- feasibility_preserving_crossover(): operator that never produces infeasibles
"""


def penalty(chromosome, dist_matrix, weight):
    raise NotImplementedError


def feasibility_preserving_crossover(parent_a, parent_b, rng):
    raise NotImplementedError
