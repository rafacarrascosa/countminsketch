# coding: utf-8

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


base_path = os.path.dirname(os.path.abspath(__file__))

long_description = ''
readme_path = os.path.join(base_path, 'README.rst')
if os.path.isfile(readme_path):
    long_description = open(readme_path).read()

setup(
    name="countminsketch",
    version="0.2",
    description="A minimalistic Count-min Sketch for Python",
    long_description=long_description,
    author="Rafael Carrascosa",
    author_email="rafacarrascosa@gmail.com",
    py_modules=["countminsketch"],
    install_requires=[],
    url="https://github.com/rafacarrascosa/countminsketch",
    keywords=["countminsketch", "count", "counting", "count min sketch",
              "count-min sketch", "randomized algorithm"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        ],
)
