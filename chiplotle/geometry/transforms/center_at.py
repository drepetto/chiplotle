from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.geometry.transforms.offset import offset
from chiplotle.geometry.core.coordinate import Coordinate

def center_at(shape, coord):
    '''Centers shape at the given coordinate.'''
    offset(shape, -shape.center + Coordinate(*coord))

