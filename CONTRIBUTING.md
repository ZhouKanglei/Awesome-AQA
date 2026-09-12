# Updating the paper list

`Awesome-AQA` is the source of truth for both this README and the AQA Survey
website.

1. Edit `data/aqa.bib`.
2. Commit and push the change to `main`.
3. GitHub Actions runs `scripts/generate_readme.py` and commits the regenerated
   `README.md` when its contents change.

The AQA Survey website reads `data/aqa.bib` and `data/ccf2026.json` directly
from this repository, so those files must not be duplicated or edited in the
AQA Survey repository.

To preview the generated README locally, run:

```bash
python scripts/generate_readme.py
```
