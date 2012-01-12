from chiplotle import *
from chiplotle.hpgl.commands import PU
from py.test import raises

### INITIALIZATION ###

def test_pu_init_01( ):
   '''PU can be initialized with nothing.'''
   t = PU( )
   assert type(t.xy) == CoordinateArray
   assert len(t.xy) == 0
   assert len(t.x) == 0
   assert len(t.y) == 0

def test_pu_init_02( ):
   '''PU can be initialized with empty list.'''
   t = PU([ ])
   assert type(t.xy) == CoordinateArray
   assert len(t.xy) == 0
   assert len(t.x) == 0
   assert len(t.y) == 0

def test_pu_init_03( ):
   '''PU argument must be list-like (list, tuple, Ndarray,...).'''
   assert raises(TypeError, 'PU(4)')

def test_pu_init_04( ):
   '''PU argument must be a list or tuple of length == 2*n'''
   assert raises(TypeError, 'PU([1])')
   assert raises(TypeError, 'PU([1,2,3])')
   assert raises(TypeError, 'PU([1,2,3,4,5])')

def test_pu_init_05( ):
   '''PU initialize properly with list or tuple of 2.'''
   t = PU([(1,2)])
   assert type(t.xy) == CoordinateArray
   assert t.xy == CoordinateArray([(1, 2)])
   assert t.x == (1, )
   assert t.y == (2, )

def test_pu_init_06( ):
   '''PU initialize properly with list or tuple of length == 2**n.'''
   t = PU([(1,2),(3,4)])
   assert type(t.xy) == CoordinateArray
   assert t.xy == CoordinateArray([(1, 2), (3, 4)])
   assert t.x == (1, 3)
   assert t.y == (2, 4)


### FORMAT ###

def test_pu_format_01( ):
   '''Empty PU( ).'''
   t = PU( )
   assert t.format == 'PU;'

def test_pu_format_02( ):
   '''Floats are left floats at format.'''
   t = PU([(1, 0.)])
   assert t.format == 'PU1.00,0.00;'

def test_pu_format_03( ):
   '''Ints are kept ints at format.'''
   t = PU([(0, 0)])
   assert t.format == 'PU0,0;'

