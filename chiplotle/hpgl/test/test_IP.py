from chiplotle import *
from chiplotle.hpgl.commands import IP
from py.test import raises

def test_IP_01( ):
   '''IP can be empty.'''
   t = IP( )
   assert t.format == 'IP;'
   assert isinstance(t.coords, CoordinateArray)


def test_IP_02( ):
   '''IP cannot take a flat tuple.'''
   assert raises(TypeError, 't = IP((1,2,3,4))')


def test_IP_03( ):
   '''IP can take a tuple or list of pairs.'''
   t = IP([(1, 2), (3, 4)])
   assert t.coords == CoordinateArray([(1, 2), (3, 4)])

def test_IP_04( ):
   '''IP can take two an only two coordinate pairs.'''
   assert raises(ValueError, 't = IP([Coordinate(1, 2)])')
   assert raises(ValueError, 't = IP([Coordinate(1, 2), Coordinate(3, 4), Coordinate(5, 6)])')
   
def test_IP_05( ):
   '''Coordinates of IP can be reset.'''
   t = IP()
   t.coords = (Coordinate(5, 6), Coordinate(7, 8))
   assert isinstance(t.coords, CoordinateArray)
   assert t.coords == CoordinateArray([(5, 6), (7, 8)])
   

