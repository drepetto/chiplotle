from chiplotle import *

def test_path_interpolated_01():
   '''path_interpolated can initialize with a list of duples.'''
   points = [(0, 0), (1000, 0), (1000, 1000), (0, 1000), (0, 0)]
   t = shapes.path_interpolated(points, 1)
   assert isinstance(t, Path)

def test_path_interpolated_02():
   '''path_interpolated can initialize with a list of Coordinates.'''
   points = [Coordinate(0, 0), Coordinate(1000, 0), \
             Coordinate(1000, 1000), Coordinate(0, 1000), Coordinate(0, 0)]
   t = shapes.path_interpolated(points, 1)
   assert isinstance(t, Path)

def test_path_interpolated_03():
   '''path_interpolated can initialize with a CoordinateArray.'''
   points = [(0, 0), (1000, 0), (1000, 1000), (0, 1000), (0, 0)]
   points = CoordinateArray(points)
   t = shapes.path_interpolated(points, 1)
   assert isinstance(t, Path)
