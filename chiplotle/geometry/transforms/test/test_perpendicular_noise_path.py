from chiplotle import *
import copy

def test_perpendicular_noise_path_01( ):
   c  = circle(1000, 200)
   cc = copy.deepcopy(c)
   perpendicular_noise(c, 360)
   assert c.points != cc.points
   assert c.points is not cc.points

