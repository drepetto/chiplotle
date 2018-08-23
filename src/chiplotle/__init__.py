from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.core.cfg.initialize_files import initialize_files
from .__version__ import __author__, __version__, __license__, __url__, __copyright__, __description__

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
# globals().pop('hpgl')
# globals().pop('tools')
# globals().pop('utils')
