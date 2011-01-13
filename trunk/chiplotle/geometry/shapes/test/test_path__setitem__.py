from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.geometry.coordinatearray import CoordinateArray

def test_path__setitem__01( ):
   '''A tuple (x, y) (point) can be set in a path by list-like indexation.'''
   t = Path([(1, 2), (3, 4)])
   t[1] = (0, 0)
   assert len(t) == 2
   assert t[0] == (1, 2)
   assert t[1] == (0, 0)
   assert isinstance(t[1], Coordinate)


def test_path__setitem__02( ):
   '''A Coordinate can be set in a path by list-like indexation.'''
   t = Path([(1, 2), (3, 4)])
   t[1] = Coordinate(0, 0)
   assert len(t) == 2
   assert t[0] == (1, 2)
   assert t[1] == (0, 0)
   assert isinstance(t[1], Coordinate)


def test_path__setitem__03( ):
   '''A list of coordinates can be set in a path by list-like indexation.'''
   t = Path([(1, 2), (3, 4), (5, 6), (7, 8)])
   t[1:2] = [(0, 0), (1, 1)]
   assert len(t) == 5
   assert t[0] == (1, 2)
   assert t[1] == (0, 0)
   assert t[2] == (1, 1)
   assert t[3] == (5, 6)
   assert t[4] == (7, 8)
   for p in t:
      assert isinstance(p, Coordinate)


def test_path__setitem__04( ):
   '''A CoordinateArray can be set in a path by list-like indexation.'''
   t = Path([(1, 2), (3, 4), (5, 6), (7, 8)])
   t[1:2] = CoordinateArray([(0, 0), (1, 1)])
   assert len(t) == 5
   assert t[0] == (1, 2)
   assert t[1] == (0, 0)
   assert t[2] == (1, 1)
   assert t[3] == (5, 6)
   assert t[4] == (7, 8)
   for p in t:
      assert isinstance(p, Coordinate)
