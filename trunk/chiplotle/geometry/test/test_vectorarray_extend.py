from chiplotle import *
from py.test import raises

def test_coordinatearray_extend_01( ):
   '''VectorArray cannot be extended with a list of (x, y) pairs.'''
   t = VectorArray( )
   assert raises(errors.InitParameterError, 't.extend([(0, 0), (1, 2)])')


def test_coordinatearray_extend_02( ):
   '''VectorArray can be extended with a list of Vector.'''
   t = VectorArray( )
   t.extend([Vector(0, 0), Vector(3, 2)])
   assert len(t) == 2
   assert isinstance(t[0], Vector)
   assert isinstance(t[1], Vector)


def test_coordinatearray_extend_03( ):
   '''Mixtures are not allowed.'''
   t = VectorArray( )
   assert raises(errors.InitParameterError, 't.extend([Vector(0, 0), (3, 2)])')
