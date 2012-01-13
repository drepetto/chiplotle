from chiplotle import *

def ca_square(wh):
   coords = [(0, 0), (wh, 0), (wh, wh), (0, wh), (0, 0)]
   coords = [Coordinate(*c) for c in coords]
   return CoordinateArray(coords)

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


def test_coordinatearray_difference_01( ):
   t = CoordinateArray([(1, 2), (3, 4), (4, 4)])
   assert t.difference == CoordinateArray([(2, 2), (1, 0)])
   assert isinstance(t, CoordinateArray)


def test_coordinatearray_cumsum_01( ):
   t = CoordinateArray([(1, 1), (1, 1), (1, 1)])
   assert t.cumsum == CoordinateArray([(0, 0), (1, 1), (2, 2), (3, 3)])
