# Liu (2014) - A Powerful Genetic Algorithm for TSP

- Paper file: `papers/liu-2014-powerful-genetic-algorithm-tsp.pdf`
- Source: https://arxiv.org/abs/1402.4699
- Candidate BibTeX key: `liu2014powerfulga`
- Report theme: Edge-based GA, local search, and scalability
- Priority for TC6544: Medium

## Scoped Summary

This paper presents a GA for large TSP benchmark instances using edge swapping
and local search. The author argues that standard GAs for TSP can be slower than
efficient local search because crossover is computationally expensive. The
proposed method localizes edge swapping to reduce cost, then switches to a more
global version when local improvement stalls.

For our project, the paper is valuable because it connects crossover design,
edge preservation, population diversity, and computational cost. It supports the
idea that edge structure is central to TSP search, which in turn supports our
edge-overlap and edge-diversity metrics.

## What To Use In Our Project

Use this paper to support three report claims:

- TSP fitness is edge-based, so preserving or improving edge combinations is a
  natural GA design goal.
- Local search can strongly improve GA performance, although it is outside our
  main repair-mechanism scope.
- Computational overhead matters when logging metrics or running parameter
  sweeps.

This last point is useful for explaining why diversity instrumentation may be
made optional in the GA loop: large experiment grids can become expensive.

## Relationship To Existing Notebooks

- `notebooks/14_diversity_metrics.ipynb`: The paper's emphasis on edge
  structure points toward edge-based diversity as a useful future extension;
  the project currently tracks Hamming diversity only.
- `notebooks/16_parameter_sweep.ipynb`: Supports concern about computational
  cost in repeated runs.
- `notebooks/20_tour_visualization.ipynb`: Edge-based interpretation can help
  discuss final tour quality visually.

## Limits

The paper studies a stronger GA than the assignment implementation and includes
local-search machinery not implemented in our core notebooks. It should not be
used as a baseline we are expected to match. Use it to frame design trade-offs,
not to set performance targets.

## Suggested Report Placement

Cite in `LiteratureReview.tex` under GA-TSP methods and in `Task3.tex` if
discussing computational cost, diversity, or why edge-based metrics are useful.

