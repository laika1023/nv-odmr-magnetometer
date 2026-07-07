# Data management

- `raw/` — as-acquired files, never edited. Name: `YYYY-MM-DD_runNN_shortdesc.csv`
- `processed/` — outputs of analysis code only (never hand-made).
- Every raw file gets a sidecar `SAMENAME.meta.json` — copy `TEMPLATE.meta.json`.
- Full raw archives too big for git → Zenodo release; keep curated examples here.
