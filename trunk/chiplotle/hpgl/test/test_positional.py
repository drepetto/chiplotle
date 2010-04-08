from chiplotle.hpgl.abstract.positional import _Positional
#from chiplotle.hpgl.scalable import Scalable
from chiplotle.hpgl.coordinatearray import CoordinateArray
import numpy
from py.test import raises

def test_positional_01( ):
   '''_Positional can be initialized with a flat iterable (list, tuple, etc. )
   of length 2*n as first argument.'''
   p = _Positional((1, 2, 3, 4))
   assert p.xy == ((1, 2), (3, 4))
   assert numpy.all(p.x == (1, 3))
   assert numpy.all(p.y == (2, 4))
   assert len(p.xy) == 2
   assert type(p.xy) == CoordinateArray
   assert type(p.x) == numpy.ndarray
   assert type(p.y) == numpy.ndarray 


def test_positional_02( ):
   '''_Positional complaines with lenghts != 2*n .'''
   assert raises(ValueError,  '_Positional((1,2,3))')


def test_positional_03( ):
   '''xy cannot be set with an single number.'''
   p = _Positional((1,2))
   assert raises(ValueError, 'p.xy = 3')


def test_positional_04( ):
   '''xy can be set with a list or tuple.'''
   p = _Positional((0,0))
   p.xy = (1,2)
   assert p.xy == [(1,2)]
   p.xy = [1,2,3,4]
   assert p.xy == [(1,2),(3,4)]
   assert all(p.x == [1, 3])
   assert all(p.y == [2, 4])


def test_positional_05( ):
   '''xy assignment must have lenth == 2*n'''
   p = _Positional((0,0))
   assert raises(ValueError, 'p.xy =(1,)')
   assert raises(ValueError, 'p.xy =(1,2,3)')
   assert raises(ValueError, 'p.xy =(1,2,3,4,5)')


def test_positional_06( ):
   '''xy can be set to None'''
   p = _Positional((0,0))
   p.xy = None
   assert isinstance(p.xy, CoordinateArray)
   assert isinstance(p.x, numpy.ndarray)
   assert isinstance(p.y, numpy.ndarray)
   assert len(p.xy) == 0
   assert len(p.x) == 0
   assert len(p.y) == 0


def test_positional_07( ):
   '''x and y can be assigned numbers or iterables.
   The length of iterables must be 1 or len(xy) / 2.'''
   p = _Positional((1,2,3,4))
   p.x = 0
   assert p.xy == ((0, 2), (0, 4))
   p.x = [1]
   assert p.xy == ((1, 2), (1, 4))
   p.x = (1, 3)
   assert p.xy == ((1, 2), (3, 4))
   assert raises(ValueError, 'p.x = (1, 2, 3)')


## FORMATTING ##

## TODO: these two tests work fine when py.test -x is run on this test
## flile only, but not when run on all files in directory... figure out
## why.
#def test_positional_format_01( ):
#   '''ints format as ints.'''
#   assert _Positional((1, 2)).format == '_Positional1,2;'
#
#
#def test_positional_format_02( ):
#   '''Floats that would normally print as Xe-n (e.g., 1e-10 instead of
#   0.0000000001) format without the 'e-n'.'''
#   assert _Positional((1e-12,2)).format == '_Positional0.00,2.00;'

