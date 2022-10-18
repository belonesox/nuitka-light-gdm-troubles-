#!/bin/sh
#Generated build_dmextract-screen 
 
export PATH="/usr/lib64/ccache:$PATH"
export PIPENV_VENV_IN_PROJECT=1

time nice -19 pipenv run python -m nuitka  --show-scons --plugin-enable=numpy --plugin-enable=pkg-resources --output-dir="wtf.dist" --standalone --follow-imports --jobs=8 ./test-lightgbm.py
