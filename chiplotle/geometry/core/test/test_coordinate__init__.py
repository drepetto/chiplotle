from chiplotle import *
from py.test import raises

## __init__ ##

def test_coordinate__init__01( ):
   '''Coordinate can be initialized with two values.'''
   t = Coordinate(1, 2)
   assert t == Coordinate(1, 2)
   assert t.x == 1
   assert t.y == 2


def test_coordinate__init__02( ):
   '''Coordinate cannot be initialized with a duple.'''
   assert raises(TypeError, 'Coordinate((1, 2))')


def test_coordinate__init__03( ):
   '''Coordinate cannot be initialized with a Coordinate.'''
   ##In this case, the constructor returns the existing coordinate.'''
   a = Coordinate(1, 2)
   assert raises(TypeError, 't = Coordinate(a)')


def test_coordinate__init__04( ):
   '''Two Coordinates have different ids.'''
   a = Coordinate(1, 2)
   b = Coordinate(1, 2)
   assert a is not b


def test_coordinate__init__05( ):
   '''Coordinate can be initialized with a single number.'''
   a = Coordinate(1)
   assert a._coords == [1]

def test_coordinate__init__06( ):
   '''Coordinate cannot be initialized with a triple.'''
   assert raises(TypeError, 't = Coordinate((1, 2, 3))')


def test_coordinate__init__07( ):
   '''Coordinate cannot be initialized with a Path.'''
   assert raises(TypeError, 't = Coordinate(Path([1,2]))')


## attribute assignment ##

def test_coordinate_attribute_assignment_01( ):
   '''Coordinates are immutable.
   Attributes cannot be set (rebound).'''
   t = Coordinate(1, 2)
   assert raises(AttributeError, 't.xy = 2')
   assert raises(AttributeError, 't.foo = 3')
   assert raises(TypeError, 't[0] = 2')


## __eq__ ##

def test_coordinate__eq__01( ):
   '''Coordinate equates with another Coordinate.'''
   t = Coordinate(1, 2)
   assert t == Coordinate(1, 2)
   assert Coordinate(1, 2) == t


def test_coordinate__eq__02( ):
   '''Coordinate does not equate with a list or tuple.'''
   t = Coordinate(1, 2)
   assert not (t == (1, 2))
   assert not ((1, 2) == t)
   assert not (t == [1, 2])
   assert not ([1, 2] == t)


def test_coordinate__eq__03( ):
   '''Coordinate __eq__ works with None.'''
   t = Coordinate(1, 2)
   assert not (t == None)


## __ne__ ##

def test_coordinate__ne__01( ):
   '''Coordinate non-equates with another Coordinate, a tuple, 
   or a list.'''
   t = Coordinate(1, 2)
   assert t != Coordinate(1, 3)
   assert t != (1, 3)
   assert t != [1, 3]


def test_coordinate__ne__02( ):
   '''Coordinate non-equates with int, float.'''
   t = Coordinate(1, 2)
   assert t != 4.5
   assert t != 2
   assert t != None



## div ##

def test_coordinate__div__01( ):
   '''True division works without __future__.division imported.'''
   a = Coordinate(1, 2)
   t = a / 2
   assert isinstance(t, Coordinate)
   assert t == Coordinate(.5, 1)

def test_coordinate__div__02( ):
   '''Denominator 0 raises ZeroDivisionError.'''
   a = Coordinate(1, 2)
   assert raises(ZeroDivisionError, 't = a / 0')
   

def test_coordinate__div__03( ):
   '''A Coordinate cannot be divided by a Coordinate.'''
   a = Coordinate(1, 2)
   b = Coordinate(2, 4)
   assert raises(TypeError, 't = a / b')


def test_coordinate__div__04( ):
   '''A Coordinate cannot be divided by a duple.'''
   a = Coordinate(1, 2)
   b = (2, 4)
   assert raises(TypeError, 'a / b')


def test_coordinate__div__05( ):
   '''Division raises an Error on wrong type.'''
   a = Coordinate(1, 2)
   assert raises(TypeError, 'a / (1, 2, 3)')


def test_coordinate__floordiv__01( ):
   '''Floor division works with ints.'''
   a = Coordinate(1, 2)
   t = a // 2
   assert isinstance(t, Coordinate)
   assert t == Coordinate(0, 1)


def test_coordinate__floordiv__02( ):
   '''Floor division does not work with two Coordinates.'''
   a = Coordinate(1, 2)
   b = Coordinate(2, -4)
   assert raises(TypeError, 't = a // b')


def test_coordinate__floordiv__03( ):
   '''Denominator 0 raises ZeroDivisionError.'''
   a = Coordinate(1, 2)
   assert raises(ZeroDivisionError, 't = a // 0')
   

def test_coordinate__floordiv__04( ):
   '''Floor Division raises an OperandError on wrong type.'''
   a = Coordinate(1, 2)
   assert raises(TypeError, 'a // (1, 2, 3)')


## __hash__ ##

def test_coordinate__hash__01( ):
   t = set([Coordinate(1, 2), Coordinate(1, 2)])
   assert len(t) == 1


## __invert__ ##

def test_coordinate__invert__01( ):
   t = Coordinate(1, 2)
   assert ~t == Coordinate(-2, 1)
   t = Coordinate(0, 0)
   assert ~t == Coordinate(0, 0)
   


## __getitem__ ##

def test_coordinate__getitem__01( ):
   t = Coordinate(1, 2)
   assert t[0] == 1
   assert t[1] == 2
   assert raises(IndexError, 't[3]')

## __len__ ##

def test_coordinate__len__01( ):
   t = Coordinate(1, 2)
   assert len(t) == 2

## __iter__ ##

def test_coordinate__iter__01( ):
   t = Coordinate(1, 2)
   t = list(t)
   assert isinstance(t, list)
   assert t == [1, 2]

## __abs__ ##

def test_coordinate__abs__01( ):
   t = Coordinate(1, 2)
   assert abs(t) == Coordinate(1, 2)
   t = Coordinate(-1, 2)
   assert abs(t) == Coordinate(1, 2)
   t = Coordinate(-1, -2)
   assert abs(t) == Coordinate(1, 2)


## __neg__ ##

def test_coordinate__neg__01( ):
   t = Coordinate(1, 2)
   assert -t == Coordinate(-1, -2)
   t = Coordinate(-1, 2)
   assert -t == Coordinate(1, -2)
   t = Coordinate(-1, -2)
   assert -t == Coordinate(1, 2)


## polar ##
import math

def test_coordinate_polar_01( ):
   t = Coordinate(1, 0)
   assert isinstance(t.polar, tuple)
   assert len(t.polar) == 2
   assert t.polar[0] == 1
   assert t.polar[1] == 0


def test_coordinate_polar_02( ):
   t = Coordinate(0, 1)
   assert t.polar[0] == 1
   assert round(t.polar[1], 2) == round(math.pi / 2., 2)


