from chiplotle import *
import math


def test_xy_to_polar_01( ):
   '''radius and angle are 0 when x and y ar 0.'''
   r, a = mathtools.xy_to_polar((0, 0))
   assert r == 0
   assert a == 0
   

## 90  degs ##

def test_xy_to_polar_02( ):
   '''Coordinate axis alignment values are correct.'''
   r, a = mathtools.xy_to_polar((1, 0))
   assert r == 1
   assert a == 0


def test_xy_to_polar_03( ):
   '''Coordinate axis alignment values are correct.'''
   r, a = mathtools.xy_to_polar((0, 1))
   assert r == 1
   assert round(a, 6) == round(math.pi / 2, 6)


def test_xy_to_polar_04( ):
   '''Coordinate axis alignment values are correct.'''
   r, a = mathtools.xy_to_polar((-1, 0))
   assert r == 1
   assert round(a, 6) == round(math.pi, 6)


def test_xy_to_polar_05( ):
   '''Coordinate axis alignment values are correct.'''
   r, a = mathtools.xy_to_polar((0, -1))
   assert r == 1
   assert round(a, 6) == round(math.pi / 2 * 3, 6)


## 45 degs ##

def test_xy_to_polar_06( ):
   '''Coordinates in positive quadrant are correct.'''
   r, a = mathtools.xy_to_polar((1, 1))
   assert round(r, 6) == round(math.sqrt(2), 6)
   assert round(a, 6) == round(math.pi / 4, 6)


def test_xy_to_polar_07( ):
   '''Coordinates in -x y quadrant are correct.'''
   r, a = mathtools.xy_to_polar((-1, 1))
   assert round(r, 6) == round(math.sqrt(2), 6)
   assert round(a, 6) == round(math.pi / 4 * 3, 6)


def test_xy_to_polar_08( ):
   '''Coordinates in -x -y quadrant are correct.'''
   r, a = mathtools.xy_to_polar((-1, -1))
   assert round(r, 6) == round(math.sqrt(2), 6)
   assert round(a, 6) == round(math.pi / 4 * 5, 6)


def test_xy_to_polar_09( ):
   '''Coordinates in x -y quadrant are correct.'''
   r, a = mathtools.xy_to_polar((1, -1))
   assert round(r, 6) == round(math.sqrt(2), 6)
   assert round(a, 6) == round(math.pi / 4 * 7, 6)


