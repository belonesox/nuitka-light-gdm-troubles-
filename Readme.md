Let's consider sample program using LightGBM and nuitka call for compilation on Linux:

https://github.com/belonesox/nuitka-light-gdm-troubles-
branch
«no_docstrings»

* `./reproduce-me.sh` to (re)install virtual environment for install/build/run compiled

Running results we get crush on «import lightgbm»
```
Traceback (most recent call last):
  File "/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/test-lightgbm.py", line 7, in <module>
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/lightgbm/__init__.py", line 21, in <module lightgbm>
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/lightgbm/dask.py", line 1088, in <module lightgbm.dask>
  File "/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/lightgbm/dask.py", line 1143, in DaskLGBMClassifier
AttributeError: 'NoneType' object has no attribute 'partition'
```

The problem option is «--python-flag=no_docstrings», without it all works fine. 
But why, if anyone wants to strip docstring… 

Same problem exists even with nuitka factory.