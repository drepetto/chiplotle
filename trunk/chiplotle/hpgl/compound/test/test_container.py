#TODO: deprecate
#from chiplotle import *
#import py.test
#
#def test_container_01( ):
#   '''Container must initialize with a position'''
#   py.test.raises(TypeError, 't = Container( )')
#
#
#def test_container_02( ):
#   '''Container can be initialized with just position tuple.'''
#   t = Container((1, 2))
#
#   assert t.xy == (1, 2)
#   assert t.x == 1
#   assert t.y == 2
#   assert t.xabsolute == 1
#   assert t.yabsolute == 2
#   assert len(t) == 0
#   assert t.format == ''
#
#
#def test_container_03( ):
#   '''Container can carry _CompoundHPGL objects.'''
#   circle = Circle((10, 20), 100)
#   t = Container((1, 2), [circle])
#
#   assert len(t) == 1
#   assert t.format == 'PU11,22;CI100.00;'
#   assert t[0] is circle
#
#
#def test_container_04( ):
#   '''All elements in a Container must be _CompoundHPGL objects.'''
#   py.test.raises(TypeError, 't = Container((1,2), [PD( ), CI(3)])')
#
#
### positioning ##
#
#def test_container_05( ):
#   '''The absolute prosition of CompoundHPGL objects contained in Container
#   depend on their container(s).'''
#   c = Circle((10, 20), 100)
#   t = Container((1, 2), [c])
#
#   assert c.x == 10
#   assert c.y == 20
#   assert c.xabsolute == 11
#   assert c.yabsolute == 22
#   assert c.xy == (10, 20)
#   assert c.xyabsolute == (11, 22)
#   assert c.parentage.parent is t
#
#
#def test_container_06( ):
#   '''Containers can embed other Containers.'''
#   c = Circle((10, 20), 100)
#   s = Container((1, 2), [c])
#   t = Container((3, 4), [s])
#
#   assert c.parentage.parent is s
#   assert s.parentage.parent is t
#   assert t.parentage.parent is None
#   assert c.xy == (10, 20)
#   assert s.xy == (1, 2)
#   assert t.xy == (3, 4)
#   assert c.xyabsolute == (14, 26)
#   assert s.xyabsolute == (4, 6)
#   assert t.xyabsolute == (3, 4)
#
#
#
### pop ##
#
#def test_container_pop_01( ):
#   '''Children of Container have no parentage.parent after poped.'''
#   c = Circle((1, 2), 100)
#   t = Container((0, 0), [c])
#   
#   assert c.parentage.parent is t
#   assert len(t) == 1
#   c = t.pop( )
#   assert c.parentage.parent is None
#   assert len(t) == 0
#
#
#def test_container_pop_02( ):
#   '''Children of Container have no parentage.parent after poped.'''
#   t = Container((0, 0), [Circle((1, 2), 100), Circle((3, 4), 200)])
#   c = t.pop(0)
#
#   assert c.parentage.parent is None
#   assert len(t) == 1
#
#
### __setitem__ ##
#
#def test_container_setitem_01( ):
#   '''Items can be set. Parenthood is set correctly.'''
#   t = Container((0, 0), [Circle((1, 2), 100)])
#   r = Rectangle((3, 4), 100, 200)
#   t[0] = r
#
#   assert len(t) == 1
#   assert t[0] is r
#   assert r.parentage.parent is t
#
#
### scale ##
#
#def test_container_scale_01( ):
#   t = Container((1, 2), [ ])
#   hpgltools.scale(t, 1.5)
#
#   assert Container._scalable == ['xy']
#   assert t.xy == (1.5, 3)
