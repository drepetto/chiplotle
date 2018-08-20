from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.geometry.shapes.circle import circle
from chiplotle.geometry.transforms.scale import scale

def symmetric_polygon_side_length(count, length):
    '''Creates a symmetric polygon with `count` sides, all with the
    same given `length`.
    '''
    result = circle(1.0, count)
    scale(result, length / result.points.difference[0].magnitude)
    return result
