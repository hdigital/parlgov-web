#!/usr/bin/env bash

# Import CSV tables created with 'migrate-db.R' into the Django project.

# Exit on error
set -e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

printf "\n\n📋 · Import csv-data legacy database into Django project\n\n"

cd "$PROJECT_ROOT/app"

# Remove and recreate database
rm -f parlgov.sqlite
python manage.py migrate --verbosity 0

# Import csv data
python manage.py loaddata \
  --exclude contenttypes \
  --exclude auth.permission parlgov-fixture.json
cat apps/views_data/views-data.sql | python manage.py dbshell

# Create fixture (without superuser)
printf "\n\n🗃️ · Dump data to fixture\n\n"
python manage.py dumpdata >parlgov-fixture.json

# Format csv files and fixture (continue on error)
set +e
python -m pre_commit run --all-files
set -e

# Run project init script
cd "$PROJECT_ROOT"
bash scripts/recreate-project.sh
bash scripts/graph-data-models.sh

# Run data validation
cd "$PROJECT_ROOT/app"
python manage.py validate_data

# Create superuser
python manage.py create_superuser

printf "\n\n📝 · Check spelling documentation tables\n\n"
cd "$SCRIPT_DIR"
uvx typos import-data-legacy/*__docs__*

printf "\n\n✅ · Legacy database import\n\n"
