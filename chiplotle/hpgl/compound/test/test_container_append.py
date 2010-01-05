from chiplotle import *
from py.test import raises

def test_container_append_01( ):
   t = Container((0, 0), [ ])
   t.append(Circle((0, 0), 100))

   assert isinstance(t[0], Circle)
   assert len(t) == 1


def test_container_append_02( ):
   '''Elements must be _CompoundHPGL.'''
   t = Container((0, 0), [ ])

   assert raises(TypeError, 't.append(3)')
   assert raises(TypeError, 't.append([Circle((0, 0), 100)])')
