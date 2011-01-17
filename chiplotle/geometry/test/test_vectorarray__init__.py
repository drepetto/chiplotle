from chiplotle import *
from py.test import raises

def test_coordinatearray__init__01( ):
   '''VectorArray can be empty.'''
   t = VectorArray( )
   assert isinstance(t.xy, list)
   assert isinstance(t.x, tuple)
   assert isinstance(t.y, tuple)
   for e in t:
      assert isinstance(e, Vector)


def test_coordinatearray__init__02( ):
   '''VectorArray can initialize with a flat list of numbers.'''
   t = VectorArray([1, 2, 3, 4])
   assert isinstance(t.xy, list)
   for e in t:
      assert isinstance(e, Vector)
   assert t.xy == [Vector(1, 2), Vector(3, 4)]


def test_coordinatearray__init__03( ):
   '''VectorArray can take a list of tuple pairs.'''
   t = VectorArray([(1, 2), (3, 4), (5, 6)])
   assert t.xy == [Vector(1, 2), Vector(3, 4), Vector(5, 6)]
   for e in t:
      assert isinstance(e, Vector)


def test_coordinatearray__init__04( ):
   '''A flat list must have an even number of elements.'''
   assert raises(errors.InitParameterError, 't = VectorArray([1, 2, 3, 4, 5])')


## iadd ##

def test_coordinatearray__iadd__01( ):
   '''In place addition with another VectorArray works.'''
   t = VectorArray([(1, 2), (3, 4)])
   b = VectorArray([(1, 1), (1, 1)])
   tid = id(t)
   t += b
   assert isinstance(t, VectorArray)
   assert t is not b
   assert id(t) == tid
   assert t.xy == [Vector(2, 3), Vector(4, 5)]


def test_coordinatearray__iadd__02( ):
   '''In place addition with a scalar.'''
   t = VectorArray([(1, 2), (3, 4)])
   tid = id(t)
   b = 1
   t += b
   assert isinstance(t, VectorArray)
   assert id(t) == tid
   assert t.xy == [Vector(2, 3), Vector(4, 5)]


## radd ##

def test_coordinatearray__radd__01( ):
   '''A scalar and a VectorArray can be added.'''
   a = VectorArray([(1, 2), (3, 4)])
   b = 2

   t = b + a

   assert isinstance(t, VectorArray)
   assert t is not a
   assert t.xy == [Vector(3, 4), Vector(5, 6)]


## div ##

#def test_coordinatearray__div__01( ):
#   '''Two VectorArrays can be divided.'''
#   a = VectorArray([(1, 2), (3, 4)])
#   b = VectorArray([(2., 2), (2, 2)])
#
#   t = a / b
#
#   assert isinstance(t, VectorArray)
#   assert t.xy == [(.5, 1), (3/2., 2)]


def test_coordinatearray__div__02( ):
   '''A VectorArray can be divided by a scalar.'''
   a = VectorArray([(1., 2), (4, 8)])
   b = 2

   t = a / b

   assert isinstance(t, VectorArray)
   assert t.xy == [Vector(.5, 1), Vector(2, 4)]


## rdiv ##

#def test_coordinatearray__rdiv__01( ):
#   '''A scalar can be divided by a VectorArray.'''
#   a = VectorArray([(1, 2), (4, 8)])
#   b = 2.
#
#   t = b / a
#
#   assert isinstance(t, VectorArray)
#   assert t.xy == [(2, 1), (0.5, 0.25)]


## idiv ##

#def test_coordinatearray__idiv__01( ):
#   '''In place division with another VectorArray works.'''
#   t = VectorArray([(1., 2), (4, 8)])
#   b = VectorArray([(2, 2), (4, 4)])
#
#   t /= b
#
#   assert isinstance(t, VectorArray)
#   assert t.xy == [(0.5, 1), (1, 2)]


def test_coordinatearray__idiv__02( ):
   '''In place division with another VectorArray works.'''
   t = VectorArray([(1., 2), (4, 8)])
   tid = id(t)
   b = 2
   t /= b
   assert isinstance(t, VectorArray)
   assert id(t) == tid
   assert t.xy == [Vector(0.5, 1), Vector(2, 4)]


## eq / ne ##

def test_coordinatearray__eq__01( ):
   '''Equality between two VectorArrays works.''' 
   a = VectorArray([(1, 2), (4, 8)])
   b = VectorArray([(1, 2), (4, 8)])
   c = VectorArray([(1, 3), (2, 2)])
   assert a == b
   assert a != c


def test_coordinatearray__eq__02( ):
   '''Equality between one VectorArray and a list is always false.''' 
   a = VectorArray([(1, 2), (4, 8)])
   b = [(1, 2), (4, 8)]
   c = [(1, 3), (2, 2)]
   assert a != b
   assert a != c


def test_coordinatearray__eq__03( ):
   '''Equality between a list and a VectorArray is always false.''' 
   a = VectorArray([(1, 2), (4, 8)])
   b = [(1, 2), (4, 8)]
   c = [(1, 3), (2, 2)]
   assert b != a
   assert c != a


## __invert__ ##

def test_coordinatearray__invert__01( ):
   t = VectorArray([(1, 2), (3, 4)])
   assert ~t == VectorArray([(-2, 1), (-4, 3)])


## __neg__ ##

def test_coordinatearray__neg__01( ):
   t = VectorArray([(1, 2), (-3, 4)])
   assert -t == VectorArray([(-1, -2), (3, -4)])
 
## TODO: pending
## sub ##
## mul ##
## pow ##
