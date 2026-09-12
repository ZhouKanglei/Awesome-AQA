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

## Venue abbreviations

**All supported conference and journal abbreviations are defined at the top of
`data/aqa.bib`.** Use those macros to keep
the venue/year badges compact and consistent. Do not wrap a full conference or
journal name in braces when a macro already exists.

Conference papers use `booktitle`:

```bibtex
booktitle = CVPR,
```

Journal papers use `journal`:

```bibtex
journal = TPAMI,
```

Common conference macros include:

| Macro | Venue |
|---|---|
| `AAAI` | AAAI Conference on Artificial Intelligence |
| `ACMMM` | ACM International Conference on Multimedia |
| `CVPR` / `CVPRW` | CVPR / CVPR Workshops |
| `ECCV` / `ECCVW` | ECCV / ECCV Workshops |
| `ICASSP` | IEEE ICASSP |
| `ICCV` | IEEE/CVF ICCV |
| `ICME` | IEEE ICME |
| `IJCAI` | International Joint Conference on Artificial Intelligence |
| `MICCAI` / `MICCAIW` | MICCAI / MICCAI Workshops |
| `NeurIPS` | Advances in Neural Information Processing Systems |
| `WACV` | IEEE/CVF WACV |

Common journal macros include:

| Macro | Journal |
|---|---|
| `ACMCS` | ACM Computing Surveys |
| `CVIU` | Computer Vision and Image Understanding |
| `IETCV` | IET Computer Vision |
| `IJCV` | International Journal of Computer Vision |
| `JBHI` | IEEE Journal of Biomedical and Health Informatics |
| `PR` | Pattern Recognition |
| `TCSVT` | IEEE Transactions on Circuits and Systems for Video Technology |
| `TIP` | IEEE Transactions on Image Processing |
| `TMM` | IEEE Transactions on Multimedia |
| `TNNLS` | IEEE Transactions on Neural Networks and Learning Systems |
| `TNSRE` | IEEE Transactions on Neural Systems and Rehabilitation Engineering |
| `TPAMI` | IEEE Transactions on Pattern Analysis and Machine Intelligence |

The tables above are representative rather than exhaustive; check the macro
declarations in `data/aqa.bib` before introducing a new name. If a venue macro
is missing, add the same macro key to the full, abbreviated, and short-name
sections and mention it in the pull request.

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
