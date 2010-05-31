from chiplotle import *
from py.test import raises

import py.test
py.test.skip( 'Scalable is deprecated.')


#def test_scalable_01( ):
#   '''Empty Scalable defaults to type 'float32'.'''
#   t = Scalable([ ])
#   assert t.dtype == 'float32'
#
#def test_scalable_02( ):
#   '''Scalable initialized with ints has type float32.'''
#   t = Scalable([1,2,3,4])
#   assert t.dtype == 'float32'
#
#def test_scalable_03( ):
#   '''Scalable initialized with floats stays float32.'''
#   t = Scalable([1.2,2.3,3,4])
#   assert t.dtype == 'float32'


def test_scalable_01( ):
   '''Scalable must be initialized with something.'''
   assert raises(TypeError, 't = Scalable( )')


def test_scalable_02( ):
   '''A scalable can take an int.'''
   t = Scalable(2)

   assert isinstance(t._data, int)
   assert t._data == 2


## add ##

def test_scalable_add_01( ):
   '''int Scalables can add with ints.'''  
   a = Scalable(2)
   b = 3
   t = a + b

   assert isinstance(t, Scalable)
   assert t._data == 5
   assert t.dtype == int
   

def test_scalable_add_02( ):
   '''int Scalables can add with floats.'''  
   a = Scalable(2)
   b = 3.0
   t = a + b

   assert isinstance(t, Scalable)
   assert t._data == 5
   assert t.dtype == float
   

def test_scalable_add_03( ):
   '''float Scalables can add with floats.'''  
   a = Scalable(2.0)
   b = 3.0
   t = a + b

   assert isinstance(t, Scalable)
   assert t._data == 5
   assert t.dtype == float
   

def test_scalable_add_04( ):
   '''float Scalables can add with ints.'''  
   a = Scalable(2.0)
   b = 3
   t = a + b

   assert isinstance(t, Scalable)
   assert t._data == 5
   assert t.dtype == float
   

## eq ##

def test_scalable_eq_01( ):
   '''Scalable can equate with another Scalable.'''
   a = Scalable(2)
   b = Scalable(2)
   c = Scalable(3)
   d = Scalable(2.0)
   
   assert a == b
   assert a != c
   assert a == d


def test_scalable_eq_02( ):
   '''Scalable can equate with a scalar.'''
   a = Scalable(2)
   b = 2
   c = 3
   d = 2.0
   
   assert a == b
   assert a != c
   assert a == d


## float ##

def test_scalable_float_01( ):
   '''Scalable can be converted to float.'''
   a = Scalable(2)
   t = float(a)

   assert isinstance(t, float)


## int ##

def test_scalable_int_01( ):
   '''Scalable can be converted to int.'''
   a = Scalable(2)
   t = int(a)

   assert isinstance(t, int)
