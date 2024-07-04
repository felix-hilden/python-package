python-package
==============
|build| |documentation|

A package template for Python.

To start using this template, familiarise yourself with the files and tooling,
change any references from "package" to your chosen package name.

Tooling
-------

- Pytest and Coverage for testing
- Uv, tox, ruff etc.
- Numpy-style ``.rst`` docs with Sphinx hosted on Read The Docs
- Hosted on GitHub with GH Actions CI

Setup
-----

- Change any references to "Package" to your liking
- Create ``.pypirc`` file for publishing the package

.. code:: ini

   [pypi]
   username = __token__
   password = pypi-<your-token>

.. code:: bash

   # Bootstrap
   pip install uv
   uv venv
   source .venv/bin/activate # or .venv/Scripts/activate on Windows

   # Setup and verify
   uv pip install -e . -r requirements/dev
   tox

.. |build| image:: https://github.com/felix-hilden/python-package/workflows/CI/badge.svg
   :target: https://github.com/felix-hilden/python-package/actions
   :alt: build status

.. |documentation| image:: https://rtfd.org/projects/nonexistentproject/badge/?version=latest
   :target: https://nonexistentproject.rtfd.org/en/latest
   :alt: documentation status
