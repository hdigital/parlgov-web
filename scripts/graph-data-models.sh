#!/usr/bin/env bash

# Exit on error and check run from project root
set -e && cd scripts/../

# Notes: This script requires 'uv' and 'Graphviz' to be installed.
#        The script is used in local development and not in production or CI/CD.

printf "\n\n📋 · Graph data models\n\n"

if ! command -v dot &>/dev/null; then
  printf "🚨 · 'graphviz' is required (see docs). Exiting...\n\n"
  exit 1
fi

# Install PyGraphviz temporarily (needs Graphviz installed, see docs)
uv pip install pygraphviz

# Create a graph of the data models
cd app
python manage.py \
  graph_models \
  base parties elections cabinets \
  -X BaseModel \
  -o ../docs/assets/graph-models_data.png

# Reset installed pip packages (remove PyGraphviz)
cd ..
uv pip sync requirements-dev.txt

# Provide information for Git commit
printf "\n\n✅ · Updated graph data models\n\n"
