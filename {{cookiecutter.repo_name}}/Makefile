.PHONY: help clean clean-pyc clean-build list test test-all coverage docs release sdist

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "compliant - make changes to code to satisfy lint rules"
	@echo "lint - check style with modfied pep8 and black"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"
	@echo "install - install the library in developmer mode"

clean: clean-build clean-pyc  ## remove all build, test, coverage and Python artifacts

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

compliant:
	auotopep8 {{ cookiecutter.repo_name }} test
	black {{ cookiecutter.repo_name }} test

lint:
	flake8 {{ cookiecutter.repo_name }} test
	black {{ cookiecutter.repo_name }} test --check

test:
	pytest test

test-all:
	tox

coverage:
	coverage run --source {{ cookiecutter.repo_name }} setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/{{ cookiecutter.repo_name }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.repo_name }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

sdist: clean
	python setup.py sdist
	python setup.py bdist_wheel upload
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	pip install -e .
