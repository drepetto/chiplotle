#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


about = dict()
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'chiplotle', '__version__.py'), 'r') as f:
    exec(f.read(), about)


setup(name              = about['__title__'],
      version           = about['__version__'],
      description       = about['__description__'],
      long_description  = about['__description__'],
      author            = about['__author__'],
      author_email      = about['__author_email__'],
      url               = 'http://music.columbia.edu/cmc/chiplotle',
      keywords          = 'vector graphics hpgl plotter plot pen',
      license           = about['__license__'],

      include_package_data = True,
      packages             = find_packages(),
      install_requires     = ['pyserial<=3', 'numpy<=2'],
      entry_points         = {'console_scripts':
         ['chiplotle = chiplotle.core.cfg._run_chiplotle:_run_chiplotle',]},
      scripts              = [
         'chiplotle/scripts/envelope.py',
         'chiplotle/scripts/find_hpgl_file_dimensions.py',
         'chiplotle/scripts/plot_hpgl_file_max_size.py',
         'chiplotle/scripts/plot_hpgl_file.py',
         'chiplotle/scripts/plot_hpgl_file_virtual.py',
         'chiplotle/scripts/typewriter.py',
         'chiplotle/scripts/view_hpgl_file.py',
         ],
      )

