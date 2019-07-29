#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages

NAME = '{{ cookiecutter.repo_name }}'
VERSION = '{{ cookiecutter.version }}'
DESCRIPTION = '{{ cookiecutter.project_short_description }}'
KEYWORDS = '{{ ccookiecutter.project_keywords }}'
URL = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'
AUTHOR = '{{ cookiecutter.full_name }}'
AUTHOR_EMAIL = '{{ cookiecutter.email }}'
REQUIRES_PYTHON = ">=3.5.0"
LICENSE = "Apache Software License 2.0"

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

requirements = list()
with open("requirements.txt") as req:
    for dependency in req.readlines():
        requirements.append(dependency)

dev_requirements = []
with open("requirements_dev.txt") as dev:
    for dependency in dev.readlines():
        dev_requirements.append(dependency)

docs_requirements = ["sphinx", "guzzle-sphinx-theme", "nbsphinx", "pandoc", "ipython"]

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://{{ cookiecutter.repo_name }}.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author=AUTHOR,
    author_email=AUTHOR,
    url=URL,
    packages=find_packages(),
    package_dir={'{{ cookiecutter.repo_name }}': '{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    install_requires=requirements,
    extras_require={"docs": docs_requirements, "dev": dev_requirements},
    license='MIT',
    zip_safe=False,
    keywords='{{ cookiecutter.project_keywords }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
