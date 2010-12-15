from chiplotle import *

def test_coordinatearray_extend_01( ):
   '''CoordinateArray can be extended with a list of (x, y) pairs.'''
   t = CoordinateArray( )
   t.extend([(0, 0), (12, 23)])
   assert len(t) == 2
   assert isinstance(t[0], CoordinatePair)
   assert isinstance(t[1], CoordinatePair)
   assert t[0] == (0, 0)
   assert t[1] == (12, 23)


def test_coordinatearray_extend_02( ):
   '''CoordinateArray can be extended with a list of CoordinatePair.'''
   t = CoordinateArray( )
   t.extend([CoordinatePair(0, 0), CoordinatePair(3, 2)])
   assert len(t) == 2
   assert isinstance(t[0], CoordinatePair)
   assert isinstance(t[1], CoordinatePair)


def test_coordinatearray_extend_03( ):
   '''Mixtures are allowed.'''
   t = CoordinateArray( )
   t.extend([CoordinatePair(0, 0), (3, 2)])
   assert len(t) == 2
   assert isinstance(t[0], CoordinatePair)
   assert isinstance(t[1], CoordinatePair)




