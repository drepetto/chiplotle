from chiplotle import *
import math


def test_rotate_2d_01( ):
   '''Rotate 2d can take a tuple.'''
   xy = (1, 2)
   mathtools.rotate_2d(xy, 0)


def test_rotate_2d_02( ):
   '''Rotate 2d can take a CoordinatePair.'''
   xy = CoordinatePair(1, 2)
   mathtools.rotate_2d(xy, 0)


## values ##

def test_rotate_2d_03( ):
   '''Rotate 2d returns correct values.'''
   xy = (0, 0)
   t = mathtools.rotate_2d(xy, 0)
   assert t == xy


def test_rotate_2d_04( ):
   '''Rotate 2d returns correct values.'''
   xy = (1, 0)
   t = mathtools.rotate_2d(xy, math.pi / 2)
   assert round(t[0], 6) == 0
   assert round(t[1], 6) == 1


