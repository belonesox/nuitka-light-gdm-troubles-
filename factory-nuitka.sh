#!/bin/sh
export PIPENV_VENV_IN_PROJECT=1
pipenv run python3 -m pip uninstall nuitka -y
pipenv run python3 -m pip install git+https://github.com/Nuitka/nuitka.git@factory
