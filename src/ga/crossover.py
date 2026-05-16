"""Crossover operators: PMX, OX, CX (TICKET-08).

These operators can produce infeasible offspring (duplicates / missing cities).
Repair happens downstream in src/repair/repair.py.
"""


def pmx(parent_a, parent_b, rng):
    raise NotImplementedError


def ox(parent_a, parent_b, rng):
    raise NotImplementedError


def cx(parent_a, parent_b, rng):
    raise NotImplementedError
