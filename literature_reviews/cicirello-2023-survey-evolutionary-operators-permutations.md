# Cicirello (2023) - Survey and Analysis of Evolutionary Operators for Permutations

- Paper file: `papers/cicirello-2023-survey-evolutionary-operators-permutations.pdf`
- Source: https://arxiv.org/abs/2311.14595
- Candidate BibTeX key: `cicirello2023permutationoperators`
- Report theme: Permutation operators for evolutionary algorithms
- Priority for TC6544: High

## Scoped Summary

This survey reviews evolutionary operators for permutation representations.
The paper is highly relevant because our TSP chromosomes are permutations, and
the main feasibility constraint is that every city appears exactly once. Cicirello
separates operator behavior by the kind of structure inherited by offspring:
absolute positions, undirected edges, directed edges, precedences, and cyclic
precedences.

That taxonomy is useful for our report because it explains why different TSP
operators preserve different kinds of useful information. PMX is more
position-oriented, OX preserves relative order, and edge-based operators are more
directly aligned with TSP tour cost because the objective is a sum of edge
distances.

## What To Use In Our Project

Use this paper to sharpen the literature review beyond "many crossover operators
exist". The project can say that permutation operators differ by what they
preserve:

- Position information helps maintain city locations within a chromosome.
- Order information helps preserve subsequences.
- Edge information is especially relevant to TSP because tour length is computed
from adjacent city pairs.

This taxonomy supports the project's choice to track Hamming diversity, which
measures positional difference across the population. The paper also points to
edge-based diversity as a more TSP-specific alternative, which is a natural
direction for future work but is out of scope for this project.

## Relationship To Existing Notebooks

- `notebooks/08_crossover.ipynb`: Supports the PMX/OX/CX operator discussion.
- `notebooks/09_mutation.ipynb`: Supports permutation-specific mutation.
- `notebooks/14_diversity_metrics.ipynb`: Supports the use of Hamming diversity
  as a population-level metric; the paper's discussion of edge-based diversity
  is noted but not implemented in this project.
- `notebooks/18_convergence_plots.ipynb`: Useful for interpreting diversity
  trends.

## Limits

The paper is a broad permutation-operator survey and uses artificial landscapes
for part of its analysis. It is not a direct empirical study of our kroA100 GA or
our repair mechanism. Its value is conceptual and taxonomic.

## Suggested Report Placement

Cite prominently in `LiteratureReview.tex` under "Genetic Algorithms for the
TSP" and "Repair Mechanisms in Permutation-based EAs". Also cite in `Task2.tex`
when motivating the choice between permutation-aware operators (PMX/OX/CX) and
the naive crossover used as the primary operator with repair.

