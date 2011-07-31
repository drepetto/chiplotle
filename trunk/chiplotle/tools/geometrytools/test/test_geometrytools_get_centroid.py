#from chiplotle import *
#from chiplotle.core.errors import OperandError
#import py.test
#
#
### ARGUMENT CHECK ##
#
#def test_get_centroid_arg_01( ):
#   '''get_centroid( ) can take a list of Coordinates.'''
#   c = [Coordinate(1, 2), Coordinate(-1, -2)]
#   t = geometrytools.get_centroid(c)
#   assert isinstance(t, Coordinate)
#   assert t == Coordinate(0, 0)
#
#
#def test_get_centroid_arg_02( ):
#   '''get_centroid( ) can take a CoordinateArray.'''
#   c = CoordinateArray([Coordinate(1, 2), Coordinate(-1, -2)])
#   t = geometrytools.get_centroid(c)
#   assert isinstance(t, Coordinate)
#   assert t == Coordinate(0, 0)
#
#
#def test_get_centroid_arg_03( ):
#   '''get_centroid( ) can not take a list of tuples.'''
#   c = [(1, 2), (-1, -2)]
#   assert py.test.raises(TypeError, 't = geometrytools.get_centroid(c)')
#
#
#
### OPERATION ##
#
#def test_get_centroid_01( ):
#   g = [Coordinate(0, 0), Coordinate(10, 10), 
#      Coordinate(0, 10), Coordinate(10, 0)]
#   t = geometrytools.get_centroid(g)
#   assert t == Coordinate(5, 5)
#
