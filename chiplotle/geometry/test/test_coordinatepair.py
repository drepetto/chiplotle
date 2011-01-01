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


def test_coordinate__init__03( ):
   '''Coordinate can be initialized with a Coordinate.'''
   t = Coordinate(Coordinate(1, 2))
   assert t == (1, 2)
   assert t.x == 1
   assert t.y == 2


def test_coordinate__init__04( ):
   '''Coordinate cannot be initialized with a single number.'''
   assert raises(TypeError, 't = Coordinate(4)')


## __eq__ ##

def test_coordinate__eq__01( ):
   '''Coordinate equates with another Coordinate, a tuple, 
   or a list.'''
   t = Coordinate(1, 2)
   assert t == Coordinate(1, 2)
   assert t == (1, 2)
   assert t == [1, 2]


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
   '''Coordinate __ne__ works with None.'''
   t = Coordinate(1, 2)
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
   b = 4
   t = a + b

   assert isinstance(t, Coordinate)
   assert t is not a
   assert t == (5, 6)


def test_coordinate__add__03( ):
   '''A Coordinate and a float scalar can be added.'''
   a = Coordinate(1, 2)
   b = 4.2
   t = a + b

   assert isinstance(t, Coordinate)
   assert t is not a
   assert t == (5.2, 6.2)


def test_coordinate__add__04( ):
   '''A Coordinate and a tuple pair can be added.'''
   a = Coordinate(1, 2)
   b = (3, 4)
   t = a + b

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


def test_coordinate__add__06( ):
   '''A Coordinate and a triple cannot be added.'''
   a = Coordinate(1, 2)
   b = (3, 4, 5)
   assert raises(TypeError, 'a+b')


def test_coordinate__mul__01( ):
   '''A coordinatePair can be multiplied with a scalar.'''
   a = Coordinate(1, 2)
   b = 2.5
   t = a * b

   assert isinstance(t, Coordinate)
   assert t is not a
   assert t == (2.5, 5)


## div ##

def test_coordinate__div__01( ):
   '''True division works without __future__.division imported.'''
   a = Coordinate(1, 2)
   t = a / 2
   assert t == Coordinate(.5, 1)


def test_coordinate__floordiv__01( ):
   '''Floor division works.'''
   a = Coordinate(1, 2)
   t = a // 2
   assert t == Coordinate(0, 1)


## __sub__ ##

def test_coordinate__sub__01( ):
   '''Coordinate pair can substract with other coordinate pairs.'''
   a = Coordinate(1, 2)
   b = Coordinate(0.5, 0.5)
   t = a - b
   assert t == Coordinate(0.5, 1.5)


def test_coordinate__sub__02( ):
   '''Coordinate pair can substract a tuple.'''
   a = Coordinate(1, 2)
   b = (0.5, 0.5)
   t = a - b
   assert t == Coordinate(0.5, 1.5)


def test_coordinate__sub__03( ):
   '''An int can be substracted from a Coordinate.'''
   a = Coordinate(1, 2)
   t = a - 1
   assert t == Coordinate(0, 1)


def test_coordinate__sub__04( ):
   '''An float can be substracted from a Coordinate.'''
   a = Coordinate(1, 2)
   t = a - 1.5
   assert t == Coordinate(-0.5, 0.5)


## __rsub__ ##

def test_coordinate__rsub__01( ):
   '''A tuple can substract a Coordinate.'''
   a = Coordinate(1, 2)
   b = (0.5, 0.5)
   t = b - a
   assert t == Coordinate(-0.5, -1.5)


def test_coordinate__rsub__02( ):
   '''A Coordinate can be substracted from an int.'''
   a = Coordinate(1, 2)
   t = 1 - a
   assert t == Coordinate(0, -1)


## hash ##

def test_coordinate__hash__01( ):
   t = set([Coordinate(1, 2), Coordinate(1, 2)])
   assert len(t) == 1

## __invert__ ##

def test_coordinate__invert__01( ):
   t = Coordinate(1, 2)
   assert ~t == Coordinate(-2, 1)
   t = Coordinate(0, 0)
   assert ~t == Coordinate(0, 0)
   



