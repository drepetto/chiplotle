from chiplotle import *
from py.test import raises

def test_ER_01( ):
   '''ER cannot initialize with a scalar.'''
   assert raises(TypeError, 't = ER(1)')


def test_ER_02( ):
   '''ER cannot initialize with a list of length > 2.'''
   assert raises(TypeError, 't = ER([1, 2, 3, 4])')


def test_ER_03( ):
   '''ER can initialize with a list of length 2.'''
   t = ER([1, 2])
   assert t.xy == [1, 2]
   assert t.format == 'ER1,2;'
