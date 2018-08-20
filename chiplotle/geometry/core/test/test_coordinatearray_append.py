from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle import *
from py.test import raises

def test_coordinatearray_append_01( ):
    '''CoordinateArray cannot be appended an (x, y) pair.'''
    t = CoordinateArray( )
    assert raises(TypeError, 't.append((0, 0))')


def test_coordinatearray_append_02( ):
    '''CoordinateArray can be appended an Coordinate.'''
    t = CoordinateArray( )
    t.append(Coordinate(0, 0))
    assert len(t) == 1
    assert isinstance(t[0], Coordinate)


