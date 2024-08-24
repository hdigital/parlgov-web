#!/bin/bash

# Exit on error and check run from project root
set -e && cd scripts/../

printf "\n🧼 · Format Markdown and config files with 'prettier'\n\n\n"

# Format specified file types with 'prettier'
prettier -w ./**/*.{md,json,jsonc,yaml}

# Specify 'sed' command for Linux (default) and macOS
OS="$(uname)"
if [ "$OS" = "Darwin" ]; then
  SED_CMD=("sed" "-i" "")
else
  SED_CMD=("sed" "-i")
fi

# Adjust list indentation for Python markdown parser in docs
cd docs

for file in *.md; do
  "${SED_CMD[@]}" \
    -e 's/^      - /            - /g' \
    -e 's/^    - /        - /g' \
    -e 's/^  - /    - /g' \
    "$file"
done

printf "\n\n✅ · Formatting with 'prettier'\n\n"
