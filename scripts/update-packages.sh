#!/usr/bin/env bash

# Exit on error and check run from project root
set -e && cd scripts/../

printf "\n\n📋 · Update pip and CSS/JS dependencies\n\n"

# Ensure uv is available
if ! command -v uv &>/dev/null; then
  printf "🚨 · 'uv' not found — installing with pip\n"
  python -m pip install --quiet uv
fi

# Show available Python packages (all updates)
uv pip list --outdated

# Update Python packages specification
uv pip compile --upgrade --quiet --generate-hashes -o requirements.txt pyproject.toml
uv pip compile --upgrade --group dev --generate-hashes --quiet -o requirements-dev.txt pyproject.toml

# Update Python packages locally (development)
uv pip sync requirements-dev.txt

# Update CSS/JS packages
bash scripts/package-to-web.sh

# Update pre-commit hooks
python -m pre_commit autoupdate
set +e
python -m pre_commit run --all-files

# Update documentation (for mkdocs updates)
printf "\n\n📔 · Build documentation\n\n"
mkdocs build --clean --strict

# Show available Python packages (locked dependencies)
printf "\n\n🔐 · Show locked dependencies\n\n"
uv pip list --outdated

# Provide information for Git commit
printf "\n\n✅ · Git commit message\n\n"
printf "     Update all dependencies (esp. ...)\n\n"
