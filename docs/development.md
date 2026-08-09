# Development · 💻

See Python development dependencies in `requirements-dev.txt` and
documentation of environment variables in `.env.example`.
[uv](https://docs.astral.sh/uv/pip/) is used as a _venv/pip_ replacement for
some development tasks.

## Commands · 🏃🏼

Use [just](https://just.systems/man/en/chapter_20.html#quick-start) command
runner for local development and in codespace.

List commands with

```sh
just
```

## Testing · 🧪

Run tests and check test coverage with

```sh
# (.venv) ./app
pytest --cov
```

Tests are run randomly with
[pytest-randomly](https://github.com/pytest-dev/pytest-randomly). This can be
turned off with

```sh
# (.venv) ./app
pytest --cov --randomly-dont-reorganize
```

## Database · 🫙

### Tables · 📂

Database tables use prefixes.

- _data_ — data tables (e.g., parties, elections, cabinets)
- _docs_ — documentation tables (e.g., codebook, news)
- _view_ — main data tables (database views, _see below_)

Django also includes other tables in the app database (`parlgov.sqlite`).

A visualization of the data tables is provided in `graph-models_data.png` (see
below).

### Normalization · ✔️

The database created with the Django models is _normalized_ except for the
`election` attribute of the `Cabinet` model. An _election_ is added or updated
to a _cabinet_ on save. A later change to the _election_ that changes the
previous election for the _cabinet_ is not updated for the _cabinet_
automatically.

All cabinets' elections can be checked and updated with

```sh
# (.venv) ./app
python manage.py update_cabinet_election
```

### Views · 🔬

Three main tables (parties, elections, cabinets) are provided as database
views. They include the most frequently used information from the primary
database tables.

These views are created during the initialization of the project (see [Data
import](usage.md#data-import)).

The three main views are not included as Django models in the project.

## Miscellaneous · 🗂️

### Documentation · 📚

Start documentation at [localhost:8888](http://localhost:8888/)

```sh
# (.venv) ./
mkdocs serve --dev-addr localhost:8888
```

Build static site documentation

```sh
# (.venv) ./
mkdocs build --clean --strict
```

### Prose linting · ✍️

Check docs and Markdown files for style issues with
[Vale](https://vale.sh/), run via `uvx` (see `.vale.ini`)

```sh
uvx vale sync
uvx vale docs README.md CHANGELOG.md
```

### Graph models · 📐

Create or update [graph
models](https://django-extensions.readthedocs.io/en/latest/graph_models.html#example-usage)
— locally only

```sh
# (.venv) ./
./scripts/graph-data-models.sh
```

The script needs _graphviz_ installed and is included only locally to keep
testing, Docker, and codespace configuration lean.

Install on macOS with Homebrew

```sh
brew install graphviz
```

Install on Ubuntu and Debian (e.g., codespace) with

```sh
sudo apt-get install graphviz graphviz-dev
```

See also `just codespace-dev`

---

![graph-models](./assets/graph-models_data.png)
