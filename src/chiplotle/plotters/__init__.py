from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

# from chiplotle.core.imports.package_import import _package_import
#
# _package_import(__path__[0], locals( ))
#
# def remove_all_but_types(lst):
#   '''Keep only classes.'''
#   from types import TypeType
#   for k, v in lst.items( ):
#      if not isinstance(v, TypeType):
#         del(lst[k])
#
# remove_all_but_types(locals( ))

from future import standard_library

standard_library.install_aliases()
from .dpx2000 import DPX2000
from .dpx3300 import DPX3300
from .dxy1100 import DXY1100
from .dxy1200 import DXY1200
from .dxy1300 import DXY1300
from .dxy880 import DXY880
from .hp7475a import HP7475A
from .hp7550a import HP7550A
from .hp7575a import HP7575A
from .hp7576a import HP7576A
from .hp7585b import HP7585B
from .hp7595a import HP7595A
from .hp7596a import HP7596A
from .plotter import Plotter
