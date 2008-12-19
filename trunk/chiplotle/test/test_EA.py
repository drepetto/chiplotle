from chiplotle import *
from py.test import raises

def test_EA_01( ):
   '''EA cannot initialize with a scalar.'''
   assert raises(TypeError, 't = EA(1)')


def test_EA_02( ):
   '''EA can initialize with a list of length 2.'''
   t = EA([1, 2])
   assert all(t.xy == [1, 2])


def test_EA_03( ):
   '''EA cannot initialize with a list of length > 2.'''
   assert raises(ValueError, 't = EA([1, 2, 3, 4])')
