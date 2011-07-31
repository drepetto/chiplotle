from chiplotle import *

def ca_square(wh):
   return CoordinateArray([(0, 0), (wh, 0), (wh, wh), (0, wh), (0, 0)])

def test_coordinatearray_properties_center_01():
   wh = 100
   t = ca_square(wh)
   assert t.center == Coordinate(wh / 2.0, wh / 2.0)


def test_coordinatearray_properties_centroid_01():
   wh = 100
   t = ca_square(wh)
   assert t.centroid == Coordinate(wh / 2.0, wh / 2.0)
   

def test_coordinatearray_properties_minmax_01():
   wh = 100
   t = ca_square(wh)
   assert t.minmax == (Coordinate(0, 0), Coordinate(wh, wh))

