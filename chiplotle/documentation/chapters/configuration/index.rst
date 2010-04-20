Configuration
==============

Chiplotle has a dedicated folder, ``$HOME/.chiplotle``, which houses the 
``config.py`` configuration file. This file is for setting various
preferences and defaults. The file is executed as a Python module, so its syntax must conform with standard Python syntax. 

At present only default serial communication parameters are defined here. Chiplotle sets these to common standard values. Make sure your hardware plotter is set to these values, or change the values in the config.py file to match those of your hardware.

.. note::
   If you have multiple plotters they must all have the same serial configuration.

