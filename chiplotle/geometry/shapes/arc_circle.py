from chiplotle.geometry.core.path import Path
from chiplotle.geometry.core.group import Group
from chiplotle.geometry.shapes.arc_ellipse import arc_ellipse

import math

def arc_circle(radius, 
               start_angle, end_angle, 
               segments = 100, segmentation_mode = '2PI'):
   '''
   Constructs an arc from a circle with the given radius,
   and number of segments. Arc goes from start_angle to end_angle,
   both of which are in radians.

      - `segmentation_mode` : '2PI' or 'arc'. The first segments
         the whole circle into the given number of segments,
         the second segments the arc.
   '''
   radius = radius * 2.0 
   return arc_ellipse(radius, radius, 
                      start_angle, end_angle, 
                      segments, segmentation_mode)



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   
   gr = Group()
   
   for radius in range(100, 1000, 100):
       ac = arc_circle(radius, 1.0, math.pi)
       assert isinstance(ac, Path)
       gr.append(ac)

   io.view(gr, 'png')

