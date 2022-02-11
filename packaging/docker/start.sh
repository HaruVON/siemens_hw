#!/bin/sh

# Start Nginx in the background
# Got to the api folder
# Start gunicorn therefore starting the Python Flask backend API
nginx &
cd /var/www/siemens_hw/api
pipenv run gunicorn -b 127.0.0.1:5000 siemens_hw:app