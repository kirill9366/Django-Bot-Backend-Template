#!/bin/sh
python manage.py migrate

python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput

gunicorn config.wsgi -b 0.0.0.0:8081 -w 3
