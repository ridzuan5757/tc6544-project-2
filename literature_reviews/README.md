# Literature Review Notes

These notes scope the downloaded papers in `papers/` to TC6544 Project 2:
Genetic Algorithms for the TSP, feasibility repair, alternative constraint
handling, diversity, convergence, and operator design.

Each review is intentionally project-focused. General background, unrelated
benchmark domains, and implementation details that do not affect the report are
kept brief.

## Review Index

| Review | Paper | Theme | Priority |
|---|---|---|---|
| `abdoun-2012-adaptive-crossover-operators-tsp.md` | Abdoun and Abouchabaka (2012) | Crossover comparison for TSP | High |
| `abdoun-2012-mutation-operators-tsp.md` | Abdoun, Abouchabaka, and Tajani (2012) | Mutation comparison for TSP | Medium |
| `chehouri-2016-constraint-handling-violation-factor-ga.md` | Chehouri et al. (2016) | Constraint handling without penalty tuning | Medium |
| `cicirello-2023-survey-evolutionary-operators-permutations.md` | Cicirello (2023) | Permutation operators and inherited features | High |
| `eremeev-2017-optimal-recombination-atsp.md` | Eremeev and Kovalenko (2017) | Optimal recombination and diversity | Medium |
| `liu-2014-powerful-genetic-algorithm-tsp.md` | Liu (2014) | Edge-based GA and local search | Medium |
| `padhye-2015-feasibility-preserving-constraint-handling.md` | Padhye, Mittal, and Deb (2015) | Feasibility-preserving repair strategies | High |
| `scholz-2019-ga-tsp-historical-review.md` | Scholz (2019) | Historical GA-TSP framing | Medium |
| `thanh-2020-combination-crossover-ga-tsp.md` | Thanh, Binh, and Lam (2020) | Combined crossover mechanisms on TSPLIB | Medium |
| `uray-2023-csrx-crossover-tsp.md` | Uray, Wintersteller, and Huber (2023) | Symmetry-aware crossover | Medium |

## Suggested Report Use

Use the high-priority notes in `report/Chapters/LiteratureReview.tex`:

- `Lit:GAforTSP`: Scholz (2019), Liu (2014), Abdoun and Abouchabaka (2012), Thanh et al. (2020), Uray et al. (2023).
- `Lit:ConstraintHandling`: Chehouri et al. (2016), Padhye et al. (2015).
- `Lit:Repair`: Padhye et al. (2015), Cicirello (2023), plus the classic repair/constraint papers listed in `papers/README.md`.
- Crossover-operator discussion in `T2:Crossover`: Abdoun and Abouchabaka (2012), Cicirello (2023), Thanh et al. (2020), Uray et al. (2023), Eremeev and Kovalenko (2017).
- Mutation discussion in `T2:Mutation`: Abdoun, Abouchabaka, and Tajani (2012), Liu (2014), Eremeev and Kovalenko (2017).

## Scope Notes

The downloaded set is useful, but it does not replace the classic sources already
identified in TICKET-22. The final report should still cite the canonical
Larranaga et al. GA-TSP survey, Coello Coello's constraint-handling survey,
Michalewicz and Schoenauer's constrained-EA paper, and Salcedo-Sanz's repair
survey if library access is available.

