#!/usr/bin/env bash

# Exit on error and check run from project root
set -e && cd scripts/../

printf "\n📋 · Initialize development project\n\n\n"

# Create virtual environment and install dependencies
printf "\n🐍 · Install Python dependencies\n\n"
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
python -m pip install \
  --no-deps --disable-pip-version-check --quiet \
  -r requirements-dev.txt

# Create .env file (if not exists) and activate debug mode
if [ ! -f app/config/.env ]; then
  echo "DJANGO_DEBUG=True" >app/config/.env
fi

# Create SQLite database and gather initial data
printf "\n🎺 · Create Django project\n\n\n"

cd app

python manage.py migrate --verbosity 0
python manage.py loaddata parlgov-fixture.json
cat apps/views_data/views-data.sql | python manage.py dbshell

python manage.py collectstatic --no-input --verbosity 0

printf "\n\n✅ · Project initialization\n\n"
