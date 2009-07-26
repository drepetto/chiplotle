#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from distutils.core import setup
from ez_setup import use_setuptools
use_setuptools( ) ### this must come before setup import
from setuptools import setup, find_packages

setup(name = 'Chiplotle', 
      version = '0.1', 
      description = 'Chiplotle is an HPGL (Hewlett-Packard Graphics Language) Python API.',
      long_description = 'Chiplotle is an HPGL (Hewlett-Packard Graphics Language) Python API.',
      author = 'Víctor Adán and Douglas Repetto',
      author_email = 'contact@victoradan.net',
      url = 'http://music.columbia.edu/cmc/chiplotle',
      keywords = 'vector graphics hpgl plotter plot pen',
      license = 'GPL', 
      include_package_data = True,
      packages = find_packages( ),
      install_requires=['pyserial', 'numpy'],
      scripts = [#'ez_setup.py', 
         'chiplotle/scripts/chiplotle', 
         'chiplotle/scripts/envelope.py',
         'chiplotle/scripts/plothpgl.py',
         'chiplotle/scripts/typewriter.py',
         ], 
## These don't work because the scripts folder is not a package. 
## scripts must have an __init__.py file for these to be found.
#      entry_points = {'console_scripts':[
#         'chiplotle = chiplotle.scripts.chiplotle:_run_chiplotle',
#         'plothpgl = chiplotle.scripts.plothpgl:plot_hpgl',
#         'typewriter= chiplotle.scripts.typewriter:typewriter',
#         'envelope  = chiplotle.scripts.envelope:envelope',
#         ]},
      )
