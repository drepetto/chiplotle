#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from distutils.core import setup
from ez_setup import use_setuptools
use_setuptools( ) ### this must come before setup import
from setuptools import setup

setup(name = 'Chiplotle', 
      version = '0.1', 
      description = 'Chiplotle is an HPGL \
      (Hewlett-Packard Graphics Language) Python API.',
      long_description = 'Chiplotle is an HPGL \
      (Hewlett-Packard Graphics Language) Python API.',
      author = 'Víctor Adán and Douglas Repetto',
      author_email = 'vga2102@columbia.edu',
      url = 'http://music.columbia.edu/cmc/chiplotle',
      keywords = 'vector graphics hpgl plotter plot pen',
      #include_package_data = True,
      license = 'GPL', 
      packages = ['chiplotle'],
      install_requires=['pyserial', 'numpy'],
      scripts = ['ez_setup.py'], 
      )
