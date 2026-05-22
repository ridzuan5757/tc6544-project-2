# TC6544-Project-2

**Metaheuristic Optimization of the Traveling Salesman Problem Using Genetic Algorithm with Feasibility Repair Mechanisms**

Course: TC6544 (Prof. Salwani Abdullah)
Type: Group project
Due date: **2026-06-23**

## Project goal

Investigate, implement, and critically analyse a Genetic Algorithm (GA) for solving a static single-objective Traveling Salesman Problem (TSP), with a key focus on **repair mechanisms** that transform infeasible chromosomes into feasible tours.

Full specification: see `TC6544-Project-Sem2Session2526-1.pdf`.

## Benchmark instance

| Property | Details |
|---|---|
| Name | kroA100 |
| Dimension | 100 cities |
| Edge-weight type | EUC_2D |
| Known optimal tour length | 21,282 |
| Source | Krolak, Felts & Nelson — via TSPLIB95 (Reinelt, 1991) |

Data files: `data/TSP-dataset/kroA100.tsp`, `data/TSP-datasets-opt-tour/kroA100.opt.tour`

## Scope highlights

- Benchmark TSP instance: **kroA100** (100 cities)
- Formal mathematical formulation
- GA: permutation encoding, selection (tournament/roulette), crossover (PMX/OX/CX), mutation (swap/inversion)
- Repair mechanism (duplicate removal + missing city insertion) — **graded focus**
- Comparative analysis against an alternative constraint-handling strategy (penalty function or feasibility-preserving operator)
- Parameter sensitivity sweep, 30 independent runs per configuration
- Convergence plots, boxplots, statistical tests
- Research-style report

## Timeline

Today: **2026-05-13** · Due: **2026-06-23** · Window: **~6 weeks**

Treated as **5 weeks of work + 1 week buffer**. The buffer absorbs inevitable bugs, compute reruns, and writing iterations.

| Week | Dates | Focus | Tickets |
|---|---|---|---|
| **W1** | May 13 – May 19 | Setup + foundations | 01, 02, 03, 04, 05; 22 starts |
| **W2** | May 20 – May 26 | Core GA operators | 06, 07, 08, 09, 10, 11 |
| **W3** | May 27 – Jun 2 | Repair + alternatives | 12, 13, 14, 15 |
| **W4** | Jun 3 – Jun 9 | Experiments (compute-heavy) | 16, 17 |
| **W5** | Jun 10 – Jun 16 | Analysis + writeup | 18, 19, 20, 21, 24, 25 |
| **W6** | Jun 17 – Jun 23 | Report finalization + buffer | 23, 26, 27 |

### Known risk points

1. **Crossover operators (TICKET-08)** — PMX/OX/CX are subtle; allocate full week.
2. **Parameter sweep (TICKET-16)** — ~45 hours of compute for a full 3×3×3×2 grid × 30 runs. Use multiprocessing; split runs across group members; reduce to 20 runs if needed.
3. **Literature review (TICKET-22)** — start day 1, run in parallel with all other work.
4. **Report writing** — start drafting sections as soon as the relevant work finishes, not in W5.

### Scope cuts if behind schedule

In order:
1. TICKET-20 (best-tour viz) — marked optional in spec
2. Reduce TICKET-08 to 2 crossovers (PMX + OX)
3. Reduce TICKET-16 sweep to 2 levels per parameter
4. TICKET-13 — implement only one alternative (penalty function is fastest)

### Non-negotiables

- Repair mechanism design + analysis (TICKET-12, 21) — the graded focus
- At least one comparative constraint-handling strategy (TICKET-13, 17)
- Minimum 30 independent runs for any statistical claim

## Role distribution (3-person group)

| Role | Tickets |
|---|---|
| Code Lead | 03, 04, 05, 06, 07, 09, 10, 14, 15 |
| Algorithm Coder | 08, 12, 13 |
| Theory / Writing Lead | 01, 02, 11, 21, 22, 23, 24, 25, 26 |
| Analyst (shared) | 16, 17, 18, 19, 20 |
| All | 27 |

## Critical path

`01 → 04 → 05 → 08 → 12 → 15 → 16 → 17 → 21 → 25 → 27`

## Tickets

All 27 tickets are tracked as GitHub issues in this repository.

## Deliverables

- Notebooks (GA implementation, repair mechanism, experiments)
- Experiment results (CSVs in `results/`)
- Figures (convergence curves, boxplots, tour visualizations)
- Research report (PDF)

## Development setup

```bash
pip install -r requirements.txt
```

### Project layout

```
notebooks/    One notebook per ticket (e.g. 04_instance_loader.ipynb → TICKET-04)
data/         TSPLIB benchmark instances
results/      Experiment outputs (CSV, figures)
report/       LaTeX report
```


## Dataset
The benchmark instance used in this task is **kroA100**, obtained from: [TSPLIB95](
https://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp.html).

| Property | Details |
|---|---|
| Name | kroA100 |
| City Count | 100 |
| Known Optimal Tour Length | 21,282 |
| Source | TSPLIB95 — Reinelt, G. (1991) |
| Coordinate Format | EUC_2D |