#!/bin/sh
#pipenv install 
export PIPENV_VENV_IN_PROJECT=1
export PATH="/usr/lib64/ccache:$PATH"
./install_env.sh 
./factory-nuitka.sh 
time nice -19 pipenv run python -m nuitka  --show-scons \
--plugin-enable=numpy \
--plugin-enable=pkg-resources \
--nofollow-import-to=matplotlib \
--nofollow-import-to=pandas  \
--standalone \
--python-flag=no_docstrings \
--follow-imports --jobs=8 ./test-lightgbm.py
./test-lightgbm.dist/test-lightgbm
