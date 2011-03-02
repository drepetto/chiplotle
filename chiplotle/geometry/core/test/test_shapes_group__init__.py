from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.path import Path
import py.test


def test_shapes_group__init__01( ):
   '''A Group can be empty.'''
   t = Group([])
   assert len(t) == 0

def test_shapes_group__init__02( ):
   '''A Group can take no parameters.'''
   t = Group()
   assert len(t) == 0


def test_shapes_group__init__03( ):
   '''A Group can be initialized with a list of Paths.'''
   t = Group([Path([(1, 2), (3, 4)])])
   assert len(t) == 1
   assert t[0] == Path([(1, 2), (3, 4)])


def test_shapes_group__init__04( ):
   '''A Group can be initialized with another Group.'''
   t = Group([Group([ ]), Path([(1, 2), (3, 4)])])
   assert len(t) == 2
   assert t[0] == Group([ ])
   assert t[1] == Path([(1, 2), (3, 4)])


def test_shapes_group__init__05( ):
   '''A Group cannot be initialized with a non-_Shape.'''
   assert py.test.raises(TypeError, 'Group([1, 2, 3])')
   assert py.test.raises(TypeError, 'Group("a")')
   assert py.test.raises(TypeError, 'Group(0)')
  

