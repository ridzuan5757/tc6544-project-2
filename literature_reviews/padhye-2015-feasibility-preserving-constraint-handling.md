# Padhye, Mittal, and Deb (2015) - Feasibility-Preserving Constraint Handling

- Paper file: `papers/padhye-2015-feasibility-preserving-constraint-handling.pdf`
- Source: https://arxiv.org/abs/1504.04421
- Candidate BibTeX key: `padhye2015feasibilitypreserving`
- Report theme: Feasibility-preserving repair and constraint handling
- Priority for TC6544: High

## Scoped Summary

This paper studies feasibility-preserving constraint-handling strategies for
evolutionary optimization. Although the experiments are on real-parameter
problems rather than TSP permutations, the conceptual link to our project is
strong: evolutionary operators can create infeasible offspring, so the algorithm
needs a strategy to bring solutions back into the feasible region or avoid
leaving it.

The authors compare penalty functions, feasibility-preserving operators, and
repair strategies. They also warn that repair mechanisms can introduce search
bias and may hinder exploration if they always push solutions into the same part
of the feasible region. This is directly relevant to our repair mechanism,
because replacing duplicate cities with missing cities is not neutral. The
choice of insertion strategy can affect diversity and convergence.

## What To Use In Our Project

Use this paper as one of the central references for the repair discussion. It
supports the following claims:

- Constraint handling is part of the algorithm design, not an afterthought.
- Penalty methods require balancing objective quality and constraint violation.
- Feasibility-preserving operators are attractive but not always available.
- Repair can be effective, but it can also bias search and reduce diversity.

This maps directly onto our project's comparison between repair, penalty or
alternative handling, and feasibility-preserving operators.

## Relationship To Existing Notebooks

- `notebooks/12_repair_mechanism.ipynb`: Directly relevant to repair design and
  insertion strategy.
- `notebooks/13_alternative_constraint.ipynb`: Supports the comparison against
  penalty or alternative handling.
- `notebooks/14_diversity_metrics.ipynb`: Supports measuring whether repair
  affects population diversity.
- `notebooks/17_comparative_experiment.ipynb`: Supports the interpretation of
  repair versus no-repair outcomes.

## Limits

The paper's repair methods are for real-parameter boundary and constraint
handling, not duplicate-removal in permutations. Use it for general principles
and caveats, then pair it with permutation-specific sources such as Cicirello
and the classic repair survey listed in `papers/README.md`.

## Suggested Report Placement

Cite in `LiteratureReview.tex` under "Constraint Handling in Evolutionary
Algorithms" and "Repair Mechanisms in Permutation-based EAs". Also cite in
`Task3.tex` when critically analyzing repair bias and diversity effects.

