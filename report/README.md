# Report

LaTeX source for the TC6544 Project 2 research report.

## Build

From this directory:

```bash
latexmk -pdf main.tex
```

To clean build artifacts:

```bash
latexmk -C
```

## Layout

```
report/
├── main.tex            Master document (imports section files)
├── references.bib      BibTeX bibliography
├── latexmkrc           Build configuration
├── sections/           One file per report section (edit independently)
│   ├── abstract.tex        TICKET-23
│   ├── introduction.tex    TICKET-23
│   ├── literature.tex      TICKET-22
│   ├── methodology.tex     TICKET-24
│   ├── repair.tex          TICKET-11 + TICKET-21
│   ├── experiments.tex     (experimental setup)
│   ├── results.tex         TICKET-25
│   └── conclusion.tex      TICKET-26
└── figures/            Figures included in the report (curated subset)
```

## Conventions

- **One section per file.** Reduces merge conflicts when multiple authors edit in parallel.
- **Figures** referenced by the report go in `report/figures/`. Experiment outputs live in `../results/figures/`; copy the curated subset into `report/figures/` for inclusion.
- **Citations** are added to `references.bib`. Use BibTeX keys of the form `lastnameyearkeyword`, e.g., `goldberg1989genetic`.
- Each section file starts with a header comment naming the ticket and owner.

## Overleaf workflow (Option B from project planning)

1. Initialize the Overleaf project by uploading this directory (zip) or via Overleaf's one-time GitHub import.
2. Writers edit in Overleaf for live collaboration.
3. The designated sync owner exports the Overleaf project as zip at the end of each week and commits to `report/` here.
4. Figures generated in `../results/figures/` should be copied (curated) into `report/figures/` and uploaded to Overleaf.

## Template

Single-column `article` class, 11pt, A4 paper, 1-inch margins, one-and-a-half line spacing, default Computer Modern font. Citation style remains IEEE (`\bibliographystyle{IEEEtran}`).

This was chosen over IEEE two-column conference format for readability — the report has substantial methodology, pseudocode, equations, and analysis that read better in a single column.

If you want to switch to IEEE two-column, change the first two lines of `main.tex`:

```latex
\documentclass[conference]{IEEEtran}
% (remove geometry, times, authblk, setspace packages — IEEEtran handles these)
```
