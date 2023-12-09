#!/bin/sh

cd app

if [ "$SQL_ENGINE" = *"postgres"* ]
then
    echo "Waiting for PostgreSQL..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

cd ..

python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput

exec "$@"
