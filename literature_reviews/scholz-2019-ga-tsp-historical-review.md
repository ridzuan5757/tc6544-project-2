# Scholz (2019) - GA and TSP Historical Review

- Paper file: `papers/scholz-2019-ga-tsp-historical-review.pdf`
- Source: https://arxiv.org/abs/1901.05737
- Candidate BibTeX key: `scholz2019historicalreview`
- Report theme: Historical GA-TSP background
- Priority for TC6544: Medium

## Scoped Summary

This paper gives a historical overview of Genetic Algorithms applied to the TSP.
It identifies phases in the development of GA-TSP research and summarizes major
operator and representation milestones. For our project, the most useful value
is framing: TSP has long been used as a benchmark for testing GA representation,
crossover, mutation, and local-search design.

The paper also notes recurring GA-TSP lessons: edge-preserving crossover can be
strong, local search is often crucial for top performance, sub-populations can
help avoid premature convergence, and larger populations can improve solution
quality. These ideas connect to our diversity and convergence analysis.

## What To Use In Our Project

Use this paper to introduce why TSP is a standard GA benchmark and why operator
design became such a large literature. It can also support the idea that a simple
GA is often not enough for state-of-the-art TSP performance, which helps keep
our report claims realistic.

For TICKET-22, this paper is a good bridging citation between foundational GA
sources and newer operator studies.

## Relationship To Existing Notebooks

- `notebooks/01_problem_and_setup.ipynb`: Supports choosing TSP as a benchmark.
- `notebooks/08_crossover.ipynb`: Provides background for why crossover
  operators are a major GA-TSP topic.
- `notebooks/14_diversity_metrics.ipynb`: Supports discussing premature
  convergence and genetic depletion.
- `notebooks/22_literature_review.ipynb`: Useful as a high-level survey source.

## Limits

This is a historical review and appears to be a seminar-style paper rather than
a core journal survey. It should not replace Larranaga et al. (1999) or other
canonical sources. Use it for accessible framing, not as the main authority.

## Suggested Report Placement

Cite early in `LiteratureReview.tex` under "Genetic Algorithms for the TSP" to
frame the history of GA-TSP research.

