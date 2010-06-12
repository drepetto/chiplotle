import math


def rotate_2d(xy, angle):
   '''2D rotation.

   - `xy` is a list or tuple with (x, y) coordinates.
   - `angle` is the angle or rotation in radians.
   '''
   xn = xy[0] * math.cos(angle) + xy[1] * math.sin(angle) 
   yn = - xy[0] * math.sin(angle) + xy[1] * math.cos(angle) 
   return (xn, yn)


