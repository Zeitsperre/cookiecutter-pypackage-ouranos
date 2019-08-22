============
Installation
============

At the command line either via pip::

    $ pip install {{ cookiecutter.repo_name }}

This is the preferred method to install {{ cookiecutter.repo_name}}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io/en/stable/
.. _Python installation guide: https://docs.python-guide.org/starting/installation/

From sources
------------
The sources for {{ cookiecutter.repo_name }} can be downloaded from the `Github repo`_.

You can either clone the public repository::

    $ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

Or download the `tarball`_::

    $ curl -OL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/tarball/master

Once you have a copy of the source, you can install it with::

    $ python setup.py install

Alternatively, you can also install a local copy via pip::

    $ pip install .

.. _Github repo: https://github.com/Ouranosinc/xclim
.. _tarball: https://codeload.github.com/Ouranosinc/xclim/legacy.tar.gz/master

Creating a Conda environment
----------------------------

To create a conda development environment including all xclim dependencies, enter the following command from within your cloned repo::

    $ conda create -n my_{{ cookiecutter.repo_name }}_env python=3.6 --file=requirements_dev.txt
    $ conda activate my_{{ cookiecutter.repo_name }}_env
    $ python setup.py install
