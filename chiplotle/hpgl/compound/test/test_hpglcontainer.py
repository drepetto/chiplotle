##TODO: deprecate
#from chiplotle import *
#from py.test import raises
#
#def test_hpglcontainer_01( ):
#   '''HPGLContainer can be empty.'''
#   t = HPGLContainer((0, 0))
#   
#   assert len(t) == 0
#   assert t.format == 'PA0,0;'
#
#
#def test_hpglcontainer_02( ):
#   '''HPGLContainer take only primitive HPGLCommands.'''
#   t = HPGLContainer((0, 0), [PU( ), PR((1, 2, 3, 4)), RR((5, 6))])
#
#   assert t.format == 'PA0,0;PU;PR1,2,3,4;RR5,6;'
#   
#   
#def test_hpglcontainer_03( ):
#   '''HPGLContainer can have absolute position commands (e.g., PA, RA).
#   These are moved relative to the HPGLContainer position.'''
#   t = HPGLContainer((2, 3), [PU( ), PA((1,2,3,4)), RR((5, 6))])
#
#   assert len(t) == 3
#   assert isinstance(t[0], PU)
#   assert isinstance(t[1], PA)
#   assert isinstance(t[2], RR)
#   assert t.format == 'PA2,3;PU;PA3,5,5,7;RR5,6;'
#
#
### scale ##
#
#def test_hpglcontainer_scale_01( ):
#   t = HPGLContainer((2, 3), [PU( ), PA((1,2,3,4)), RR((5, 6))])
#   hpgltools.scale(t, 2)
#
#   assert HPGLContainer._scalable == ['xy']
#   assert t.xy == (4, 6)
