from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.shapes.group import Group

import math

def arc_ellipse(width, height, start_angle, end_angle, segments = 100):  
   '''
   Constructs an arc from an ellipse with the given width, height,
   and number of segments. Arc goes from start_angle to end_angle,
   both of which are in radians.
   '''

   two_pi = math.pi * 2.0
   
   rads_incr = two_pi / float(segments)
   half_width = width * 0.5
   half_height = height * 0.5
   
   rads = start_angle
   
   arc_points = []
   
   while rads < end_angle: 
      sin = math.sin(rads);
      cos = math.cos(rads);

      point_x = (half_width * cos);
      point_y = (half_height * sin);

      arc_points.append((point_x, point_y))
      
      rads += rads_incr
 
   return Path(arc_points)


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   
   gr = Group()
   
   for radius in range(100, 1000, 10):
       ae = arc_ellipse(radius, radius * 2, 1.0, math.pi)
       assert isinstance(ae, Path)
       gr.append(ae)

   io.view(gr)

