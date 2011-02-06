from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.shapes.group import Group
from chiplotle.geometry.factory.arc_ellipse import arc_ellipse

import math

def arc_circle(radius, start_angle, end_angle, segments = 100):
   '''
   Constructs an arc from a circle with the given radius,
   and number of segments. Arc goes from start_angle to end_angle,
   both of which are in radians.
   '''
   
   return arc_ellipse(radius, radius, start_angle, end_angle, segments)



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   
   gr = Group()
   
   for radius in range(100, 1000, 10):
       ac = arc_circle(radius, 1.0, math.pi)
       assert isinstance(ac, Path)
       gr.append(ac)


   io.view(gr)

