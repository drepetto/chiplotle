from chiplotle import *
from py.test import raises

## __init__ ##

def test_coordinate__init__01( ):
   '''Vector can be initialized with two values.'''
   t = Vector(1, 2)
   assert t == Vector(1, 2)
   assert t.x == 1
   assert t.y == 2


def test_coordinate__init__02( ):
   '''Vector cannot be initialized with a duple.'''
   assert raises(errors.InitParameterError, 'Vector((1, 2))')


def test_coordinate__init__03( ):
   '''Vector can be initialized with a Vector.'''
   ##In this case, the constructor returns the existing coordinate.'''
   a = Vector(1, 2)
   t = Vector(a)
   assert t is not a
   assert t == Vector(1, 2)
   assert t.x == 1
   assert t.y == 2


def test_coordinate__init__04( ):
   '''Two Vectors have different ids.'''
   a = Vector(1, 2)
   b = Vector(1, 2)
   assert a is not b


def test_coordinate__init__05( ):
   '''Vector cannot be initialized with a single number.'''
   assert raises(errors.InitParameterError, 't = Vector(4)')


def test_coordinate__init__06( ):
   '''Vector cannot be initialized with a triple.'''
   assert raises(errors.InitParameterError, 't = Vector((1, 2, 3))')


## attribute assignment ##

def test_coordinate_attribute_assignment_01( ):
   '''Vectors are immutable.
   Attributes cannot be set (rebound).'''
   t = Vector(1, 2)
   assert raises(AttributeError, 't.x = 2')
   assert raises(AttributeError, 't.y = 2')
   assert raises(AttributeError, 't.xy = 2')
   assert raises(AttributeError, 't.foo = 3')
   assert raises(TypeError, 't[0] = 2')


## __eq__ ##

def test_coordinate__eq__01( ):
   '''Vector equates with another Vector.'''
   t = Vector(1, 2)
   assert t == Vector(1, 2)
   assert Vector(1, 2) == t


def test_coordinate__eq__02( ):
   '''Vector does not equate with a list or tuple.'''
   t = Vector(1, 2)
   assert not (t == (1, 2))
   assert not ((1, 2) == t)
   assert not (t == [1, 2])
   assert not ([1, 2] == t)


def test_coordinate__eq__03( ):
   '''Vector __eq__ works with None.'''
   t = Vector(1, 2)
   assert not (t == None)


## __ne__ ##

def test_coordinate__ne__01( ):
   '''Vector non-equates with another Vector, a tuple, 
   or a list.'''
   t = Vector(1, 2)
   assert t != Vector(1, 3)
   assert t != (1, 3)
   assert t != [1, 3]


def test_coordinate__ne__02( ):
   '''Vector non-equates with int, float.'''
   t = Vector(1, 2)
   assert t != 4.5
   assert t != 2
   assert t != None


## __add__ ##

def test_coordinate__add__01( ):
   '''Two Vectors can be added.'''
   a = Vector(1, 2)
   b = Vector(3, 4)
   t = a + b
   assert isinstance(t, Vector)
   assert t is not a
   assert t is not b
   assert t == Vector(4, 6)


def test_coordinate__add__02( ):
   '''A Vector and an int scalar can be added.'''
   a = Vector(1, 2)
   t = a + 4
   assert isinstance(t, Vector)
   assert t is not a
   assert t == Vector(5, 6)


def test_coordinate__radd__02( ):
   '''An int scalar and a  Vector can be added.'''
   a = Vector(1, 2)
   t = 4 + a
   assert isinstance(t, Vector)
   assert t is not a
   assert t == Vector(5, 6)


def test_coordinate__add__03( ):
   '''A Vector and a float scalar can be added.'''
   a = Vector(1, 2)
   t = a + 4.2
   assert isinstance(t, Vector)
   assert t is not a
   assert t == Vector(5.2, 6.2)


def test_coordinate__radd__03( ):
   '''A float scalar and a Vector scalar can be added.'''
   a = Vector(1, 2)
   t = 4.2 + a
   assert isinstance(t, Vector)
   assert t is not a
   assert t == Vector(5.2, 6.2)


def test_coordinate__add__04( ):
   '''A Vector and a tuple pair cannot be added.'''
   a = Vector(1, 2)
   assert raises(errors.OperandError, 'a + (3, 4)')


def test_coordinate__radd__04( ):
   '''A tuple pair and a Vector cannot be added.'''
   a = Vector(1, 2)
   assert raises(errors.OperandError, '(3, 4) + a')


def test_coordinate__add__05( ):
   '''A Vector and a VectorArray can be added.'''
   a = Vector(1, 2)
   b = VectorArray([(3, 4), (5, 6)])
   t = a + b
   assert isinstance(t, VectorArray)
   assert t[0] == Vector(4, 6)
   assert t[1] == Vector(6, 8)


def test_coordinate__radd__05( ):
   '''A VectorArray and a Vector can be added.'''
   a = Vector(1, 2)
   b = VectorArray([(3, 4), (5, 6)])
   t = b + a
   assert isinstance(t, VectorArray)
   assert t[0] == Vector(4, 6)
   assert t[1] == Vector(6, 8)


def test_coordinate__add__06( ):
   '''A Vector and a triple cannot be added.'''
   a = Vector(1, 2)
   b = (3, 4, 5)
   assert raises(errors.OperandError, 'a + b')

def test_coordinate__radd__06( ):
   '''A triple and a Vector cannot be added.'''
   a = Vector(1, 2)
   b = (3, 4, 5)
   assert raises(errors.OperandError, 'b + a')


## __mul__ ##

def test_coordinate__mul__01( ):
   '''A Vector can be multiplied with a scalar.'''
   a = Vector(1, 2)
   b = 2.5
   t = a * b
   assert isinstance(t, Vector)
   assert t is not a
   assert t == Vector(2.5, 5)


def test_coordinate__mul__02( ):
   '''A Vector cannot be multiplied with a pair.'''
   a = Vector(2, 3)
   assert raises(errors.OperandError, 'a * (2, 3)')


def test_coordinate__mul__03( ):
   '''A Vector can be multiplied with another Vector.'''
   a = Vector(2, 3)
   t = a * Vector(2, 3)
   assert isinstance(t, Vector)
   assert t == Vector(4, 9)



## div ##

def test_coordinate__div__01( ):
   '''True division works without __future__.division imported.'''
   a = Vector(1, 2)
   t = a / 2
   assert isinstance(t, Vector)
   assert t == Vector(.5, 1)

def test_coordinate__div__02( ):
   '''Denominator 0 raises ZeroDivisionError.'''
   a = Vector(1, 2)
   assert raises(ZeroDivisionError, 't = a / 0')
   

def test_coordinate__div__03( ):
   '''A Vector can be divided by a Vector.'''
   a = Vector(1, 2)
   b = Vector(2, 4)
   t = a / b
   assert isinstance(t, Vector)
   assert t == Vector(0.5, 0.5)


def test_coordinate__div__04( ):
   '''A Vector cannot be divided by a duple.'''
   a = Vector(1, 2)
   b = (2, 4)
   assert raises(errors.OperandError, 'a / b')


def test_coordinate__div__05( ):
   '''Division raises an OperandError on wrong type.'''
   a = Vector(1, 2)
   assert raises(errors.OperandError, 'a / (1, 2, 3)')


def test_coordinate__floordiv__01( ):
   '''Floor division works with ints.'''
   a = Vector(1, 2)
   t = a // 2
   assert isinstance(t, Vector)
   assert t == Vector(0, 1)


def test_coordinate__floordiv__02( ):
   '''Floor division works with two Vectors.'''
   a = Vector(1, 2)
   b = Vector(2, -4)
   t = a // b
   assert isinstance(t, Vector)
   assert t == Vector(0, -1)


def test_coordinate__floordiv__03( ):
   '''Denominator 0 raises ZeroDivisionError.'''
   a = Vector(1, 2)
   assert raises(ZeroDivisionError, 't = a // 0')
   

def test_coordinate__floordiv__04( ):
   '''Floor Division raises an OperandError on wrong type.'''
   a = Vector(1, 2)
   assert raises(errors.OperandError, 'a // (1, 2, 3)')


## __sub__, __rsub__ ##

def test_coordinate__sub__01( ):
   '''Vector pair can substract with other coordinate pairs.'''
   a = Vector(1, 2)
   b = Vector(0.5, 0.5)
   t = a - b
   assert isinstance(t, Vector)
   assert t == Vector(0.5, 1.5)


def test_coordinate__sub__02( ):
   '''Vector pair cannot substract a tuple.'''
   a = Vector(1, 2)
   assert raises(errors.OperandError, 'a - (0.5, 0.5)')


def test_coordinate__rsub__02( ):
   '''A tuple can substract a Vector.'''
   a = Vector(1, 2)
   assert raises(errors.OperandError, '(0.5, 0.5) - a')


def test_coordinate__sub__03( ):
   '''An int can be substracted from a Vector.'''
   a = Vector(1, 2)
   t = a - 1
   assert isinstance(t, Vector)
   assert t == Vector(0, 1)

def test_coordinate__rsub__03( ):
   '''A Vector can be substracted from an int.'''
   a = Vector(1, 2)
   t = 1 - a
   assert isinstance(t, Vector)
   assert t == Vector(0, -1)


def test_coordinate__sub__04( ):
   '''An float can be substracted from a Vector.'''
   a = Vector(1, 2)
   t = a - 1.5
   assert isinstance(t, Vector)
   assert t == Vector(-0.5, 0.5)

def test_coordinate__rsub__04( ):
   '''A Vector can be substracted from a float.'''
   a = Vector(1, 2)
   t = 1.5 - a
   assert isinstance(t, Vector)
   assert t == Vector(0.5, -0.5)



## __hash__ ##

def test_coordinate__hash__01( ):
   t = set([Vector(1, 2), Vector(1, 2)])
   assert len(t) == 1


## __invert__ ##

def test_coordinate__invert__01( ):
   t = Vector(1, 2)
   assert ~t == Vector(-2, 1)
   t = Vector(0, 0)
   assert ~t == Vector(0, 0)
   


## __getitem__ ##

def test_coordinate__getitem__01( ):
   t = Vector(1, 2)
   assert t[0] == 1
   assert t[1] == 2
   assert raises(IndexError, 't[3]')

## __len__ ##

def test_coordinate__len__01( ):
   t = Vector(1, 2)
   assert len(t) == 2

## __iter__ ##

def test_coordinate__iter__01( ):
   t = Vector(1, 2)
   t = list(t)
   assert isinstance(t, list)
   assert t == [1, 2]

## __abs__ ##

def test_coordinate__abs__01( ):
   t = Vector(1, 2)
   assert abs(t) == Vector(1, 2)
   t = Vector(-1, 2)
   assert abs(t) == Vector(1, 2)
   t = Vector(-1, -2)
   assert abs(t) == Vector(1, 2)


## __neg__ ##

def test_coordinate__neg__01( ):
   t = Vector(1, 2)
   assert -t == Vector(-1, -2)
   t = Vector(-1, 2)
   assert -t == Vector(1, -2)
   t = Vector(-1, -2)
   assert -t == Vector(1, 2)

