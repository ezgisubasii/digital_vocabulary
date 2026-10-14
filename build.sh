#!/usr/bin/env bash
# Render runs this on every deploy
set -o errexit

pip install -r requirements.txt

cd digitalvocabulary
python manage.py collectstatic --no-input
python manage.py migrate
