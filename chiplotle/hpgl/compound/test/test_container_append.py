##TODO: deprecate 
#from chiplotle import *
#from py.test import raises
#
### append ##
#
#def test_container_append_01( ):
#   t = Container((0, 0), [ ])
#   c = Circle((1, 2), 100)
#   t.append(c)
#
#   assert c.parentage.parent is t
#   assert t[0] is c
#   assert len(t) == 1
#
#
#def test_container_append_02( ):
#   '''Elements must be _CompoundHPGL.'''
#   t = Container((0, 0), [ ])
#
#   assert raises(TypeError, 't.append(3)')
#   assert raises(TypeError, 't.append([Circle((0, 0), 100)])')
