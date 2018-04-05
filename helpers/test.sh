#!/bin/bash

docker-compose run --rm web app/venv/bin/python manage.py test $@
