# Abdoun, Abouchabaka, and Tajani (2012) - Mutation Operators for TSP

- Paper file: `papers/abdoun-2012-mutation-operators-tsp.pdf`
- Source: https://arxiv.org/abs/1203.3099
- Candidate BibTeX key: `abdoun2012mutationoperators`
- Report theme: GA-TSP mutation operators
- Priority for TC6544: Medium

## Scoped Summary

This paper compares mutation operators for a GA applied to the TSP and frames
mutation as one of the major parameter choices affecting GA performance. The
authors emphasize that a GA variant is defined by representation, initial
population, selection, crossover, mutation, crossover probability, mutation
probability, and insertion strategy. That framing matches our project structure,
where each operator and parameter is isolated in its own notebook.

The paper is most useful for justifying the inclusion of multiple mutation
operators, especially swap and inversion-style mutation. For a permutation
problem such as TSP, mutation must change the order of cities without breaking
the permutation constraint. This is exactly why our mutation notebook checks
validity after random trials.

## What To Use In Our Project

Use this paper to support these report points:

- Mutation is not just a secondary operator; it affects diversity and helps the
  GA escape local optima.
- TSP mutation should preserve permutation feasibility.
- Mutation probability should be treated as an experimental parameter, not a
  fixed universal constant.

The paper does not directly study repair, but it reinforces a key repair-related
point: some operators can preserve feasibility by construction, while others
need additional constraint handling.

## Relationship To Existing Notebooks

- `notebooks/09_mutation.ipynb`: Directly supports swap and inversion mutation
  as permutation-safe operations.
- `notebooks/16_parameter_sweep.ipynb`: Supports mutation-rate sensitivity as a
  reportable experiment.
- `notebooks/14_diversity_metrics.ipynb`: Indirectly relevant because mutation
  is one driver of population diversity.

## Limits

The paper is operator-focused rather than repair-focused. It should not be used
as central evidence for repair effectiveness. Its best role is methodological:
it supports why mutation choice and mutation rate are part of the GA design.

## Suggested Report Placement

Cite in `Task2.tex` under `T2:Mutation`, and mention briefly in
`LiteratureReview.tex` when discussing GA operator choices for permutation-coded
TSP.

