================================
{{ cookiecutter.project_name }}
================================

|build| |coveralls| |codefactor| |black|

{{ cookiecutter.project_short_description }}

* Documentation: |docs|
* Free Software: |license|

Features
--------

* TODO

.. |build| image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
        :alt: Build Status

.. |coveralls| image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge.svg
        :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
        :alt: Coveralls

.. |codefactor| image:: https://www.codefactor.io/repository/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge
        :target: https://www.codefactor.io/repository/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
        :alt: CodeFactor

.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge
        :target: https://{{ cookiecutter.repo_name }}.readthedocs.io/en/latest
        :alt: Documentation Status

.. |license| image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/blob/master/LICENSE
        :alt: License

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black
        :alt: Python Black
