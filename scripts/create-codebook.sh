#!/bin/bash

# Exit on error and check run from project root
set -e && cd scripts/../

printf "\n\n📙 · Create Markdown and pdf codebook\n\n"

# Create codebook markdown file with Django manage.py command
cd app
python manage.py create_codebook >../docs/assets/parlgov-codebook.md

# Format codebook markdown file and render pdf
cd ../docs/assets
prettier -w parlgov-codebook.md

if command -v pandoc &>/dev/null; then
  pandoc parlgov-codebook.md -f markdown -t pdf -o parlgov-codebook.pdf
else
  printf "\n\n🚨 · Pandoc not found, skipping PDF creation\n\n"
fi

printf "\n\n✅ · Creating codebook\n\n"
