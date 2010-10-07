#TODO: deprecate
#from chiplotle import *
#from py.test import raises
#
#def test_container_getitem_01( ):
#   circles = [Circle((0, 0), 100), Circle((100, 0), 50)]
#   t = Container((0, 0), circles)
#
#   assert t[0] is circles[0]
#   assert t[1] is circles[1]
#   assert t[:] == circles
#   assert raises(IndexError, 't[3]')
#   
#
#def test_container_getitem_02( ):
#   '''Empty Container.'''
#   t = Container((0, 0), [ ])
#
#   assert raises(IndexError, 't[0]')
#
