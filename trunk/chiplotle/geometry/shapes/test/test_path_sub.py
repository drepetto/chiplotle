from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.vector import Vector
from chiplotle.core import errors
from py.test import raises

def test_path_sub_01( ):
   '''A Path can substract an int.
   The operation returns a new instance (copy) of Path.'''
   a = Path([(1, 2), (3, 4)])
   t = a - 2
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(-1, 0), (1, 2)])


def test_path_sub_02( ):
   '''A Path can substract a float.'''
   a = Path([(1, 2), (3, 4)])
   t = a - 2.5
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(-1.5, -0.5), (0.5, 1.5)])


def test_path_rsub_02( ):
   '''A float can substract a Path.'''
   a = Path([(1, 2), (3, 4)])
   t = 2.5 - a
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(1.5, 0.5), (-0.5, -1.5)])


def test_path_sub_03( ):
   '''A Path can substract a Vector.'''
   a = Path([(1, 2), (3, 4)])
   t = a - Vector(1, 2)
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(0, 0), (2, 2)])


def test_path_rsub_03( ):
   '''A Vector can substract a Path.'''
   a = Path([(1, 2), (3, 4)])
   t = Vector(1, 2) - a
   assert t is not a
   assert isinstance(t, Path)
   assert t == Path([(0, 0), (-2, -2)])


def test_path_sub_04( ):
   '''A Path cannot substract a duple.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(errors.OperandError, 'a - (1, 2)')


def test_path_rsub_04( ):
   '''A duple cannot substract a Path.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(errors.OperandError, '(1, 2) - a')


def test_path_sub_05( ):
   '''A Path cannot substract a triple.'''
   a = Path([(1, 2), (3, 4)])
   assert raises(errors.OperandError, 'a - (1, 2, 3)')


def test_path_sub_06( ):
   '''Two paths cannot be substracted.'''
   a = Path([(1, 2), (3, 4)])
   b = Path([(2, 3)])
   assert raises(errors.OperandError, 'a - b')


## in place addition __isub__ ##

def test_path_isub_01( ):
   '''A float can be substracted from a Path in place.'''
   t = Path([(1, 2), (3, 4)])
   t -= 2.5
   assert isinstance(t, Path)
   assert t == Path([(-1.5, -0.5), (0.5, 1.5)])



