from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.shapes.group import Group
import math

def arc_circle(radius, start_angle, end_angle, segments = 100):
   '''
   Constructs an arc from a circle with the given radius,
   and number of segments. Arc goes from start_angle to end_angle,
   both of which are in radians.
   '''
   
   return arc_ellipse(radius, radius, start_angle, end_angle, segments)

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
   
   ae = arc_ellipse(1000, 2000, 1.0, math.pi)
   assert isinstance(ae, Path)
   print ae.format
   gr.append(ae)

   ac = arc_circle(1000, 1.0, math.pi)
   assert isinstance(ac, Path)
   print ac.format
   gr.append(ac)
   
   io.view(gr)

