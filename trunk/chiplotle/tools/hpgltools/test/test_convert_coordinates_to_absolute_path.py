from chiplotle import *
from py.test import raises

def test_convert_coordinates_to_absolute_hpgl_path_01( ):
   '''Coordinates can be generic tuples.'''
   c = [(1, 2), (3, 4), (5, 6)]
   t = hpgltools.convert_coordinates_to_hpgl_absolute_path(c)
   assert t[0] == PU( )
   assert t[1] == PA(c[0])
   assert t[2] == PD( )
   assert t[3] == PA(c[1:])


def test_convert_coordinates_to_absolute_hpgl_path_02( ):
   '''Coordinates can be CoordinatePairs.'''
   c = [CoordinatePair(1, 2), CoordinatePair(3, 4), CoordinatePair(5, 6)]
   t = hpgltools.convert_coordinates_to_hpgl_absolute_path(c)
   assert t[0] == PU( )
   assert t[1] == PA(c[0])
   assert t[2] == PD( )
   assert t[3] == PA(c[1:])


def test_convert_coordinates_to_absolute_hpgl_path_03( ):
   '''Argument must be a list of coordinate pairs..'''
   c = [1, 2, 3, 4]
   assert raises(TypeError, 'hpgltools.convert_coordinates_to_hpgl_absolute_path(c)')


