from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.shapes.group import Group
from chiplotle.tools.mathtools import polar_to_xy
import math

def fan(radius, angle, width_angle, height, chord=None, filled=False):
   '''A Fan is a slice of a donut seen from above (the hole in the middle).
   Or think of it as bent rectangle.
   
   All angles are assumed to be in radians.'''

   ## get corners of shape...
   ## lower_right (viewing from pole outward)
   r = radius - height / 2 ## assumes the fan is centered on (r, a)
   a = angle - width_angle / 2
   lr = polar_to_xy((r, a))

   a = angle + width_angle / 2
   ll = polar_to_xy((r, a))

   r = radius + height / 2 
   a = angle - width_angle / 2
   ur = polar_to_xy((r, a))

   a = angle + width_angle / 2
   ul = polar_to_xy((r, a))

   points1 = []
   ## outward lines...
   points1.append(lr)
   points1.append(ur)
   
   points2 = []
   points2.append(ll)
   points2. append(ul)
   ## arches...
   '''
   points3 = []
   a = math.degrees(width_angle)
   
   NOT SURE HOW TO IMPLENT THE AA CALLS!
   points += [PU( ), PA(lr), PD( ), AA(xy, a)]
   points += [PU( ), PA(ur), PD( ), AA(xy, a)]
   '''
   
   return Group([Path(points1), Path(points2)])


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   f = fan(100, 0, .5, 100)
   assert isinstance(f, Group)
   print f.format
   io.view(f)
