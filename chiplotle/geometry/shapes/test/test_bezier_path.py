from chiplotle import *

def test_bezier_path_01():
   '''bezier_path can initialize with a list of duples.'''
   points = [(0, 0), (1000, 0), (1000, 1000), (0, 1000), (0, 0)]
   t = shapes.bezier_path(points, 1)
   assert isinstance(t, Path)

def test_bezier_path_02():
   '''bezier_path can initialize with a list of Coordinates.'''
   points = [Coordinate(0, 0), Coordinate(1000, 0), \
             Coordinate(1000, 1000), Coordinate(0, 1000), Coordinate(0, 0)]
   t = shapes.bezier_path(points, 1)
   assert isinstance(t, Path)

def test_bezier_path_03():
   '''bezier_path can initialize with a CoordinateArray.'''
   points = [(0, 0), (1000, 0), (1000, 1000), (0, 1000), (0, 0)]
   points = CoordinateArray(points)
   t = shapes.bezier_path(points, 1)
   assert isinstance(t, Path)
