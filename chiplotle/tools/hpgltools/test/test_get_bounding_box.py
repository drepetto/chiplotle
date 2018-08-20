from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle import *
from chiplotle.hpgl.commands import PA, EA

def test_get_bounding_box_01( ):
    '''The function can take a list of _HPGLPrimitives.'''
    t = hpgltools.get_bounding_box([PA([(1, 2), (3, 4)])])
    assert t == (Coordinate(1, 2), Coordinate(3, 4))


def test_get_bounding_box_02( ):
    '''The function can take a list of _HPGLPrimitives.'''
    a = [PA([(1, 2), (3, 4)]), EA((10, -2))]
    t = hpgltools.get_bounding_box(a)
    assert t == (Coordinate(1, -2), Coordinate(10, 4))


