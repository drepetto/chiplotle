from chiplotle import *
import math

def test_rotate_formation_01():
   p1 = Path([(1, 1)])
   p2 = Path([(2, 2)])
   f = Formation([p1, p2])
   f.position = Coordinate(10, 10)
   rotate(f, math.pi / 2, Coordinate(0, 0))
   assert f[0] is p1
   assert f[1] is p2
   assert f[0].points == CoordinateArray([(1, 1)])
   assert f[1].points == CoordinateArray([(2, 2)])
   assert f.points == CoordinateArray([(-9, 11), (-8, 12)])
   assert f.position == Coordinate(-10, 10)

