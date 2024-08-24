# show 'just' recipes (default)
default:
  just --list

alias pf := git-push-force

## Recipes 'just' — https://just.systems/man/en/chapter_20.html

# initialize Codespace
codespace-init: venv
  sudo apt-get update -y && sudo apt-get install -y sqlite3
  npm install --global --quiet prettier
  cp .vscode/settings.json.dev .vscode/settings.json
  cp app/config/.env.codespace app/config/.env
  # 'venv' activation with '.' needed instead of 'source'
  . .venv/bin/activate && pre-commit install --install-hooks
  . .venv/bin/activate && cd app && python manage.py collectstatic --no-input --verbosity 0
  . .venv/bin/activate && cd app && python manage.py migrate --verbosity 0

# prune Git and remove stale branches
git-prune:
  git remote prune origin

# push Git and force updates
git-push-force:
  git push --force-with-lease --force-if-includes

# pull Git and force updates
git-pull-force branch:
  git fetch --all
  git reset --soft origin/{{branch}}
  @echo "📝 · Creating backup with 'git stash'"
  git stash --message "pull-force stash backup"
  git reset --hard origin/{{branch}}

# initialize and create project
init: venv load-data

# lint and format code
lint:
  cd app && python manage.py validate_templates
  bash scripts/format-with-prettier.sh
  prettier --write .devcontainer .github .vscode
  mypy --ignore-missing-imports .
  ruff format .
  ruff check --fix .
  pre-commit run --all-files

# load project data (fixtures and static files)
load-data:
  cd app && python manage.py migrate --verbosity 0
  cd app && python manage.py collectstatic --no-input --verbosity 0
  cd app && python manage.py loaddata parlgov-fixture.json
  cd app && cat apps/views_data/views-data.sql | python manage.py dbshell
  cd app && python manage.py create_superuser

# synchronize Python packages
pip-sync:
  uv pip sync requirements-dev.txt

# update Python packages
pip-update:
  uv pip compile --upgrade --quiet --generate-hashes -o requirements.txt pyproject.toml
  uv pip compile --upgrade --quiet --generate-hashes -o requirements-dev.txt --all-extras pyproject.toml
  uv pip sync requirements-dev.txt
  @echo "\n\n✅ · Use only for temporary updates, for production use './scripts/update-packages.sh'\n"

# run Django and MKDocs server
serve:
  mkdocs serve --dev-addr localhost:8888 &
  cd app && python manage.py runserver &
  @sleep 3
  @echo "\n📝 · Django server running at http://localhost:8000"
  @echo "📝 · MKDocs server running at http://localhost:8888"
  @echo "\n📝 · just serve-quit  # quit server (background processes)\n"

# quit running servers
serve-quit:
  pkill -f mkdocs &
  pkill -f runserver &
  @sleep 1

# test code
test:
  cd app && pytest --quiet --cov --cov-report term-missing:skip-covered -n auto

# update all dependencies (pip, pre-commit, js)
update-all: venv pip-update
  bash scripts/update-packages.sh
  cd app && pytest --quiet
  @echo "\nGit commit message: Update all dependencies'\n"

# recreate Python environment
venv:
  uv venv --quiet --seed
  uv pip sync --quiet requirements-dev.txt
  uv pip --quiet install pip
  @echo "\n\n✅ · Activate virtualenv with: source .venv/bin/activate\n"
