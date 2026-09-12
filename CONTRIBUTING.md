# Contributing to Awesome-AQA

`Awesome-AQA` is the source of truth for both this README and the AQA Survey
website.

## Submit a pull request

1. Fork this repository and create a branch from `main`.
2. Edit `data/aqa.bib`. Edit `data/survey.bib` instead when contributing a
   survey/review paper.
3. Add one focused change per pull request.
4. Run `python scripts/generate_readme.py` to preview the result.
5. Do not manually edit or commit the generated paper tables in `README.md`.
6. Push your branch and open a pull request. GitHub will automatically show the
   pull request template and run the README-generation check.

After a pull request is merged, GitHub Actions regenerates and commits
`README.md` on `main`.

The AQA Survey website reads `data/aqa.bib` and `data/ccf2026.json` directly
from this repository, so those files must not be duplicated or edited in the
AQA Survey repository.

To preview the generated README locally, run:

```bash
python scripts/generate_readme.py
```

If the preview changed `README.md`, inspect it and then restore the generated
file before committing:

```bash
git diff -- README.md
git restore README.md
```

## BibTeX template

Use `@inproceedings` for conference papers and `@article` for journal or arXiv
papers. Use an existing venue macro such as `CVPR`, `ECCV`, `TPAMI`, or `TMM`
where available.

```bibtex
@inproceedings{surname2026shorttitle,
  author    = {Surname, Given Name and Another, Author},
  title     = {Full Paper Title},
  booktitle = CVPR,
  year      = {2026},
  pages     = {},
  pdf       = {https://arxiv.org/pdf/xxxx.xxxxx},
  domain    = {Sports},
  modality  = {RGB},
  project   = {https://example.org/project-page},
  code      = {https://github.com/owner/repository},
  tags      = {Interpretable Feedback, Dataset, ExampleSet (new)},
  comment   = {A concise description of the paper's main contribution.}
}
```

Use empty braces when an optional value is not available. Mark a newly
introduced dataset as `DatasetName (new)` in `tags`; the README generator uses
that marker for the dataset column.

## Resource links

Keep project pages and source repositories in separate BibTeX fields:

```bibtex
project = {https://example.org/project-page},
code    = {https://github.com/owner/repository},
```

- Use `project` for an official project, demo, dataset, or resource page.
- Use `code` for a source-code or implementation repository.
- Do not put a GitHub repository in `project`; this keeps both links visible
  when a paper provides both resources.

## Corrections

- Edit the existing entry instead of adding a duplicate.
- Keep its BibTeX key stable unless the key itself contains incorrect metadata.
- Include an authoritative source in the pull request description for venue,
  year, author, or publication-status corrections.
- Keep unrelated formatting changes out of the pull request.
