from chiplotle import *
import numpy
from py.test import raises

### INITIALIZATION ###

def test_pu_init_01( ):
   '''PU can be initialized with nothing.'''
   t = PU( )
   assert type(t.xy) == Scalable
   assert type(t.x)  == Scalable
   assert type(t.y)  == Scalable
   assert len(t.xy) == 0
   assert len(t.x) == 0
   assert len(t.y) == 0
   assert t.format == 'PU;'

def test_pu_init_02( ):
   '''PU can be initialized with empty list.'''
   t = PU([ ])
   assert type(t.xy) == Scalable
   assert type(t.x)  == Scalable
   assert type(t.y)  == Scalable
   assert len(t.xy) == 0
   assert len(t.x) == 0
   assert len(t.y) == 0
   assert t.format == 'PU;'

def test_pu_init_03( ):
   '''PU argument must be list-like (list, tuple, Scalable, Ndarray,...).'''
   assert raises(TypeError, 'PU(4)')

def test_pu_init_04( ):
   '''PU argument must be a list or tuple of length == 2*n'''
   assert raises(AssertionError, 'PU([1])')
   assert raises(AssertionError, 'PU([1,2,3])')
   assert raises(AssertionError, 'PU([1,2,3,4,5])')

def test_pu_init_05( ):
   '''PU initialize properly with list or tuple of 2.'''
   t = PU([1,2])
   assert type(t.xy) == Scalable
   assert type(t.x) == numpy.float32 
   assert type(t.y) == numpy.float32 
   assert all(t.xy == [1, 2])
   assert t.x == 1
   assert t.y == 2
   assert t.format == 'PU1,2;'

def test_pu_init_06( ):
   '''PU initialize properly with list or tuple of length == 2**n.'''
   t = PU([1,2,3,4])
   assert type(t.xy) == Scalable
   assert type(t.x) == Scalable
   assert type(t.y) == Scalable
   assert all(t.xy == [1, 2, 3, 4])
   assert all(t.x == [1, 3])
   assert all(t.y == [2, 4])
   assert t.format == 'PU1,2,3,4;'


### FORMAT ###

def test_pu_format_01( ):
   '''Floats are truncated at format.'''
   t = PU([1, 0.])
   assert t.format == 'PU1,0;'

def test_pu_format_02( ):
   '''Ints are kept as ints in format.'''
   t = PU([0, 0])
   assert t.format == 'PU0,0;'

