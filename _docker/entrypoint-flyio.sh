#!/bin/sh

# Docker configuration Fly.io -- for Django with SQLite on Docker volume

python manage.py collectstatic --noinput
python manage.py migrate --noinput

echo "Completed Django 'collectstatic' and 'migrate' -- see 'entrypoint.sh'"
echo "Starting server on Docker port 8000 -- see 'entrypoint.sh'"

gunicorn --bind 0.0.0.0:8000 --workers 2 config.wsgi:application

exec "$@"
