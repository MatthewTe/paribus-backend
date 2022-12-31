#!/bin/sh

printf "Setting up the development environment, migrating static files locally"

# Applying Database Migrations:
echo "Making Database Migrations"
python manage.py makemigrations
python manage.py migrate 
#python manage.py runserver 0.0.0.0:8000


# If it is in development, make local static migrations:
#if [ "$PRODUCTION" = False ]; then


#fi


