from chiplotle import *
from py.test import raises

def test_coordinatearray__init__01( ):
   '''CoordinateArray can be empty.'''
   t = CoordinateArray( )
   assert isinstance(t.xy, list)
   assert isinstance(t.x, tuple)
   assert isinstance(t.y, tuple)
   for e in t:
      assert isinstance(e, Coordinate)


def test_coordinatearray__init__02( ):
   '''CoordinateArray can initialize with a flat list of numbers.'''
   t = CoordinateArray([1, 2, 3, 4])
   assert isinstance(t.xy, list)
   for e in t:
      assert isinstance(e, Coordinate)
   assert t.xy == [(1, 2), (3, 4)]


def test_coordinatearray__init__03( ):
   '''CoordinateArray can take a list of tuple pairs.'''
   t = CoordinateArray([(1, 2), (3, 4), (5, 6)])
   assert t.xy == [(1, 2), (3, 4), (5, 6)]
   for e in t:
      assert isinstance(e, Coordinate)


def test_coordinatearray__init__04( ):
   '''A flat list must have an even number of elements.'''
   assert raises(ValueError, 't = CoordinateArray([1, 2, 3, 4, 5])')


## iadd ##

def test_coordinatearray__iadd__01( ):
   '''In place addition with another CoordinateArray works.'''
   t = CoordinateArray([(1, 2), (3, 4)])
   b = CoordinateArray([(1, 1), (1, 1)])
   tid = id(t)
   t += b

   assert isinstance(t, CoordinateArray)
   assert t is not b
   assert id(t) != tid
   assert t == [(2, 3), (4, 5)]


def test_coordinatearray__iadd__02( ):
   '''In place addition with a scalar.'''
   t = CoordinateArray([(1, 2), (3, 4)])
   tid = id(t)
   b = 1

   t += b

   assert isinstance(t, CoordinateArray)
   assert id(t) != tid
   assert t == [(2, 3), (4, 5)]


## radd ##

def test_coordinatearray__radd__01( ):
   '''A scalar and a CoordinateArray can be added.'''
   a = CoordinateArray([(1, 2), (3, 4)])
   b = 2

   t = b + a

   assert isinstance(t, CoordinateArray)
   assert t is not a
   assert t == [(3, 4), (5, 6)]


## div ##

#def test_coordinatearray__div__01( ):
#   '''Two CoordinateArrays can be divided.'''
#   a = CoordinateArray([(1, 2), (3, 4)])
#   b = CoordinateArray([(2., 2), (2, 2)])
#
#   t = a / b
#
#   assert isinstance(t, CoordinateArray)
#   assert t == [(.5, 1), (3/2., 2)]


def test_coordinatearray__div__02( ):
   '''A CoordinateArray can be divided by a scalar.'''
   a = CoordinateArray([(1., 2), (4, 8)])
   b = 2

   t = a / b

   assert isinstance(t, CoordinateArray)
   assert t == [(.5, 1), (2, 4)]


## rdiv ##

#def test_coordinatearray__rdiv__01( ):
#   '''A scalar can be divided by a CoordinateArray.'''
#   a = CoordinateArray([(1, 2), (4, 8)])
#   b = 2.
#
#   t = b / a
#
#   assert isinstance(t, CoordinateArray)
#   assert t == [(2, 1), (0.5, 0.25)]


## idiv ##

#def test_coordinatearray__idiv__01( ):
#   '''In place division with another CoordinateArray works.'''
#   t = CoordinateArray([(1., 2), (4, 8)])
#   b = CoordinateArray([(2, 2), (4, 4)])
#
#   t /= b
#
#   assert isinstance(t, CoordinateArray)
#   assert t == [(0.5, 1), (1, 2)]


def test_coordinatearray__idiv__02( ):
   '''In place division with another CoordinateArray works.'''
   t = CoordinateArray([(1., 2), (4, 8)])
   tid = id(t)
   b = 2

   t /= b

   assert isinstance(t, CoordinateArray)
   assert id(t) != tid
   assert t == [(0.5, 1), (2, 4)]


## eq / ne ##

def test_coordinatearray__eq__01( ):
   '''Equality between two CoordinateArrays works.''' 
   a = CoordinateArray([(1, 2), (4, 8)])
   b = CoordinateArray([(1, 2), (4, 8)])
   c = CoordinateArray([(1, 3), (2, 2)])

   assert a == b
   assert a != c


def test_coordinatearray__eq__02( ):
   '''Equality between one CoordinateArrays and a list works.''' 
   a = CoordinateArray([(1, 2), (4, 8)])
   b = [(1, 2), (4, 8)]
   c = [(1, 3), (2, 2)]

   assert a == b
   assert a != c


def test_coordinatearray__eq__03( ):
   '''Equality between a list and one CoordinateArrays works.''' 
   a = CoordinateArray([(1, 2), (4, 8)])
   b = [(1, 2), (4, 8)]
   c = [(1, 3), (2, 2)]

   assert b == a
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
