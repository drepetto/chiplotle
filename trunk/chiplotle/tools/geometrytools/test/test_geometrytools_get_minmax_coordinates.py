from chiplotle import *
from chiplotle.geometry.shapes.circle import circle
from chiplotle.tools.geometrytools.get_minmax_coordinates \
   import get_minmax_coordinates
import py.test

def test_geometrytools_get_minmax_coordinates_01( ):
   '''Argument cannot be an int.'''
   s = 3
   assert py.test.raises(Exception, 't = get_minmax_coordinates(s)')

def test_geometrytools_get_minmax_coordinates_02( ):
   '''Returns a duple of Coordinates.'''
   s = circle(100)
   t = get_minmax_coordinates(s.points)
   assert t == (Coordinate(-100, -100), Coordinate(100, 100))

