# Eremeev and Kovalenko (2017) - Optimal Recombination for ATSP

- Paper file: `papers/eremeev-2017-optimal-recombination-atsp.pdf`
- Source: https://arxiv.org/abs/1706.06920
- Candidate BibTeX key: `eremeev2017optimalrecombination`
- Report theme: Recombination, local search, and diversity
- Priority for TC6544: Medium

## Scoped Summary

This paper proposes a GA for the asymmetric TSP using optimal recombination,
3-opt local search, and mutation based on 3-opt or 4-opt neighborhoods. Although
the problem variant is ATSP rather than our symmetric Euclidean kroA100
instance, the paper is relevant because it shows how much GA performance depends
on representation, crossover design, local search, population management, and
diversity restoration.

The paper is especially useful for its discussion of diversity. The authors note
that decreasing population diversity changes the cost of solving recombination
problems, and that restart behavior can restore diversity and avoid localized
search. This aligns with our project's decision to measure diversity over
generations instead of reporting only best tour length.

## What To Use In Our Project

Use this paper to support these points:

- High-quality GA-TSP variants often combine crossover with local search or
  neighborhood moves.
- Recombination can be designed to preserve meaningful parent structure.
- Diversity loss is a practical issue, not just a theoretical concern.

The paper can also be used as a contrast: our project remains simpler and more
assignment-focused, using PMX/OX/CX, swap/inversion mutation, and repair rather
than optimal recombination.

## Relationship To Existing Notebooks

- `notebooks/08_crossover.ipynb`: Supports the importance of crossover design.
- `notebooks/09_mutation.ipynb`: Supports neighborhood-based mutation as a TSP
  improvement mechanism.
- `notebooks/14_diversity_metrics.ipynb`: Supports diversity monitoring.
- `notebooks/17_comparative_experiment.ipynb`: Provides context for comparing
  strategies beyond raw fitness.

## Limits

This is an ATSP paper and uses a more advanced algorithm than our coursework
implementation. Do not use it to justify exact expectations for kroA100. Use it
as supporting evidence that recombination and diversity management matter.

## Suggested Report Placement

Cite in `LiteratureReview.tex` under GA-TSP operator design, and optionally in
`Task3.tex` when discussing diversity and premature convergence.

