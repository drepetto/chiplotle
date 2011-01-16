from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.coordinate import Coordinate

def test_path_add_01( ):
   '''A Path and an int can be added.
   The operation returns a new instance (copy) of Path.'''
   a = Path([(1, 2), (3, 4)])
   t = a + 2
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(3, 4), (5, 6)])


def test_path_add_02( ):
   '''A Path and a float can be added.'''
   a = Path([(1, 2), (3, 4)])
   t = a + 2.1
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(3.1, 4.1), (5.1, 6.1)])


def test_path_radd_02( ):
   '''A float and a Path can be added.'''
   a = Path([(1, 2), (3, 4)])
   t = 2.1 + a
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(3.1, 4.1), (5.1, 6.1)])


def test_path_add_03( ):
   '''A Path and a Coordinate can be added.'''
   a = Path([(1, 2), (3, 4)])
   t = a + Coordinate(1, 2)
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(2, 4), (4, 6)])


def test_path_radd_03( ):
   '''A Coordinate and a Path can be added.'''
   a = Path([(1, 2), (3, 4)])
   t = Coordinate(1, 2) + a
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(2, 4), (4, 6)])


def test_path_add_04( ):
   '''A Path and a duple can be added.'''
   a = Path([(1, 2), (3, 4)])
   t = a + (1, 2)
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(2, 4), (4, 6)])


def test_path_radd_04( ):
   '''A duple and a Path can be added.'''
   a = Path([(1, 2), (3, 4)])
   t = (1, 2) + a
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(2, 4), (4, 6)])


## in place addition __iadd__ ##

def test_path_iadd_01( ):
   '''A float and a Path can be added.'''
   t = Path([(1, 2), (3, 4)])
   t += 2.1
   assert isinstance(t, Path)
   assert t == Path([(3.1, 4.1), (5.1, 6.1)])





