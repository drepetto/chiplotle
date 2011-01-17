from chiplotle import *
import math
from py.test import raises

## arguments ##

def test_polar_to_xy_01( ):
   '''The function can take a tuple pair (r, a)'''
   t = mathtools.polar_to_xy(Coordinate(1, 0))
   assert isinstance(t, tuple)
   assert len(t) == 2
   assert t == (1, 0)


def test_polar_to_xy_02( ):
   '''The function cannot take two values r and A'''
   assert raises(TypeError, 'mathtools.polar_to_xy(1, 0)')


def test_polar_to_xy_03( ):
   '''Three arguments throw a TypeError.'''
   assert raises(TypeError, 'mathtools.polar_to_xy(1, 2, 3)')


def test_polar_to_xy_04( ):
   '''One numeric argument throws a TypeError.'''
   assert raises(TypeError, 'mathtools.polar_to_xy(1)')


def test_polar_to_xy_05( ):
   '''One tuple argument with > 2 arguments throws a TypeError.'''
   assert raises(TypeError, 'mathtools.polar_to_xy((1, 2, 3))')


## values 90 degs. ##

def test_polar_to_xy_06( ):
   t = mathtools.polar_to_xy(Coordinate(1, math.pi / 2))
   assert round(t[0], 6) == 0
   assert round(t[1], 6) == 1


def test_polar_to_xy_07( ):
   t = mathtools.polar_to_xy(Coordinate(1, math.pi))
   assert round(t[0], 6) == -1
   assert round(t[1], 6) == 0


def test_polar_to_xy_08( ):
   t = mathtools.polar_to_xy(Coordinate(1, math.pi / 2 * 3))
   assert round(t[0], 6) == 0
   assert round(t[1], 6) == -1


def test_polar_to_xy_09( ):
   t = mathtools.polar_to_xy(Coordinate(1, math.pi / 2 * 4))
   assert round(t[0], 6) == 1
   assert round(t[1], 6) == 0


## values 45 degs. ##


def test_polar_to_xy_10( ):
   t = mathtools.polar_to_xy(Coordinate(1, math.pi / 4 * 1))
   assert round(t[0], 6) == round(math.sqrt(2) / 2, 6)
   assert round(t[1], 6) == round(math.sqrt(2) / 2, 6)


def test_polar_to_xy_11( ):
   t = mathtools.polar_to_xy(Coordinate(1, math.pi / 4 * 3))
   assert round(t[0], 6) == round(-math.sqrt(2) / 2, 6)
   assert round(t[1], 6) == round(math.sqrt(2) / 2, 6)


def test_polar_to_xy_12( ):
   t = mathtools.polar_to_xy(Coordinate(1, math.pi / 4 * 5))
   assert round(t[0], 6) == round(-math.sqrt(2) / 2, 6)
   assert round(t[1], 6) == round(-math.sqrt(2) / 2, 6)


def test_polar_to_xy_13( ):
   t = mathtools.polar_to_xy(Coordinate(1, math.pi / 4 * 7))
   assert round(t[0], 6) == round(math.sqrt(2) / 2, 6)
   assert round(t[1], 6) == round(-math.sqrt(2) / 2, 6)
