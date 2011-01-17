from chiplotle import *
from py.test import raises

## __init__ ##

def test_coordinate__init__01( ):
   '''Coordinate can be initialized with two values.'''
   t = Coordinate(1, 2)
   assert t == (1, 2)
   assert t.x == 1
   assert t.y == 2


def test_coordinate__init__02( ):
   '''Coordinate can be initialized with a duple.'''
   t = Coordinate((1, 2))
   assert t == (1, 2)
   assert t.x == 1
   assert t.y == 2


#def test_coordinate__init__03( ):
#   '''Coordinate can be initialized with a Coordinate.
#   In this case, the constructor returns the existing coordinate.'''
#   a = Coordinate(1, 2)
#   t = Coordinate(a)
#   assert t is a
#   assert t == (1, 2)
#   assert t.x == 1
#   assert t.y == 2


def test_coordinate__init__04( ):
   '''Two Coordinates have different ids.'''
   a = Coordinate(1, 2)
   b = Coordinate(1, 2)
   assert a is not b


def test_coordinate__init__05( ):
   '''Coordinate cannot be initialized with a single number.'''
   assert raises(errors.InitParameterError, 't = Coordinate(4)')


## attribute assignment ##

def test_coordinate_attribute_assignment_01( ):
   '''Coordinates are immutable.
   Attributes cannot be set (rebound).'''
   t = Coordinate(1, 2)
   assert raises(AttributeError, 't.x = 2')
   assert raises(AttributeError, 't.y = 2')
   assert raises(AttributeError, 't.xy = 2')
   assert raises(AttributeError, 't.foo = 3')
   assert raises(TypeError, 't[0] = 2')


## __eq__ ##

def test_coordinate__eq__01( ):
   '''Coordinate equates with another Coordinate, a tuple, 
   or a list.'''
   t = Coordinate(1, 2)
   assert t == Coordinate(1, 2)
   assert Coordinate(1, 2) == t
   assert t == (1, 2)
   assert (1, 2) == t
   assert t == [1, 2]
   assert [1, 2] == t


def test_coordinate__eq__02( ):
   '''Coordinate __eq__ works with None.'''
   t = Coordinate(1, 2)
   assert not (t == None)


## __ne__ ##

def test_coordinate__ne__01( ):
   '''Coordinate non-equates with another Coordinate, a tuple, 
   or a list.'''
   t = Coordinate(Coordinate(1, 2))
   assert t != Coordinate(1, 3)
   assert t != (1, 3)
   assert t != [1, 3]


def test_coordinate__ne__02( ):
   '''Coordinate non-equates with int, float.'''
   t = Coordinate(Coordinate(1, 2))
   assert t != 4.5
   assert t != 2
   assert t != None


## __add__ ##

def test_coordinate__add__01( ):
   '''Two Coordinates can be added.'''
   a = Coordinate(1, 2)
   b = Coordinate(3, 4)
   t = a + b
   assert isinstance(t, Coordinate)
   assert t is not a
   assert t is not b
   assert t == (4, 6)


def test_coordinate__add__02( ):
   '''A Coordinate and an int scalar can be added.'''
   a = Coordinate(1, 2)
   t = a + 4
   assert isinstance(t, Coordinate)
   assert t is not a
   assert t == (5, 6)


def test_coordinate__radd__02( ):
   '''An int scalar and a  Coordinate can be added.'''
   a = Coordinate(1, 2)
   t = 4 + a
   assert isinstance(t, Coordinate)
   assert t is not a
   assert t == (5, 6)


def test_coordinate__add__03( ):
   '''A Coordinate and a float scalar can be added.'''
   a = Coordinate(1, 2)
   t = a + 4.2
   assert isinstance(t, Coordinate)
   assert t is not a
   assert t == (5.2, 6.2)


def test_coordinate__radd__03( ):
   '''A float scalar and a Coordinate scalar can be added.'''
   a = Coordinate(1, 2)
   t = 4.2 + a
   assert isinstance(t, Coordinate)
   assert t is not a
   assert t == (5.2, 6.2)


def test_coordinate__add__04( ):
   '''A Coordinate and a tuple pair can be added.'''
   a = Coordinate(1, 2)
   t = a + (3, 4)
   assert isinstance(t, Coordinate)
   assert t is not a
   assert t == (4, 6)


def test_coordinate__radd__04( ):
   '''A tuple pair and a Coordinate can be added.'''
   a = Coordinate(1, 2)
   t = (3, 4) + a
   assert isinstance(t, Coordinate)
   assert t is not a
   assert t == (4, 6)


def test_coordinate__add__05( ):
   '''A Coordinate and a CoordinateArray can be added.'''
   a = Coordinate(1, 2)
   b = CoordinateArray([(3, 4), (5, 6)])
   t = a + b
   assert isinstance(t, CoordinateArray)
   assert t[0] == (4, 6)
   assert t[1] == (6, 8)


def test_coordinate__radd__05( ):
   '''A CoordinateArray and a Coordinate can be added.'''
   a = Coordinate(1, 2)
   b = CoordinateArray([(3, 4), (5, 6)])
   t = b + a
   assert isinstance(t, CoordinateArray)
   assert t[0] == (4, 6)
   assert t[1] == (6, 8)


def test_coordinate__add__06( ):
   '''A Coordinate and a triple cannot be added.'''
   a = Coordinate(1, 2)
   b = (3, 4, 5)
   assert raises(errors.OperandError, 'a + b')

def test_coordinate__radd__06( ):
   '''A triple and a Coordinate cannot be added.'''
   a = Coordinate(1, 2)
   b = (3, 4, 5)
   assert raises(errors.OperandError, 'b + a')


## __mul__ ##

def test_coordinate__mul__01( ):
   '''A Coordinate can be multiplied with a scalar.'''
   a = Coordinate(1, 2)
   b = 2.5
   t = a * b
   assert isinstance(t, Coordinate)
   assert t is not a
   assert t == (2.5, 5)


def test_coordinate__mul__02( ):
   '''A Coordinate can be multiplied with a pair.'''
   a = Coordinate(2, 3)
   t = a * (2, 3)
   assert isinstance(t, Coordinate)
   assert t == (4, 9)


def test_coordinate__mul__03( ):
   '''A Coordinate can be multiplied with another Coordinate.'''
   a = Coordinate(2, 3)
   t = a * Coordinate(2, 3)
   assert isinstance(t, Coordinate)
   assert t == (4, 9)



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
   '''A Coordinate can be divided by a Coordinate.'''
   a = Coordinate(1, 2)
   b = Coordinate(2, 4)
   t = a / b
   assert isinstance(t, Coordinate)
   assert t == (0.5, 0.5)


def test_coordinate__div__04( ):
   '''A Coordinate can be divided by a duple.'''
   a = Coordinate(1, 2)
   b = (2, 4)
   t = a / b
   assert isinstance(t, Coordinate)
   assert t == (0.5, 0.5)


def test_coordinate__div__05( ):
   '''Division raises an OperandError on wrong type.'''
   a = Coordinate(1, 2)
   assert raises(errors.OperandError, 'a / (1, 2, 3)')


def test_coordinate__floordiv__01( ):
   '''Floor division works with ints.'''
   a = Coordinate(1, 2)
   t = a // 2
   assert isinstance(t, Coordinate)
   assert t == Coordinate(0, 1)


def test_coordinate__floordiv__02( ):
   '''Floor division works with two Coordinates.'''
   a = Coordinate(1, 2)
   b = Coordinate(2, -4)
   t = a // b
   assert isinstance(t, Coordinate)
   assert t == Coordinate(0, -1)


def test_coordinate__floordiv__03( ):
   '''Denominator 0 raises ZeroDivisionError.'''
   a = Coordinate(1, 2)
   assert raises(ZeroDivisionError, 't = a // 0')
   

def test_coordinate__floordiv__04( ):
   '''Floor Division raises an OperandError on wrong type.'''
   a = Coordinate(1, 2)
   assert raises(errors.OperandError, 'a // (1, 2, 3)')


## __sub__, __rsub__ ##

def test_coordinate__sub__01( ):
   '''Coordinate pair can substract with other coordinate pairs.'''
   a = Coordinate(1, 2)
   b = Coordinate(0.5, 0.5)
   t = a - b
   assert isinstance(t, Coordinate)
   assert t == Coordinate(0.5, 1.5)


def test_coordinate__sub__02( ):
   '''Coordinate pair can substract a tuple.'''
   a = Coordinate(1, 2)
   t = a - (0.5, 0.5)
   assert isinstance(t, Coordinate)
   assert t == Coordinate(0.5, 1.5)

def test_coordinate__rsub__02( ):
   '''A tuple can substract a Coordinate.'''
   a = Coordinate(1, 2)
   t = (0.5, 0.5) - a
   assert isinstance(t, Coordinate)
   assert t == Coordinate(-0.5, -1.5)


def test_coordinate__sub__03( ):
   '''An int can be substracted from a Coordinate.'''
   a = Coordinate(1, 2)
   t = a - 1
   assert isinstance(t, Coordinate)
   assert t == Coordinate(0, 1)

def test_coordinate__rsub__03( ):
   '''A Coordinate can be substracted from an int.'''
   a = Coordinate(1, 2)
   t = 1 - a
   assert isinstance(t, Coordinate)
   assert t == Coordinate(0, -1)


def test_coordinate__sub__04( ):
   '''An float can be substracted from a Coordinate.'''
   a = Coordinate(1, 2)
   t = a - 1.5
   assert isinstance(t, Coordinate)
   assert t == Coordinate(-0.5, 0.5)

def test_coordinate__rsub__04( ):
   '''A Coordinate can be substracted from a float.'''
   a = Coordinate(1, 2)
   t = 1.5 - a
   assert isinstance(t, Coordinate)
   assert t == Coordinate(0.5, -0.5)



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
   assert abs(t) == (1, 2)
   t = Coordinate(-1, 2)
   assert abs(t) == (1, 2)
   t = Coordinate(-1, -2)
   assert abs(t) == (1, 2)


## __neg__ ##

def test_coordinate__neg__01( ):
   t = Coordinate(1, 2)
   assert -t == (-1, -2)
   t = Coordinate(-1, 2)
   assert -t == (1, -2)
   t = Coordinate(-1, -2)
   assert -t == (1, 2)

