from chiplotle.geometry.core.path import Path
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.core import errors
from py.test import raises

def test_path_add_01( ):
   '''A Path and an int cannot be added.'''
   assert raises(TypeError, 'Path([(1, 2), (3, 4)]) + 3')


def test_path_add_02( ):
   '''A Path and a float cannot be added.'''
   assert raises(TypeError, 'Path([(1, 2), (3, 4)]) + 3.2')


def test_path_radd_02( ):
   '''A float and a Path cannot be added.'''
   assert raises(TypeError, '3.2 + Path([(1, 2), (3, 4)])')


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
   '''A Path and a duple cannot be added.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(TypeError, 'a + (1, 2)')


def test_path_radd_04( ):
   '''A duple and a Path cannot be added.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(TypeError, '(1, 2) + a')


def test_path_add_05( ):
   '''A 2D Path and a triple cannot be added.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(TypeError, 'a + (1, 2, 3)')


def test_path_add_06( ):
   '''A Path and a Path cannot be added.'''
   a = Path([(1, 2), (3, 4)])
   b = Path([(2, 3)])
   assert raises(TypeError, 'a + b')


## in place addition __iadd__ ##

def test_path_iadd_01( ):
   '''A float and a Path cannot be added.'''
   t = Path([(1, 2), (3, 4)])
   assert raises(TypeError, 't += 3.2')


