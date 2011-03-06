from __future__ import division
from chiplotle.geometry.core.coordinate import Coordinate
import math


def xy_to_polar(args):
   '''Converts cartesian to polar coordinates.
   Argument may be two coordinates x, y, a tuple (x, y),
   or a Coordinate(x, y).

   Returns an (r, a) tuple, where `r` is the magnitude, `a` is the angle
   in radians.
   '''
   x, y = tuple(Coordinate(*args))

   r = math.sqrt(x**2 + y**2)
   x = x or 1E-10
   a = math.atan(y / x) 

   if x >= 0:
      if y >= 0:
         pass
      else:
         a += 2 * math.pi
   else:
      a += math.pi
#      if y >= 0:
#         a += math.pi
#      else:
#         a = math.pi / 2 * 3 - a

   return r, a
