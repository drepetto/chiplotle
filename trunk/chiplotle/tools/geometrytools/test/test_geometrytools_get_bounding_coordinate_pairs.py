from chiplotle import *
from chiplotle.geometry.factory.circle import circle
from chiplotle.tools.geometrytools.get_bounding_coordinate_pairs \
   import get_bounding_coordinate_pairs
import py.test

def test_geometrytools_get_bounding_coordinate_pairs_01( ):
   '''Argument must be a _Shape.'''
   s = 3
   assert py.test.raises(AttributeError, 't = get_bounding_coordinate_pairs(s)')

def test_geometrytools_get_bounding_coordinate_pairs_02( ):
   '''Returns a duple of Coordinates.'''
   s = circle(100)
   t = get_bounding_coordinate_pairs(s)
   assert t == (Coordinate(-100, -100), Coordinate(100, 100))

