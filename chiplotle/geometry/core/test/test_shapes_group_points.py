from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.path import Path
from chiplotle.geometry.core.coordinate import Coordinate

def test_shapes_group_points_01( ):
   '''An empty Group has an empty CoordinateArray.'''
   t = Group( )
   assert t.points == CoordinateArray([ ])


def test_shapes_group_points_02( ):
   '''A flat Group has a CoordinateArray.'''
   t = Group([Path([(1, 2), (3, 4)]), Path([(4, 2), (4, 2)])])
   assert t.points == CoordinateArray([(1, 2), (3, 4), 
      (4, 2), (4, 2)])


def test_shapes_group_points_03( ):
   '''A non-flat Group has a CoordinateArray.'''
   g = Group([Path([(1, 2), (3, 4)]), Path([(4, 2), (4, 2)])])
   t = Group([g, Path([(100, 200)])])
   assert t.points == CoordinateArray([(1, 2), (3, 4), (4, 2), (4, 2), (100, 200)])

