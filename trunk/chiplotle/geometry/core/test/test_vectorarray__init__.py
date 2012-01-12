from chiplotle import *
from py.test import raises

def test_coordinatearray__init__01( ):
   '''CoordinateArray can be empty.'''
   t = CoordinateArray( )
   assert isinstance(t.coords, list)
   assert isinstance(t.x, tuple)
   assert isinstance(t.y, tuple)
   for e in t:
      assert isinstance(e, Coordinate)


def test_coordinatearray__init__03( ):
   '''CoordinateArray can take a list of tuple pairs.'''
   t = CoordinateArray([(1, 2), (3, 4), (5, 6)])
   assert t[:] == [Coordinate(1, 2), Coordinate(3, 4), Coordinate(5, 6)]
   for e in t:
      assert isinstance(e, Coordinate)


## iadd ##

def test_coordinatearray__iadd__01( ):
   '''In place addition with another CoordinateArray works.'''
   t = CoordinateArray([(1, 2), (3, 4)])
   b = CoordinateArray([(1, 1), (1, 1)])
   tid = id(t)
   t += b
   assert isinstance(t, CoordinateArray)
   assert t is not b
   assert id(t) == tid
   assert t[:] == [Coordinate(2, 3), Coordinate(4, 5)]


def test_coordinatearray__iadd__02( ):
   '''In place addition with a scalar raises.'''
   t = CoordinateArray([(1, 2), (3, 4)])
   tid = id(t)
   b = 1
   assert raises(TypeError, 't += b')


## div ##

#def test_coordinatearray__div__01( ):
#   '''Two CoordinateArrays can be divided.'''
#   a = CoordinateArray([(1, 2), (3, 4)])
#   b = CoordinateArray([(2., 2), (2, 2)])
#
#   t = a / b
#
#   assert isinstance(t, CoordinateArray)
#   assert t.xy == [(.5, 1), (3/2., 2)]


def test_coordinatearray__div__02( ):
   '''A CoordinateArray can be divided by a scalar.'''
   a = CoordinateArray([(1., 2), (4, 8)])
   b = 2

   t = a / b

   assert isinstance(t, CoordinateArray)
   assert t[:] == [Coordinate(.5, 1), Coordinate(2, 4)]


## rdiv ##

## idiv ##

def test_coordinatearray__idiv__02( ):
   '''In place division with another CoordinateArray works.'''
   t = CoordinateArray([(1., 2), (4, 8)])
   tid = id(t)
   b = 2
   t /= b
   assert isinstance(t, CoordinateArray)
   assert id(t) == tid
   assert t[:] == [Coordinate(0.5, 1), Coordinate(2, 4)]


## eq / ne ##

def test_coordinatearray__eq__01( ):
   '''Equality between two CoordinateArrays works.''' 
   a = CoordinateArray([(1, 2), (4, 8)])
   b = CoordinateArray([(1, 2), (4, 8)])
   c = CoordinateArray([(1, 3), (2, 2)])
   assert a == b
   assert a != c


def test_coordinatearray__eq__02( ):
   '''Equality between one CoordinateArray and a list is always false.''' 
   a = CoordinateArray([(1, 2), (4, 8)])
   b = [(1, 2), (4, 8)]
   c = [(1, 3), (2, 2)]
   assert a != b
   assert a != c


def test_coordinatearray__eq__03( ):
   '''Equality between a list and a CoordinateArray is always false.''' 
   a = CoordinateArray([(1, 2), (4, 8)])
   b = [(1, 2), (4, 8)]
   c = [(1, 3), (2, 2)]
   assert b != a
   assert c != a


## __invert__ ##

def test_coordinatearray__invert__01( ):
   t = CoordinateArray([(1, 2), (3, 4)])
   assert ~t == CoordinateArray([(-2, 1), (-4, 3)])


## __neg__ ##

def test_coordinatearray__neg__01( ):
   t = CoordinateArray([(1, 2), (-3, 4)])
   assert -t == CoordinateArray([(-1, -2), (3, -4)])
 
## TODO: pending
## sub ##
## mul ##
## pow ##
