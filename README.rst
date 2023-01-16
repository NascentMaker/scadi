| |pypiversion| |pypiwheel| |pypipyversions| |pypilicense| |pypidownloads|
| |precommit| |coverage| |maintainability|

=====
scadi
=====

Command-line tool for rolling up all includes into the main file of your model so that you can easily share it online.

Installation
============

::

   pip3 install scadi

Usage
=====

::

   scadi inline ./my-model.scad

The above command will create a file called ``./inline-my-model.scad`` that can be shared on sites that have OpenSCAD customizers.

License
=======

Copyright 2021 Nascent Maker, nascentmaker.com.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Support me
==========

If you found that this tool saved you some time and you want to give back, please consider using Ko-Fi to buy me a coffee.

.. image:: https://ko-fi.com/img/githubbutton_sm.svg
   :target: https://ko-fi.com/S6S7GJUG3
   :alt: ko-fi

.. |pypiversion| image:: https://img.shields.io/pypi/v/scadi
   :target: https://pypi.org/project/scadi/
   :alt: PyPI

.. |pypipyversions| image:: https://img.shields.io/pypi/pyversions/scadi
   :target: https://pypi.org/project/scadi/
   :alt: PyPI - Python Version

.. |pypiwheel| image:: https://img.shields.io/pypi/wheel/scadi
   :target: https://pypi.org/project/scadi/
   :alt: PyPI - Wheel

.. |pypilicense| image:: https://img.shields.io/pypi/l/scadi
   :target: https://pypi.org/project/scadi/
   :alt: PyPI - License

.. |pypidownloads| image:: https://img.shields.io/pypi/dm/scadi
   :target: https://pypi.org/project/scadi/
   :alt: PyPI - Downloads

.. |precommit| image:: https://results.pre-commit.ci/badge/github/NascentMaker/scadi/main.svg
   :target: https://results.pre-commit.ci/latest/github/NascentMaker/scadi/main
   :alt: pre-commit.ci status

.. |coverage| image:: https://img.shields.io/codeclimate/coverage/NascentMaker/scadi
   :target: https://codeclimate.com/github/NascentMaker/scadi
   :alt: Code Climate coverage

.. |maintainability| image:: https://img.shields.io/codeclimate/maintainability/NascentMaker/scadi
   :target: https://codeclimate.com/github/NascentMaker/scadi
   :alt: Code Climate maintainability
