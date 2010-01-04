
__version__ = "v0.1 "
__authors__ = "Victor Adan, Douglas Repetto"
__license__ = "GPL"
__url__     = "http://music.columbia.edu/cmc/chiplotle"
__doc__     = \
"""Chiplotle
Python library for pen plotting.

Copyright %s
Version %s
License %s
Homepage %s

""" % (__authors__,__version__,__license__,__url__)


### IMPORTS ###

#def _remove_modules():
#   from types import ModuleType
#   for key, value in globals().items():
#      if isinstance(value, ModuleType) and not key.startswith('_'):
#         globals().pop(key)


from chiplotle.hpgl.commands import *
from chiplotle.hpgl.compound import *
from chiplotle import plotters
from chiplotle.tools import *

from chiplotle.utils.instantiate_plotter import instantiate_plotter

#_remove_modules()

## remove unnecessary modules...
globals().pop('cfg')
globals().pop('hpgl')
globals().pop('interfaces')
globals().pop('tools')
globals().pop('utils')
