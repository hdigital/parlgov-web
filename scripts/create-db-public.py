#!/usr/bin/env python3
"""Create public ParlGov database (exclude Django tables)."""

import shutil
import sqlite3

db_public = "parlgov-public.sqlite"
shutil.copy("app/parlgov.sqlite", db_public)

with sqlite3.connect(db_public) as conn:
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    # Delete Django tables
    for table in tables:
        if not table[0].startswith(("data_", "docs_", "sqlite_")):
            cur.execute(f"DROP TABLE {table[0]};")

    conn.commit()

print(f"\n\n✅ · Creating database '{db_public}'\n\n")
