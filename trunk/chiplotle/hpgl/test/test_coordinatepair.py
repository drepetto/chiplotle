from chiplotle import *
from py.test import raises

## __init__ ##

def test_coordinatepair__init__01( ):
   '''CoordinatePair can be initialized with two values.'''
   t = CoordinatePair(1, 2)
   assert t == (1, 2)
   assert t.x == 1
   assert t.y == 2


def test_coordinatepair__init__02( ):
   '''CoordinatePair can be initialized with a duple.'''
   t = CoordinatePair((1, 2))
   assert t == (1, 2)
   assert t.x == 1
   assert t.y == 2


def test_coordinatepair__init__03( ):
   '''CoordinatePair can be initialized with a CoordinatePair.'''
   t = CoordinatePair(CoordinatePair(1, 2))
   assert t == (1, 2)
   assert t.x == 1
   assert t.y == 2


def test_coordinatepair__init__04( ):
   '''CoordinatePair cannot be initialized with a single number.'''
   assert raises(TypeError, 't = CoordinatePair(4)')


## __eq__ ##

def test_coordinatepair__eq__01( ):
   '''CoordinatePair equates with another CoordinatePair, a tuple, 
   or a list.'''
   t = CoordinatePair(1, 2)
   assert t == CoordinatePair(1, 2)
   assert t == (1, 2)
   assert t == [1, 2]


def test_coordinatepair__eq__02( ):
   '''CoordinatePair __eq__ works with None.'''
   t = CoordinatePair(1, 2)
   assert not (t == None)


## __ne__ ##

def test_coordinatepair__ne__01( ):
   '''CoordinatePair non-equates with another CoordinatePair, a tuple, 
   or a list.'''
   t = CoordinatePair(CoordinatePair(1, 2))
   assert t != CoordinatePair(1, 3)
   assert t != (1, 3)
   assert t != [1, 3]


def test_coordinatepair__ne__02( ):
   '''CoordinatePair __ne__ works with None.'''
   t = CoordinatePair(1, 2)
   assert t != None



## __add__ ##

def test_coordinatepair__add__01( ):
   '''Two CoordinatePairs can be added.'''
   a = CoordinatePair(1, 2)
   b = CoordinatePair(3, 4)
   t = a + b

   assert isinstance(t, CoordinatePair)
   assert t is not a
   assert t is not b
   assert t == (4, 6)


def test_coordinatepair__add__02( ):
   '''A CoordinatePair and an int scalar can be added.'''
   a = CoordinatePair(1, 2)
   b = 4
   t = a + b

   assert isinstance(t, CoordinatePair)
   assert t is not a
   assert t == (5, 6)


def test_coordinatepair__add__03( ):
   '''A CoordinatePair and a float scalar can be added.'''
   a = CoordinatePair(1, 2)
   b = 4.2
   t = a + b

   assert isinstance(t, CoordinatePair)
   assert t is not a
   assert t == (5.2, 6.2)


def test_coordinatepair__add__04( ):
   '''A CoordinatePair and a tuple pair can be added.'''
   a = CoordinatePair(1, 2)
   b = (3, 4)
   t = a + b

   assert isinstance(t, CoordinatePair)
   assert t is not a
   assert t == (4, 6)


def test_coordinatepair__add__05( ):
   '''A CoordinatePair and a CoordinateArray can be added.'''
   a = CoordinatePair(1, 2)
   b = CoordinateArray([(3, 4), (5, 6)])
   t = a + b
   assert isinstance(t, CoordinateArray)
   assert t[0] == (4, 6)
   assert t[1] == (6, 8)


def test_coordinatepair__add__06( ):
   '''A CoordinatePair and a triple cannot be added.'''
   a = CoordinatePair(1, 2)
   b = (3, 4, 5)
   assert raises(TypeError, 'a+b')


def test_coordinatepair__mul__01( ):
   '''A coordinatePair can be multiplied with a scalar.'''
   a = CoordinatePair(1, 2)
   b = 2.5
   t = a * b

   assert isinstance(t, CoordinatePair)
   assert t is not a
   assert t == (2.5, 5)


## div ##

def test_coordinatepair__div__01( ):
   '''True division works without __future__.division imported.'''
   a = CoordinatePair(1, 2)
   t = a / 2
   assert t == CoordinatePair(.5, 1)


def test_coordinatepair__floordiv__01( ):
   '''Floor division works.'''
   a = CoordinatePair(1, 2)
   t = a // 2
   assert t == CoordinatePair(0, 1)


## __sub__ ##

def test_coordinatepair__sub__01( ):
   '''Coordinate pair can substract with other coordinate pairs.'''
   a = CoordinatePair(1, 2)
   b = CoordinatePair(0.5, 0.5)
   t = a - b
   assert t == CoordinatePair(0.5, 1.5)


def test_coordinatepair__sub__02( ):
   '''Coordinate pair can substract a tuple.'''
   a = CoordinatePair(1, 2)
   b = (0.5, 0.5)
   t = a - b
   assert t == CoordinatePair(0.5, 1.5)


def test_coordinatepair__sub__03( ):
   '''An int can be substracted from a CoordinatePair.'''
   a = CoordinatePair(1, 2)
   t = a - 1
   assert t == CoordinatePair(0, 1)


def test_coordinatepair__sub__04( ):
   '''An float can be substracted from a CoordinatePair.'''
   a = CoordinatePair(1, 2)
   t = a - 1.5
   assert t == CoordinatePair(-0.5, 0.5)


## __rsub__ ##

def test_coordinatepair__rsub__01( ):
   '''A tuple can substract a CoordinatePair.'''
   a = CoordinatePair(1, 2)
   b = (0.5, 0.5)
   t = b - a
   assert t == CoordinatePair(-0.5, -1.5)


def test_coordinatepair__rsub__02( ):
   '''A CoordinatePair can be substracted from an int.'''
   a = CoordinatePair(1, 2)
   t = 1 - a
   assert t == CoordinatePair(0, -1)


## hash ##

def test_coordinatepair__hash__01( ):
   t = set([CoordinatePair(1, 2), CoordinatePair(1, 2)])
   assert len(t) == 1
