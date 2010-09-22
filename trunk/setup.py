#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from distutils.core import setup
from ez_setup import use_setuptools
use_setuptools( ) ### this must come before setup import
from setuptools import setup, find_packages

setup(name = 'Chiplotle', 
      version = '0.2.3', 
      description = 'Chiplotle is an HPGL (Hewlett-Packard Graphics Language) Python API.',
      long_description = 'Chiplotle is an HPGL (Hewlett-Packard Graphics Language) Python API.',
      author = 'Víctor Adán and Douglas Repetto',
      author_email = 'chiplotle@music.columbia.edu',
      url = 'http://music.columbia.edu/cmc/chiplotle',
      keywords = 'vector graphics hpgl plotter plot pen',
      license = 'GPL', 
      include_package_data = True,
      packages = find_packages( ),
## numpy seems to not install properly via easy_install.
## probably better to have the user figure out how to install it manually.
      #install_requires=['pyserial', 'numpy'],
      install_requires=['pyserial'],
      entry_points = {'console_scripts':[
         'chiplotle = chiplotle.cfg._run_chiplotle:_run_chiplotle',
         ]},
      scripts = [ 
         'chiplotle/scripts/envelope.py',
         'chiplotle/scripts/dorkbot_font.py',
         'chiplotle/scripts/plot_hpgl_file.py',
         'chiplotle/scripts/plot_hpgl_file_max_size.py',
         'chiplotle/scripts/typewriter.py',
         'chiplotle/scripts/view_hpgl_file.py',
         ], 
      )
