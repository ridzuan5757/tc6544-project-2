# Report

LaTeX source for the TC6544 Project 2 research report.

Adapted from the Steve Gunn / Sunil Patel thesis template (originally used by Ridzuan for his undergraduate honours thesis at USYD).

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
│   ├── TitlePage.tex       Title page (UKM, TC6544, authors, supervisor)
│   └── AbstractPage.tex    Abstract (TICKET-23)
├── Chapters/
│   ├── Chapter1.tex        Introduction (TICKET-23)
│   ├── Chapter2.tex        Literature Review (TICKET-22)
│   ├── Chapter3.tex        Methodology (TICKET-24)
│   ├── Chapter4.tex        Repair Mechanism Analysis (TICKET-11 + TICKET-21)
│   ├── Chapter5.tex        Experimental Setup
│   ├── Chapter6.tex        Results and Discussion (TICKET-25)
│   └── Chapter7.tex        Conclusion and Future Work (TICKET-26)
└── Figures/                Figures included in the report
```

## Conventions

- **One chapter per file.** Reduces merge conflicts when multiple authors edit in parallel.
- **Figures** referenced by the report go in `Figures/`. Experiment outputs live in `../results/figures/`; copy the curated subset into `Figures/` for inclusion.
- **Citations** are added to `Bibliography.bib`. BibTeX keys use the form `lastnameyearkeyword`, e.g., `goldberg1989genetic`. Cite with `\cite{key}`.
- **Cross-references** use the helpers from `Thesis.cls`:
  - `\fref{label}` --- Figure
  - `\tref{label}` --- Table
  - `\eref{label}` --- Equation
  - `\cref{label}` --- Chapter
  - `\sref{label}` --- Section
  - `\aref{label}` --- Appendix
- Each chapter file starts with a header comment naming the ticket and owner.

## Document variables

Author names, supervisor, university details, keywords, etc. live in `DocumentVariables.tex`. Edit them once there and they propagate throughout the document.

## Overleaf workflow (Option B from project planning)

1. Initialize the Overleaf project by uploading this directory (zip) or via Overleaf's one-time GitHub import.
2. Writers edit in Overleaf for live collaboration.
3. The designated sync owner exports the Overleaf project as zip at the end of each week and commits to `report/` here.
4. Figures generated in `../results/figures/` are copied (curated) into `Figures/` and uploaded to Overleaf.

## Template notes

- Based on the LaTeX `book` class via the `Thesis` document class.
- Single-sided (`oneside`), 11pt, A4 paper.
- 1.5 line spacing, default Computer Modern font.
- Numbered IEEE-style references (`natbib`, `ieeetr` style).
- The thesis-only front matter (declaration of authorship, dedication, quotation, acknowledgements, acronyms, nomenclature, appendices) was removed for this report. Re-enable any of them by following the patterns in the original skeleton if needed.
