from chiplotle import *

def test_coordinatearray_difference_01( ):
   a = CoordinateArray([(1, 2), (3, 4), (4, 4)])
   t = a.difference
   assert t == CoordinateArray([(2, 2), (1, 0)])
   assert isinstance(t, CoordinateArray)


def test_coordinatearray_cumsum_01( ):
   a = CoordinateArray([(1, 1), (1, 1), (1, 1)])
   t = a.cumsum
   assert t == CoordinateArray([(0, 0), (1, 1), (2, 2), (3, 3)])
