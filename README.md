# Excuse Generator API

## Purpose
This app enables the user to get excuses by category whilst indicating the number of excuses they would like to receive.
It then shows the user their historical excuses together with some stats showing total counts of excuse categories.


## Architecture
This project runs on the below libraries

- Python 3.6.9
- Django 3.1.4
- djangorestframework 3.11.0
- django-cors-headers 3.4.0
- requests 2.11.1
- urllib3 1.25.9


## Development server
Run `python3 manage.py runserver 8080`


## Running unit tests
Run `python3 manage.py test`


## Docker
### Build
Run `docker-compose build` to build


### Start Application
Run `docker-compose up` to start the app
