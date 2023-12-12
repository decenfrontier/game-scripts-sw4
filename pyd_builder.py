from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["wnd_login_code.py"]))
