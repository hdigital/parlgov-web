#!/usr/bin/env bash

# Exit on error and check run from project root
set -e && cd scripts/../

printf "\n\n📋 · Recreate project\n\n"

cd app

# Remove database and existing migrations
rm -f parlgov.sqlite
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Create migrations, migrate database and import data
python manage.py makemigrations --no-header --verbosity 0 datacore parties elections cabinets docs
python manage.py migrate --verbosity 0
python -m pre_commit run --all-files

# Import data from fixture
printf "\n\n🗄️ · Load data from fixture\n\n"
python manage.py loaddata --exclude contenttypes --exclude auth.permission parlgov-fixture.json

# Create views main data tables
python manage.py dbshell <apps/views_data/views-data.sql

# Generate OpenAPI schema (install 'drf-spectacular' on demand)
uv --project .. pip install --quiet --group docs-drf
python manage.py spectacular --color --file ../schema.yaml

# Collect static files (CSS, JS, images)
python manage.py collectstatic --noinput

# Run tests and validations
python -m pytest --quiet
python manage.py check
python manage.py validate_templates

cd ..

# Run Ruff code formatter and linter
python -m ruff format .
python -m ruff check --fix .

# Create codebook (md, pdf) in './docs/assets/'
bash scripts/create-codebook.sh

printf "\n\n✅ · Project recreation\n\n"
