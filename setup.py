#!/usr/bin/env python

from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name='unicodecsv',
    version=version,
    description="Python2's stdlib csv module is nice, but it doesn't support unicode. This module is a drop-in replacement which *does*.",
    long_description=open('README', 'r').read(),
    author='Jeremy Dunck',
    url='https://github.com/jdunck/python-unicodecsv',
    packages=find_packages(),
    )

