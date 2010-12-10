from chiplotle.hpgl.coordinatepair import CoordinatePair
import math


def polar_to_xy(*args):
   '''Converts polar (r, A) to Cartesian (x y) coordinates,
   where r is the radius and A is the angle in radians.
   '''
   try:
      r, A = tuple(CoordinatePair(args))
   except:
      raise TypeError('`args` must be an (r, A) tuple or a pair of values r, A.')
   x = r * math.cos(A)
   y = r * math.sin(A)
   return (x, y)

