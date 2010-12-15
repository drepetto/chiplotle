from chiplotle.hpgl.coordinatepair import CoordinatePair
import math


def rotate_2d(xy, angle, pivot=(0, 0)):
   '''2D rotation.

   - `xy` is an (x, y) coordinate pair.
   - `angle` is the angle of rotation in radians.
   - `pivot` the point around which to rotate `xy`.

   Returns a CoordinatePair.
   '''
   ## rotate counter-clockwise...
   angle = -angle
   cp = CoordinatePair(xy)
   cp -= pivot
   x = cp.x * math.cos(angle) + cp.y * math.sin(angle) 
   y =  -cp.x * math.sin(angle) + cp.y * math.cos(angle) 
   result = CoordinatePair(x, y) + pivot
   return result


