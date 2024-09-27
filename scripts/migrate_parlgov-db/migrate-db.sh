#!/usr/bin/env bash

# This script is used to migrate tables from the legacy ParlGov database.
# An R version with the 'tidyverse' package is required to run the script.
# It creates csv-files, a SQLite database, a Django fixture and a models graph.
#
# The script is used in local development and not in production.
#
# Use '.scripts/recreate-project.sh' to initialize the project with the data created by this script.

# Exit on error
set -e

printf "\n📋 · Import csv-data legacy database into Django project\n\n\n"

cd scripts/migrate_parlgov-db

if command -v Rscript &>/dev/null; then
  # Format and check R code in folder
  Rscript -e "styler::style_dir()"
  Rscript -e "lintr::lint_dir()"

  # Create csv files in './app/scripts/import-data-legacy/'
  Rscript --vanilla migrate-db.R
else
  printf "\n\n🚨 · R not found, skipping CSV creation from database\n\n"
fi

cd ../../app

# Remove and recreate database
rm -f parlgov.sqlite
python manage.py migrate --verbosity 0

# Import csv data
python manage.py import_data

# Create fixture (without superuser)
printf "\n\n🗃️ · Dump data to fixture\n\n"
python manage.py dumpdata >parlgov-fixture.json

# Format csv files and fixture (continue on error)
set +e
python -m pre_commit run --all-files
set -e

# Run project init script
cd ..
bash scripts/recreate-project.sh
bash scripts/graph-data-models.sh

# Run data validation
cd app
python manage.py validate_data

# Create superuser
python manage.py create_superuser

# Check documentation database migration
cd ../scripts/migrate_parlgov-db
Rscript --vanilla migration-check.R

printf "\n\n✅ · Data import legacy database\n\n"
