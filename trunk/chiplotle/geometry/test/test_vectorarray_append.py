from chiplotle import *
from py.test import raises

def test_coordinatearray_append_01( ):
   '''VectorArray cannot be appended an (x, y) pair.'''
   t = VectorArray( )
   assert raises(errors.InitParameterError, 't.append((0, 0))')


def test_coordinatearray_append_02( ):
   '''VectorArray can be appended an Vector.'''
   t = VectorArray( )
   t.append(Vector(0, 0))
   assert len(t) == 1
   assert isinstance(t[0], Vector)


