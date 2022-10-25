#!/bin/sh
export PIPENV_VENV_IN_PROJECT=1
pipenv --rm
pipenv install
#pipenv run pip install -r requirements.txt