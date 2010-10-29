from chiplotle import *
from py.test import raises

def test_IP_01( ):
   '''IP can be empty.'''
   t = IP( )
   assert t.format == 'IP;'
   assert isinstance(t.coords, CoordinateArray)


def test_IP_02( ):
   '''IP can take a flat tuple.'''
   t = IP((1,2,3,4))
   assert len(t.coords) == 2
   assert t.format == 'IP1,2,3,4;'


def test_IP_03( ):
   '''IP can take a tuple or list of pairs.'''
   t = IP([(1, 2), (3, 4)])
   assert len(t.coords) == 2
   assert t.format == 'IP1,2,3,4;'
   

def test_IP_04( ):
   '''IP can take two an only two coordinate pairs.'''
   assert raises(ValueError, 't = IP([1, 2, 3, 4, 5])')
   assert raises(ValueError, 't = IP([1, 2, 3])')
   assert raises(ValueError, 't = IP([1])')
   assert raises(ValueError, 't = IP([(1, 2), (3, 4), (5, 6)])')
   

def test_IP_05( ):
   '''Coordinates of IP can be reset.'''
   t = IP([1,2,3,4])
   t.coords = (5, 6, 7, 8)
   assert isinstance(t.coords, CoordinateArray)
   assert t.coords == (5, 6, 7, 8)
   

