# Chehouri et al. (2016) - Constraint Handling Using a Violation Factor

- Paper file: `papers/chehouri-2016-constraint-handling-violation-factor-ga.pdf`
- Source: https://arxiv.org/abs/1610.00976
- Candidate BibTeX key: `chehouri2016violationfactor`
- Report theme: Constraint handling in genetic algorithms
- Priority for TC6544: Medium

## Scoped Summary

This paper proposes VCH, a violation constraint-handling method for genetic
algorithms. The authors position VCH as an alternative to penalty functions,
arguing that penalty approaches require parameter tuning and can be difficult to
calibrate. Instead of converting the constrained problem into an unconstrained
penalized objective, VCH ranks population members using constraint-violation
information while keeping the objective function separate.

For our project, the paper is relevant because TICKET-13 uses an alternative
constraint-handling strategy and TICKET-17 compares repair against non-repair or
penalty-style handling. Although Chehouri et al. study engineering optimization
rather than TSP permutations, the conceptual point is useful: penalty functions
are not neutral. They introduce tuning choices that affect selection pressure.

## What To Use In Our Project

Use this paper to explain why a penalty baseline needs careful interpretation.
In our TSP setting, a penalty method must balance tour length against duplicate
and missing-city violations. If the penalty is too low, infeasible chromosomes
can dominate. If it is too high, the search may discard useful genetic material
too aggressively.

This supports the report's repair argument: repair avoids penalty-weight tuning
by converting offspring back into feasible permutations before evaluation.

## Relationship To Existing Notebooks

- `notebooks/13_alternative_constraint.ipynb`: Directly relevant to penalty and
  alternative constraint handling.
- `notebooks/17_comparative_experiment.ipynb`: Supports the interpretation of
  repair versus non-repair or penalty comparisons.
- `notebooks/11_infeasibility_analysis.ipynb`: Reinforces the idea that
  infeasible solutions distort selection pressure.

## Limits

The benchmark problems are continuous or engineering-oriented, not permutation
TSP. Do not cite this paper as evidence that VCH works for kroA100. Cite it only
for the broader constraint-handling principle and the penalty-tuning critique.

## Suggested Report Placement

Cite in `LiteratureReview.tex` under "Constraint Handling in Evolutionary
Algorithms". It can also be referenced in `Task3.tex` when discussing why
penalty-based alternatives are sensitive to parameter choice.

