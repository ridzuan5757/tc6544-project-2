# Abdoun and Abouchabaka (2012) - Adaptive Crossover Operators for TSP

- Paper file: `papers/abdoun-2012-adaptive-crossover-operators-tsp.pdf`
- Source: https://arxiv.org/abs/1203.3097
- Candidate BibTeX key: `abdoun2012adaptivecrossover`
- Report theme: GA-TSP crossover operators
- Priority for TC6544: High

## Scoped Summary

This paper compares several crossover operators for a GA applied to the TSP. The
tested operators include OX, NWOX, PMX, UPMX, and CX, with experiments on
BERLIN52. The paper is useful for our project because it treats TSP chromosomes
as permutations and focuses on how recombination affects search performance.
That is directly aligned with our notebooks on PMX, OX, CX, naive crossover,
and repair.

The strongest project-relevant result is that crossover design matters. The
authors report that OX performed strongly on the BERLIN52 experiment and that
operators based on creating and filling holes produced high-quality results.
This supports our decision to treat PMX/OX/CX as feasibility-preserving
operators and to compare them against naive crossover, which can create
duplicate and missing cities.

## What To Use In Our Project

Use this paper to support the claim that TSP crossover operators cannot be
treated as interchangeable. For permutation-coded TSP, an operator must preserve
the city set while also transmitting useful parent structure. This fits our
report's contrast between:

- Feasibility-preserving operators such as PMX, OX, and CX.
- Naive string crossover, which may produce infeasible tours.
- Repair mechanisms, which restore feasibility after infeasible offspring are
created.

The paper also helps justify why `notebooks/08_crossover.ipynb` compares
multiple crossover operators instead of selecting only one.

## Relationship To Existing Notebooks

- `notebooks/08_crossover.ipynb`: Directly relevant to the PMX/OX/CX
  explanation and feasibility analysis.
- `notebooks/10_ga_loop.ipynb`: Supports the configurable `crossover_method`
  design.
- `notebooks/17_comparative_experiment.ipynb`: Useful background for explaining
  why naive crossover is a stress test rather than the preferred production
  operator.

## Limits

The experiment uses BERLIN52, which is smaller than our kroA100 instance. Page 1
text extraction failed locally, so the review is based on the extracted body,
conclusion, and the paper metadata. The paper is useful for crossover discussion,
but it is not a repair-mechanism paper.

## Suggested Report Placement

Cite in `LiteratureReview.tex` under "Genetic Algorithms for the TSP" or in a
new crossover-operator subsection. Also cite in `Task2.tex` under
`T2:Crossover` when explaining why OX and other permutation-aware crossovers are
included.

