Let's consider sample program using LightGBM and nuitka call for compilation on Linux:

https://github.com/belonesox/nuitka-light-gdm-troubles-

* `pipenv install` to install virtual environment.
* `./reproduce-me.sh` for install/build/run compiled

While building, Nuitka missed ``lib_lightgbm.so``

```
$ find . -name lib_lightgbm.so
./.venv/lib/python3.10/site-packages/lightgbm/lib_lightgbm.so
```

and we got

```
Traceback (most recent call last):
  File "/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/test-lightgbm.py", line 7, in <module>
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/lightgbm/__init__.py", line 8, in <module lightgbm>
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/lightgbm/basic.py", line 110, in <module lightgbm.basic>
  File "/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/lightgbm/basic.py", line 98, in _load_lib
  File "/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/lightgbm/libpath.py", line 38, in find_lib_path
Exception: Cannot find lightgbm library file in following paths:
/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/lightgbm/lib_lightgbm.so
/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/lib_lightgbm.so
/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/lightgbm/compile/lib_lightgbm.so
/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/test-lightgbm.dist/compile/lib_lightgbm.so
/home/stas/projects/nuitka-wtf/nuitka-light-gdm-troubles/lib/lib_lightgbm.so
[stas@stasbox64gb nuitka-light-gdm-troubles]$
```