"""Parameter sensitivity grid sweep (TICKET-16).

Sweep population size, crossover rate, mutation rate, selection method.
30 independent runs per cell (drop to 20 if compute budget bites).
"""


def run_sweep(grid, n_runs, out_csv):
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Wire up CLI args before running.")
