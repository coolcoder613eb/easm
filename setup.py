from setuptools import setup
from Cython.Build import cythonize
import os

setup(
    name="cyeasm",
    ext_modules=cythonize("cyeasm.pyx")
)
os.system(r'copy build\lib.win-amd64-cpython-310\cyeasm.cp310-win_amd64.pyd cyeasm.cp310-win_amd64.pyd')
