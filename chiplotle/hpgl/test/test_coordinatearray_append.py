from chiplotle import *

def test_coordinatearray_append_01( ):
   '''CoordinateArray can be appended an (x, y) pair.'''
   t = CoordinateArray( )
   t.append((0, 0))
   assert len(t) == 1
   assert isinstance(t[0], CoordinatePair)
   assert t[0] == (0, 0)


def test_coordinatearray_append_02( ):
   '''CoordinateArray can be appended an CoordinatePair.'''
   t = CoordinateArray( )
   t.append(CoordinatePair(0, 0))
   assert len(t) == 1
   assert isinstance(t[0], CoordinatePair)


