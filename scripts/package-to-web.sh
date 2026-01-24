#!/usr/bin/env bash

# Exit on error and check run from project root
set -e && cd scripts/../

printf "\n\n📋 · Install Bootstrap and Bootstrap Icons\n\n"

# Install bootstrap with npm and create "package-lock.json"
npm install --quiet --no-fund bootstrap bootstrap-icons

mv package-lock.json scripts

# Copy minified versions of packages into Django static
cp node_modules/bootstrap/dist/css/bootstrap.min.css app/static/css
cp node_modules/bootstrap/dist/css/bootstrap.min.css.map app/static/css
cp node_modules/bootstrap/dist/js/bootstrap.bundle.min.js* app/static/js
cp node_modules/bootstrap-icons/font/bootstrap-icons.css app/static/css
cp -r node_modules/bootstrap-icons/font/fonts app/static/css

# Remove local npm data
rm package.json
rm -r node_modules

printf "\n\n✅ · Bootstrap install\n\n"
