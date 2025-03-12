# Makefile for Django project

# Variable for virtual environment
VENV_NAME = venv
PYTHON = $(VENV_NAME)/bin/python
PIP = $(VENV_NAME)/bin/pip

# Load environment variables from .env file
include .env
export $(shell sed 's/=.*//' .env)

# Variables for Django project
PROJECT_NAME = $(DJANGO_PROJECT_NAME)
DJANGO_APP_NAME = $(filter-out $@,$(MAKECMDGOALS))

# Install dependencies
install:
	@echo "Instalowanie zależności..."
	python3 -m venv $(VENV_NAME)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run Django server
run:
	@echo "Running Django server..."
	$(PYTHON) $(PROJECT_NAME)/manage.py runserver

# Migration of database
migrate:
	@echo "Database migration..."
	$(PYTHON) $(PROJECT_NAME)/manage.py migrate

# Making new Django app
app:
	@echo "Making new Django app..."
	$(PYTHON) $(PROJECT_NAME)/manage.py startapp $(DJANGO_APP_NAME)

# Running tests
test:
	@echo "Running tests..."
	$(PYTHON) $(PROJECT_NAME)/manage.py test

# Generating migrations
makemigrations:
	@echo "Generating migrations..."
	$(PYTHON) $(PROJECT_NAME)/manage.py makemigrations

# Stopping server
stop:
	@echo "Stopping server..."
	@pkill -f runserver

# Running Django shell
shell:
	@echo "Running Django shell..."
	$(PYTHON) $(PROJECT_NAME)/manage.py shell

# Checking dependencies
check:
	@echo "Sprawdzanie aktualności zależności..."
	$(PIP) check

# Collecting static files
collectstatic:
	@echo "Collecting static files..."
	$(PYTHON) $(PROJECT_NAME)/manage.py collectstatic --noinput

# Deleting virtual environment
clean:
	@echo "Deleting virtual environment..."
	rm -rf $(VENV_NAME)

# Installing dependencies and running server
dev: install run
