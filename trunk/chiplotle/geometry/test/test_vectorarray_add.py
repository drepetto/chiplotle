from chiplotle import *
from py.test import raises


def test_coordinatearray__add__01( ):
   '''Two VectorArrays of the same size can be added.'''
   a = VectorArray([(1, 2), (3, 4)])
   b = VectorArray([(1, 1), (2, 2)])
   t = a + b
   assert isinstance(t, VectorArray)
   assert t is not a
   assert t is not b
   assert t == VectorArray([(2, 3), (5, 6)])


def test_coordinatearray__add__02( ):
   '''Two VectorArrays of different length cannot be added.'''
   a = VectorArray([(1, 2), (3, 4)])
   b = VectorArray([(1, 1), (2, 2), (3, 3)])
   assert raises(errors.OperandError, 't = a + b')


def test_coordinatearray__add__03( ):
   '''A VectorArray and an int can be added.'''
   a = VectorArray([(1, 2), (3, 4)])
   t = a + 2
   assert isinstance(t, VectorArray)
   assert t is not a
   assert t == VectorArray([(3, 4), (5, 6)])


def test_coordinatearray__radd__04( ):
   '''An int and a VectorArray can be added.'''
   a = VectorArray([(1, 2), (3, 4)])
   t = 2 + a
   assert isinstance(t, VectorArray)
   assert t is not a
   assert t == VectorArray([(3, 4), (5, 6)])


def test_coordinatearray__add__05( ):
   '''A VectorArray and a float can be added.'''
   a = VectorArray([(1, 2), (3, 4)])
   t = a + 2.3
   assert isinstance(t, VectorArray)
   assert t is not a
   assert t == VectorArray([(3.3, 4.3), (5.3, 6.3)])


def test_coordinatearray__add__06( ):
   '''A float and a VectorArray can be added.'''
   a = VectorArray([(1, 2), (3, 4)])
   t = 2.3 + a
   assert isinstance(t, VectorArray)
   assert t is not a
   assert t == VectorArray([(3.3, 4.3), (5.3, 6.3)])


def test_coordinatearray__add__07( ):
   '''A VectorArray and a Vector can be added.'''
   a = VectorArray([(1, 2), (3, 4)])
   t = a + Vector(2, 3)
   assert isinstance(t, VectorArray)
   assert t is not a
   assert t == VectorArray([(3, 5), (5, 7)])


def test_coordinatearray__radd__08( ):
   '''A Vector and a VectorArray can be added.'''
   a = VectorArray([(1, 2), (3, 4)])
   t = Vector(2, 3) + a
   assert isinstance(t, VectorArray)
   assert t is not a
   assert t == VectorArray([(3, 5), (5, 7)])

