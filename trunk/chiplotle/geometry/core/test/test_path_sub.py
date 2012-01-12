from chiplotle.geometry.core.path import Path
from chiplotle.geometry.core.coordinate import Coordinate
from py.test import raises

def test_path_sub_01( ):
   '''A Path cannot substract an int.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(TypeError, 't = a - 2')


def test_path_sub_02( ):
   '''A Path cannot substract a float.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(TypeError, 't = a - 2.5')


def test_path_rsub_02( ):
   '''A float cannot substract a Path.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(TypeError, 't = 2.5 - a')


def test_path_sub_03( ):
   '''A Path can substract a Coordinate.'''
   a = Path([(1, 2), (3, 4)])
   t = a - Coordinate(1, 2)
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(0, 0), (2, 2)])


def test_path_rsub_03( ):
   '''A Coordinate can substract a Path.'''
   a = Path([(1, 2), (3, 4)])
   t = Coordinate(1, 2) - a
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(0, 0), (-2, -2)])


def test_path_sub_04( ):
   '''A Path cannot substract a duple.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(TypeError, 'a - (1, 2)')


def test_path_rsub_04( ):
   '''A duple cannot substract a Path.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(TypeError, '(1, 2) - a')


def test_path_sub_05( ):
   '''A Path cannot substract a triple.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(TypeError, 'a - (1, 2, 3)')


def test_path_sub_06( ):
   '''Two paths cannot be substracted.'''
   a = Path([(1, 2), (3, 4)])
   b = Path([(2, 3)])
   assert raises(TypeError, 'a - b')


## in place addition __isub__ ##

def test_path_isub_01( ):
   '''A float cannot be substracted from a Path in place.'''
   t = Path([(1, 2), (3, 4)])
   assert raises(TypeError, 't -= 2.5')
