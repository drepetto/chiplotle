from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.coordinatearray import CoordinateArray
import math

## TODO: refactor, this is nasty. Take one type only!

def rotate_2d(xy, angle, pivot=(0, 0)):
   '''2D rotation.

   - `xy` is an (x, y) coordinate pair or a list of coordinate pairs.
   - `angle` is the angle of rotation in radians.
   - `pivot` the point around which to rotate `xy`.

   Returns a Coordinate or a CoordinateArray.
   '''
   try:
      xy = Coordinate(*xy)
      pivot = Coordinate(*pivot)
      result = rotate_coordinate_2d(xy, angle, pivot)
   except:
      xy = CoordinateArray(xy)
      pivot = Coordinate(*pivot)
      result = rotate_coordinatearray_2d(xy, angle, pivot)
   return result


def rotate_coordinate_2d(xy, angle, pivot):
   '''Coordinate 2D rotation.

   - `xy` is an (x, y) coordinate pair.
   - `angle` is the angle of rotation in radians.
   - `pivot` the point around which to rotate `xy`.

   Returns a Coordinate.
   '''
   pivot = Coordinate(*list(pivot))
   ## rotate counter-clockwise...
   angle = -angle
   #cp = Coordinate(xy)
   xy -= pivot
   x = xy.x * math.cos(angle) + xy.y * math.sin(angle) 
   y =  -xy.x * math.sin(angle) + xy.y * math.cos(angle) 
   result = Coordinate(x, y) + pivot
   return result

def rotate_coordinatearray_2d(xylst, angle, pivot):
   '''2D rotation of list of coordinate pairs (CoordinateArray).

   - `xylst` list of (x, y) coordinate pairs.
   - `angle` is the angle of rotation in radians.
   - `pivot` the point around which to rotate `xy`.

   Returns a CoordinateArray.
   '''
   result = CoordinateArray( )
   for xy in xylst:
      r = rotate_coordinate_2d(xy, angle, pivot)
      result.append(r)
   return result

