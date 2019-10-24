from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.core.cfg.initialize_files import initialize_files
from .__version__ import (
    __author__,
    __version__,
    __license__,
    __url__,
    __copyright__,
    __description__,
)

__doc__ = """Chiplotle
Python library for pen plotting.

Copyright %s
Version %s
License %s
Homepage %s

""" % (
    __author__,
    __version__,
    __license__,
    __url__,
)

initialize_files()
globals().pop("initialize_files")


## IMPORTS ##

from .core import errors

from .geometry.core.coordinatearray import CoordinateArray
from .geometry.core.coordinate import Coordinate

from .hpgl import commands as hpgl
from .hpgl import formatters
from .hpgl.pen import Pen

from .geometry.core import Group
from .geometry.core import Path
from .geometry.core import Polygon
from .geometry.core import Label
from .geometry import shapes
from .geometry import transforms
from .geometry.shapes import *
from .geometry.transforms import *

from .tools.plottertools import instantiate_plotters
from .tools.plottertools import instantiate_virtual_plotter
from .tools import *

from . import plotters


## shortcuts / abbreviations ##

CoordArray = CoordinateArray
Coord = Coordinate
