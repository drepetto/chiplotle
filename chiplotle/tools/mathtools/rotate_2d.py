from chiplotle.geometry.vector import Vector
from chiplotle.geometry.vectorarray import VectorArray
import math


def rotate_2d(xy, angle, pivot=(0, 0)):
   '''2D rotation.

   - `xy` is an (x, y) coordinate pair or a list of coordinate pairs.
   - `angle` is the angle of rotation in radians.
   - `pivot` the point around which to rotate `xy`.

   Returns a Vector or a VectorArray.
   '''
   try:
      xy = Vector(*xy)
      pivot = Vector(*pivot)
      result = _rotate_coordinate_2d(xy, angle, pivot)
   except:
      xy = VectorArray(xy)
      pivot = Vector(*pivot)
      result = _rotate_coordinatearray_2d(xy, angle, pivot)
   return result


def _rotate_coordinate_2d(xy, angle, pivot):
   '''Vector 2D rotation.

   - `xy` is an (x, y) coordinate pair.
   - `angle` is the angle of rotation in radians.
   - `pivot` the point around which to rotate `xy`.

   Returns a Vector.
   '''
   ## rotate counter-clockwise...
   angle = -angle
   #cp = Vector(xy)
   xy -= pivot
   x = xy.x * math.cos(angle) + xy.y * math.sin(angle) 
   y =  -xy.x * math.sin(angle) + xy.y * math.cos(angle) 
   result = Vector(x, y) + pivot
   return result

def _rotate_coordinatearray_2d(xylst, angle, pivot):
   '''2D rotation of list of coordinate pairs (VectorArray).

   - `xylst` list of (x, y) coordinate pairs.
   - `angle` is the angle of rotation in radians.
   - `pivot` the point around which to rotate `xy`.

   Returns a VectorArray.
   '''
   result = VectorArray( )
   for xy in xylst:
      r = _rotate_coordinate_2d(xy, angle, pivot)
      result.append(r)
   return result

