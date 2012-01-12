from chiplotle import *
from chiplotle.hpgl.commands import *
from py.test import raises

def test_convert_coordinates_to_absolute_hpgl_path_01( ):
   '''Coordinates can be generic tuples.'''
   c = [(1, 2), (3, 4), (5, 6)]
   t = hpgltools.convert_coordinates_to_hpgl_absolute_path(c)
   assert t[0] == PU( )
   assert t[1] == PA([c[0]])
   assert t[2] == PD( )
   assert t[3] == PA(c[:])


def test_convert_coordinates_to_absolute_hpgl_path_02( ):
   '''Coordinates can be Coordinates.'''
   c = [Coordinate(1, 2), Coordinate(3, 4), Coordinate(5, 6)]
   t = hpgltools.convert_coordinates_to_hpgl_absolute_path(c)
   assert t[0] == PU( )
   assert t[1] == PA([c[0].xy])
   assert t[2] == PD( )
   assert t[3] == PA(c)


def test_convert_coordinates_to_absolute_hpgl_path_03( ):
   '''The argument can be a CoordinateArray'''
   c = CoordinateArray([Coordinate(1, 2), Coordinate(3, 4), Coordinate(5, 6)])
   t = hpgltools.convert_coordinates_to_hpgl_absolute_path(c)
   assert t[0] == PU( )
   assert t[1] == PA([list(c[0])])
   assert t[2] == PD( )
   assert t[3] == PA([list(x) for x in c])


def test_convert_coordinates_to_absolute_hpgl_path_04( ):
   '''Argument must be a list of coordinate pairs..'''
   c = [1, 2, 3, 4]
   assert raises(TypeError, 'hpgltools.convert_coordinates_to_hpgl_absolute_path(c)')


