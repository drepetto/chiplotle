##TODO: deprecate
#from chiplotle import *
#from py.test import raises
#
#def test_container_setitem_01( ):
#   '''Items set must be _CompoundHPGL.'''
#   circles = [Circle((0, 0), 50), Circle((100, 0), 100)]
#   t = Container((0, 0), circles)
#   
#   assert raises(TypeError, 't[0] = 3')
#
#
#def test_container_setitem_02( ):
#   circles = [Circle((0, 0), 50), Circle((100, 0), 100)]
#   t = Container((0, 0), circles)
#   t[0] = Rectangle((0, 0), 100, 200)
#
#   assert isinstance(t[0], Rectangle)
#   assert isinstance(t[1], Circle)
#   assert t[1] is circles[1]
#
#   
#def test_container_setitem_03( ):
#   '''Slices can be set.'''
#   circles = [Circle((0, 0), 50), Circle((100, 0), 100)]
#   t = Container((0, 0), circles)
#   t[0:2] = [Rectangle((0, 0), 100, 200), Rectangle((100, 0), 40, 30)]
#
#   assert isinstance(t[0], Rectangle)
#   assert isinstance(t[1], Rectangle)
#   assert t[0].xy == [0, 0]
#   assert t[1].xy == [100, 0]
#   
#   
