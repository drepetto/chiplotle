from chiplotle import *
from py.test import raises

def test_coordinate__add__01( ):
   '''Two Coordinates can be added.'''
   a = Coordinate(1, 2)
   b = Coordinate(3, 4)
   t = a + b
   assert isinstance(t, Coordinate)
   assert t is not a
   assert t is not b
   assert t == Coordinate(4, 6)


def test_coordinate__add__02( ):
   '''A Coordinate and an int scalar cannot be added.'''
   a = Coordinate(1, 2)
   assert raises(TypeError, 't = a + 4')


def test_coordinate__radd__02( ):
   '''An int scalar and a  Coordinate cannot be added.'''
   a = Coordinate(1, 2)
   assert raises(TypeError, 't = 4 + a')


def test_coordinate__add__03( ):
   '''A Coordinate and a float scalar cannot be added.'''
   a = Coordinate(1, 2)
   assert raises(TypeError, 't = a + 4.2')


def test_coordinate__radd__03( ):
   '''A float scalar and a Coordinate can be added.'''
   a = Coordinate(1, 2)
   assert raises(TypeError, 't = 4.2 + a')


def test_coordinate__add__04( ):
   '''A Coordinate and a tuple pair cannot be added.'''
   a = Coordinate(1, 2)
   assert raises(TypeError, 'a + (3, 4)')


def test_coordinate__radd__04( ):
   '''A tuple pair and a Coordinate cannot be added.'''
   a = Coordinate(1, 2)
   assert raises(TypeError, '(3, 4) + a')


def test_coordinate__add__05( ):
   '''A Coordinate and a CoordinateArray can be added.'''
   a = Coordinate(1, 2)
   b = CoordinateArray([(3, 4), (5, 6)])
   t = a + b
   assert isinstance(t, CoordinateArray)
   assert t[0] == Coordinate(4, 6)
   assert t[1] == Coordinate(6, 8)


def test_coordinate__radd__05( ):
   '''A CoordinateArray and a Coordinate can be added.'''
   a = Coordinate(1, 2)
   b = CoordinateArray([(3, 4), (5, 6)])
   t = b + a
   assert isinstance(t, CoordinateArray)
   assert t[0] == Coordinate(4, 6)
   assert t[1] == Coordinate(6, 8)


def test_coordinate__add__06( ):
   '''A 2D Coordinate and a triple cannot be added.'''
   a = Coordinate(1, 2)
   b = (3, 4, 5)
   assert raises(TypeError, 'a + b')

def test_coordinate__radd__06( ):
   '''A triple and a 2D Coordinate cannot be added.'''
   a = Coordinate(1, 2)
   b = (3, 4, 5)
   assert raises(TypeError, 'b + a')


