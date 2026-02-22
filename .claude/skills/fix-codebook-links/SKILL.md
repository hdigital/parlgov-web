---
name: fix-codebook-links
description: Fix broken links in the ParlGov codebook. Converts old parlgov.org/explore/ URLs to the current site structure, updates /documentation/ paths to /docs/codebook/, removes /data/table/ links, and rewrites old-domain absolute links to parlgov.fly.dev. Use when asked to fix, update, or repair codebook links.
disable-model-invocation: true
allowed-tools: Bash, Read, Grep
---

# Fix Codebook Links

Fixes broken links in `scripts/migrate_parlgov-db/import-data-legacy/13__docs__Page.csv`,
which is the source of truth for all codebook content. Changes flow:

```
13__docs__Page.csv  →  Django import  →  DB  →  docs/assets/parlgov-codebook.md
```

Only rows for pages rendered by the codebook template are modified:
`codebook` · `country` · `credits` · `changelog`

## Transformations

| Old pattern | New URL |
|---|---|
| `/explore/{country}/party/{id}/` | `https://parlgov.fly.dev/data/parties/{country_lower}/{id}/` |
| `/explore/{country}/cabinet/{date}/` | `https://parlgov.fly.dev/data/cabinets/{country_lower}/{date}/` |
| `/explore/{country}/election/{date}/` | `https://parlgov.fly.dev/data/elections/{country_lower}/{date}/` |
| `/documentation/codebook/#election` | `https://parlgov.fly.dev/docs/codebook/#elections` |
| `/documentation/country/#ltu` | `https://parlgov.fly.dev/docs/codebook/#lithuania` |
| `/documentation/country` | `https://parlgov.fly.dev/docs/codebook/#countries` |
| `/documentation/readme/` | `'readme.txt'` (no equivalent — link removed, text single-quoted) |
| `[text]` linked to a data table URL | `'text'` (link removed, text single-quoted) |
| `http://www.parlgov.org/...` | `https://parlgov.fly.dev/...` + path transform above |

## Steps

### 1 — Perform

Run the fix script from the repository root:

```bash
python .claude/skills/fix-codebook-links/scripts/fix_links.py
```

The script reports every transformation applied and its count. It is **idempotent**: a
second run on an already-fixed CSV will report "No changes needed" and exit without
writing the file.

### 2 — Check

After the script runs:

**a) Verify no broken patterns remain in the CSV:**

The script's own `verify()` step is the authoritative check — its output is printed after
the change log. A passing run ends with:

```
Verification passed — no remaining broken patterns in codebook pages.
```

As an additional cross-check on the raw file:

```bash
grep -c '/explore/' scripts/migrate_parlgov-db/import-data-legacy/13__docs__Page.csv
grep -c 'parlgov\.org/explore' scripts/migrate_parlgov-db/import-data-legacy/13__docs__Page.csv
```

Both should be **0**. Do not check `/documentation/` across the full file — there is one
known false positive in the `manage` page (`readme.txt` linked to `/documentation/readme/`).
The `manage` page is legacy data from the old site: never rendered by any view or template
in the current app, so intentionally excluded from the script and ignored.

**b) Review the git diff to confirm changes look correct:**

```bash
git diff scripts/migrate_parlgov-db/import-data-legacy/13__docs__Page.csv
```

Inspect a sample of changed lines to confirm the URL structure is correct.

**c) Update the database and regenerate the codebook markdown:**

`create_codebook` reads from the database, not the CSV directly. The database must be
re-imported first, otherwise the codebook will still contain old links.

```bash
cd app
python manage.py import_data          # re-import all CSVs into the database
python manage.py create_codebook > ../docs/assets/parlgov-codebook.md
```

Verify the regenerated file has fly.dev links and no legacy patterns (run from repo root):

```bash
grep -c 'parlgov.fly.dev' docs/assets/parlgov-codebook.md   # should be > 0
grep -c '/explore/' docs/assets/parlgov-codebook.md          # should be 0
```

**d) Manual review — check for remaining non-standard links:**

The script only handles systematic patterns. After regenerating the codebook, scan for any
remaining links that fall outside those patterns and fix them directly in the CSV:

```bash
grep -oP '\[([^\]]+)\]\(([^)]+)\)' docs/assets/parlgov-codebook.md | grep -v 'parlgov.fly.dev'
```

Review each result and decide: fix the URL, remove the link (keep text), or leave as-is
(e.g. external references that are still valid).

**Known dead domains — reviewed and kept as-is** (domain gone, no suitable replacement):

| Domain | Link text | Reason kept |
|---|---|---|
| `elections.uwa.edu.au` | Australian Government and Politics Database | Generic `www.uwa.edu.au` has no relevant content |
| `www.historisch.apa.at` | Meldungen der APA 1955-1985 | Archive discontinued; `www.apa.at` has no equivalent |
| `www.nsd.uib.no` | Data on the Political System — PolSys | Reviewed 2026-02; `www.nsd.no/polsys/en/` exists but not applied |
| `www.election.demon.co.uk` | United Kingdom Election Results; references | Old Demon Internet hosting; no direct successor |

**Known dead domains — updated:**

| Old URL | New URL | Reason |
|---|---|---|
| `http://www3.istat.it/dati/catalogo/...` | `https://www.istat.it` | Institutional domain migration |
| `http://www.nsd.uib.no/polsys/index.cfm?...` | `https://www.nsd.no/polsys/en/` | NSD moved from uib.no to nsd.no |

### 3 — Document

Report the following summary to the user:

- Total number of links changed (per category from the script output)
- Verification result (pass / warnings)
- Whether the codebook markdown was regenerated
- Any patterns that could not be automatically resolved (script warnings)

Include in the git commit message which link categories were fixed and why (e.g.
"Fix codebook links: /explore/ → fly.dev/data/..., remove /data/table/ links").
