# Thanh, Binh, and Lam (2020) - Combination Crossover Operators for TSP

- Paper file: `papers/thanh-2020-combination-crossover-ga-tsp.pdf`
- Source: https://arxiv.org/abs/2001.11590
- Candidate BibTeX key: `thanh2020combinationcrossover`
- Report theme: Combined crossover mechanisms on TSPLIB
- Priority for TC6544: Medium

## Scoped Summary

This paper proposes two crossover operators, RX and MSCX Radius, and combines
them with MSCX in a GA for symmetric Euclidean TSP instances. The experiments
use 12 TSPLIB instances ranging from 51 to 575 vertices, including kroA100 and
lin105, which makes the paper especially close to our project scale.

The authors report that the combined crossover GA improves mean and minimum
cost over a GA using MSCX alone on their benchmark set. Their results reinforce
a project-relevant point: crossover design affects both quality and convergence,
and hybridizing operators can adapt to different population states.

## What To Use In Our Project

Use this paper to support the crossover subsection and the decision to treat
kroA100 as an appropriate benchmark. It is also useful because it includes
experiments on kroA100, matching our chosen instance.

For our report, the paper can motivate the phrase "feasibility-preserving
operator" carefully. Operators such as MSCX-style constructive crossovers build
valid tours, while our repair mechanism handles the case where offspring become
invalid.

## Relationship To Existing Notebooks

- `notebooks/08_crossover.ipynb`: Supports the importance of crossover
  mechanisms.
- `notebooks/16_parameter_sweep.ipynb`: Supports evaluating parameters such as
  crossover rate and mutation rate.
- `notebooks/17_comparative_experiment.ipynb`: Provides context for comparing
  strategy-level variants.

## Limits

The proposed operators are not implemented in our project. Do not describe them
as part of our GA. Use them as evidence that crossover design is a major
performance factor and that TSPLIB instances around 100 cities are common in
GA-TSP studies.

## Suggested Report Placement

Cite in `LiteratureReview.tex` under GA-TSP crossover studies. It can also
support `Task1.tex` or `Task3.tex` by showing that kroA100-sized TSPLIB
instances are used in empirical GA-TSP work.

