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
