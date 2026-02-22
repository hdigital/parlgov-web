#!/usr/bin/env python3
"""Fix broken links in the ParlGov codebook CSV.

Only processes rows for pages included in the codebook:
  codebook · country · credits · changelog

Transformations applied to content fields of those rows:

1. /explore/{country}/party|cabinet|election/...
      → https://parlgov.fly.dev/data/parties|cabinets|elections/{country_lower}/...

2. /documentation/... → https://parlgov.fly.dev/docs/... with correct anchors
   - /documentation/codebook/#election → .../docs/codebook/#elections
   - /documentation/country/#ltu       → .../docs/codebook/#lithuania
   - /documentation/country            → .../docs/codebook/#countries
   - /documentation/readme/            → 'text' (no equivalent)

3. [text](/data/table/...) → 'text'  (link removed, text single-quoted)

4. http://www.parlgov.org/... → https://parlgov.fly.dev/...
   applying the same path transformations as 1–3 above.
"""

import csv
import io
import re
import sys
from pathlib import Path

CSV_PATH = Path("scripts/migrate_parlgov-db/import-data-legacy/13__docs__Page.csv")

FLY = "https://parlgov.fly.dev"
OLD_DOMAIN = r"http://(?:www\.)?parlgov\.org"

# Pages rendered by the codebook template
CODEBOOK_PAGES = {"codebook", "country", "credits", "changelog"}

# Column indices (0-based); header: section,modified,page,content,data_json,id
PAGE_COL = 2
CONTENT_COL = 3


def fix_content(text: str) -> tuple[str, list[str]]:
    """Apply all link fixes to one content field. Returns (fixed, change_log)."""
    log: list[str] = []

    def sub(pattern: str, repl, description: str) -> None:
        nonlocal text
        new_text, n = re.subn(pattern, repl, text)
        if n:
            log.append(f"  {n:2d}  {description}")
        text = new_text

    # ── 1. Relative /explore/ → absolute fly.dev ─────────────────────────────

    sub(
        r"\(/explore/([A-Za-z]+)/party/(\d+)/?\)",
        lambda m: f"({FLY}/data/parties/{m.group(1).lower()}/{m.group(2)}/)",
        "relative /explore/.../party/{id}/ → fly.dev/data/parties/",
    )
    sub(
        r"\(/explore/([A-Za-z]+)/cabinet/(\d{4}-\d{2}-\d{2})/?\)",
        lambda m: f"({FLY}/data/cabinets/{m.group(1).lower()}/{m.group(2)}/)",
        "relative /explore/.../cabinet/{date}/ → fly.dev/data/cabinets/",
    )
    sub(
        r"\(/explore/([A-Za-z]+)/election/(\d{4}-\d{2}-\d{2})/?\)",
        lambda m: f"({FLY}/data/elections/{m.group(1).lower()}/{m.group(2)}/)",
        "relative /explore/.../election/{date}/ → fly.dev/data/elections/",
    )
    # Cabinet list page (no date) — one known occurrence: /explore/DNK/cabinet/
    sub(
        r"\(/explore/([A-Za-z]+)/cabinet/\)",
        lambda m: f"({FLY}/data/cabinets/{m.group(1).lower()}/)",
        "relative /explore/.../cabinet/ (list) → fly.dev/data/cabinets/",
    )

    # ── 2. Relative /documentation/ → absolute fly.dev ───────────────────────

    # Most-specific anchors first
    sub(
        r"\(/documentation/codebook/#election\)",
        f"({FLY}/docs/codebook/#elections)",
        "relative /documentation/codebook/#election → fly.dev/docs/codebook/#elections",
    )
    sub(
        r"\(/documentation/country/#ltu\)",
        f"({FLY}/docs/codebook/#lithuania)",
        "relative /documentation/country/#ltu → fly.dev/docs/codebook/#lithuania",
    )
    sub(
        r"\(/documentation/country\)",
        f"({FLY}/docs/codebook/#countries)",
        "relative /documentation/country → fly.dev/docs/codebook/#countries",
    )
    sub(
        r"\[([^\]]+)\]\(/documentation/readme/\)",
        r"'\1'",
        "relative /documentation/readme/ → 'text'",
    )

    # ── 3. /data/table/ relative links → 'text' ──────────────────────────────

    sub(
        r"\[([^\]]+)\]\(/data/table/[^)]+\)",
        r"'\1'",
        "relative /data/table/... → 'text'",
    )

    # ── 4. http://www.parlgov.org/... → https://parlgov.fly.dev/... ──────────

    sub(
        rf"\({OLD_DOMAIN}/explore/([A-Za-z]+)/party/(\d+)/?\)",
        lambda m: f"({FLY}/data/parties/{m.group(1).lower()}/{m.group(2)}/)",
        "old domain .../explore/.../party/{id}/ → fly.dev/data/parties/",
    )
    sub(
        rf"\({OLD_DOMAIN}/explore/([A-Za-z]+)/cabinet/(\d{{4}}-\d{{2}}-\d{{2}})/?\)",
        lambda m: f"({FLY}/data/cabinets/{m.group(1).lower()}/{m.group(2)}/)",
        "old domain .../explore/.../cabinet/{date}/ → fly.dev/data/cabinets/",
    )
    sub(
        rf"\({OLD_DOMAIN}/explore/([A-Za-z]+)/election/(\d{{4}}-\d{{2}}-\d{{2}})/?\)",
        lambda m: f"({FLY}/data/elections/{m.group(1).lower()}/{m.group(2)}/)",
        "old domain .../explore/.../election/{date}/ → fly.dev/data/elections/",
    )
    sub(
        rf"\({OLD_DOMAIN}/documentation/codebook-all/?\)",
        f"({FLY}/docs/codebook/)",
        "old domain .../documentation/codebook-all/ → fly.dev/docs/codebook/",
    )
    sub(
        rf"\({OLD_DOMAIN}/documentation/country\)",
        f"({FLY}/docs/codebook/#countries)",
        "old domain .../documentation/country → fly.dev/docs/codebook/#countries",
    )
    sub(
        rf"\({OLD_DOMAIN}/documentation/news/[^)]*\)",
        f"({FLY}/docs/news/)",
        "old domain .../documentation/news/... → fly.dev/docs/news/",
    )
    sub(
        rf"\[([^\]]+)\]\({OLD_DOMAIN}/data/table/[^)]+\)",
        r"'\1'",
        "old domain .../data/table/... → 'text'",
    )

    return text, log


def verify_content(text: str) -> list[str]:
    """Return warnings for remaining broken patterns in a content field."""
    issues = []
    checks = [
        (r"\(/explore/", "remaining relative /explore/ link"),
        (rf"\({OLD_DOMAIN}/explore/", "remaining old-domain /explore/ link"),
        (r"\(/documentation/", "remaining relative /documentation/ link"),
        (
            rf"\({OLD_DOMAIN}/documentation/",
            "remaining old-domain /documentation/ link",
        ),
        (r"\[([^\]]+)\]\(/data/table/", "remaining relative /data/table/ link"),
        (
            rf"\[([^\]]+)\]\({OLD_DOMAIN}/data/table/",
            "remaining old-domain /data/table/ link",
        ),
    ]
    for pattern, desc in checks:
        matches = re.findall(pattern, text)
        if matches:
            issues.append(f"  {len(matches):2d}  {desc}")
    return issues


def main() -> int:
    """Fix broken links in the codebook CSV and regenerate the codebook markdown."""
    if not CSV_PATH.exists():
        print(
            f"ERROR: {CSV_PATH} not found — run from repository root.", file=sys.stderr
        )
        return 1

    original = CSV_PATH.read_text(encoding="utf-8")
    reader = csv.reader(io.StringIO(original))
    rows = [list(row) for row in reader]

    change_log: list[str] = []
    verify_log: list[str] = []

    for row in rows:
        if len(row) <= CONTENT_COL or row[PAGE_COL] not in CODEBOOK_PAGES:
            continue

        page = row[PAGE_COL]
        new_content, changes = fix_content(row[CONTENT_COL])

        if changes:
            change_log.append(f"\n  [{page}]")
            change_log.extend(changes)
            row[CONTENT_COL] = new_content

        issues = verify_content(row[CONTENT_COL])
        if issues:
            verify_log.append(f"\n  [{page}]")
            verify_log.extend(issues)

    if not change_log:
        print("No changes needed — all links already up to date.")
        return 0

    print("Changes applied:")
    for line in change_log:
        print(line)

    if verify_log:
        print("\nWARNING — remaining unresolved patterns:")
        for line in verify_log:
            print(line)
    else:
        print("\nVerification passed — no remaining broken patterns in codebook pages.")

    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerows(rows)
    CSV_PATH.write_text(output.getvalue(), encoding="utf-8")
    print(f"\nWritten: {CSV_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
