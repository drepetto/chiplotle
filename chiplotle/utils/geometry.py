
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""
import math

# utility functions

def polar2xy(r, A):
   x = r * math.cos(A)
   y = r * math.sin(A)
   return (x, y)


def rotate2d(xy, angle):
   xn = xy[0] * math.cos(angle) + xy[1] * math.sin(angle) 
   yn = - xy[0] * math.sin(angle) + xy[1] * math.cos(angle) 
   return (xn, yn)
