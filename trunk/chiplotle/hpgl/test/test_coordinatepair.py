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
   '''CoordinatePair equaties with another CoordinatePair, a tuple, 
   or a list.'''
   t = CoordinatePair(CoordinatePair(1, 2))

   assert t == CoordinatePair(1, 2)
   assert t == (1, 2)
   assert t == [1, 2]


## __ne__ ##

def test_coordinatepair__ne__01( ):
   '''CoordinatePair non-equaties with another CoordinatePair, a tuple, 
   or a list.'''
   t = CoordinatePair(CoordinatePair(1, 2))

   assert t != CoordinatePair(1, 3)
   assert t != (1, 3)
   assert t != [1, 3]



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


def test_coordinatepair__hash__01( ):
   t = set([CoordinatePair(1, 2), CoordinatePair(1, 2)])
   assert len(t) == 1
