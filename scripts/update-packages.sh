#!/usr/bin/env bash

# Exit on error and check run from project root
set -e && cd scripts/../

printf "\n📋 · Update pip and CSS/JS dependencies\n\n\n"

# Show available Python packages (all updates)
python -m pip list --outdated

# Update Python packages specification
python -m piptools compile --upgrade --generate-hashes --quiet -o requirements.txt pyproject.toml
python -m piptools compile --upgrade --all-extras --generate-hashes --quiet -o requirements-dev.txt pyproject.toml

# Update Python packages locally (development)
python -m piptools sync requirements-dev.txt

# Update CSS/JS packages
bash scripts/package-to-web.sh

# Update pre-commit hooks
python -m pre_commit autoupdate
set +e
python -m pre_commit run --all-files

# Show available Python packages (locked dependencies)
python -m pip list --outdated

# Provide information for Git commit
printf "\n\n✅ · Git commit message:"
printf "\n\n     Update all dependencies (esp. ...)\n\n"
