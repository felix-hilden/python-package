python-package
==============
|build| |documentation|

A package template for Python.

Please find the assumed tooling, further considerations and explanations below.
Any unwanted part of the package can simply be removed.
To start using this template, familiarise yourself with the files and tooling,
change any references from "package" to your chosen package name
and set up with external providers like Read The Docs.

Assumed tooling
---------------
- Hosted on GitHub
- Pytest and Coverage for testing
- Tox and linters for static analysis
- Numpy-style ``.rst`` documentation with Sphinx (see ``docs/src/conf.py``)
- CI performed with GitHub Actions
- Documentation hosted on Read The Docs

Considerations
--------------
- Create a separate readme for PyPI
- Create a contribution guide

.. |build| image:: https://github.com/felix-hilden/python-package/workflows/CI/badge.svg
   :target: https://github.com/felix-hilden/python-package/actions
   :alt: build status

.. |documentation| image:: https://rtfd.org/projects/nonexistentproject/badge/?version=latest
   :target: https://nonexistentproject.rtfd.org/en/latest
   :alt: documentation status
