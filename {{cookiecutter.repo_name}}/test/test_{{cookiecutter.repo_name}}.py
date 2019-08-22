"""
Tests for `{{ cookiecutter.repo_name }}` module.
"""
import pytest
import {{ cookiecutter.repo_name }}

from {{ cookiecutter.repo_name }} import __version__


class Test{{ cookiecutter.repo_name|capitalize }}Version(object):
    def test_version(self):
        assert __version__


class Test{{ cookiecutter.repo_name|capitalize }}(object):
    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass

