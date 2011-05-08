from chiplotle import *

def test_scale_formation_01():
   p1 = Path([(1, 1)])
   p2 = Path([(2, 2)])
   f = Formation([p1, p2])
   f.position = Coordinate(10, 10)
   scale(f, 2, Coordinate(0, 0))
   assert f[0] is p1
   assert f[1] is p2
   assert f[0].points == CoordinateArray([(1, 1)])
   assert f[1].points == CoordinateArray([(2, 2)])
   assert f.points == CoordinateArray([(21, 21), (22, 22)])
   assert f.position == Coordinate(20, 20)

