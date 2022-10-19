#!/bin/sh
#Generated build_dmextract-screen 
 
export PATH="/usr/lib64/ccache:$PATH"
export PIPENV_VENV_IN_PROJECT=1

pipenv install 
time nice -19 pipenv run python -m nuitka  --show-scons --plugin-enable=numpy --plugin-enable=pkg-resources --nofollow-import-to=matplotlib --nofollow-import-to=pandas  --standalone --follow-imports --jobs=8 ./test-lightgbm.py
./test-lightgbm.dist/test-lightgbm
