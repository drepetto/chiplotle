from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.vector import Vector
from chiplotle.geometry.vectorarray import VectorArray
from py.test import raises

def test_path__setitem__01( ):
   '''A tuple (x, y) cannot be set in a path by list-like indexation.'''
   t = Path([(1, 2), (3, 4)])
   assert raises(TypeError, 't[1] = (0, 0)')


def test_path__setitem__02( ):
   '''A Vector can be set in a path by list-like indexation.'''
   t = Path([(1, 2), (3, 4)])
   t[1] = Vector(0, 0)
   assert len(t) == 2
   assert t[0] == Vector(1, 2)
   assert t[1] == Vector(0, 0)
   assert isinstance(t[1], Vector)


def test_path__setitem__03( ):
   '''A list of coordinates can be set in a path by list-like indexation.'''
   t = Path([(1, 2), (3, 4), (5, 6), (7, 8)])
   t[1:2] = [Vector(0, 0), Vector(1, 1)]
   assert len(t) == 5
   assert t[0] == Vector(1, 2)
   assert t[1] == Vector(0, 0)
   assert t[2] == Vector(1, 1)
   assert t[3] == Vector(5, 6)
   assert t[4] == Vector(7, 8)
   for p in t:
      assert isinstance(p, Vector)


def test_path__setitem__04( ):
   '''A VectorArray can be set in a path by list-like indexation.'''
   t = Path([(1, 2), (3, 4), (5, 6), (7, 8)])
   t[1:2] = VectorArray([(0, 0), (1, 1)])
   assert len(t) == 5
   assert t[0] == Vector(1, 2)
   assert t[1] == Vector(0, 0)
   assert t[2] == Vector(1, 1)
   assert t[3] == Vector(5, 6)
   assert t[4] == Vector(7, 8)
   for p in t:
      assert isinstance(p, Vector)
