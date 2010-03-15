from chiplotle import *
import py.test

def test_container_01( ):
   '''Container must initialize with a position'''
   py.test.raises(TypeError, 't = Container( )')


def test_container_02( ):
   '''Container can be initialized with just position tuple.'''
   t = Container((1, 2))

   assert all(t.xy == [1, 2])
   assert t.x == 1
   assert t.y == 2
   assert t.xabsolute == 1
   assert t.yabsolute == 2
   assert len(t) == 0
   assert t.format == ''

def test_container_03( ):
   '''Container can carry _CompoundHPGL objects.'''
   circle = Circle((10, 20), 100)
   t = Container((1, 2), [circle])

   assert len(t) == 1
   assert t.format == 'PU11.00,22.00;CI100.0;'
   assert t[0] is circle


def test_container_04( ):
   '''All elements in a Container must be _CompoundHPGL objects.'''
   py.test.raises(TypeError, 't = Container((1,2), [PD( ), CI(3)])')


## positioning ##

def test_container_05( ):
   '''The absolute prosition of CompoundHPGL objects contained in Container
   depend on their container(s).'''
   c = Circle((10, 20), 100)
   t = Container((1, 2), [c])

   assert c.x == 10
   assert c.y == 20
   assert c.xabsolute == 11
   assert c.yabsolute == 22
   assert all(c.xy == (10, 20))
   assert all(c.xyabsolute == (11, 22))
   assert c._parent is t


def test_container_06( ):
   '''Containers can embed other Containers.'''
   c = Circle((10, 20), 100)
   s = Container((1, 2), [c])
   t = Container((3, 4), [s])

   assert c._parent is s
   assert s._parent is t
   assert t._parent is None
   assert all(c.xy == (10, 20))
   assert all(s.xy == (1, 2))
   assert all(t.xy == (3, 4))
   assert all(c.xyabsolute == (14, 26))
   assert all(s.xyabsolute == (4, 6))
   assert all(t.xyabsolute == (3, 4))

