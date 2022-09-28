#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata artista_dataset.json
python manage.py loaddata musica_dataset.json
DJANGO_SUPERUSER_USERNAME=admin@example.com \
DJANGO_SUPERUSER_EMAIL=admin@example.com \
DJANGO_SUPERUSER_PASSWORD=Admin123! \
./manage.py createsuperuser \
--first_name "super" \
--last_name "admin" \
--is_staff "True" \
--noinput
python manage.py runserver 0.0.0.0:8000