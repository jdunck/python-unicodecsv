#!/usr/bin/env python

from setuptools import setup, find_packages

version = __import__('unicodecsv').__version__

setup(
    name='unicodecsv',
    version=version,
    description="Python2's stdlib csv module is nice, but it doesn't support unicode. This module is a drop-in replacement which *does*.",
    long_description=open('README.rst', 'r').read(),
    author='Jeremy Dunck',
    url='https://github.com/jdunck/python-unicodecsv',
    packages=find_packages(),
    tests_require=['unittest2>=0.5.1'],
    test_suite='runtests.get_suite',
    )

