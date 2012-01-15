from chiplotle.core.cfg.cfg import __version__
from chiplotle.core.cfg.initialize_files import initialize_files
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

initialize_files()
globals().pop('initialize_files')


## IMPORTS ##

from chiplotle.core import errors

from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.core.coordinate import Coordinate

from chiplotle.hpgl import commands as hpgl
from chiplotle.hpgl import formatters
from chiplotle.hpgl.pen import Pen

from chiplotle.geometry.core import Group
from chiplotle.geometry.core import Path
from chiplotle.geometry.core import Polygon
from chiplotle.geometry.core import Label
from chiplotle.geometry import shapes
from chiplotle.geometry import transforms
from chiplotle.geometry.shapes import *
from chiplotle.geometry.transforms import *

from chiplotle.tools.plottertools import instantiate_plotters
from chiplotle.tools.plottertools import instantiate_virtual_plotter
from chiplotle.tools import *

from chiplotle import plotters


## shortcuts / abbreviations ##

CoordArray = CoordinateArray
Coord = Coordinate

## remove unnecessary modules...
#globals().pop('hpgl')
#globals().pop('tools')
#globals().pop('utils')
