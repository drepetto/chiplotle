import math


def polar_to_xy(r, A):
   '''Converts polar to Cartesian coordinates. 
   Angle `A` is in radians.
   '''
   x = r * math.cos(A)
   y = r * math.sin(A)
   return (x, y)


