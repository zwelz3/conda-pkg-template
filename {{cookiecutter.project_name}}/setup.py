#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

root = path.dirname(__file__)
__version__ = '{{cookiecutter.version}}'

requirements = []

setup(name='{{cookiecutter.project_name}}',
      version=__version__,
      description='{{cookiecutter.project_name}}',
      long_description=open(path.join(root, 'README.md')).read(),
      download_url='',
      keywords='mdao openmdao tradespace execution',
      author='{{cookiecutter.full_name}}',
      author_email='{{cookiecutter.email}}',
      url='',
      packages=find_packages(),
      package_data={'{{cookiecutter.project_name}}': ['*.pickle']},
      install_requires=requirements,
      extras_require={},
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: Other/Proprietary License',
                   'Environment :: Web Environment :: Cortex',
                   'Topic :: Scientific/Engineering',
                   'Environment :: Plugins',
                   'Framework :: Cortex',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3.4',
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
      entry_points={})
