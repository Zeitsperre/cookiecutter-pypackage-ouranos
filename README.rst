==============================
cookiecutter-pypackage-ouranos
==============================

Cookiecutter template (Ouranos recipe) for a Python package. See https://github.com/audreyr/cookiecutter.

* Free software: Apache2_ license
* Pytest_ runner: Supports `unittest`, `pytest`, `nose` style tests and more
* Travis-CI_: Ready for Travis Continuous integration testing
* Tox_ testing: Setup to easily test for python 3.5, 3.6, 3.7 and PyPy_
* Black_ formatting: Adherance to a PEP8-esque code formatting standard
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Pre-commit_ hooks: Automate code compliance for easy contributor development
* Wheel_ support: Use the newest python package distribution standard from the get go

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/Nekroze/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Run `tox` to make sure all tests pass.
* Release your package the standard Python way.

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `audreyr/cookiecutter-pypackage`_: The original pypackage, uses unittest
for testing and other minor changes.

Fork This
~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Once you have your fork working, add it to the
Similar Cookiecutter Templates list with a brief explanation. It's up to you
whether or not to rename your fork.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.

.. _Apache2: https://www.apache.org/licenses/LICENSE-2.0.html
.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Black: https://black.readthedocs.io/en/stable/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _`audreyr/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _Pytest: http://pytest.org/
.. _PyPy: http://pypy.org/
.. _Pre-commit: https://pre-commit.com/
.. _Wheel: http://pythonwheels.com
