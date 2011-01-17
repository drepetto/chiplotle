from chiplotle import *
import math


def test_rotate_2d_args_01( ):
   '''Rotate 2d can take a tuple.'''
   xy = (1, 2)
   t = mathtools.rotate_2d(xy, 0)
   assert t == Coordinate(*xy)


def test_rotate_2d_args_02( ):
   '''Rotate 2d can take a Coordinate.'''
   xy = Coordinate(1, 2)
   t = mathtools.rotate_2d(xy, 0)
   assert t == xy


def test_rotate_2d_args_03( ):
   '''Rotate 2d can take a list of tuples.'''
   xy = [(1, 2), (2, 3)]
   t = mathtools.rotate_2d(xy, 0)
   assert t == CoordinateArray(xy)


def test_rotate_2d_args_04( ):
   '''Rotate 2d can take a CoordinateArray.'''
   xy = CoordinateArray([(1, 2), (2, 3)])
   t = mathtools.rotate_2d(xy, 0)
   assert t == xy


def test_rotate_2d_args_05( ):
   '''Rotate 2d returns a Coordinate if it gets a pair.'''
   xy = Coordinate(1, 2)
   t = mathtools.rotate_2d(xy, 0)
   assert isinstance(t, Coordinate)


def test_rotate_2d_args_05( ):
   '''Rotate 2d returns a CoordinateArray if it gets a list of coordinates.'''
   xy = [(1, 2), (3, 4)]
   t = mathtools.rotate_2d(xy, 0)
   assert isinstance(t, CoordinateArray)


## values ##

def test_rotate_2d_04( ):
   '''Rotate 2d leaves (x, y) unchanged on 0 rotation.'''
   xy = (0, 0)
   t = mathtools.rotate_2d(xy, 0)
   assert t == Coordinate(*xy)
   xy = (1, 0)
   t = mathtools.rotate_2d(xy, 0)
   assert t == Coordinate(*xy)
   xy = (-1, 0)
   t = mathtools.rotate_2d(xy, 0)
   assert t == Coordinate(*xy)
   xy = (-1, 1)
   t = mathtools.rotate_2d(xy, 0)
   assert t == Coordinate(*xy)
   xy = (-1, -2)
   t = mathtools.rotate_2d(xy, 0)
   assert t == Coordinate(*xy)


def test_rotate_2d_05( ):
   '''Rotate 2d turns counter-clockwise.'''
   xy = (1, 0)
   t = mathtools.rotate_2d(xy, math.pi / 2)
   assert round(t[0], 6) == 0
   assert round(t[1], 6) == 1
   t = mathtools.rotate_2d(xy, math.pi / 4)
   assert round(t[0], 3) == 0.707
   assert round(t[1], 3) == 0.707
   xy = (-1, 0)
   t = mathtools.rotate_2d(xy, math.pi / 2)
   assert round(t[0], 6) == 0
   assert round(t[1], 6) == -1
   t = mathtools.rotate_2d(xy, math.pi / 4)
   assert round(t[0], 3) == -0.707
   assert round(t[1], 3) == -0.707



def test_rotate_2d_06( ):
   '''Rotate 2d returns correct values.'''
   xy = (1, 0)
   t = mathtools.rotate_2d(xy, math.pi / 2)
   assert round(t[0], 6) == 0
   assert round(t[1], 6) == 1


## pivot ##

def test_rotate_2d_pivot_01( ):
   '''Rotate 2d can rotate around an arbitrary pivot point.'''
   xy = (1, 0)
   t = mathtools.rotate_2d(xy, math.pi / 1.5, (1, 0))
   assert round(t[0], 6) == 1
   assert round(t[1], 6) == 0


def test_rotate_2d_pivot_02( ):
   '''Rotate 2d can rotate around an arbitrary pivot point.'''
   xy = (1, 0)
   t = mathtools.rotate_2d(xy, math.pi / 2, (1, 1))
   assert round(t[0], 6) == 2
   assert round(t[1], 6) == 1
   t = mathtools.rotate_2d(xy, math.pi / 4, (1, 1))
   r = Coordinate(0.707, -0.707) + Coordinate(1, 1)
   assert round(t[0], 3) == round(r[0], 3)
   assert round(t[1], 3) == round(r[1], 3)


