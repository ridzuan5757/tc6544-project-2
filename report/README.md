# Report

LaTeX source for the TC6544 Project 2 assignment report.

Adapted from the Steve Gunn / Sunil Patel thesis template; shares the same template assets as `tc6544/project_1/report/`.

## Build

From this directory:

```bash
latexmk -pdf main.tex
```

To clean build artifacts:

```bash
latexmk -C
```

Produces `main.pdf`.

## Layout

```
report/
├── main.tex                Master document
├── DocumentVariables.tex   Title, authors, supervisor, university, etc.
├── Thesis.cls              Custom document class (book-based, thesis style)
├── vector.sty              Vector typesetting helpers
├── lstpatch.sty            Patch for the listings package
├── Bibliography.bib        BibTeX bibliography
├── latexmkrc               Build configuration
├── FrontMatter/
│   ├── TitlePage.tex       Title page (UKM, TC6544, authors, lecturer)
│   └── AbstractPage.tex    Abstract (~250 words, currently disabled in main.tex)
├── Chapters/
│   ├── Introduction.tex        Mandated by Task 4.2
│   ├── LiteratureReview.tex    Mandated by Task 4.2
│   ├── Task1.tex               Problem Definition and Experimental Design (1.1, 1.2, 1.3)
│   ├── Task2.tex               Algorithm Development (2.1, 2.2)
│   ├── Task3.tex               Evaluation Methodology and Analysis (3.1, 3.2, 3.3)
│   ├── Task4.tex               Visualisation and Results (4.1)
│   └── Conclusion.tex          Conclusion and Future Research Directions
└── Figures/                Figures included in the report
```

## Assignment-Task Mapping

The report sections map directly to the project brief in `../TC6544-Project-Sem2Session2526-1.pdf`:

| Brief task | Source file / subsection |
|---|---|
| 1.1 Benchmark TSP instance | `Task1.tex` --- `T1:Benchmark` |
| 1.2 Mathematical formulation | `Task1.tex` --- `T1:Formulation` |
| 1.3 Experimental-setup justification | `Task1.tex` --- `T1:Setup` |
| 2.1 GA design | `Task2.tex` --- `T2:GADesign` |
| 2.2 Constraint handling via repair | `Task2.tex` --- `T2:Repair` |
| 3.1 Parameter sensitivity | `Task3.tex` --- `T3:Sensitivity` |
| 3.2 Performance evaluation | `Task3.tex` --- `T3:Performance` |
| 3.3 Critical analysis of repair | `Task3.tex` --- `T3:RepairCritique` |
| 4.1 Visualisation | `Task4.tex` --- `T4:Convergence`, `T4:Boxplots`, `T4:BestTour` |
| 4.2 Research report (meta) | Structure of this whole document |

Task 4.2 also mandates an abstract, an introduction, a literature review, and a future-work section --- handled by `Introduction.tex`, `LiteratureReview.tex`, and `Conclusion.tex`.

## Conventions

- **One top-level section per file.** Reduces merge conflicts when multiple authors edit in parallel.
- **Figures** referenced by the report go in `Figures/`.
- **Citations** are added to `Bibliography.bib`. BibTeX keys use the form `lastnameyearkeyword`, e.g., `goldberg1989genetic`. Cite with `\cite{key}`.
- **Cross-references** use the helpers from `Thesis.cls`:
  - `\fref{label}` --- Figure
  - `\tref{label}` --- Table
  - `\eref{label}` --- Equation
  - `\sref{label}` --- Section / subsection (e.g.\ `\sref{T3:RepairCritique}`)
  - `\aref{label}` --- Appendix
- Labels follow `TX:Topic` for the Task files (e.g.\ `T2:Repair`) and `Section:Topic` for the framing files.

## Template notes

- Based on the LaTeX `book` class via the `Thesis` document class, but the report uses `\section`/`\subsection`/`\subsubsection` (no `\chapter`) so it flows as an assignment rather than a thesis.
- Single-sided (`oneside`), 11pt, A4 paper, symmetric 1in margins.
- 1.5 line spacing, default Computer Modern font.
- Numbered IEEE-style references (`natbib`, `ieeetr` style).
