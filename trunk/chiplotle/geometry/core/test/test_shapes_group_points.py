from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.path import Path
from chiplotle.geometry.coordinate import Coordinate

def test_shapes_group_points_01( ):
   '''An empty Group has an empty list of points.'''
   t = Group( )
   assert t.points == [ ]


def test_shapes_group_points_02( ):
   '''A flat Group has a flat list of points.'''
   t = Group([Path([1, 2, 3, 4]), Path([4, 2, 4, 2])])
   assert t.points == [Coordinate(1, 2), Coordinate(3, 4), 
      Coordinate(4, 2), Coordinate(4, 2)]


def test_shapes_group_points_03( ):
   '''A non-flat Group has a flat list of points.'''
   g = Group([Path([1, 2, 3, 4]), Path([4, 2, 4, 2])])
   t = Group([g, Path([100, 200])])
   assert t.points == [Coordinate(1, 2), Coordinate(3, 4), 
      Coordinate(4, 2), Coordinate(4, 2), Coordinate(100, 200)]




