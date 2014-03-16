# coding: utf-8

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


base_path = os.path.dirname(os.path.abspath(__file__))
long_description = open(os.path.join(base_path, 'README.rst')).read()

setup(
    name="countminsketch",
    version="0.1",
    description="A minimalistic Count-min Sketch for Python",
    long_description=long_description,
    author="Rafael Carrascosa",
    py_modules=["countminsketch"],
    install_requires=[],
)
