from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.geometry.shapes.rectangle import rectangle

def square(width_height):
    '''Returns a square centered at (0, 0).'''
    return rectangle(width_height, width_height)
