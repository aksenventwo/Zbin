#!/usr/bin/env python
"""
setup.py: utilities to install this package
"""
from setuptools import find_packages, setup
from zbin import __version__


setup(name='Zbin',
      version=__version__,
      description='Lightweight library for reading binary files.',
      author='Wei zou',
      author_email='xiaoshengzou@163.com',
      packages=find_packages(),
      install_requires=[],
      test_suite='tests',
      )
