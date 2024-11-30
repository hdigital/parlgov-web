# Usage · ⚙️

## Run · 🚀

Use codespace, locally, or with Docker.

Start server in **codespace** and open website in the PORTS tab.

```sh
# (.venv) ./
just serve
```

Start **locally** with Django at [localhost:8000](http://localhost:8000/)

```sh
# (.venv) ./app
python manage.py runserver
```

Use with **Docker** at [localhost:8000](http://localhost:8000/)

```sh
docker compose up
```

Create an **admin user** (see [Django
docs](https://docs.djangoproject.com/en/stable/intro/tutorial02/#creating-an-admin-user))
to edit data with

```sh
# (.venv) ./app
python manage.py createsuperuser
```

See the example of a production deployment in `Dockerfile-flyio`.

## Installation · 🛠️

Run in codespace, install locally, or use Docker (see above).

**Codespace** is fully configured. Load the data and run a local server with
_just_ commands.

```sh
# (.venv) ./
just load-data
just serve
```

**Local** install and project initialization examples are provided in
`init-dev-project.sh`.

```sh
bash ./scripts/init-dev-project.sh
source .venv/bin/activate
cd app
python manage.py runserver
```

**Docker** version requires a local database.

```sh
docker compose up --build
```

See the section _Data import_ below or use init the script in a Docker container
terminal.

```sh
» # /app
» bash ./scripts/init-dev-project.sh
```

## Data import · 🏗️

Import data from ParlGov stable release, create database views, and create an
admin user to access the Django admin site for data editing.

```sh
# (.venv) ./app
python manage.py loaddata parlgov-fixture.json
cat apps/views_data/views-data.sql | python manage.py dbshell
python manage.py createsuperuser
```

## Data validation · 🕵🏼‍♀️

All data is validated during the addition to the database with Django. The
`validate_data` command can run these and additional validations (see below).

```sh
# (.venv) ./app
python manage.py validate_data
```

Additional validations include

- parties
    - inclusion criteria check — see priority in `run_include_checks(party)`
- elections
    - one election result for election
    - seats sum equals _seats_total_
    - vote share sum in defined interval
    - _no seat_ party (first loser) included
    - max. one party with vote share < 1.0% and 0 seats
- cabinets
    - PM for one party specified
    - previous election included

Additional scripts data checks

- `cabinet_update_election` — check and update election variable in all cabinets
- `election_no_seats_party` — show elections with missing coding of first loser
  (largest party no seats)

## Codebook · 📙

All codebook sections are recorded in the database as Markdown entries. They can
be edited using the ParlGov website.

A Markdown version of the codebook based on the sections from the database is
available on the ParlGov website and can be dumped with a Django management
command.

```sh
# (.venv) ./app
python manage.py create_codebook
```

A shell script creates the codebook, formats the Markdown text file, renders a
[PDF](assets/parlgov-codebook.pdf), and adds the two documents to the
documentation.

```sh
# (.venv) ./
bash scripts/create-codebook.sh
```

## API · 🔗

The website provides an API with [Django REST
framework](https://www.django-rest-framework.org/).

It is a read-only API; no login is required.

Documentation with an OpenAPI 3 schema is provided in `schema.yaml`.

---

![ParlGov Web 2024](./assets/parlgov-web_2024.png)
