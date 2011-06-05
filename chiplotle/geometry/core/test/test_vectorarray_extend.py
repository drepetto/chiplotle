from chiplotle import *
from py.test import raises

def test_coordinatearray_extend_01( ):
   '''CoordinateArray cannot be extended with a list of (x, y) pairs.'''
   t = CoordinateArray( )
   assert raises(TypeError, 't.extend([(0, 0), (1, 2)])')


def test_coordinatearray_extend_02( ):
   '''CoordinateArray can be extended with a list of Coordinate.'''
   t = CoordinateArray( )
   t.extend([Coordinate(0, 0), Coordinate(3, 2)])
   assert len(t) == 2
   assert isinstance(t[0], Coordinate)
   assert isinstance(t[1], Coordinate)


def test_coordinatearray_extend_03( ):
   '''Mixtures are not allowed.'''
   t = CoordinateArray( )
   assert raises(TypeError, 't.extend([Coordinate(0, 0), (3, 2)])')
