# Uray, Wintersteller, and Huber (2023) - CSRX Crossover for TSP

- Paper file: `papers/uray-2023-csrx-crossover-tsp.pdf`
- Source: https://arxiv.org/abs/2303.12447
- Candidate BibTeX key: `uray2023csrx`
- Report theme: Symmetry-aware crossover
- Priority for TC6544: Medium

## Scoped Summary

This paper introduces CSRX, a family of crossover operators for GAs applied to
the TSP. The key idea is that TSP tours have symmetries: rotating a tour or
reversing its direction does not change its fitness in the symmetric TSP. The
authors argue that common crossover operators do not fully respect these
symmetries, which can cause fit parents to produce poor offspring.

For our project, this paper is useful because it deepens the explanation of why
TSP crossover is subtle. It is not enough for an offspring to be a valid
permutation. A good crossover should also preserve meaningful tour structure
despite equivalent rotations and reversals.

## What To Use In Our Project

Use this paper to support a nuanced statement in the literature review:
feasibility is necessary but not sufficient. Repair can convert an infeasible
chromosome into a valid tour, but repair does not guarantee that high-quality
edge or order structure is preserved. This helps frame the critical analysis of
repair in TICKET-21 and Task 3.3.

The paper's discussion of symmetric TSP quality being tied to adjacent-city
relationships motivates edge-based diversity as a stronger TSP-specific metric.
This project tracks Hamming diversity only; edge-based diversity is a natural
extension for future work but is out of scope here.

## Relationship To Existing Notebooks

- `notebooks/08_crossover.ipynb`: Supports why TSP crossover operators require
  special handling.
- `notebooks/12_repair_mechanism.ipynb`: Helps critique repair as feasibility
  restoration rather than quality preservation.
- `notebooks/14_diversity_metrics.ipynb`: The project tracks Hamming
  diversity; the paper's edge-structure framing motivates edge-based
  diversity as a useful extension for future work.

## Limits

The paper proposes an operator that is not implemented here, and it is a modern
preprint/conference contribution rather than a classic source. Use it as a
recent supporting reference, not as the foundation of the review.

## Suggested Report Placement

Cite in `LiteratureReview.tex` under crossover/operator studies. It is also
useful in `Task3.tex` for explaining why repair may affect structure even after
restoring feasibility.
