# ParlGov database migration scripts

Scripts to migrate the legacy ParlGov database to the new Django-based system.

Use `parlgov-experimental.db` from [ParlGov Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/2VZ5ZC) and place it in this directory. The migration extracts data from the legacy database, imports it into Django, creates a fixture (`parlgov-fixture.json`), and runs data validation.

- `migrate-db.R` — Extract and transform data from legacy database to CSV files
- __`migrate-csv.sh`__ — Import CSV files, create fixture, and run project initialization
- `migration-check.R` — Verify migration by comparing databases (optional)
- `import-data-legacy/` — Generated CSV files for Django import
- `migration-check.csv` — Migration mapping table ('legacy' → 'new' table names)
