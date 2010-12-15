from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.coordinatearray import CoordinateArray
import math


def rotate_2d(xy, angle, pivot=(0, 0)):
   '''2D rotation.

   - `xy` is an (x, y) coordinate pair or a list of coordinate pairs.
   - `angle` is the angle of rotation in radians.
   - `pivot` the point around which to rotate `xy`.

   Returns a CoordinatePair or a CoordinateArray.
   '''
   try:
      xy = CoordinatePair(xy)
      result = _rotate_coordinatepair_2d(xy, angle, pivot)
   except TypeError:
      xy = CoordinateArray(xy)
      result = _rotate_coordinatearray_2d(xy, angle, pivot)
   return result


def _rotate_coordinatepair_2d(xy, angle, pivot):
   '''Coordinate 2D rotation.

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

def _rotate_coordinatearray_2d(xylst, angle, pivot):
   '''2D rotation of list of coordinate pairs (CoordinateArray).

   - `xylst` list of (x, y) coordinate pairs.
   - `angle` is the angle of rotation in radians.
   - `pivot` the point around which to rotate `xy`.

   Returns a CoordinateArray.
   '''
   result = CoordinateArray( )
   for xy in xylst:
      r = _rotate_coordinatepair_2d(xy, angle, pivot)
      result.append(r)
   return result
